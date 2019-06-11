#!/usr/bin/env python

import sys
import getopt

def mult_inverse_mod(n,m):
    answer = -1

    while answer < m:
        if (n*answer)%m == 1:
            break
        else:
            answer += 1

    return answer%m

def main():

    m = 26
    optlist,args = getopt.getopt(sys.argv[1:],"m:")

    for opt,val in optlist:
        if opt in ["-m"]:
            m = int(val)

    for val in args:
        n = int(val)
        n_i = mult_inverse_mod(n,m)
        print("%d (== %d mod %d): %d"%(n,n%m,m,n_i))

if __name__ == "__main__":
    main()
