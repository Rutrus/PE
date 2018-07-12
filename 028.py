#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

def solve(l):
    suma = 1
    for i in range(3,l+1,2):
        for j in range(4):
            suma += i*i - (i-1)*j
    return suma

if __name__ == "__main__":
    assert solve(5) == 101, "First";
    print((solve(1001))) # 669171001
