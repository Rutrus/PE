#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

def calculaPrimos():
    global primos
    primos = [2,3]
    for i in range(5,999999999,2):
        added = True
        for j in primos[::-1]:
            if i%j == 0:
                added = False
                break
        if added:
            primos.append(i)
            yield i
            
def test(num):
    if num in primos:
        return False
    for p in primos[::-1]:
        condition = ((num - p)/2) ** (1/2)
        if type(condition) == complex:
            continue
        elif condition == int(condition):
            return False
    return True


def solve():
    last = 33
    for p in calculaPrimos():
        while last < p:
            print("probando", last)
            if test(last):
                return last
            else:
                last += 2
        last += 2

if __name__ == "__main__":
    print(solve())
