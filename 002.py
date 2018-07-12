#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

from functools import reduce
def solve():
    def fib():
        a, b = 1, 1
        while a < 4e6:
            yield a
            a, b = b, a + b
    return reduce(lambda x, y: x+y, filter(lambda x: x%2 == 0, fib()))

if __name__ == "__main__":
    #assert solve() == None, "First example";
    print(solve()) # 4613732
