#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    assert 1 <= n <= 1000
    x = arr[n - 1]
    y = 0
    for i in range(n - 1, 0, -1):
        if i == 1 and arr[0] > x:
            j = arr[1]
            arr[i] = arr[i - 1]
            for i in arr:
                print(i, end=" ")
            print("")
            arr[1] = j
            z = arr[0]
            arr[0] = x
            arr[1] = z
            for p in arr:
                print(p, end=" ")
            print("")
            break
        if y != 0:
            break
        assert -10000 <= arr[i] <= 10000
        if x <= arr[i - 1]:
            arr[i] = arr[i - 1]
            #for i in arr:
            #    print(i, end=" ")
            #print("")
        else:
            arr[i] = x
            y += 1
        for i in arr:
            print(i, end=" ")
        print("")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
