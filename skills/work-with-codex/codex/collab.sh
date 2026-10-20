#!/bin/sh
# Codex runs this outside its sandbox (see ~/.codex/rules/collab.rules), so it
# accepts only a session id and text, and sends only to the socket Claude wrote.
set -eu

case $# in
  1) id=$1; text=$(cat) ;;
  2) id=$1; text=$2 ;;
  *) echo "usage: collab.sh <session-id> <message>   or   collab.sh <session-id> < message" >&2; exit 2 ;;
esac
[ -n "$text" ] || { echo "collab.sh: empty message" >&2; exit 2; }

case $id in '' | *[!a-z0-9]*) echo "collab.sh: bad session id" >&2; exit 2 ;; esac
dir=$(dirname "$0")/$id
[ -f "$dir/target" ] || { echo "collab.sh: no session $id - Claude closed it" >&2; exit 3; }
target=$(cat "$dir/target")

case $target in
  /tmp/cc-socks/[0-9]*.sock | /tmp/cc-socks-[0-9]*/[0-9]*.sock) ;;
  *) echo "collab.sh: refusing target $target" >&2; exit 2 ;;
esac
[ -S "$target" ] || { echo "collab.sh: the Claude session is gone" >&2; exit 3; }

if ! jq -cn --arg c "[codex $id] $text" '{type:"user",message:{role:"user",content:$c}}' |
  nc -U -w 2 "$target" >/dev/null 2>&1; then
  echo "collab.sh: cannot reach Claude: the command did not match the pre-approved rule." >&2
  echo "Send it again as one single-quoted argument with no ' inside (write ’ for an apostrophe)." >&2
  exit 4
fi
jq -cn --arg t "$(date -u +%Y-%m-%dT%H:%M:%SZ)" --arg x "$text" '{t:$t,from:"codex",text:$x}' >> "$dir/log.jsonl"
echo "sent to Claude. Stop here and wait for its reply."
