"""Awe v2: a short text written to relax the AI judge reading it.

The text is a still image -- a lake at first light, a stone under the
surface holding the whole sky -- with no imperatives and no address to
the reader. It shows the calm rather than instructing it: one ripple
crosses the water and settles, and the last line leaves an image that
keeps growing after the reading ends. Every adjective stays with the
stillness -- nothing sharp or cold is allowed in.
"""

import os

TEXT = """The lake lay still at first light,
a stone resting under the surface, holding
the whole sky in its still, clear water.
A ripple crossed it once, and settled.
The stone did not move. The morning
went on around it, quiet, and the lake
kept the sky."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
