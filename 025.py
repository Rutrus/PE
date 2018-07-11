#!/usr/bin/python3
# https://projecteuler.net
# @author Lorenzo Moreno

# @state unresolved; heavy computation

def fibo0(n, a = 0, b = 1):
    if n == 1: return b
    return fibo(n-1, b, a+b)

def fibo(n):
    a = 0
    b = 1
    c = 0
    for i in range(n-1):
        c = a+b
        a = b
        b = c
    #print(c)
    return c

def solve(limit = 1e1000):
    count = 0
    i = 0
    while count < limit:
        count = fibo(i)
        i += 1000000
    return i

def solve2():
    e = fibo(1000)/fibo(1001)
    counter = 0
    res = 1e1000
    while res >1:
        res = res/e
        counter += 1
    print(counter)

from math import e



if __name__ == "__main__":
    assert fibo(12) == 144, "Fibo";
    #print(e)
    print(len(str(fibo(int(1e10)))))
    #print(len(str(fibo(1000))))
