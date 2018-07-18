#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#
import time

start = time.time()
N_DECIMALS = 2000
import math
def digitsCycle(decimalsList):
    decimalsList = "".join(map(str,decimalsList))
    pos = set()
    for i in range(1,N_DECIMALS):
        value = decimalsList.find(decimalsList[-i-1:])
        if value in pos:
            break
        else:
            pos.add(value)        
    return len(pos)

def decimals(divisor):
    list_ = []
    c = r = 1
    cycle = 0
    while r != 0:
        c, r = divmod(10*r,divisor)
        list_.append(c)
        if not len(list_) % N_DECIMALS:
            cycle = digitsCycle(list_)
            break
    return cycle

def isPrime(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if not divmod(n,i)[1]: return False
    return True

def solve(m):
    num, max_ = 0,0
    for i in range(3,m,2):
        if isPrime(i):
            tmp = decimals(i)
            if tmp > max_:
                num, max_ = i, tmp
    print("Número", num, "tiene", max_, "ciclos")
    return num

if __name__ == "__main__":
    assert decimals(7) == 6, "Seven" 
    print(solve(1000))
print(time.time()-start,"seconds")