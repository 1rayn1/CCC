import sys
import collections

sys.setrecursionlimit(2000000)

def flood_fill(grid, row, col, rows, cols):
    if grid[row][col] != '.':
        return 0
    
    area = 0
    stack = collections.deque([(row, col)])
    
    while stack:
        r, c = stack.pop()
        
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '.':
            grid[r][c] = 'X' 
            area += 1
            
            stack.append((r - 1, c))
            stack.append((r + 1, c))
            stack.append((r, c - 1))
            stack.append((r, c + 1))
            
    return area

try:
    flooring = int(sys.stdin.readline())
    rows = int(sys.stdin.readline())
    cols = int(sys.stdin.readline())
    
    grid = []
    for _ in range(rows):
        line = sys.stdin.readline().strip()
        grid.append(list(line))
        
    rooms = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '.':
                area = flood_fill(grid, i, j, rows, cols)
                rooms.append(area)
                
    rooms.sort(reverse=True)
    
    room_count = 0
    for area in rooms:
        if area <= flooring:
            flooring -= area
            room_count += 1
        else:
            break
            
    s = "" if room_count == 1 else "s"
    print(f"{room_count} room{s}, {flooring} square metre(s) left over")
    
except EOFError:
    pass
except ValueError:
    pass