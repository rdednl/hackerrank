def getBiggestRegion(grid):
    biggest = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            biggest = max(biggest, recur(grid, i, j))
    return biggest
            
def recur(grid, i, j):
    if not(i in range(len(grid)) and j in range(len(grid[0]))):
        return 0
    if grid[i][j] == 0:
        return 0

    count = 1
    grid[i][j] = 0

    count += recur(grid, i - 1, j - 1)
    count += recur(grid, i - 1, j)
    count += recur(grid, i - 1, j + 1)
    count += recur(grid, i, j - 1)
    count += recur(grid, i, j + 1)
    count += recur(grid, i + 1, j - 1)
    count += recur(grid, i + 1, j)
    count += recur(grid, i + 1, j + 1)
    return count

n = int(input().strip())
m = int(input().strip())
grid = []
current = 0
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
    
print(getBiggestRegion(grid))
