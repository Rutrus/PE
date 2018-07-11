#!/usr/bin/python3
# https://projecteuler.net
# @author Lorenzo Moreno

def dlen(number):
    mydict = {
        "1" : "one",
        "2" : "two",
        "3" : "three",
        "4" : "four",
        "5" : "five",
        "6" : "six",
        "7" : "seven",
        "8" : "eight",
        "9" : "nine",
        "10" : "ten",
        "11" : "eleven",
        "12" : "twelve",
        "13" : "thirteen",
        "14" : "fourteen",
        "15" : "fifteen",
        "16" : "sixteen",
        "17" : "seventeen",
        "18" : "eighteen",
        "19" : "nineteen",
        "20" : "twenty",
        "30" : "thirty",
        "40" : "forty",
        "50" : "fifty",
        "60" : "sixty",
        "70" : "seventy",
        "80" : "eighty",
        "90" : "ninety",
        "00" : "",
        "0"  : "",
        }
    print(mydict[number],end="")
    return len(mydict[number])

def counter(num):
    counter = 0
    txt = ""

    while True:
        num = str(num)
        l = len(num)
        if l == 4:
            txt = "ONETHOUSAND"
            counter += len(txt)
            print(txt)
            break
        elif l == 3:
            txt = "HUNDRED"
            if num[1:] != "00":
                txt += "AND"
            counter += dlen(num[0])+len(txt)
        elif l == 2:
            if int(num) < 10:
                counter += dlen(num[1])
            elif int(num) < 20:
                counter += dlen(num)
            else:
                counter += dlen(num[0]+"0") + dlen(num[1])
            break
        elif l == 1:
            counter += dlen(num)
            break
        num = num[1:]
        print(txt,end="")

    return counter

def solve():
    sumat = 0
    for i in range(1,1001):
        print()
        print(i,end=": ")
        sumat += counter(i)
    return sumat

if __name__ == "__main__":
    assert dlen("1") == len("one"), "Solve test";
    assert counter("21") == len("twentyone"), "Solve test";
    assert counter("581") == len("fivehundredandeightyone"), "Solve test";
    print(solve()) # Right answer: 21124
