#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    assert 2 <= len(a) <= 600
    for i in a:
        assert 1 <= i <= 2000000
    count = 0
    for i in range(0, len(a)):
        for i in range(0, len(a) - 1):
            if i == len(a) - 1:
                break
            else:
                if a[i] > a[i + 1]:
                    greater = a[i]
                    lesser = a[i + 1]
                    a[i] = lesser
                    a[i + 1] = greater
                    count = count + 1
    print("Array is sorted in " + str(count) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[len(a) - 1]))

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
