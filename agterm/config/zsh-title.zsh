# agterm: idle terminal title; command and application titles stay dynamic.
if [[ "$AGTERM_ENABLED" == 1 ]]; then
  ZSH_THEME_TERM_TAB_TITLE_IDLE='Ghostty'
  ZSH_THEME_TERM_TITLE_IDLE='Ghostty'
  # Normalize the launch title after Oh My Zsh's command-title hook.
  _agterm_codex_title() {
    emulate -L zsh
    local -a args
    args=("${(@Q)${(z)1}}")
    while (( $#args )) && [[ ${args[1]} == *=* || ${args[1]} == command || ${args[1]} == env ]]; do
      args[1]=()
    done
    if [[ ${args[1]:t} == codex ]]; then
      printf '\e]0;Codex\a'
    fi
  }
  autoload -Uz add-zsh-hook
  add-zsh-hook preexec _agterm_codex_title
fi
