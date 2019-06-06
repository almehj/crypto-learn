#!/usr/bin/env python3

import sys
import getopt
import re

from ngrams import get_ngram_freqs,get_text

def process_file(infile_name):

    with open(infile_name,"r") as infile:
        text = get_text(infile)
        text_str = ''.join(text)
        n = 3
        while True:
            n_dist = get_ngram_freqs(text,n)
            n_list = [g for g in n_dist if n_dist[g] > 1]
            if len(n_list) > 0:
                for g in n_list:
                    ndxs = [m.start() for m in re.finditer(g,text_str)]
                    diffs = [t[0]-t[1] for t in zip(ndxs[1:],ndxs)]
                    print("%s: %s"%(g," ".join([str(d) for d in diffs])))
            else:
                break
            n += 1


def main():
    optlist,args = getopt.getopt(sys.argv[1:],"")

    for infile_name in args:
        process_file(infile_name)

if __name__ == "__main__":
    main()
