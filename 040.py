#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

import functools

def solve(n = 1e6):
    decimals = ""
    for i in range(0,int(n)):
        decimals += str(i)
        if len(decimals) > n: break
    return functools.reduce(lambda x,y:x*y, (int(decimals[10**i]) for i in range(6)))

if __name__ == "__main__":
    print((solve())) #210
