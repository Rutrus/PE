#!/usr/bin/python3
# @tittle Count the different combinations of android unlocking pattern
# @author Lorenzo Moreno

# Rule0: Minimum of 4 points
# Rule1: Every number is different
# Rule2: You can't skip points visually -> No: 13; Yes: 123


import itertools
import functools

coords = {
            "1":"00", "2":"01", "3":"02",
            "4":"10", "5":"11", "6":"12",
            "7":"20", "8":"21", "9":"22",}

def rotate(iterable):
    # Given a list/tuple, returns every combinations by rotation
    pass

def isPossible(comb):
    forced = ("123","147","159","258") # Search first and last; force center.
    force = rotate((forced))
    pass

def solve(n = 9):
    combs = list(map(lambda line: "".join(line),itertools.combinations(map(str,range(1,10)),4)))
    print(len(combs))
    print(combs)

solve(20)
exit()
if __name__ == "__main__":
    #assert solve(1) == 2, "Solve test";
    #assert solve(2) == 6, "Solve test";
    assert (factorial(4)) == 24, "factorial";
    assert solve(1) == 2, "1 square";
    assert solve(2) == 6, "1 square";
    print(solve(20))
