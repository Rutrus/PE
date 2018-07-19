#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

import functools as f
def solve():
    return 4 * f.reduce(lambda x,y: x*y, [2,3,5,7,11,13,17,19])

if __name__ == "__main__":
    print(solve()) # 38798760