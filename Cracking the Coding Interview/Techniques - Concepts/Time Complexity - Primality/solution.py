from math import sqrt

def is_prime(i):
    if i == 1:
        return False
    if i <= 3:
        return True
    if i%2 == 0:
        return False
    
    for _ in range(3, int(sqrt(i))+1, 2):
        if i%_ == 0:
            return False
    
    return True

p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")