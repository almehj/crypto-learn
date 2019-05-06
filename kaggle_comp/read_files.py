#!/usr/bin/env python3

import sys
import csv
import getopt
import string

def main():


    difficulties = []
    print_cipher = False
    optlist,args = getopt.getopt(sys.argv[1:],"d:p")
    for opt,val in optlist:
        if opt in ["-d"]:
            d = int(val)
            if d not in difficulties:
                difficulties += [d]
        elif opt in ["-p"]:
            print_cipher = True

    if difficulties == []:
        difficulties = [1,2,3,4]
        
    for infile_name in args:
        print("Trying %s"%(infile_name))
        with open(infile_name,'r') as infile:
            rdr = csv.reader(infile)
            header = next(rdr)
            for row in rdr:                
                n_chars = len(row[2])
                difficulty = int(row[1])
                if difficulty in difficulties:
                    print("Entry %s: diffculty %s, %d chars (target %s)"%
                          (row[0],row[1],n_chars,row[3]))
                    if print_cipher:
                        txt = []
                        for c in row[2]:
                            txt.append("%02x"%(ord(c)))
                                
                        print("   TEXT: %s"%" ".join(txt))

if __name__ == "__main__":
    main()

    
