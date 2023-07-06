#!/usr/bin/env python

import sys
import getopt
from string import ascii_uppercase as alphabet


def init_counts(n):
    answer = {}
    for i in range(n):
        answer[i] = {}
        for c in alphabet:
            answer[i][c] = 0

    return answer

def main():
    n = 1

    optlist,args = getopt.getopt(sys.argv[1:],"n:")

    for opt,val in optlist:
        if opt in ["-n"]:
            n = int(val)

    for infile_name in args:
        with open(infile_name) as infile:
            text = infile.read()
            counts = init_counts(n)
            i = 0
            for c in text:
                if c not in alphabet: continue

                counts[i][c] += 1
                i += 1
                i %= n

            for i in range(n):
                print("Slot number %d"%i)
                for c in alphabet:
                    print("  %s: %3d"%(c,counts[i][c]))
                print("\n")
                

    

if __name__ == "__main__":
    main()
