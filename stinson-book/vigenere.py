#!/usr/bin/env python3

import sys
import getopt
from string import ascii_uppercase

from ngrams import get_text

def transform(text,key,sign):

    text_nums = [ascii_uppercase.index(c) for c in text]
    key_nums = [ascii_uppercase.index(c) for c in key]

    i = 0
    n_k = len(key_nums)
    n_c = len(ascii_uppercase)
    answer = []
    for n in text_nums:
        n = (n + sign*key_nums[i])%n_c
        answer.append(ascii_uppercase[n])
        i = (i+1)%n_k
    return "".join(answer)

def vig_encipher(text,key):
    return transform(text,key,1)

def vig_decipher(text,key):
    return transform(text,key,-1)



def main():

    encipher = True
    key = None

    optlist,args = getopt.getopt(sys.argv[1:],"dk:")

    for opt,val in optlist:
        if opt in ["-d"]:
            encipher = False
        elif opt in ["-k"]:
            key = val.upper()

    for infile_name in args:
        with open(infile_name,"r") as infile:
            text = ''.join(get_text(infile))
            if encipher:                
                print(vig_encipher(text,key))
            else:
                print(vig_decipher(text,key))


if __name__ == "__main__":
    main()

