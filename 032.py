#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

def pandigital(n):
    digits = {1,2,3,4,5,6,7,8,9}
    pans = set()
    for i in range(2,n):
        if n%i == 0 and digits-(set(i)+set(n)+set(n//i)) == {}:
            print(i,"*",n//i,"=",n)
            pans.add(n)
    print(pans)
    return pans

def solve(maxi = 28123):
    return sum(pandigital(int(1e6)))

if __name__ == "__main__":

    #assert abundants(12) == [12], "First";
    print((solve(28123))) # 297633032 incluye 28123
                          # 22273504
