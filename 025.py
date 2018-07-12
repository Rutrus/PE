#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

def fibo(n):
    a=b=1
    while n > 2:
        c = a+b
        a = b
        b = c
        n -= 1
    return b

def solve(n):

    for i in range(n,0,-1):
        digits = len(str(fibo(i)))
        #print(i,digits)
        if digits < 1000: return i+1


if __name__ == "__main__":
    #assert solve() == None, "First example";
    print((solve(5000))) #4782
