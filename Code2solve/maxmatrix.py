def largestlocal(grid):
    n = len(grid)
    result = [[0] * (n - 2) for _ in range(n - 2)]

    for i in range(n - 2):
        for j in range(n - 2):
            max_val = float('-inf')
            for x in range(i, i + 3):
                for y in range( j, j + 3):
                    max_val = max(max_val, grid[x][y])
            result[i][j] = max_val
    
    return result