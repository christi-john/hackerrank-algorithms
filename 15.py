# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    list1=[]
    ans1=0
    ans2=0
    for i in range(len(scores)):
        list1.append(scores[i])
        if(max(list1)==scores[i] and i!=0):
            if(list1[-1]!=list1[-2]):
                ans1+=1
        elif((min(list1)==scores[i] and i!=0)):
            if(list1[-1]!=list1[-2]):
                ans2+=1
    return[ans1,ans2]

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()