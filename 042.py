#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

import math

def value(word):
    abc=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0
    for letter in word:
        result += abc.index(letter)
    return result

def test(word):
    positive = 1+8*value(word)
    return positive >=0 and math.modf((-1+math.sqrt(positive))/2)[0] == 0

def solve():
    with open("p042_words.txt") as fp:
        words = fp.read().replace('\"','').split(',')
        return sum(map(test,words))
        
if __name__ == "__main__":
    assert test("SKY") == True, "Error"
    assert value("SKY") == 55, "value"
    print((solve())) #162
    