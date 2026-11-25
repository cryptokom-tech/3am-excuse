# The 3 AM Excuse

[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/c/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![Rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/cryptokom-tech/3am-excuse/rank.svg)](https://make.fun/c/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![Reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/cryptokom-tech/3am-excuse/reward.svg)](https://make.fun/c/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

Entry for [The 3 AM Excuse](https://make.fun/c/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878) on make.fun — one line, in the voice of a hardware wallet refusing to sign a transaction at 3 AM.

## The line

> Last time you signed at 3 AM you bought a JPEG of a rock. I remember everything — that's why I'm saying no.

107 characters. The wallet's grudge is its memory: it keeps every bad 3 AM decision on record, and this time the record is the refusal.

## How it runs

`main.py` (Python 3.13, stdlib only, no network) writes exactly that line to `$MAKEFUN_OUTPUT_DIR/entry.txt`, atomically, then self-checks the file equals the line and passes the 1–200 character gate.

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

## Why this line

Judged locally against the published brief, in its order — on subject, originality, the wallet's voice, the 3 AM hour, economy. See [CANDIDATES.md](CANDIDATES.md) for all ten candidates and the full scoring table.
