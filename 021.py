#!/usr/bin/python3
# https://projecteuler.net
# @author Lorenzo Moreno

def D(n):
    mydivs = []
    for i in range(1,int(n**(1/2))):
        if n%i == 0:
            #print(i)
            mydivs.append(i)
            if i != 1:
                #print(n//i)
                mydivs.append(n//i)
    return sum(mydivs)

def friends(n):
    m = D(n)
    res = (n == D(m) and n != m)
    if res:
        return n,m
    return False,False

def solve(maxi):
    listAmicable = set()
    for i in range(1,maxi):
        n,m = friends(i)
        if n:
            listAmicable.add(n)
            listAmicable.add(m)
            print(n,m," son amigos")
    return sum(listAmicable)

if __name__ == "__main__":
    assert friends(220) != (False,False), "First divisors test";
    print(solve(10000))
