# Read grid dimensions and number of operations
m = int(input())   # number of rows
n = int(input())   # number of columns
k = int(input())   # number of paint operations

# Arrays to count how many times each row/column is painted
row = [0] * (m + 1)
col = [0] * (n + 1)

# Process each operation
for _ in range(k):
    c, idx = input().split()  # c = 'R' or 'C', idx = row/column index
    idx = int(idx)

    if c == 'R':
        row[idx] += 1         # increment paint count for this row
    else:
        col[idx] += 1         # increment paint count for this column

# Count cells that end up painted an odd number of times
ans = 0
for i in range(1, m + 1):
    for j in range(1, n + 1):
        # A cell (i, j) is painted if row[i] + col[j] is odd
        if (row[i] + col[j]) % 2 == 1:
            ans += 1

# Output the number of painted cells
print(ans)