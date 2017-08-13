pos = {0: 1, 2: 2, 3: 4}

def possibilities(n):
    if n < 0:
        return 0
    if n not in pos:
        pos[n] = possibilities(n-1) + possibilities(n-2) + possibilities(n-3)
    return pos[n]
    

s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(possibilities(n))