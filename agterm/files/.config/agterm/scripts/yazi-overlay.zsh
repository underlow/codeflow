#!/bin/zsh
set -eu
cmd=(env "YAZI_AGTERM_SESSION=$1" "YAZI_AGTERM_PANE=$2" "YAZI_AGTERM_SOCKET=$3" zsh -lc yazi)
quoted=("${(@q)cmd}")
agtermctl session overlay open "${(j: :)quoted}" --size-percent 95 --target "$1" --socket "$3"
