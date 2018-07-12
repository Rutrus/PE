#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

def solve(power):
    suma = 0
    for i in range(2,int(1e6)):
        counter = 0

        for num in str(i):
            counter += int(num)**power
            if counter > i : break
        if counter == i:
            suma += counter
            print(counter)
    return suma

if __name__ == "__main__":
    print((solve(5))) #9110846700
