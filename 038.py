#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

def isPandigital(num, n):
    assert n > 1, "Must be n > 1"
    candidate = "".join([str(num * i) for i in range(1, n+1)])
    if len(candidate) == 9 and len(set(candidate)) == 9 and ('0' not in candidate):
        #print(f"Pandigital: {candidate} = {num} × {n}")
        return candidate
    return False


def estimateVector(num):
    candidate = ""
    for i in range(1, 10):
        candidate += str(num*i)
        if len(candidate) >= 9:
            return isPandigital(num, i)
    return False


def solve():
    i = 1
    winner = "0"
    while len(str(i * 1) + str(i * 2) ) <= 9:
        candidate = estimateVector(i)
        if candidate and (winner < candidate):
            winner = candidate
        i += 1
    return winner

if __name__ == "__main__":
    assert estimateVector(192) == "192384576", "First example"
    print(solve())
