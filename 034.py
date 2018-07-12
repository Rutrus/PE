#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

def factorial(n):
    num = 1
    for i in range(n,0,-1):
        num *= i
    return num


def solve(maxi = 28123):
    curiousNum = []
    for i in range(3,maxi):
        suma = sum([factorial(int(digit)) for digit in str(i)])
        if suma == i:
            print(i)
            curiousNum.append(i)
    return sum(curiousNum)

if __name__ == "__main__":
    assert factorial(4) == 24, "First";
    print((solve(int(1e6)))) # 40730
