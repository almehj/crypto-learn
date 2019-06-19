#!/usr/bin/env python3

import sys
from string import ascii_uppercase

from ngrams import get_text

def main():
    for infile_name in sys.argv[1:]:
        print("\n%s:"%(infile_name))
        with open(infile_name,"r") as infile:
            text = [ascii_uppercase.index(c) for c in get_text(infile)]
            
            for i in range(len(ascii_uppercase)):
                shift_text = [(x-i)%len(ascii_uppercase) for x in text]
                print(ascii_uppercase[i]+" (== %2d): "%(i)+''.join([ascii_uppercase[i] for i in shift_text]))
        
if __name__ == "__main__":
    main()
    
