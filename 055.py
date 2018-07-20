#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

def isPalindromic(n):
    n = str(n)
    return n == n[::-1]

def iterate(n):
    return n + int(str(n)[::-1])

def solve():
    counter = 0
    for i in range(10,int(1e4)):
        result = i
        isLychrel = True
        for j in range(50):
            result = iterate(result)
            if isPalindromic(result):
                isLychrel = False
                break
        counter += int(isLychrel)
        if not i%100: print("Probando",i)
    return counter


if __name__ == "__main__":
    assert isPalindromic(iterate(47)) == True, "First example";
    print(solve())
