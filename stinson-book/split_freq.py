#!/usr/bin/env python3

import sys
import getopt
from string import ascii_uppercase

from ngrams import get_text,get_ngram_freqs

def main():

    n = 1
    optlist,args = getopt.getopt(sys.argv[1:],"n:")
    for opt,val in optlist:
        if opt in ['-n']:
            n = int(val)
            
    for infile_name in args:
        with open(infile_name,"r") as infile:

            text = get_text(infile)
            print("%s\n"%(''.join(text)))
            
            
            split_text = [[] for i in range(n)]

            for i,c in enumerate(text):
                split_text[i%n].append(c)

            for i,l in enumerate(split_text):
                print("Position %d:"%(i))
                print("  %s"%("".join(l)))
                dist = get_ngram_freqs(l,1)
                dist_l = [(dist[c],c) for c in dist]
                dist_l.sort(reverse=True)
                for ndx in range(min(5,len(dist))):
                    c = dist_l[ndx][1]
                    n_c = dist_l[ndx][0]
                    i_c = ascii_uppercase.index(c)
                    i_e = (i_c - 5)%len(ascii_uppercase)
                    print(" %s: %d %s"%(c,n_c,ascii_uppercase[i_e]))

if __name__ == "__main__":
    main()
            


