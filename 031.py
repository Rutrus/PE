#!/usr/bin/python3
# https://projecteuler.net
# @author Lorenzo Moreno
import time
def solve(goal):
    combs = 0
    a = b = c = d = e = f = g = h = 0
    while a*200 <= goal:
        b = c = d = e = f = g = h = 0
        while a*200+b*100 <= goal:
            c = d = e = f = g = h = 0
            while a*200+b*100+c*50 <= goal:
                d = e = f = g = h = 0
                while a*200+b*100+c*50+d*20 <= goal:
                    e = f = g = h = 0
                    while a*200+b*100+c*50+d*20+e*10 <= goal:
                        f = g = h = 0
                        while a*200+b*100+c*50+d*20+e*10+f*5 <= goal:
                            g = h = 0
                            while a*200+b*100+c*50+d*20+e*10+f*5+g*2 <= goal:
                                h = 0
                                while a*200+b*100+c*50+d*20+e*10+f*5+g*2+h <= goal:
                                    if a*200+b*100+c*50+d*20+e*10+f*5+g*2+h == goal:
                                        #print(a,b,c,d,e,f,g,h)
                                        combs += 1
                                    h += 1
                                g += 1
                            f += 1
                        e += 1
                    d += 1
                c += 1
            b += 1
        a += 1
    return combs

START = time.time()
if __name__ == "__main__":
    print(solve(200)) # 73682
    print("Took",time.time()-START,"ms")
