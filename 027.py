#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

import math
def isPrime(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if not divmod(n,i)[1]: return False
    return True

def numPrimes(a,b):
    cont = 0
    for i in range(0,1000):
        num = i * i + a * i + b
        if isPrime(num):
            cont += 1
        else:
            break
    return cont

def solve():
    sol_a = sol_b = primes = 0
    for a in range(-999,1000):
        for b in range(-999,1001):
            if isPrime(b):
                primes_tmp = numPrimes(a,b)
                if primes_tmp >= primes:
                    sol_a,sol_b,primes = a,b,primes_tmp
    return sol_a * sol_b

if __name__ == "__main__":
    print(solve()) # -59231
