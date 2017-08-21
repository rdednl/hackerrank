s = int(input())
w = list(map(int, input().split()))
n = list(map(int, input().split()))
print(round(sum([w[_]*n[_] for _ in range(s)])/sum(n), 1))