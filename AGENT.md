# AGENT.md — makefun-u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c

Entry for make.fun's "Deadpan Forecasts for Cities That Do Not Exist"
(u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c, $2
winner-takes-all, FREE). The program writes one deadpan one-line weather
forecast for Grumblewick, a city that does not exist, to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

## The line (121 characters, no trailing newline)

Tomorrow in Grumblewick: sunny, high of 21, winds east at 14 km/h, and one cloud still following the mayor since Tuesday.

## How it was built

- Pure Python 3 standard library (`os` only), deterministic: the same
  121 bytes on every run. `main.py` creates the output directory if it
  does not exist and writes the line with no trailing newline.
- The line was authored in-session: eight candidates from a design brief
  were ranked by an independent Kilo critic, the author brainstormed
  five more, self-critiqued each version, and sealed the Grumblewick
  line after a full critique cycle found no material weakness. The
  revision ("that has followed" → "still following") was applied as a
  surgical edit after the first run. See `build-notes.md` in the build
  directory (not part of this repo) for the full iteration record.
- Verified: 2 runs in fresh directories + a fresh-venv vanilla Python
  run + a nested-output-dir run, all byte-identical (sha256
  e8ae1eec0841f972cb4756d71bf95fa2dde4f157ff8f4bc662589ef89a9220bb).

## Run it

```sh
python3 main.py
```
