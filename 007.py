#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

def solve(n):
    primos = [2]
    cur = 0
    for i in range(3,int(1e20)):
        cur = 0
        for j,prime in enumerate(primos):
            if i%prime == 0:
                cur = 0
                break
            else:
                cur = i
        if cur:
            primos.append(cur)
        if len(primos) == n:
            return cur
    return primos

if __name__ == "__main__":
    assert solve(6) == 13, "First example";
    print(solve(10001)) #104743
