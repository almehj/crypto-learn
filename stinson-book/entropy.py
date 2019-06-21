#!/usr/bin/env python3

from vig_analysis import read_ngram_table

import sys
from math import log2


def calc_entropy(freqs):

    answer = 0.0
    for k in freqs:
        p = freqs[k]
        answer += -1 * p * log2(p)
    return answer

for infile_name in sys.argv[1:]:
    with open(infile_name,"r") as infile:
        freqs = read_ngram_table(infile)
        H = calc_entropy(freqs)
        print("Table in %s has entropy of %.3f"%(infile_name,H)) 
