#!/usr/bin/python3
# https://projecteuler.net
# @author Lorenzo Moreno


def collatz(n):
    numbers = []
    while(n > 1):
        numbers.append(n)
        if n%2:
            n = n*3+1
        else:
            n /= 2
    numbers.append(1)
    return numbers

def solve(maxi= 1e6):
    winner = 0
    longo = 0
    for i in range(int(1e6),13,-1):
        series = collatz(i)
        if len(series) > longo:
            longo = len(series)
            winner = i
            print(winner,", Longitud: ",longo)
    return winner


if __name__ == "__main__":
    assert len(collatz(13)) == 10, "First test";
    print(solve()) #837799 (525 divisors)
