#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

import functools
def solve(n):
    return functools.reduce(
        lambda x, y: x+y,
        filter(lambda x: x%3 == 0 or x%5 == 0,range(n))
        )

if __name__ == "__main__":
    assert solve(10) == 23, "First example";
    print(solve(1000)) #233168
