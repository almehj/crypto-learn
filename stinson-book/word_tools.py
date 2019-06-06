#!/usr/bin/env python3

import sys
import getopt
import re
from string import ascii_uppercase


def get_hat(word):
    word = prep_word(word)
    hat = [c for c in word]

    n = 0
    for c in ascii_uppercase:
        for i in range(len(word)):
            if hat[i] == c:
                hat[i] = n
                n += 1
            
    return tuple(hat)    


def get_counts(word):
    counts = {}
    for c in word:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1
    return counts

def has_pattern(word,counts=None):
    if counts == None:
        counts = get_counts(word)
    multis = [n>1 for n in list(counts.values())]

    return sum(multis) > 1

def gen_pattern(word):
    counts = get_counts(word)

    if not has_pattern(word,counts):
        return ascii_uppercase[:len(word)],0
    
    next_ndx = 0
    chars = {}
    pattern = []
    in_pattern = False
    start_ndx = 0
    last_double_ndx = 0
    for c in word:
        if counts[c] < 2 and not in_pattern:
            start_ndx += 1
            continue
        else:
            in_pattern = True
            
        if c not in chars:
            chars[c] = ascii_uppercase[next_ndx]
            next_ndx += 1

        pattern.append(chars[c])
        if counts[c] > 1:
            last_double_ndx = len(pattern) 

    pattern = ''.join(pattern[:last_double_ndx])

    return pattern,start_ndx


def find_pattern(word):
    return gen_pattern(word)
    
def prep_word(word,**kwargs):
    preserve_non_letters = kwargs.get("punct",False)

    s = word.strip()
    s = s.upper()

    if preserve_non_letters:
        return s
    else:
        return re.sub('[^%s]'%(ascii_uppercase),'',s)


def print_pattern_report(pattern_words):

    patterns = list(pattern_words.keys())
    patterns.sort()

    max_pattern_length = max([len(p) for p in patterns])
    pattern_format = "%%-%ds"%(max_pattern_length)

    for pattern in patterns:
        items = pattern_words[pattern]
        max_start_ndx = max([x[1] for x in items])        
        word_format = "%%%ds %%s %%s"%(max_start_ndx)
        pattern_str = "%s "%(pattern)

        dec_items = []
        for word,ndx in items:
            (pre,fragment,post) = (word[:ndx],
                                   word[ndx:ndx+len(pattern)],
                                   word[ndx+len(pattern):])
            dec_item = (fragment,pre,post)
            dec_items.append(dec_item)
        dec_items.sort()
        for fragment,pre,post in dec_items:
            word_data = (pre,fragment,post)
            word_str = word_format%word_data
            print("%s %s"%(pattern_str,word_str))

        print(" ")
        


def main():

    optlist,args = getopt.getopt(sys.argv[1:],"")

    pattern_words = {}
    n = 0
    
    for infile_name in args:
        with open(infile_name) as infile:
            for line in infile:
                n += 1
                if n%1000 == 0:
                    sys.stderr.write('.')
                    sys.stderr.flush()

                
                word = prep_word(line)
                if has_pattern(word):
                    (pattern,start_ndx) = gen_pattern(word)
                    if pattern not in pattern_words:
                        pattern_words[pattern] = []
                    pt = (word,start_ndx)
                    if pt not in pattern_words[pattern]:
                        pattern_words[pattern].append(pt)

    sys.stderr.write('\n')
    print_pattern_report(pattern_words)




        
if __name__ == "__main__":
    main()
    
