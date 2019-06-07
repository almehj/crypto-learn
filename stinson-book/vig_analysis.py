#!/usr/bin/env python3

import sys
import getopt
from string import ascii_uppercase

from coincidence import mod_split
from ngrams import get_text

def read_ngram_table(tablefile):
    answer = {}
    for line in tablefile:
        if line[0] == '#':
            continue
        bits = line.split()
        c = bits[0].strip()
        f = float(bits[2].strip())/100

        answer[ascii_uppercase.index(c)] = f

    return answer

base_dist = {}
with open("./dist1grams.dat",'r') as infile:
    base_dist = read_ngram_table(infile)

def numberize_text(text):
    return [ascii_uppercase.index(c) for c in text]

def shift_text_nums(text,n):
    return [(i + n)%len(ascii_uppercase) for i in text]

def text_from_nums(text_nums):
    return ''.join([ascii_uppercase[i] for i in text_nums])

def gen_freq_table(text):
    answer = {}
    for c in text:
        answer[c] = answer.get(c,0) + 1
    return answer

def compute_coincidence_base(text_nums):
    dist = gen_freq_table(text_nums)
    coinc = 0.
    total = sum([dist[n] for n in dist])
    for n in dist:
        f_d = dist[n]/total
        coinc += f_d*base_dist[n]

    return coinc

def process_file(infile,key_len):

    text_nums = numberize_text(get_text(infile))
    split_nums = mod_split(text_nums,key_len)

    format_str = " ".join(["%.5f"]*key_len)
    
    for k_i in range(len(ascii_uppercase)):
        curr_split = [shift_text_nums(l,-k_i) for l in split_nums]
        coincs = []
        for l in curr_split:
            coinc = compute_coincidence_base(l)
            coincs.append(coinc)
        
        coinc_str = format_str%(tuple(coincs))
        print("%s: %s"%("%2d %s"%(k_i,ascii_uppercase[k_i]),coinc_str))

        
def main():

    optlist,args = getopt.getopt(sys.argv[1:],"n:")

    key_len = 1
    for opt,val in optlist:
        if opt in ["-n"]:
            key_len = int(val)
    
    for infile_name in args:
        with open(infile_name,'r') as infile:
            process_file(infile,key_len)

if __name__ == "__main__":
    main()
