#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

def solve():
    for i,j,k in [(i,j,(i*i+j*j)**(1/2)) for i in range(1000) for j in range(1000) if (i*i+j*j)**(1/2) == (i*i+j*j)**(1/2)]:
        if i+j+k == 1000:
            print(i,j,k)
            yield i*j*k

if __name__ == "__main__":
    #assert solve() == None, "First example";
    print(list(solve()))
