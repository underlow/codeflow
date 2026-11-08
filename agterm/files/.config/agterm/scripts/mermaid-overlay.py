#!/usr/bin/env python3
"""Render the keymap's AGT_SELECTION in a local Mermaid overlay."""
import hashlib
import html
import os
import re
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import textwrap

VERSION = "11.12.1"
SHA256 = "198b19442f86f0b46a17e56d3abf744c3a28a3427e66fa8dada3b589a77babcc"
URL = f"https://cdn.jsdelivr.net/npm/mermaid@{VERSION}/dist/mermaid.min.js"


def source_from_selection(selection):
    lines = selection.strip().splitlines()
    if lines and lines[0].strip().lower() in {"mermaid", "```mermaid", "~~~mermaid"}:
        opener = lines.pop(0).strip()
        if opener.startswith(("```", "~~~")) and lines and lines[-1].strip() == opener[:3]:
            lines.pop()
    source = textwrap.dedent("\n".join(lines)).strip()
    if not source:
        raise ValueError("Выделите код Mermaid в терминале и вызовите команду ещё раз.")
    return source


def library_path():
    cache = Path.home() / "Library/Caches/agterm-mermaid"
    cache.mkdir(parents=True, exist_ok=True)
    target = cache / f"mermaid-{VERSION}.min.js"
    if target.exists() and hashlib.sha256(target.read_bytes()).hexdigest() == SHA256:
        return target
    # Download to a unique file; interrupted or simultaneous launches cannot poison the cache.
    with tempfile.TemporaryDirectory(dir=cache) as directory:
        download = Path(directory) / "mermaid.js"
        subprocess.run(["/usr/bin/curl", "-fsSL", "--connect-timeout", "10", "--max-time", "60",
                        URL, "-o", str(download)], check=True)
        if hashlib.sha256(download.read_bytes()).hexdigest() != SHA256:
            raise ValueError("Не совпала контрольная сумма библиотеки Mermaid.")
        download.replace(target)
    return target


def page(source):
    template = Path(__file__).with_name("mermaid-overlay.html").read_text()
    # Selected terminal output is text, never executable HTML or JavaScript.
    return template.replace("<!-- MERMAID_SOURCE -->", html.escape(source))


def selected_source():
    selection = os.environ.get("AGT_SELECTION", "")
    if selection.strip():
        return source_from_selection(selection)
    # Claude's fullscreen renderer owns its selection and normally copies it on release.
    # Accept only recognisable diagram text, never an unrelated clipboard value.
    copied = subprocess.run(["/usr/bin/pbpaste"], capture_output=True, text=True, check=True).stdout
    if copied.strip():
        source = source_from_selection(copied)
        definition = "\n".join(line for line in source.splitlines() if not line.lstrip().startswith("%%")).lstrip()
        if re.match(r"(?:flowchart|graph|sequenceDiagram|classDiagram|stateDiagram(?:-v2)?|erDiagram|"
                    r"journey|gantt|pie|quadrantChart|requirementDiagram|gitGraph|mindmap|timeline|"
                    r"zenuml|sankey-beta|xychart(?:-beta)?|block-beta|packet-beta|architecture-beta|"
                    r"kanban|radar-beta|treemap-beta)\b", definition):
            return source
    raise ValueError("В Claude Code выделите код, нажмите Ctrl+Shift+C и снова вызовите Mermaid. "
                     "Либо выделите код с зажатым Shift, чтобы выделение прочитал agterm.")


def main():
    source = selected_source()
    session = os.environ.get("AGT_SESSION_ID", "")
    socket = os.environ.get("AGT_SOCKET", "")
    if not session or not socket:
        raise ValueError("Запустите Mermaid через команду или горячую клавишу agterm.")
    library = library_path()
    with tempfile.TemporaryDirectory(prefix="agterm-mermaid-") as directory:
        root = Path(directory)
        shutil.copyfile(library, root / "mermaid.min.js")
        document = root / "diagram.html"
        document.write_text(page(source))
        result = subprocess.run([
            "agtermctl", "session", "overlay", "open", "--html", str(document),
            "--cwd", directory, "--js", "--block", "--size-percent", "95",
            "--target", session, "--socket", socket,
        ], stdout=subprocess.DEVNULL)
        # --block returns 2 for normal dismissal; preserve genuine open failures.
        if result.returncode not in (0, 2):
            raise ValueError("Не удалось открыть Mermaid: проверьте, не занят ли оверлей.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"Mermaid: {error}", file=sys.stderr)
        sys.exit(1)
