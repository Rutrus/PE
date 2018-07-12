#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

def solve(n,k = None):
    if k == None:
        k = n
    results = []
    for i in range(n):
        my = set((i,n-i))
        if my not in results:
            results.append(set((i,n-i)))
        print(results)
    for i in range(2,n):

        my = sorted((i,n-i-1))

if __name__ == "__main__":
    assert solve(5,2) == 3, "First example";
    assert solve(5,3) == 5, "First example";
    print(solve(200))
