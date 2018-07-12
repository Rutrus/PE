#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

def solve(n):
    result = 0
    for i in range(n,0,-1):
        result += i**i
    return str(result)[-10:]


if __name__ == "__main__":
    print((solve(1000))) #9110846700
