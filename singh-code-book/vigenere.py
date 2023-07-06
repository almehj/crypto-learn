#!/usr/bin/env python

import sys
import getopt
from string import ascii_uppercase as alphabet

def de_vin(text,key):
    answer = []
    offsets = []
    for c in key:
        offsets.append(alphabet.index(c))
    print(offsets)
    
    i = 0
    for c in text:
        if c in alphabet:
            ci = alphabet.index(c)
            ci = (ci - offsets[i])%len(alphabet)
            answer.append(alphabet[ci])
            i += 1
            i %= len(offsets)
        else:
            answer.append(c)
        
    return ''.join(answer)
    
def main():
    key = "A"

    optlist,args = getopt.getopt(sys.argv[1:],"k:")

    for opt,val in optlist:
        if opt in ["-k"]:
            key = val
            
    print("Key is %s\n"%key)

    for infile_name in args:
        with open(infile_name) as infile:
            text = infile.read()
            print(de_vin(text,key))


if __name__ == "__main__":
    main()
