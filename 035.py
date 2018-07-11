#!/usr/bin/python3
# https://projecteuler.net
# @author Lorenzo Moreno

import math
def isPrime(n):
    return not any(n % i == 0 for i in range(2,int(math.sqrt(n))+1))

def circularPrime(n):
    n = str(n)
    for i in range(len(str(n))-1):
        n = n[-1]+n[:-1]
        if int(n) not in prime:
            return False
    return True

def solve(below):
    counter = 0
    global prime
    prime = set(filter(isPrime,range(2,below)))
    print(len(prime),"prime numbers")
    for n in prime:
        counter += circularPrime(n)
    return counter

if __name__ == "__main__":
    assert solve(100) == len([2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97]), "First test";
    print(solve(int(1e6))) # 55 # 78498 prime numbers
