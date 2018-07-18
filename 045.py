#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#
import math

def isPentagonal(p):
        return divmod((1 + math.sqrt(1 + 24*p)),6)[1] == 0

def solve():
    for i in range(144,int(1e6)):
        hexagonal = i*(2*i-1)
        if isPentagonal(hexagonal):
            return hexagonal

if __name__ == "__main__":
    assert isPentagonal(40755) == True, "First example";
    print(solve()) # 57722156241751
