#!/usr/bin/env python

import sys
import getopt
from string import ascii_uppercase as alphabet

def get_counts(infile):
    answer = {}
    for c in alphabet:
        answer[c] =0

    for line in infile:
        for c in line:
            if c in alphabet:
                answer[c] += 1

    return answer

def print_count_report(counts):
    for c in alphabet:
        print("%c (%2d): %s"%(c,counts[c],"".join(['*']*counts[c])))


def main():

    optlist,args = getopt.getopt(sys.argv[1:],"")

    for infile_name in args:
        with open(infile_name,"r") as infile:
            counts = get_counts(infile)
            print_count_report(counts)


if __name__ == "__main__":
    main()

