#!/usr/bin/python3
# https://projecteuler.net
# @author Lorenzo Moreno

def solve(base, exp):
    return sum(map(int,str(base**exp)))
    
if __name__ == "__main__":
    assert solve(2,15) == 26, "Solve test";
    print(solve(2,1000))
