#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    jumps = 0
    while len(c) > 1:
        if len(c) > 2:
            if c[2] == 0:
                c.pop(0)
                c.pop(0)
                jumps += 1
            else:
                c.pop(0)
                jumps += 1
        elif len(c) == 2:
            if c[1] == 0:
                c.pop(0)
                jumps += 1
            else:
                break

    return jumps
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
