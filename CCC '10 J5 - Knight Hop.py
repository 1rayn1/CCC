from collections import deque
import sys

dir_8 = [(1,2),(2,1),(2,-1),(1,-2),(-1,2),(-2,1),(-2,-1),(-1,-2)]

x_start, y_start = map(int, input().split())
x_end,   y_end   = map(int, input().split())
x_start, y_start = x_start - 1, y_start - 1
x_end,   y_end = x_end   - 1, y_end   - 1

grid = [["-"]*8 for _ in range(8)]

if (x_start, y_start) == (x_end, y_end):
    print(0)
    sys.exit()

q = deque([(0, x_start, y_start)])
grid[x_start][y_start] = "X" 

while q:
    dist, row, col = q.popleft()
    for dr, dc in dir_8:
        nr, nc = row + dr, col + dc
        if 0 <= nr < 8 and 0 <= nc < 8 and grid[nr][nc] != "X":
            if (nr, nc) == (x_end, y_end):
                print(dist + 1)
                sys.exit()
            grid[nr][nc] = "X"
            q.append((dist + 1, nr, nc))
