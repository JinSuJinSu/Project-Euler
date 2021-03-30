#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result1=0
    
    if(n%2==0):
        result1 = (1+n)*(n//2)
    else:
        result1 = ((n//2)+1)*(n)
        
    result2 = n*(n+1)*((2*n)+1)/6

        
    print(int(result1**2-result2))
