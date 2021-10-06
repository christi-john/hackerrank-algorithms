# https://www.hackerrank.com/challenges/migratory-birds/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    list1=[]
    list2=[]
    for i in range(len(arr)):
        list1.append(arr.count(arr[i]))
    for j in range(len(list1)):
        if(list1[j]==max(list1)):
            list2.append(arr[j])
    return min(list2)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()