def get_flavors(m, a):
    h = {}
    for i in range(len(a)):
        if a[i] in h:
            return h[a[i]], i+1
        h[m-a[i]] = i+1

t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    flavors = get_flavors(m, a)
    print(flavors[0], flavors[1])