#!/usr/bin/env python

import sys
import re
from string import ascii_uppercase as alphabet

def count_ngrams(text,n):
    answer = {}
    i = 0
    while i+n < len(text):
        g = text[i:i+n]
        answer[g] = answer.get(g,0)+1
        i += 1
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

        gaps = []
        for gram in ngrams:
            if ngrams[gram] > 1:
                print("  %s:%d"%(gram,ngrams[gram]))
                occurs = [m.start() for m in re.finditer(gram,text)]
                line = []
                for i in range(len(occurs) - 1):
                    gap = occurs[i+1]-occurs[i]
                    if gap not in gaps:
                        gaps.append(gap)
                    line.append(str(occurs[i]))
                    line.append(" + %d = "%(gap))
                line.append(str(occurs[-1]))
                print("".join(line))

        gaps.sort()
        print("gaps found: %s"%(" ".join(map(str,gaps))))
if __name__ == "__main__":
    main()
