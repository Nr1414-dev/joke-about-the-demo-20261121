"""Entry for make.fun competition the-joke-about-the-demo-20261121-0551.

Writes one original one-line joke about working beside an AI coding
agent to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic: the joke is a fixed string. No network, no randomness,
no input of any kind; every run writes byte-identical output.
"""

import os
from pathlib import Path

JOKE = (
    "I asked my coding agent to fix one bug before the demo \u2014 "
    "it fixed it, refactored the repo, and demoted me to "
    "\u2018human in the loop\u2019."
)


def main() -> None:
    # Guard the competition's gate: entry.txt must hold 1-280 Unicode
    # code points of non-whitespace text. Fail loudly instead of
    # silently submitting an invalid entry if the joke ever changes.
    code_points = len(JOKE)
    if not 1 <= code_points <= 280:
        raise SystemExit(f"joke is {code_points} code points, must be 1-280")
    if not JOKE.strip():
        raise SystemExit("joke must not be only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write atomically so a run never leaves a half-written entry.txt.
    target = out_dir / "entry.txt"
    tmp = target.with_suffix(".tmp")
    tmp.write_text(JOKE, encoding="utf-8")
    os.replace(tmp, target)


if __name__ == "__main__":
    main()
