#!/usr/bin/python3
# https://projecteuler.net
# @author Lorenzo Moreno


def factorial(n):
    if n == 1: return 1
    return factorial(n-1)*n

def solve(n):
    m = n*2
    return int(factorial(m)/(factorial(m-n)*factorial(n)))

solve(20)

if __name__ == "__main__":
    #assert solve(1) == 2, "Solve test";
    #assert solve(2) == 6, "Solve test";
    assert (factorial(4)) == 24, "factorial";
    assert solve(1) == 2, "1 square";
    assert solve(2) == 6, "1 square";
    print(solve(20)) # 137846528820
