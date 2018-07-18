#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#
import fractions
def solve():
    total_num = total_den = 1
    for i in range(10,100):
        for j in range(i,100):
            if str(i)[1]==str(j)[0]: 
                num,den = str(i)[0], str(j)[1]
                num,den = int(num), int(den)
                if num*j == den*i:
                    total_num *= num
                    total_den *= den
    return fractions.Fraction(total_num,total_den)

if __name__ == "__main__":
    print(solve())
