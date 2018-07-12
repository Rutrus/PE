#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#
import functools
def solve(n):
    def getPrimes(n):
        global primos
        primos = [2]
        cur = 0
        for i in range(3,n):
            cur = 0
            for prime in primos:
                if i%prime == 0:
                    cur = 0
                    break
                else:
                    cur = i
            if cur:
                primos.append(cur)
    
    def divisors(num):
        divisor = []
        for p in primos:
            if num % p == 0:
                divisor.append(p)
                divisor += divisors(num//p)
                break
        return divisor

    getPrimes(n)
    allDivisors = []
    for i in range(1,n+1):
        allDivisors.append(divisors(i))

    div = set(functools.reduce(lambda x,y:x+y,allDivisors))
    resultado = 1
    for d in div:
        maximo = 0
        for divisor in allDivisors:
            maximo = max(maximo,divisor.count(d))
        resultado *= d**maximo
    return resultado

if __name__ == "__main__":
    assert solve(10) == 2520, "First example";
    print(solve(20)) # 232792560
