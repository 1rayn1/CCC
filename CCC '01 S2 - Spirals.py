start = int(input())
end = int(input())

size = 101 
grid = [[0] * size for _ in range(size)]
r = c = size // 2 
grid[r][c] = start

num = start + 1
step = 1
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] 
min_r = max_r = r
min_c = max_c = c

while num <= end:
    for d in directions:
        for _ in range(step):
            if num > end:
                break
            r += d[0]
            c += d[1]
            grid[r][c] = num
            num += 1
            min_r = min(min_r, r)
            max_r = max(max_r, r)
            min_c = min(min_c, c)
            max_c = max(max_c, c)
        if d in [(0, 1), (0, -1)]:  # Increase step after right and left
            step += 1

    # Print the spiral
for i in range(min_r, max_r + 1):
    row = []
    for j in range(min_c, max_c + 1):
        if grid[i][j] == 0:
            row.append("   ")
        else:
            row.append(f"{grid[i][j]:>3}")
    print(" ".join(row))

