#!/usr/bin/python3
# https://projecteuler.net
# @author Lorenzo Moreno

def solve(n):
    def factorial(n):
        if n==1: return 1
        return factorial(n-1)*n

    return sum(int(x) for x in str(factorial(n)))

if __name__ == "__main__":
    assert solve(4) == 6, "First divisors test";
    print(solve(100)) # 171
