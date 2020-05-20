# coding=utf-8
import sys
from collections import OrderedDict

sys.stdin.reconfigure(encoding="utf-8")
all_emojis = dict()

for line in sys.stdin:
    ln = line.strip().split("\t")
    term = ln[0]
    if term == "":
        continue
    for e in ln[1].split(" ")[1:]:
        if e in all_emojis:
            all_emojis[e] += [term]
        else:
            all_emojis[e] = [term]

ordered_all_emojis = OrderedDict(sorted(all_emojis.items()))

for e in ordered_all_emojis:
    print(e, ",", ",".join(all_emojis[e]), sep="")
