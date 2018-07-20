#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

UNITS = ["I","X","C","M"]
FIVES = ["V","L","D"]

def saveChars(roman):
    for i,letter in enumerate(UNITS[:-1]):
        if roman.count(letter) < 4: continue
        roman = roman.replace(letter*5,FIVES[i])
        roman = roman.replace(FIVES[i]+letter*4,letter+UNITS[i+1])
        roman = roman.replace(letter*4,letter+FIVES[i])
        roman = roman.replace(FIVES[i]*2,UNITS[i+1])
    return roman

def solve():
    saved = 0
    with open("p089_roman.txt") as fp:
        for line in fp.readlines():
            my_line = line.strip()
            saved += len(my_line)-len(saveChars(my_line))
    return saved

if __name__ == "__main__":
    print(solve())