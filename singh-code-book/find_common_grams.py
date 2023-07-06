#!/usr/bin/env python

import sys
import re
from string import ascii_uppercase as alphabet


def gen_ngrams(text,n,offset):
    answer = []
    i = offset
    while i < len(text):
        g = text[i:i+n]
        if len(g) == n:
            answer.append(g)
        i += n
        
    return answer
        
def count_ngrams(text,n):
    answer = {}
    for offset in range(n):
        grams = gen_ngrams(text,n,offset)
        counts = {}
        for gram in grams:
            if gram not in counts:
                counts[gram] = 0
            counts[gram] += 1
        answer[offset] = counts

    return answer


def prep_text(text):
    answer = []

    for c in text.upper():
        if c in alphabet:
            answer.append(c)
    
    return ''.join(answer)

def main():

    with open(sys.argv[1]) as infile:
        text = infile.read()
        text = prep_text(text)
        print(text)

        n = int(sys.argv[2])

        print("Looking for %dgrams"%n)
        ngrams = count_ngrams(text,n)
        for offset in range(n):
            these_grams = ngrams[offset]
            print(" Offset %d"%offset)
            for gram in these_grams:
                if these_grams[gram] > 1:
                    print("  %s:%d"%(gram,these_grams[gram]))
                    occurs = [m.start() for m in re.finditer(gram,text)]
                    line = []
                    for i in range(len(occurs)):
                        line.append(str(occurs[i]))
                        if i+1 < len(occurs):
                            line.append(" + %d = "%(occurs[i+1]-occurs[i]))
                    print("".join(line))
            

if __name__ == "__main__":
    main()
