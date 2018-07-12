#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

def solve(maximum):
    candidates =[]
    def testPalindrome(num):
        return str(num) == str(num)[::-1]

    a = maximum
    while a >= 91:
        for i in range(a,90,-1):
            if testPalindrome(i*a):
                print(i,a,i*a)
                candidates.append(i*a)
                break
        a -= 1
    return max(candidates)


if __name__ == "__main__":
    assert solve(99) == 9009, "First example";
    print(solve(999)) #913x993=906609
