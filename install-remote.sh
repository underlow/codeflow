#!/bin/sh
set -eu

archive_url=https://github.com/underlow/codeflow/archive/refs/heads/main.tar.gz
tmp_dir=$(mktemp -d)
trap 'rm -rf -- "$tmp_dir"' EXIT HUP INT TERM

curl -fsSL "$archive_url" -o "$tmp_dir/codeflow.tar.gz"
tar -xzf "$tmp_dir/codeflow.tar.gz" -C "$tmp_dir"
sh "$tmp_dir/codeflow-main/install.sh" "$@"
