# Read the grid dimensions
rows, cols = map(int, input().split())

# Read the grid
grid = [list(input().strip()) for _ in range(rows)]

# Apply gravity
for col in range(cols):
    # Start from the bottom of the column
    bottom = rows - 1
    for row in range(rows - 1, -1, -1):
        if grid[row][col] == '#':
            # Obstacle found, update the bottom position
            bottom = row - 1
        elif grid[row][col] == 'a':
            # Apple found, move it to the bottom position
            if row != bottom:
                grid[bottom][col] = 'a'
                grid[row][col] = '.'
            # Update the bottom position
            bottom -= 1

# Print the final grid
for row in grid:
    print(''.join(row))