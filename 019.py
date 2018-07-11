#!/usr/bin/python3
# https://projecteuler.net
# @author Lorenzo Moreno

def isLeap(year):
    return (year%4 == 0) and (year%100 != 0) or (year%400 == 0)

def solve():
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    dow = 1 # Starts in Monday
    counter = 0
    for year in range(1900,2001):
        leap = isLeap(year)
        for i,month in enumerate(months):
            if i == 2 and leap:
                dow += 1
            dow = (dow) % 7
            if dow == 0 and year > 1900:
                counter += 1
                print("Month ",i+1," of ",year," starts in Sunday")
            dow += month
    return counter

if __name__ == "__main__":
    #assert divisors(28) == 6, "First divisors test";
    #assert divisors(21) == 4, "First divisors test";
    print(solve()) # 171
