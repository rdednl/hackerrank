import numpy as np
from scipy import stats

s = int(input())
n = list(map(int, input().split()))
print(np.mean(n))
print(np.median(n))
print(int(stats.mode(n)[0]))