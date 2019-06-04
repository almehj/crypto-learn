#!/usr/bin/env python3

import sys
import getopt
from string import ascii_uppercase

def get_text(infile,**kwargs):
    alphabet = kwargs.get('alphabet',ascii_uppercase)
    return [c for c in infile.read() if c in alphabet]
            

def get_digraph_freqs(infile):
    text = get_text(infile)

    digraphs = zip(text,text[1:])
    answer = {}
    for d in digraphs:
        answer[d] = answer.get(d,0) + 1
    return answer

def main():
    for infile_name in sys.argv[1:]:
        with open(infile_name,"r") as infile:
            print("%s:"%(infile_name))

            dist = get_digraph_freqs(infile)
            total = sum([dist[k] for k in dist])
            hist = [(d,dist.get(d,0)) for d in dist]
            hist.sort(key=lambda t:t[1],reverse=True)
            for d,n in hist:
                print("%s: %3d %5.3f"%("".join(d),n,n/total))


            
if __name__ == "__main__":
    main()
