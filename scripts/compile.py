# coding=utf-8
import sys
from collections import OrderedDict

sys.stdin.reconfigure(encoding="utf-8")
phrases = dict()

for line in sys.stdin:
    ln = line.strip().split(",")
    emoji = ln[0]
    if emoji == "":
        continue
    for term in ln[1:]:
        if term in phrases:
            phrases[term] += [emoji]
        else:
            phrases[term] = [emoji]

ordered_phrases = OrderedDict(sorted(phrases.items()))

for p in ordered_phrases:
    print(p, "\t", p, " ", " ".join(ordered_phrases[p]), sep="")
