#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
import time
from math import ceil, log


def print_matrix(matrix):
    for line in matrix:
        print("\t".join(map(str, line)))


def ikj_matrix_product(A, B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def add(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C


def subtract(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C


def strassenR(A, B):
    n = len(A)

    if n <= CrossOverPoint:
        return ikj_matrix_product(A, B)
    else:
        # initializing the new sub-matrices
        new_size = int(n/2)
        # print(new_size)
        a11 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        a12 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        a21 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        a22 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]

        b11 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        b12 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        b21 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        b22 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]

        # dividing the matrices in 4 sub-matrices:
        for i in range(0, new_size):
            for j in range(0, new_size):
                a11[i][j] = A[i][j]                        # top left
                a12[i][j] = A[i][j + new_size]             # top right
                a21[i][j] = A[i + new_size][j]             # bottom left
                a22[i][j] = A[i + new_size][j + new_size]  # bottom right

                b11[i][j] = B[i][j]                        # top left
                b12[i][j] = B[i][j + new_size]             # top right
                b21[i][j] = B[i + new_size][j]             # bottom left
                b22[i][j] = B[i + new_size][j + new_size]  # bottom right
        # print("\na11:")
        # print_matrix(a11)
        # print("\na12:")
        # print_matrix(a12)
        # print("\na21:")
        # print_matrix(a21)
        # print("\na22:")
        # print_matrix(a22)
        # print()

        # Calculating p1 to p7:
        p1 = strassenR(add(a11, a22), add(b11, b22))       # p1 = (a11+a22) * (b11+b22)
        p2 = strassenR(add(a21, a22), b11)                 # p2 = (a21+a22) * (b11)
        p3 = strassenR(a11, subtract(b12, b22))            # p3 = (a11) * (b12 - b22)
        p4 = strassenR(a22, subtract(b21, b11))            # p4 = (a22) * (b21 - b11)
        p5 = strassenR(add(a11, a12), b22)                 # p5 = (a11+a12) * (b22)
        p6 = strassenR(subtract(a21, a11), add(b11, b12))  # p6 = (a21-a11) * (b11+b12)
        p7 = strassenR(subtract(a12, a22), add(b21, b22))  # p7 = (a12-a22) * (b21+b22)

        # calculating c11, c12, c21, c22:
        c11 = subtract(add(add(p1, p4), p7), p5)           # c11 = p1 + p4 - p5 + p7
        c12 = add(p3, p5)                                  # c12 = p3 + p5
        c21 = add(p2, p4)                                  # c21 = p2 + p4
        c22 = subtract(add(add(p1, p3), p6), p2)           # c22 = p1 + p3 - p2 + p6

        # Grouping the results obtained in a single matrix:
        C = [[0 for j in range(0, n)] for i in range(0, n)]
        for i in range(0, new_size):
            for j in range(0, new_size):
                C[i][j] = c11[i][j]                        # top left
                C[i][j + new_size] = c12[i][j]             # top right
                C[i + new_size][j] = c21[i][j]             # bottom left
                C[i + new_size][j + new_size] = c22[i][j]  # bottom right
        return C


def strassen(A, B):
    assert type(A) == list and type(B) == list
    assert len(A) == len(A[0]) == len(B) == len(B[0])

    # Make the matrices bigger so that you can apply the strassen
    # algorithm recursively without having to deal with odd matrix sizes
    nextPowerOfTwo = lambda n: 2**int(ceil(log(n,2)))
    n = len(A)
    m = nextPowerOfTwo(n)
    APrep = [[0 for i in range(m)] for j in range(m)]
    BPrep = [[0 for i in range(m)] for j in range(m)]
    for i in range(n):
        for j in range(n):
            APrep[i][j] = A[i][j]
            BPrep[i][j] = B[i][j]
    CPrep = strassenR(APrep, BPrep)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = CPrep[i][j]
    return C

if __name__ == "__main__":
    # if sys.argv[1] != "0" or len(sys.argv) != 4:
    #     print("Try 'python3 strassen.py 0 dimension inputfile'!")
    # else:
    #     dimension = sys.argv[2]
    #     filename = sys.argv[3]

    for dimension in (32, 64, 128, 256):  # 32, 64, 128, 256, 512, 207, 105, 57

        with open("generate.txt", 'w') as wf:
            for i in range(2*dimension**2):
                wf.write(str(random.randint(-2, 2))+'\n')
    
        listA = []
        listB = []
        with open("generate.txt", 'r') as f:
            for line in f:
                # print(line)
                if len(listA) < int(dimension)**2:
                    listA.append(int(line))
                else:
                    listB.append(int(line))
        # convert listA and listB to matrix A and matrix B
        A = [[0 for j in range(int(dimension))] for i in range(int(dimension))]
        B = [[0 for j in range(int(dimension))] for i in range(int(dimension))]
        for i in range(int(dimension)):
            for j in range(int(dimension)):
                A[i][j] = listA[i*int(dimension)+j]
                B[i][j] = listB[i*int(dimension)+j]
        # print(A)
        # print(B)
    
        # run time compare
        t0 = time.time()
        ikj_matrix_product(A, B)
        t1 = time.time()
        with open("result.txt", "a") as file:
            print("dimension:", dimension)
            file.write("dimension: "+ str(dimension)+"\n")            
            print("conventional:", t1 - t0)
            file.write("conventional:"+str(t1 - t0)+"\n")            
        
            for i in range(1, 300):
                if dimension >= i:
                    CrossOverPoint = i
                    t2 = time.time()
                    C = strassen(A, B)
                    t3 = time.time()
                    print(t3 - t2, ",", CrossOverPoint)
                    file.write(str(CrossOverPoint)+","+str(t3 - t2)+"\n")
            file.write("\n")
                
        
 
    
    

    # print_matrix(A)
    # print()
    # print_matrix(B)
    # print()
    # print_matrix(C)
    # print()
    # print_matrix(ikj_matrix_product(A, B))
    # print()
    # for i in range(int(dimension)):
    #         print(C[i][i])

