#!/usr/bin/env python3

import sys
import getopt

from ngrams import get_ngram_freqs,get_text

def process_file(infile_name):

    with open(infile_name,"r") as infile:
        text = get_text(infile)
        print(text)


def main():
    optlist,args = getopt.getopt(sys.argv[1:],"")

    for infile_name in args:
        process_file(infile_name)

if __name__ == "__main__":
    main()
