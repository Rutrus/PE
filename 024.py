#!/usr/bin/python3
# https://projecteuler.net
# @author Lorenzo Moreno


def factorial(n):
    if n <= 1: return 1
    return factorial(n-1)*n

def solve(n = 10,target = 1e6):
    options = [0,1,2,3,4,5,6,7,8,9]
    result = []
    target -=1

    for i in range(n-1,-1,-1):
        facto = factorial(i)
        divisor = int(target//facto)
        target = int(target%facto)
        result.append(options.pop(divisor))
    return result

if __name__ == "__main__":
    assert solve(3,6) == [2,1,0], "Three numbers";
    print(solve(10,1e6)) # 2783915460
