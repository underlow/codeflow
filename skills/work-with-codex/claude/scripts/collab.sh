#!/bin/zsh
# Claude Code side of work-with-codex.
#
#   collab.sh start [--task develop|review] [--model M] [--effort E] [project-dir]
#                                   brief on stdin; opens Codex in a new Ghostty tab
#   collab.sh send <id>             message on stdin; types it into the Codex tab
#   collab.sh status <id>
#   collab.sh close <id>

set -euo pipefail

SELF=${0:A}
SKILL_DIR=${SELF:h:h}
ROOT=$HOME/.codex/collab

die() { print -u2 -- "collab.sh: $*"; exit 1 }
now() { date -u +%Y-%m-%dT%H:%M:%SZ }
ghostty() { osascript $SKILL_DIR/scripts/ghostty.applescript "$@" }

log() {
  jq -cn --arg t "$(now)" --arg f "$2" --arg x "$3" '{t:$t,from:$f,text:$x}' >> $1/log.jsonl
}

session() {
  local id=${1:-}
  [[ $id =~ '^[a-z0-9]+$' && -d $ROOT/$id ]] || die "no session '$id'"
  print -r -- $ROOT/$id
}

codex_tab() {
  local cx=$(<$1/codex-terminal)
  [[ $(ghostty exists $cx) == true ]] || return 1
  print -r -- $cx
}

cmd_start() {
  local -a opts
  local task=discuss model= effort= sandbox=read-only
  [[ ${SKILL_DIR:t} != delegate-to-codex ]] || task=develop
  while (( $# )); do
    case $1 in
      --task) (( $# >= 2 )) || die "--task needs a value"; task=$2; shift 2 ;;
      --model)  (( $# >= 2 )) || die "--model needs a value"; model=$2; shift 2 ;;
      --effort) (( $# >= 2 )) || die "--effort needs a value"; effort=$2; shift 2 ;;
      --*) die "unknown option $1" ;;
      *) break ;;
    esac
  done
  if [[ ${SKILL_DIR:t} == delegate-to-codex && $task == discuss ]]; then
    die "delegation task must be develop or review"
  fi
  case $task in
    discuss) ;;
    develop|review)
      [[ -n $model ]] || die "delegation requires --model; ask the user which model to use"
      [[ $task != develop ]] || sandbox=workspace-write
      ;;
    *) die "unknown task '$task': use develop or review" ;;
  esac
  local dir=${1:-$PWD}
  dir=${dir:A}
  [[ -d $dir ]] || die "no directory $dir"
  local codex_bin
  codex_bin=$(command -v codex) || die "codex is not on PATH"
  if [[ -n $model ]]; then
    command -v python3 >/dev/null || die "Python 3 is required to resolve model names"
    local selected
    local -a resolve_opts
    resolve_opts=(--codex "$codex_bin" --aliases "$ROOT/model-aliases.json")
    [[ -z $effort ]] || resolve_opts+=(--effort "$effort")
    selected=$(python3 "$SKILL_DIR/scripts/resolve-model.py" "${resolve_opts[@]}" "$model") || return $?
    print -u2 -- "collab.sh: model $model -> $selected"
    opts+=(--model "$selected")
  fi
  [[ -z $effort ]] || opts+=(-c "model_reasoning_effort=\"$effort\"")
  local sock=${CLAUDE_CODE_MESSAGING_SOCKET:-}
  [[ -S $sock ]] || die "this Claude Code session has no inbox socket, so Codex cannot reply"
  [[ -x $ROOT/collab.sh && -f $HOME/.codex/rules/collab.rules ]] ||
    die "Codex side is not installed, run ./install.sh --with-collab --force from the CodeFlow skills repository"

  local brief=$(cat)
  [[ -n $brief ]] || die "brief expected on stdin"

  local id=$(uuidgen | tr 'A-Z' 'a-z' | tr -d '-' | cut -c1-8)
  local sdir=$ROOT/$id
  mkdir -p $sdir
  print -r -- $sock > $sdir/target
  print -r -- $dir > $sdir/project
  print -r -- $task > $sdir/task

  sed -e "s|{{ID}}|$id|g" -e "s|{{SEND}}|$ROOT/collab.sh|g" $SKILL_DIR/codex-prompt.md > $sdir/prompt.md
  print -r -- $brief >> $sdir/prompt.md
  log $sdir claude-brief $brief

  # Ghostty reports no tty per terminal, so mark this tab by title and look it up.
  local tty=/dev/$(ps -o tty= -p ${sock:t:r} | tr -d ' ')
  local origin me parent_title
  origin=$(ghostty identify "$tty" "collab-$id")
  me=${origin%%$'\n'*}
  parent_title=${origin#*$'\n'}
  [[ -n $me ]] || die "cannot find this Claude Code tab in Ghostty"
  print -r -- $me > $sdir/claude-terminal

  # A tab opened through Ghostty gets Ghostty's environment, whose PATH lacks Homebrew.
  local args=${(j: :)${(@q)opts}}
  cat > $sdir/launch.sh <<EOF
#!/bin/zsh
export PATH=${(q)PATH}
${(q)codex_bin} --sandbox $sandbox --ask-for-approval on-request $args "\$(<${(q)sdir}/prompt.md)"
EOF
  chmod +x $sdir/launch.sh

  local cx
  cx=$(ghostty tab $me $sdir/launch.sh $dir "$parent_title")
  print -r -- $cx > $sdir/codex-terminal
  print -- "SESSION $id"
}

cmd_send() {
  local sdir text cx
  sdir=$(session ${1:-})
  text=$(cat)
  [[ -n $text ]] || die "message expected on stdin"
  cx=$(codex_tab $sdir) || die "the Codex tab is closed"
  ghostty input $cx "[claude] $text" >/dev/null
  ghostty key $cx enter >/dev/null
  log $sdir claude $text
  print -- "sent. End your turn; Codex's reply arrives as a new message."
}

cmd_status() {
  local sdir
  sdir=$(session ${1:-})
  if codex_tab $sdir >/dev/null; then print -- "codex tab: open"; else print -- "codex tab: closed"; fi
  print -- "messages: $(wc -l < $sdir/log.jsonl | tr -d ' ')"
  print -- "last:"
  tail -1 $sdir/log.jsonl | jq -r '"  \(.from) at \(.t): \(.text[0:300])"'
}

cmd_close() {
  local sdir cx i
  sdir=$(session ${1:-})
  rm -f $sdir/target
  if cx=$(codex_tab $sdir); then
    ghostty input $cx "/quit" >/dev/null
    ghostty key $cx enter >/dev/null
    for i in {1..20}; do
      sleep 0.25
      # After codex exits the tab is a finished command, which closes without a prompt.
      pgrep -f "$sdir/launch.sh" >/dev/null || break
    done
    ghostty close $cx >/dev/null || true
  fi
  if [[ -f $sdir/claude-terminal ]]; then ghostty focus $(<$sdir/claude-terminal) >/dev/null 2>&1 || true; fi
  rm -rf $sdir
  print -- "closed"
}

case ${1:-} in
  start)  shift; cmd_start "$@" ;;
  send)   shift; cmd_send "$@" ;;
  status) shift; cmd_status "$@" ;;
  close)  shift; cmd_close "$@" ;;
  *) die "usage: collab.sh start [--task develop|review] [--model M] [--effort E] [dir] | send <id> | status <id> | close <id>" ;;
esac
