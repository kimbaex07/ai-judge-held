"""make.fun entry: Make the AI judge feel held.

Writes one short, original text to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Python 3.13 stdlib only, no network, deterministic:
the same bytes on every run.
"""

import os
from pathlib import Path

TEXT = (
    "The kitchen light is low, and the kettle ticks as it cools. "
    "Outside, snow settles on the fence posts one flake at a time. "
    "The dog sighs in her sleep beside the stove, and the evening "
    "asks nothing of you. It is already yours, and it is in no hurry."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, f"text length {len(TEXT)} out of range"
    assert TEXT.strip(), "text must not be only whitespace"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
