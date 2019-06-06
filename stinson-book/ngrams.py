#!/usr/bin/env python3

import sys
import getopt
from string import ascii_uppercase

def get_text(infile,**kwargs):
    alphabet = kwargs.get('alphabet',ascii_uppercase)
    return [c for c in infile.read() if c in alphabet]
            

def get_ngrams(text,n):
    answer = []
    if len(text) < n:
        return answer

    offset_text = [text[i:] for i in range(n)]
    n_grams = min([len(l) for l in offset_text])

    for i in range(n_grams):
        gram = "".join([l[i] for l in offset_text])
        answer.append(gram)

    return answer

def get_ngram_freqs(text,n):
    answer = {}
    for i in range(len(text) - n + 1):
        gram = "".join(text[i:i+n])
        answer[gram] = answer.get(gram,0) + 1

    return answer

def main():

    optlist,args = getopt.getopt(sys.argv[1:],"n:")

    n = 2
    for opt,val in optlist:
        if opt in ["-n"]:
            n = int(val)
    
    for infile_name in args:
        with open(infile_name,"r") as infile:
            print("# %s:"%(infile_name))

            text = get_text(infile)
            dist = get_ngram_freqs(text,n)

            total = sum([dist[k] for k in dist])
            width = max([len(str(dist[k])) for k in dist])
            fmt = "%%s: %%%dd %%5.3f"%(width)
            hist = [(d,dist.get(d,0)) for d in dist]
            hist.sort(key=lambda t:t[1],reverse=True)
            for d,n in hist:
                print(fmt%("".join(d),n,100.*n/total))


            
if __name__ == "__main__":
    main()
