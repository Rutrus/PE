#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

def solve(n):
    def primeNumbers(n):
        global primos
        primos = [2]
        cur = 0
        for i in range(3,n):
            cur = 0
            for j,prime in enumerate(primos):
                if i%prime == 0:
                    cur = 0
                    break
                else:
                    cur = i
            if cur:
                primos.append(cur)
                if n%cur == 0:
                    print(cur)
                    yield cur
        return primos

    return max(primeNumbers(n))


if __name__ == "__main__":
    assert solve(13195) == 29, "First example";
    print(solve(600851475143)) #
