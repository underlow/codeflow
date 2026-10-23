#!/bin/sh
set -eu

usage() {
  echo "Usage: ./install.sh [--target DIR] [--with-collab] [--force]" >&2
  exit 2
}

target=${HOME:?}
with_collab=false
force=false
while [ "$#" -gt 0 ]; do
  case "$1" in
    --target) [ "$#" -ge 2 ] || usage; target=$2; shift 2 ;;
    --with-collab) with_collab=true; shift ;;
    --force) force=true; shift ;;
    *) usage ;;
  esac
done

[ -d "$target" ] || { echo "Target does not exist: $target" >&2; exit 1; }
target=$(cd "$target" && pwd)
case "$target" in /*) ;; *) usage ;; esac
source_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

claude_backlog=$target/.claude/skills/backlog
codex_backlog=$target/.agents/skills/backlog
claude_designer=$target/.claude/skills/talk-to-designer
codex_designer=$target/.agents/skills/talk-to-designer
for path in "$claude_backlog" "$codex_backlog" "$claude_designer" "$codex_designer"; do
  if { [ -e "$path" ] || [ -L "$path" ]; } && [ "$force" = false ]; then
    echo "Already exists: $path (use --force to replace)" >&2
    exit 1
  fi
done

claude_flow=$target/.claude/skills/flow
codex_flow=$target/.agents/skills/flow
claude_project=$target/.claude/skills/project
codex_project=$target/.agents/skills/project
claude_architecture_review=$target/.claude/skills/architecture-review
codex_architecture_review=$target/.agents/skills/architecture-review
claude_collab=$target/.claude/skills/work-with-codex
claude_delegate=$target/.claude/skills/delegate-to-codex
codex_sender=$target/.codex/collab/collab.sh
codex_rule=$target/.codex/rules/collab.rules

for path in "$claude_flow" "$codex_flow" "$claude_project" "$codex_project" \
  "$claude_architecture_review" "$codex_architecture_review"; do
  if { [ -e "$path" ] || [ -L "$path" ]; } && [ "$force" = false ]; then
    echo "Already exists: $path (use --force to replace)" >&2
    exit 1
  fi
done
if [ "$with_collab" = true ]; then
  for path in "$claude_collab" "$claude_delegate" "$codex_sender" "$codex_rule"; do
    if { [ -e "$path" ] || [ -L "$path" ]; } && [ "$force" = false ]; then
      echo "Already exists: $path (use --force to replace)" >&2
      exit 1
    fi
  done
fi

mkdir -p "$target/.claude/skills" "$target/.agents/skills"
for platform in claude codex; do
  if [ "$platform" = claude ]; then destination=$claude_flow; else destination=$codex_flow; fi
  [ "$force" = false ] || rm -rf -- "$destination"
  mkdir -p "$destination"
  cp -R "$source_dir/skills/flow/shared/." "$destination/"
  cp -R "$source_dir/skills/flow/$platform/." "$destination/"
  echo "Installed $destination"
done

for platform in claude codex; do
  if [ "$platform" = claude ]; then destination=$claude_designer; else destination=$codex_designer; fi
  [ "$force" = false ] || rm -rf -- "$destination"
  mkdir -p "$destination"
  cp -R "$source_dir/skills/talk-to-designer/shared/." "$destination/"
  cp -R "$source_dir/skills/talk-to-designer/$platform/." "$destination/"
  echo "Installed $destination"
done

for platform in claude codex; do
  if [ "$platform" = claude ]; then destination=$claude_project; else destination=$codex_project; fi
  [ "$force" = false ] || rm -rf -- "$destination"
  mkdir -p "$destination"
  cp -R "$source_dir/skills/underlow/project/shared/." "$destination/"
  cp -R "$source_dir/skills/underlow/project/$platform/." "$destination/"
  echo "Installed $destination"
done

for platform in claude codex; do
  if [ "$platform" = claude ]; then destination=$claude_architecture_review; else destination=$codex_architecture_review; fi
  [ "$force" = false ] || rm -rf -- "$destination"
  mkdir -p "$destination"
  cp -R "$source_dir/skills/architecture-review/shared/." "$destination/"
  cp -R "$source_dir/skills/architecture-review/$platform/." "$destination/"
  echo "Installed $destination"
done

if [ "$with_collab" = true ]; then
  [ "$force" = false ] || rm -rf -- "$claude_collab"
  mkdir -p "$claude_collab" "$target/.codex/collab" "$target/.codex/rules"
  cp -R "$source_dir/skills/work-with-codex/claude/." "$claude_collab/"
  [ "$force" = false ] || rm -rf -- "$claude_delegate"
  mkdir -p "$claude_delegate"
  cp -R "$source_dir/skills/delegate-to-codex/claude/." "$claude_delegate/"
  cp -R "$source_dir/skills/work-with-codex/claude/scripts" "$claude_delegate/"
  cp "$source_dir/skills/work-with-codex/codex/collab.sh" "$codex_sender"
  chmod +x "$claude_collab/scripts/collab.sh" "$claude_delegate/scripts/collab.sh" "$codex_sender"
  printf 'prefix_rule(pattern=["%s"], decision="allow")\n' "$codex_sender" > "$codex_rule"
  echo "Installed $claude_collab"
  echo "Installed $claude_delegate"
  echo "Installed $codex_sender and $codex_rule"
fi

for platform in claude codex; do
  if [ "$platform" = claude ]; then destination=$claude_backlog; else destination=$codex_backlog; fi
  [ "$force" = false ] || rm -rf -- "$destination"
  mkdir -p "$destination"
  cp -R "$source_dir/skills/underlow/backlog/shared/." "$destination/"
  cp -R "$source_dir/skills/underlow/backlog/$platform/." "$destination/"
  echo "Installed $destination"
done
