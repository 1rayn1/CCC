#doesn't pass 7th case
EPS = 1e-9  

n = int(input().strip())
sheep = []
for _ in range(n):
    x = int(input().strip())
    y = int(input().strip())
    sheep.append((x, y))

might_be_eaten = []

for i, (x1, y1) in enumerate(sheep):
    min_x, max_x = 0, 1000000

    for j, (x2, y2) in enumerate(sheep):
        if i == j:
            continue

        if abs(x1 - x2) < EPS:
            if y1 > y2:
                min_x, max_x = 1, 0
            continue

        x_intersect = (x2*x2 - x1*x1 + y2*y2 - y1*y1) / (2 * (x2 - x1))

        if x2 > x1:
            max_x = min(max_x, x_intersect + EPS)
        else:
            min_x = max(min_x, x_intersect - EPS)

        if min_x > max_x + EPS:
            break

    if min_x <= max_x + EPS:
        might_be_eaten.append((x1, y1))

for x, y in sorted(might_be_eaten):
    print(f"The sheep at ({x}, {y}) might be eaten.")