#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

import math 

def isPrime(n):
    n = int(n)
    value = True
    if n == 1: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

def primes():
    for i in range(8,int(1e6)):
        if isPrime(i):
            yield i

def isTruncatable(n):
    n = str(n)
    for i in range(len(n)-1):
        if isPrime(n[i+1:]) == False or isPrime(n[:-(i+1)]) == False:
            return False
    print(n)
    return True

def solve():
    suma = 0
    counter = 0
    for p in primes():
        if isTruncatable(p):
            suma += p
            counter += 1
        if counter >= 11:
            break
    return suma

if __name__ == "__main__":
    print((solve())) #748317
