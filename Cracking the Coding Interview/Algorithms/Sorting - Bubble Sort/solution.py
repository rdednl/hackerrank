def bubble_sort(a):
    totSwaps = 0
    for i in range(len(a)):
        tmpSwaps = 0
        for j in range(len(a)-1):
            if a[j] > a[j + 1]:
                a[j + 1], a[j] = a[j], a[j + 1]
                tmpSwaps+=1
        if tmpSwaps == 0:
            return a, totSwaps
        totSwaps += tmpSwaps

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
a, tot = bubble_sort(a)
print("Array is sorted in %d swaps.\nFirst Element: %d\nLast Element: %d" %(tot, a[0], a[-1]))