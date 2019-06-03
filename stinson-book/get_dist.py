#!/usr/bin/env python3

import sys
from string import ascii_uppercase 

def get_dist(text,**kwargs):
    alphabet = kwargs.get('alphabet',ascii_uppercase)

    answer = {}
    for line in text:
        for c in line:
            if c in alphabet:
                answer[c] = answer.get(c,0) + 1

    return answer

def main():
    for infile_name in sys.argv[1:]:
        with open(infile_name,"r") as infile:
            dist = get_dist(infile)
            hist = [(c,dist.get(c,0)) for c in ascii_uppercase]
            hist.sort(key=lambda t:t[1],reverse=True)
            for t in hist:
                print("%s: %3d"%t)


if __name__ == "__main__":
    main()
