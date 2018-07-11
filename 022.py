#!/usr/bin/python3
# https://projecteuler.net
# @author Lorenzo Moreno

# DATA
DATA = ""
with open("p022_names.txt") as fp:
    DATA = sorted(fp.read().replace("\"","").split(","))

def score(name):
    counter = 0
    for letter in name:
        counter += ord(letter)-64
    return counter

def solve():
    counter = 0
    for i,name in enumerate(DATA):
        counter += score(name)*(i+1)

    return counter

if __name__ == "__main__":
    assert score("COLIN") == 53, "First test";
    assert DATA.index("COLIN") == 937, "Index error"
    print(solve()) # 871198282
