import math

def number_needed(a, b):
    val = [0] * 26
    for _ in a:
        val[ord(_) - ord('a')]+=1
    for _ in b:
        val[ord(_) - ord('a')]-=1
    x = 0
    for _ in val:
        x += math.fabs(_)
    return x

a = input().strip()
b = input().strip()

print("%d" %(number_needed(a, b)))