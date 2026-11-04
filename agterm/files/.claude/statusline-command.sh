#!/bin/sh
input=$(cat)

# Record the transcript for claude-recap without changing the displayed status line.
if [ -n "${AGTERM_SESSION_ID:-}" ]; then
    transcript_path=$(printf '%s' "$input" | jq -r '.transcript_path // empty' 2>/dev/null)
    if [ -n "$transcript_path" ]; then
        mkdir -p /tmp/claude/panes 2>/dev/null
        printf '%s\n' "$transcript_path" > "/tmp/claude/panes/${AGTERM_SESSION_ID}.${AGTERM_PANE:-left}"
    fi
fi
cwd=$(echo "$input" | jq -r '.cwd')

# Colors
ESC=$(printf '\033')
green="${ESC}[32m"
red="${ESC}[31m"
yellow="${ESC}[33m"
magenta="${ESC}[35m"
cyan="${ESC}[36m"
blue="${ESC}[94m"
reset="${ESC}[0m"

# Directory (abbreviated ~ for home), POSIX-safe
case "$cwd" in
    "$HOME") short_cwd="~" ;;
    "$HOME"/*) short_cwd="~${cwd#"$HOME"}" ;;
    *) short_cwd="$cwd" ;;
esac

# Git branch info
git_info=""
branch=$(GIT_OPTIONAL_LOCKS=0 git -C "$cwd" symbolic-ref --short HEAD 2>/dev/null)
if [ -n "$branch" ]; then
    git_info=" ${magenta}(${branch})${reset}"
fi

# Context usage percentage
used_pct=$(echo "$input" | jq -r '.context_window.used_percentage // empty')
if [ -z "$used_pct" ] && [ -n "$CLAUDE_CONTEXT_PERCENT" ]; then
    used_pct="$CLAUDE_CONTEXT_PERCENT"
fi
ctx_info=""
if [ -n "$used_pct" ]; then
    ctx_info=" ${cyan}$(printf "%.0f%%" "$used_pct")${reset}"
fi

# Tokens in context, rounded: 850, 58k, 1.2M
ctx_tokens=$(echo "$input" | jq -r '.context_window.total_input_tokens // empty')
if [ -n "$ctx_tokens" ]; then
    ctx_info="${ctx_info} ${cyan}($(awk -v n="$ctx_tokens" 'BEGIN {
        if (n >= 1000000) printf "%.1fM", n / 1000000
        else if (n >= 1000) printf "%.0fk", n / 1000
        else printf "%d", n }'))${reset}"
fi

# Duration as 45s, 12m, 1h16m
fmt_dur() {
    awk -v ms="$1" 'BEGIN { s = int(ms / 1000)
        if (s >= 3600) printf "%dh%02dm", s / 3600, (s % 3600) / 60
        else if (s >= 60) printf "%dm", s / 60
        else printf "%ds", s }'
}
dur_info=""
total_ms=$(echo "$input" | jq -r '.cost.total_duration_ms // empty')
api_ms=$(echo "$input" | jq -r '.cost.total_api_duration_ms // empty')
if [ -n "$total_ms" ]; then
    dur_info=" $(fmt_dur "$total_ms")"
    [ -n "$api_ms" ] && dur_info="${dur_info} (api $(fmt_dur "$api_ms"))"
fi

# Lines added / removed
lines_info=""
added=$(echo "$input" | jq -r '.cost.total_lines_added // empty')
removed=$(echo "$input" | jq -r '.cost.total_lines_removed // empty')
if [ -n "$added" ] || [ -n "$removed" ]; then
    lines_info=" ${green}+${added:-0}${reset} ${red}−${removed:-0}${reset}"
fi

# Model display name
model_name=$(echo "$input" | jq -r '.model.display_name // empty')
model_info=""
if [ -n "$model_name" ]; then
    short_model="${model_name#Claude }"
    short_model="${short_model%% *}"
    model_info="$short_model"
    effort=$(echo "$input" | jq -r '.effort.level // empty')
    [ -n "$effort" ] && model_info="$model_info($effort)"
    model_info=" ${blue}${model_info}${reset}"
fi

# Rate limit segment: label, used_percentage, resets_at (epoch seconds)
rate_seg() {
    label="$1"; key="$2"; fmt="$3"
    pct=$(echo "$input" | jq -r ".rate_limits.$key.used_percentage // empty")
    [ -z "$pct" ] && return
    pct_txt=$(printf "%.0f%%" "$pct")
    if awk -v p="$pct" 'BEGIN { exit !(p >= 80) }'; then
        pc="$red"
    elif awk -v p="$pct" 'BEGIN { exit !(p >= 50) }'; then
        pc="$yellow"
    else
        pc="$green"
    fi
    seg=" $label:${pc}${pct_txt}${reset}"
    reset_at=$(echo "$input" | jq -r ".rate_limits.$key.resets_at // empty")
    if [ -n "$reset_at" ]; then
        if [ "$fmt" = "rel" ]; then
            diff=$(( ${reset_at%.*} - $(date +%s) ))
            [ "$diff" -lt 0 ] && diff=0
            if [ "$diff" -ge 86400 ]; then
                rt="in $((diff / 86400))d $((diff % 86400 / 3600))h"
            elif [ "$diff" -ge 3600 ]; then
                rt="in $((diff / 3600))h"
            else
                rt="in $((diff / 60))m"
            fi
        else
            rt=$(date -r "${reset_at%.*}" "+$fmt" 2>/dev/null)
        fi
        [ -n "$rt" ] && seg="$seg ($rt)"
    fi
    printf "%s" "$seg"
}
rate_info="$(rate_seg 5h five_hour rel)$(rate_seg 7d seven_day rel)"

left="${yellow}${short_cwd}${reset}${git_info}${model_info}${ctx_info}${lines_info}${dur_info}"
right="${rate_info# }"

# Visible length: strip ANSI escapes, count characters (not bytes)
vis_len() {
    printf "%s" "$1" | sed "s/${ESC}\[[0-9;]*m//g" | LC_ALL=en_US.UTF-8 wc -m | tr -d ' '
}

# Terminal width: input JSON has no width field; try the tty, then $COLUMNS
cols=$( { stty size </dev/tty; } 2>/dev/null | awk '{print $2}')
case "$cols" in ''|*[!0-9]*) cols="$COLUMNS" ;; esac
case "$cols" in ''|*[!0-9]*) cols=0 ;; esac

if [ -n "$right" ]; then
    pad=4
    if [ "$cols" -gt 0 ]; then
        pad=$(( cols - 6 - $(vis_len "$left") - $(vis_len "$right") ))
        [ "$pad" -lt 1 ] && pad=1
    fi
    printf "%s%*s%s%s\n" "$left" "$pad" "" "$right" "$reset"
else
    printf "%s%s\n" "$left" "$reset"
fi
