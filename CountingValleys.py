#!/bin/python3

import math
import os
import random
import re
import sys
def countingValleys(steps, path):
    level=0
    valley=0
    for p in path:
        if(p=='U'): 
            level+=1
        elif(p=='D'): 
            level-=1
        if(level==0 and p=='U'):
            valley+=1
    return valley




if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout 
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()