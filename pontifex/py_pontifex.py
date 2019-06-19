#!/usr/bin/env python

import sys
import getopt

def process_cmd_line():
    config = {
        "decipher":False
    }
    
    optlist,args = getopt.getopt(sys.argv[1:],"d")

    for opt,val in optlist:
        if opt in ['-d']:
            config["decipher"] = True

    return config,args


    
def main():
    config,args = process_cmd_line()
    

if __name__ == "__main__":
    main()
