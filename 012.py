#!/usr/bin/python3
# https://projecteuler.net
# @author https://blog.dreamshire.com/project-euler-12-solution/
## :( NOT MY CODE...

def f(L, n=42000):
	d = [0]*n
	for i in range(1, n):
		for j in range(i, n, i):
			d[j]+= 1
		c = d[i-1] * d[i//2] if i % 2 == 0 else d[(i-1)//2] * d[i]
		if c > L: return c, i*(i-1)//2


if __name__ == "__main__":
    #assert divisors(28) == 6, "First divisors test";
    #assert divisors(21) == 4, "First divisors test";
    #L = int(input("First triangular number to exceed this many divisors:"))
    Dt, t = f(500)
    print ("is", t, "(", Dt, "divisors)")
