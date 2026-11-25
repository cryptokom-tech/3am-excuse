"""The 3 AM Excuse — make.fun entry.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: the excuse a hardware
wallet gives for refusing to sign a transaction at 3 AM.
Stdlib only, no network, deterministic.
"""

import os

LINE = "Last time you signed at 3 AM you bought a JPEG of a rock. I remember everything \u2014 that's why I'm saying no."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.replace(tmp, path)
    # Self-check: the file must be exactly the line and pass the gate.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt differs from LINE"
    assert 1 <= len(written) <= 200 and written.strip(), "gate failed"


if __name__ == "__main__":
    main()
