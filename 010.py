#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

def solve(n):
    primos = [2]
    cur = 0
    for i in range(3,int(n)):
        if i%1000 == 0:
            print(len(primos))
        cur = 0
        for j,prime in enumerate(primos):
            if i%prime == 0:
                cur = 0
                break
            else:
                cur = i
        if cur:
            primos.append(cur)
    return sum(primos)

if __name__ == "__main__":
    assert solve(10) == 17, "First example";
    print(solve(2e6)) #
