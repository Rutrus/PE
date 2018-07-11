#!/usr/bin/python3
# https://projecteuler.net
# @author Lorenzo Moreno

import math
def d(n):
    mydivs = set()
    for i in range(int((math.sqrt(n))),1,-1):
        if n%i == 0:
            mydivs.add(i)
            mydivs.add(n//i)
    return sum(mydivs)+1

def solve():
    global abun
    abun = set()
    isolated = set()
    for num in range(1,20161+1):
        if d(num) > num: abun.add(num)
        if not any((num-i in abun) for i in abun):
            isolated.add(num)
    return sum(isolated)

if __name__ == "__main__":
    assert d(12) == 16, "First test";
    assert d(6) == 6, "Second test";
    print(solve()) #correct 4179871
