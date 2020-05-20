#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

def minGenerator(digits):
    digits = set(digits)
    result = ""
    while digits:
        menor = min(digits)
        result += menor
        digits -= set(menor)
    return result

def maxGenerator(digits):
    digits = set(digits)
    result = ""
    while digits:
        mayor = max(digits)
        result += mayor
        digits -= set(mayor)
    return result

def reduceNum(num):
    for i in range(2,len(num)+1):
        if num[-i:] != minGenerator(num[-i:]):
            part = num[-i:]
            primer = part["".join(sorted(part)).find(part[0])]
            part = primer + maxGenerator(set(part) - set(primer))
            return part

def calculaPrimos():
    global primos
    primos = [2]
    for i in range(3,2767,2):
        added = True
        for j in primos[::-1]:
            if i%j == 0:
                added = False
                break
        added and primos.append(i)

def esPrimo(x):
    x = int(x)
    return not bool(sum([(x % p) == 0 for p in primos ]))

def solve():
    calculaPrimos()
    num = "7654231"
    global listado
    listado = []
    while num != "1234567":
        part = reduceNum(num)
        num = (num[:-len(part)] + part)
        if esPrimo(num):
            return (num)

if __name__ == "__main__":
    print((solve())) #7652413