#!/bin/zsh
set -eu
[[ -n ${YAZI_AGTERM_SESSION:-} && -n ${YAZI_AGTERM_PANE:-} && -n ${YAZI_AGTERM_SOCKET:-} ]]
printf '%s' "${(q)1}" | /opt/homebrew/bin/agtermctl session type --stdin --target "$YAZI_AGTERM_SESSION" --pane-id "$YAZI_AGTERM_PANE" --socket "$YAZI_AGTERM_SOCKET"
