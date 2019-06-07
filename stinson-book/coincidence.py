#!/usr/bin/env python3

import sys
import getopt
import re

from ngrams import get_ngram_freqs,get_text

def compute_coinicidence(text,**kwargs):
    dist = get_ngram_freqs(text,1)
    total = sum([dist[c] for c in dist])
    answer = 0.0
    for c in dist:
        f = dist[c]/total
        answer += f*f

    return answer

def mod_split(l,m):
    answer = [[] for i in range(m)]
    for i,c in enumerate(l):
        answer[i%m].append(c)
    return answer

def process_file(infile_name,key_len):

    with open(infile_name,"r") as infile:
        text = get_text(infile)

        split_text = mod_split(text,key_len)
        for i,seg in enumerate(split_text):
            print("%d: %.5f"%(i,compute_coinicidence(seg)))
        
def main():
    optlist,args = getopt.getopt(sys.argv[1:],"n:")

    key_len = 1    
    for opt,val in optlist:
        if opt in ["-n"]:
            key_len = int(val)
    
    for infile_name in args:
        process_file(infile_name,key_len)

if __name__ == "__main__":
    main()
