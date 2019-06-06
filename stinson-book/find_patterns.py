#!/usr/bin/env python3

import sys
import getopt


from word_tools import *

def prep_line(line):
    line = line.strip()
    answer = []    
    for c in line:
        if c.isalpha():
            answer.append(c)
        else:
            answer.append(' ')
            
    return ''.join(answer)
    
def words_from_line(line):
    line = prep_line(line)
    return line.split()
    
def process_file(infile):
    seen = []
    line_num = 0
    for line in infile:
        line_num += 1
        words = words_from_line(line)
        if len(words) > 0:
            print("\n  Line %d:"%line_num)
        for word in words:
            if word in seen: continue
            seen.append(word)

            if has_pattern(word):
                pattern,start = gen_pattern(word)
                print("    %s: %s"%(word,pattern))

def main():

    optlist,args = getopt.getopt(sys.argv[1:],"")

    for infile_name in args:
        print("Looking in %s:"%infile_name)
        with open(infile_name,"r") as infile:
            process_file(infile)
            
if __name__ == "__main__":
    main()
