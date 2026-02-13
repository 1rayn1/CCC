from collections import deque

n = int(input())
grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

if grid[0][0] == 1 or grid[n-1][n-1] == 1:
    print("no")
else:
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    vis = [[False] * n for _ in range(n)]
    q = deque([(0, 0)])
    vis[0][0] = True
    
    found = False
    while q:
        r, c = q.popleft()
        if r == n - 1 and c == n - 1:
            found = True
            break
        
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and not vis[nr][nc]:
                vis[nr][nc] = True
                q.append((nr, nc))
    
    if found:
        print("yes")
    else:
        print("no")