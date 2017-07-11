#!/bin/python3
import bisect
import sys

def eval_median(a):
    if len(a)%2==0:
        return (a[len(a)//2]+a[(len(a)//2)-1])/2
    else:
        return a[len(a)//2]

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    bisect.insort(a, a_t)
    print("%.1f" %(eval_median(a)))