import math
from decimal import Decimal

def read_input():
    n = int(input())
    sheep = []
    for _ in range(n):
        x1 = Decimal(input())
        y1 = Decimal(input())
        sheep.append((x1, y1))
    return sheep

def euclidean_dist(x1, y1, x2, y2):
    dx = Decimal(x1) - x2
    dy = Decimal(y1) - y2
    return math.hypot(dx, dy)

def generate_sweep_positions(sheep):
    positions = set()
    sorted_sheep = sorted(sheep, key=lambda s: s[0])
    n = len(sorted_sheep)

    for x, _ in sorted_sheep:
        positions.add(round(Decimal(x), 6))

    for i in range(n - 1):
        x1, y1 = sorted_sheep[i]
        x2, y2 = sorted_sheep[i + 1]
        if abs(x2 - x1) < 1e-9:
            continue
        x_intersect = (x2**2 + y2**2 - x1**2 - y1**2) / (2 * (x2 - x1))
        if 0.0 <= x_intersect <= 1000.0:
            positions.add(round(x_intersect, 6))

    return sorted(positions)

def find_eaten_sheep(sheep):
    eaten = set()
    positions = generate_sweep_positions(sheep)
    for x in positions:
        min_dist = Decimal('inf')
        closest = []
        for i, (sx, sy) in enumerate(sheep):
            d = euclidean_dist(x, 0.0, sx, sy)
            if d < float(min_dist) - float(1e-8):
                min_dist = d
                closest = [i]
            elif abs(d - min_dist) <= 1e-8:
                closest.append(i)
        eaten.update(closest)
    return eaten

# Main
sheep = read_input()
eaten = find_eaten_sheep(sheep)
for i in sorted(eaten):
    x, y = sheep[i]
    print(f"The sheep at ({float(x):.2f}, {float(y):.2f}) might be eaten.")