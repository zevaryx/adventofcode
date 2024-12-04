with open("input.txt") as f:
    data = f.read().strip()
    
grid = data.split("\n")

rows = len(grid)
cols = len(grid[0])

count_1 = 0
count_2 = 0

def search_xmas(row, col):
    count = 0
    # Lines
    if col < cols - 3 and grid[row][col+1] == "M" and grid[row][col+2] == "A" and grid[row][col+3] == "S":
        count += 1
    if col >= 3 and grid[row][col-1] == "M" and grid[row][col-2] == "A" and grid[row][col-3] == "S":
        count += 1
    if row < rows - 3 and grid[row+1][col] == "M" and grid[row+2][col] == "A" and grid[row+3][col] == "S":
        count += 1
    if row >= 3 and grid[row-1][col] == "M" and grid[row-2][col] == "A" and grid[row-3][col] == "S":
        count += 1

    # Diags
    if row < rows - 3 and col < cols - 3 and grid[row+1][col+1] == "M" and grid[row+2][col+2] == "A" and grid[row+3][col+3] == "S":
        count += 1
    if row < rows - 3 and col >= 3 and grid[row+1][col-1] == "M" and grid[row+2][col-2] == "A" and grid[row+3][col-3] == "S":
        count += 1
    if row >= 3 and col >= 3 and grid[row-1][col-1] == "M" and grid[row-2][col-2] == "A" and grid[row-3][col-3] == "S":
        count += 1
    if row >= 3 and col < cols - 3 and grid[row-1][col+1] == "M" and grid[row-2][col+2] == "A" and grid[row-3][col+3] == "S":
        count += 1        
        
    return count
        
    
def search_x_mas(row, col):
    count = 0
    valid_one = False
    valid_two = False
    
    if 0 < row < rows-1 and 0 < col < cols-1:
        if (grid[row-1][col-1] == "M" and grid[row+1][col+1] == "S") or (grid[row-1][col-1] == "S" and grid[row+1][col+1] == "M"):
            valid_one = True
        if (grid[row-1][col+1] == "M" and grid[row+1][col-1] == "S") or (grid[row-1][col+1] == "S" and grid[row+1][col-1] == "M"):
            valid_two = True
        if valid_one and valid_two:
            count += 1
    
    return count
    
    

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "X":
            count_1 += search_xmas(i, j)
        elif grid[i][j] == "A":
            count_2 += search_x_mas(i, j)
            
            
print(count_1)
print(count_2)