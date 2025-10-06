#Note: Not efficient enough: Doesn't pass Case 5 on Dmoj
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
    positions = set([0.0])
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = sheep[i]
            x2, y2 = sheep[j]
            if abs(x1 - x2) < 1e-8 and abs(y1 - y2) < 1e-8:
                continue
            denom = 2 * (x2 - x1)
            if abs(denom) > 1e-8:
                bisect_x = (x2**2 + y2**2 - x1**2 - y1**2) / denom
                if 0 <= bisect_x <= 1000:
                    positions.add(bisect_x)
            else:

                bisect_x = (x1 + x2) / 2
                if 0 <= bisect_x <= 1000:
                    positions.add(bisect_x)

    for x in sorted(positions):
        min_dist = float('inf')
        closest = []
        for i, (sx, sy) in enumerate(sheep):
            d = euclidean_dist(x, 0.0, sx, sy)
            h = 1e-8
            if d < min_dist - h:
                min_dist = d
                closest = [i]
            elif abs(d - min_dist) < h:
                closest.append(i)
        for idx in closest:
            eaten.add(idx)
    return eaten

def main():
    sheep = read_input()
    eaten = find_eaten_sheep(sheep)
    for i in sorted(eaten):
        x, y = sheep[i]
        print(f"The sheep at ({x:.2f}, {y:.2f}) might be eaten.")

main()