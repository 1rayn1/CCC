
import sys
data = sys.stdin.read().strip().split()
n = int(data[0])
l = int(data[1])
q = int(data[2])

diff = [0] * (n + 2)

idx = 3
for _ in range(l):
    p = int(data[idx]); s = int(data[idx + 1])
    idx += 2

    lo = max(1, p - s)
    hi = min(n, p + s)

    diff[lo] += 1
    diff[hi + 1] -= 1

lit = [False] * (n + 1)
total = 0
for i in range(1, n + 1):
    total += diff[i]
    lit[i] = total > 0

out = []
for _ in range(q):
    x = int(data[idx])
    idx += 1
    out.append("Y" if lit[x] else "N")

print("\n".join(out))