#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

def solve(maxi):
    suma = set()
    for a in range(2, maxi+1):
        for b in range(2, maxi+1):
            suma.add(a**b)
    return len(suma)

if __name__ == "__main__":
    assert solve(5) == 15, "First";
    print((solve(100))) # 669171001
