#!/usr/bin/env python

import sys
import getopt
from string import ascii_uppercase as alphabet


def caesar_shift(text,offset):
    answer = []

    for c in text:
        if c in alphabet:
            ndx = alphabet.index(c)
            ndx = (ndx + offset)%len(alphabet)
            answer.append(alphabet[ndx])
        else:
            answer.append(c)
            
    return ''.join(answer)


def main():

    optlist,args = getopt.getopt(sys.argv[1:],"s:a")

    offset = 0
    do_all = False
    for opt,val in optlist:
        if opt in ["-s"]:
            offset = int(val)
        elif opt in ["-a"]:
            do_all = True

    text = " ".join(args)
    if do_all:
        for i in range(len(alphabet)):
            print("%3d: %s"%(i,caesar_shift(text,i)))
    else:
        print("Offset is %d"%offset)
        print(text)
        print(caesar_shift(text,offset))

    
if __name__ == "__main__":
    main()
    
