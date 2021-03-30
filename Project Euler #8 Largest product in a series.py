#!/bin/python3

import sys
from functools import reduce


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    result=0
    
    while len(num)>=k:
        new_string = num[0:k]
        num_list = list(map(int, list(new_string)))
        multiple_result = reduce(lambda x, y: x * y, num_list,1)
        
        if multiple_result>=result:
            result = multiple_result
        else:
            result = result
        
        num = num[1:]
        
    print(result)
        
        

        
        
