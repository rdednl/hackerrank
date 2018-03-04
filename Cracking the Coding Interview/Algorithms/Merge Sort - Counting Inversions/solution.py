import sys

def merge_sort(arr1, arr2):
    if not len(arr1) or not len(arr2):
        return arr1 or arr2
    
    res = []
    inversions = 0
    i, j = 0, 0
    
    while len(res) < len(arr1) + len(arr2):
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i = i + 1
        else:
            inversions = inversions + len(arr1) - i
            res.append(arr2[j])
            j = j + 1
        
        if i==len(arr1) or j==len(arr2):
            res.extend(arr2[j:]) or res.extend(arr1[i:])
            break
    
    return res, inversions    
    
def merge_sort_recur(arr):
    if len(arr) < 2:
        return arr, 0
    
    part1, count1 = merge_sort_recur(arr[0:int(len(arr)/2)])
    part2, count2 = merge_sort_recur(arr[int(len(arr)/2):])
    sorted_array, count = merge_sort(part1, part2)
    return sorted_array, count + count1 + count2

def countInversions(arr):
    sorted_array, nr_inversions = merge_sort_recur(arr)
    return nr_inversions
                    
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = countInversions(arr)
        print(result)