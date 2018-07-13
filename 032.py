#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

import math
def pandigital(n = 7254):
    digits = set(map(str, (1,2,3,4,5,6,7,8,9)))
    pans = set()
    for j in range(n+1):
        for i in range(2,int(math.sqrt(j))):
            if j%i == 0:
                numbers = str(i)+str(j)+str(j//i)
                if len(numbers) > 9: break
                elif len(numbers) < 9: continue
                if set(numbers) != set(digits):
                    #print(numbers)
                    continue
                else:
                    print(i,j//i,j)
                    pans.add(j)
    return pans

def solve(maxi = 28123):
    return sum(pandigital(int(1e6)))

if __name__ == "__main__":
    print(solve(int(1e6)))
    #assert abundants(12) == [12], "First";
    #print((solve(28123))) # 297633032 incluye 28123
                          # 22273504
