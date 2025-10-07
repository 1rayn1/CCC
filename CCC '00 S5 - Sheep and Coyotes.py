import math

def read_input():
    n = int(input())
    sheep = []
    for _ in range(n):
        x = float(input())
        y = float(input())
        sheep.append((x, y))
    return sheep

def euclidean_dist(x1, y1, x2, y2):
    return math.hypot(x1 - x2, y1 - y2)

def find_eaten_sheep(sheep):
    eaten = set()
    n = len(sheep)
    positions = set([0])
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = sheep[i]
            x2, y2 = sheep[j]
            if abs(x1 - x2) <= 0 and abs(y1 - y2) <= 0:
                continue
            try:
                bisect_x = (x2 * x2 + y2 * y2 - x1 * x1 - y1 * y1) / (2 * (x2 - x1))
            except ZeroDivisionError:
                bisect_x = x1
            if 0 <= bisect_x <= 1000:
                positions.add(bisect_x)

    for x in sorted(positions):
        min_dist = float('inf')
        closest = []
        for i, (sx, sy) in enumerate(sheep):
            d = euclidean_dist(x, 0, sx, sy)
            if d <= min_dist:
                min_dist = d
                closest = [i]
        for idx in closest:
            eaten.add(idx)
    return eaten

sheep = read_input()
eaten = find_eaten_sheep(sheep)
for i in sorted(eaten):
    x, y = sheep[i]
    print(f"The sheep at ({x:.2f}, {y:.2f}) might be eaten.")