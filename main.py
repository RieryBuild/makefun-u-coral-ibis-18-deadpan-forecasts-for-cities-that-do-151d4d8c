"""Write the deadpan forecast for Grumblewick to entry.txt.

The line: tomorrow in Grumblewick is sunny with a high of 21 and
winds east at 14 km/h -- and one cloud still following the mayor
since Tuesday. The joke is a single deadpan twist at the end: the
cloud is reported like a wind reading, a stalking cloud treated as
routine meteorology, and "still" marks the stalking as old news to
the forecaster. The line is plain ASCII, commas carrying the
pivots instead of dashes.
"""

import os

LINE = "Tomorrow in Grumblewick: sunny, high of 21, winds east at 14 km/h, and one cloud still following the mayor since Tuesday."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
