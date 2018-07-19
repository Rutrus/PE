#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

from fractions import Fraction

def primeSieve(n = 1e6):
    primes = [2]
    for i in range(2,int(n)):
        isPrime = True
        for prime in primes:
            if i%prime == 0:
                isPrime = False
        if isPrime:
            primes.append(i)

def ratio():
    for d in range(12,int(1e6)):
        if not d%100: print(d)
        counter = 0
        for i in range(1,d):
            counter += int(Fraction(i,d).denominator == d)
        ratio = counter/(d-1)

def solve():
    solution = 1e6
        if ratio < 15499/94744:
            solution = min(solution,d)
            print("SOLUTION:",solution, "FOR D:", d)
    return solution

if __name__ == "__main__":
    #assert solve() == None, "First example";
    print(solve())
