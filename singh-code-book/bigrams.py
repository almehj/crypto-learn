#!/usr/bin/env python

import sys

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ*"

def compute_bigram_dist(text):

    prepped_text = [c for c in text if c != '\n']
    answer = {}
    for i in range(len(prepped_text)-1):
        gram = "".join(prepped_text[i:i+2])
        if gram not in answer:
            answer[gram] = 0
        answer[gram] += 1

    ngrams = len(prepped_text)-1
    for gram in answer:
        answer[gram] = float(answer[gram])/ngrams

    return answer
            

def print_gram_table(bigram_dist):

    header = ["   %s   "%c for c in alphabet]
    print("  %s"%" ".join(header))
    for row_c in alphabet:
        row_grams = ["".join([row_c,col_c]) for col_c in alphabet]
        row_data = [bigram_dist.get(bigr,0.0) for bigr in row_grams]
        
        row_text = ["%7.5f"%x for x in row_data]
        for i,x in enumerate(row_data):
            if not x > 0.:
                row_text[i] = "       "
        print("%s %s"%(row_c," ".join(row_text)))
        
with open(sys.argv[1]) as infile:
    text = infile.read()
    bigrams = compute_bigram_dist(text)

    print_gram_table(bigrams)
    

    
