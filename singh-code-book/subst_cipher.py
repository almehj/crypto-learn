#!/usr/bin/env python3

import sys

from string import ascii_uppercase

class subst_cipher:

    unknown_char = '.'
    
    def __init__(self):
        self.clear()

    def clear(self):
        self.clear2cipher = {}
        self.cipher2clear = {}
        self.base_alphabet = ascii_uppercase

    def read_from_cipher_map(self,cipher_map):
        if len(cipher_map) != len(self.base_alphabet):
            raise RuntimeError(
                "Cipher map must contain %d characters, % dprovided"%
                (len(self.base_alphabet), len(cipher_map))
            )

        for cl,ci in zip(self.base_alphabet,cipher_map):
            if ci in self.base_alphabet:
                self.add_mapping(cl,ci)
                
    def add_mapping(self,cl,ci):
        self.remove_forward_mapping(cl)
        self.remove_reverse_mapping(ci)
        self.clear2cipher[cl] = ci
        self.cipher2clear[ci] = cl
        
    def remove_forward_mapping(self,cl):
        if cl in self.clear2cipher:
            ci = self.clear2cipher[cl]
            self.cipher2clear.pop(ci)
            self.clear2cipher.pop(cl)

    def remove_reverse_mapping(self,ci):
        if ci in self.cipher2clear:
            self.remove_forward_mapping(self.cipher2clear[ci])

    def transform(self,s,char_map):
        answer = []
        for cl in s:
            if cl in self.base_alphabet:
                cl = char_map.get(cl,subst_cipher.unknown_char)
            answer.append(cl)
        return ''.join(answer)

    def encipher(self,s):
        return self.transform(s,self.clear2cipher)

    def decipher(self,s):
        return self.transform(s,self.cipher2clear)

    def show_mapping(self,**kwargs):
        outfile = kwargs.get('outfile',sys.stdout)
        prefix = kwargs.get('prefix',"")
        
        outfile.write("%s%s\n"%(prefix,self.base_alphabet))
        outfile.write("%s%s\n"%(prefix,self.encipher(self.base_alphabet)))
        
    def find_chains(self):

        chains = []
        seen = []
        for cl in self.clear2cipher:
            if cl in seen:
                continue
            chain = self.chain_from_letter(cl)
            for c in chain:
                seen.append(c)
            chains.append(chain)

        chains.sort(key=len, reverse=True)
        answer = []
        
        for new_chain in chains:
            is_substring = False
            for old_chain in answer:
                if new_chain in old_chain:
                    is_substring = True
            if not is_substring:
                answer.append(new_chain)
        
        return answer

    def chain_from_letter(self,cl):
        answer = []
        ci = cl
        while ci in self.clear2cipher:
            if ci in answer:
                break
            answer.append(ci)
            ci = self.clear2cipher[ci]
        if ci not in answer:
            answer.append(ci)
        return ''.join(answer)
        
    def __str__(self):
        return self.encipher(self.base_alphabet)


def read_ciphers_from_file(cipher_file,**kwargs):

    base_alphabet = kwargs.get('base',ascii_uppercase)
    
    answer = []
    line_num = 0
    for line in cipher_file:
        line_num += 1
        line = line.strip()

        if line[0] == '#': continue
        if len(line) != len(base_alphabet):
            sys.stderr.write("Error: Line %d has %d characters, %d expected\n"%
                             (line_num,len(line),len(base_alphabet)))
            sys.stderr.write("       Skipping line.\n")
            continue

        C = subst_cipher()
        C.read_from_cipher_map(line)
        answer.append(C)
        
    return answer

        
def main():

    cipher_filename = sys.argv[1]
    text_filename = sys.argv[2]

    ciphers = []
    with open(cipher_filename) as cipher_file:
        ciphers = read_ciphers_from_file(cipher_file)
    with open(text_filename) as infile:
        text = infile.read()
        print("Cipher text:\n")
        print(text)
        print("\n")
        for i,C in enumerate(ciphers):
            print("Cipher %d:\n"%i)
            print(C.decipher(text))
    

    

if __name__ == "__main__":
    main()

