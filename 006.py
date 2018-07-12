#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

def solve(n):
    return sum(range(n+1))**2-sum([x**2 for x in range(n+1)])

if __name__ == "__main__":
    assert solve(10) == 2640, "First example";
    print(solve(100)) # 25164150
