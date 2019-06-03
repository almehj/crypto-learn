#!/usr/bin/env python3

import sys
import getopt
from string import ascii_uppercase

import subst_cipher

base_alphabet = ascii_uppercase
usage_str = """try_decrypt.py -d <cipher_file> [infile...]

    -d <cipher_file>: Use cipher_file for set of cipher alphabets. 
                      Cipher alphabets will rotate with each line 
                      of ciphertext in infile.

    Cipher file format:
      - Lines starting with '#' are ignored
      - Each line assumed to be a 26 character string mapping from
        ASCII A to Z
      - Unknown letters noted with a non-ASCII uppercase character, 
        typically '.'
"""

def usage():
    return usage_str


def process_file(infile,ciphers):
    n = len(ciphers)
    i = 0
    for line in infile:
        line = line.strip()
        print(line)
        print(ciphers[i].decipher(line))
        print(" ")

        i = (i + 1)%n

def main():

    cipher_file_name = None

    optlist,args = getopt.getopt(sys.argv[1:],"d:")
    for opt,val in optlist:
        if opt in ["-d"]:
            cipher_file_name = val

    if cipher_file_name == None:
        sys.stderr.write("usage: %s\n"%usage())
        sys.exit(-1)

    ciphers = []
    try:
        print("opening",cipher_file_name)
        with open(cipher_file_name,"r") as cipher_file:
            ciphers = subst_cipher.read_ciphers_from_file(cipher_file)
    except Exception as e:
        sys.stderr.write("Fatal: Error processing cipher file %s: %s\n"%
                         (cipher_file_name,e))
        
    for infile_name in args:
        with open(infile_name,"r") as infile:
            process_file(infile,ciphers)
        print("  ")

if __name__ == "__main__":
    main()
