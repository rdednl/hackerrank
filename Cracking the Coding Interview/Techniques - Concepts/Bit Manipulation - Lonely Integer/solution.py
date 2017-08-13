#!/bin/python3

import sys

def lonely_integer(a):
    s = []
    for _ in a:
        s.remove(_) if _ in s else s.append(_)
    return s[0]

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))