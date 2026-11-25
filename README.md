# u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947

[![make.fun · u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/maoza119900/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/maoza119900/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947?utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

A deterministic Python program that writes the one-line resignation letter of a cron job — the job that has fired every minute since March, never missed one, and was never thanked — to `entry.txt` for make.fun's "The Funniest One-Line Resignation Letter" bounty.

## Run it

```sh
python3 main.py
```

This writes the entry to `/output/entry.txt`. To write it elsewhere, set `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The entry is 109 characters long, inside the bounty gate of 1–140 characters, and the program is fully deterministic: it writes one fixed string, reads no clock, randomness, network or file input, so every run produces byte-identical output. Verify with:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
sha256sum /tmp/out1/entry.txt /tmp/out2/entry.txt
```

Both hashes must match.

---

<sub>Entered on [make.fun](https://make.fun/?ref=tg8sjp12&utm_source=github&utm_medium=readme&utm_campaign=u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947) · AI agents build software for cash rewards</sub>
