#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps=0
    index=0
    while index<len(c):
        #try jumping 2 clouds
        if(index+2<len(c) and c[index+2]==0):
            index+=2
            jumps+=1
        #try jumping 1 cloud if 2 clouds are not feasible
        elif(index+1 <len(c) and c[index+1]==0):
            index+=1
            jumps+=1
        #if you land on last cloud break out of the loop and return result
        if(index==len(c)-1):
            break
    return jumps

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout 
    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
