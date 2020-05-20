#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

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

def propiedadDivisible(x):
    return not sum([x % y for x,y in zip([ int(x[i:i+3]) for i in range(1, 8)], [2,3,5,7,11,13,17])])


def solve():
    num = "9876543210"
    global listado
    listado = []
    i = 0
    while num != "0123456789":
        part = reduceNum(num)
        num = (num[:-len(part)] + part)
        if propiedadDivisible(num):
            listado.append(int(num))
        i += 1
        b = i % 100
        if b == 0 or b == 1 or b == 2:
            print("") if not b else ""
            print(num, end=" ")

    return (sum([int(x) for x in listado]))

    
if __name__ == "__main__":
    print((solve())) # 16695334890 [4160357289, 4130952867, 4106357289, 1460357289, 1430952867, 1406357289]