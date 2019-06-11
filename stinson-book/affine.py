#!/usr/bin/env python3

import sys
import getopt
from string import ascii_uppercase

from ngrams import get_text

def apply_affine(c,a,b):
    n = ascii_uppercase.index(c)
    n = ((a*n) + b)%len(ascii_uppercase)

    return n

def main():
    a = 1
    b = 0

    optlist,args = getopt.getopt(sys.argv[1:],"a:b:")

    for opt,val in optlist:
        if opt in ["-a"]:
            a = int(val)
        elif opt in ["-b"]:
            b = int(val)

    for infile_name in args:
        with open(infile_name,"r") as infile:
            text = get_text(infile)
            text = [apply_affine(c,a,b) for c in text]
            text = [ascii_uppercase[i] for i in text]
            
            print("".join(text))
            
    

if __name__ == "__main__":
    main()
    
