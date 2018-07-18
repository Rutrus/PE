#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

import math
def solutions(maximo):
    results = 0
    for a in range(1,maximo//2):
        b = 0
        while (a+b < maximo):
            if maximo-a-b == math.sqrt(a*a + b*b):
                if b < a: return results
                results +=1
            b +=1
    return results

def solve(maximo):
    num,sols = 0,0
    for i in range(maximo,12,-1):
        sol_tmp = solutions(i)
        if sols <= sol_tmp:
            num, sols = i, sol_tmp
    return num

if __name__ == "__main__":
    assert solutions(120) == 3, "First example";
    print(solve(1000)) #840
