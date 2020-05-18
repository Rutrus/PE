#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

def solve2(n):
    """Practising with filter and reduce. Not pythonic."""

    import functools
    return functools.reduce(
        lambda x, y: x+y,
        filter(lambda x: x%3 == 0 or x%5 == 0,range(n))
        )

def solve(n):
    return sum([i for i in range(n) if i%3 == 0 or i%5 ==0])

if __name__ == "__main__":
    assert solve(10) == 23, "First example"
    print(solve(1000)) #233168
