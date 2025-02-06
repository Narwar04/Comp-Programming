rows, cols = map(int, input().split())
grid = [list(input().strip()) for _ in range(rows)]

for col in range(cols):
    bottom = rows - 1
    for row in range(rows - 1, -1, -1):
        if grid[row][col] == '#':
            bottom = row - 1
        elif grid[row][col] == 'a':
            if row != bottom:
                grid[bottom][col] = 'a'
                grid[row][col] = '.'
            bottom -= 1

for row in grid:
    print(''.join(row))