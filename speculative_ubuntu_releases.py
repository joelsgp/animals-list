#!/usr/bin/python

"""Scry to discover the complete future of Ubuntu release names!"""

from random import shuffle
from string import capwords

from lines import animals


def name_filter(animal: str) -> bool:
    words = animal.split()
    if len(words) != 2:
        return False
    if words[0][0] != words[1][0]:
        return False
    return True


new_releases = filter(name_filter, animals)
new_releases = list(new_releases)
shuffle(new_releases)

number = 26.04
for rel in new_releases:
    print(f"Ubuntu {number} {capwords(rel)}")
    number += 2
