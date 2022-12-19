#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    assert 1 <= grades_count <= 60
    INTEGER_ARRAY =[]
    for i in grades:
        assert 0 <= i <=100
        if int(i) < 38:
            INTEGER_ARRAY.append(i)
            continue
        for j in range(0, 101, 5):
            if j < int(i):
                continue
            elif j == i:
                INTEGER_ARRAY.append(j)
                break
            elif (j - int(i)) < 3:
                INTEGER_ARRAY.append(j)
                break
            else:
                INTEGER_ARRAY.append(i)
                break
    return INTEGER_ARRAY

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
