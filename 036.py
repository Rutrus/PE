#!/usr/bin/python3
# https://projecteuler.net
# @author Lorenzo Moreno

import functools as f
def palindromic(n):
    print(str(bin(n))[2:],str(bin(n))[:1:-1])
    return str(n) == str(n)[::-1] and str(bin(n))[2:] == str(bin(n))[:1:-1]

def solve():
    return sum(filter(palindromic,range(int(1e6))))

if __name__ == "__main__":
    assert palindromic(585) == True, "First test";
    print(solve()) # 872187
