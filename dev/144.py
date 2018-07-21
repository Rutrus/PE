#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

import math
limit_x = 1e-2
limit_y = math.sqrt(100-4*limit_x**2)
limit_m = 4*limit_x/y

def lineSlope(p1, p2):
    a, b = p2[0]-p1[0],p2[1]-p1[1]
    return b/a

def intersect(r = (,), angle = None ):
    # Intersect line with elipse and get the point
    pass

def calculateAngle(r):
    # Intersect line with elipse and get the points
    # Data: line (inner or outter??)
    # Returns: angle (inner or outter)
    pass

def solve():
    pass

if __name__ == "__main__":
    assert solve() == None, "First example";
    print(solve())
