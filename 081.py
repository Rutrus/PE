#!/usr/bin/python3
# https://projecteuler.net/
# @author Lorenzo Moreno
# @license GPLv3
#

FILE = "p081_matrix.txt"

def read(FILE = FILE):
    matrix = []
    with open(FILE) as fp:
        for line in fp.read().splitlines():
            my_lines = []
            for num in line.split(","):
                my_lines.append(num)
            matrix.append(list(map(int,my_lines)))
    return matrix

def solve():
    matrix = read()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i or j:
                if i == 0:
                    matrix[i][j] += matrix[i][j-1]
                elif j == 0:
                    matrix[i][j] += matrix[i-1][j]
                else:
                    matrix[i][j] += min(matrix[i][j-1],matrix[i-1][j])
    return matrix[-1][-1]

if __name__ == "__main__":
    print(solve()) # 427337
