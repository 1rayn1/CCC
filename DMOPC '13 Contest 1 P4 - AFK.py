from collections import deque

ti = int(input())
outputs = []

for _ in range(ti):
    COLS, ROWS = map(int, input().split())
    dir_4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    grid = [list(input().strip()) for _ in range(ROWS)]

    q = deque()
    end = None
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == "C":
                q.append((0, i, j))
                grid[i][j] = "X"   # mark start visited immediately
            elif grid[i][j] == "W":
                end = (i, j)

    # default result if unreachable or too far
    result = "#notworth"

    while q:
        dist, row, col = q.popleft()

        if (row, col) == end:
            steps = dist   
            if steps < 60:
                result = str(steps)
            else:
                result = "#notworth"
            break              

        for dr, dc in dir_4:
            new_r, new_c = row + dr, col + dc
            if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] != "X":
                grid[new_r][new_c] = "X"
                q.append((dist + 1, new_r, new_c))

    outputs.append(result)

print("\n".join(outputs))