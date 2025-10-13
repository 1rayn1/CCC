import math
import random

def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def circle_from(points):
    """Return circle (cx, cy, r) from 0–3 points."""
    if not points:
        return (0.0, 0.0, 0.0)
    if len(points) == 1:
        return (points[0][0], points[0][1], 0.0)
    if len(points) == 2:
        (x1, y1), (x2, y2) = points
        cx, cy = (x1 + x2) / 2.0, (y1 + y2) / 2.0
        r = dist((x1, y1), (x2, y2)) / 2.0
        return (cx, cy, r)
    # 3 points → circumcircle
    (x1, y1), (x2, y2), (x3, y3) = points
    d = 2 * (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
    if abs(d) < 1e-12:
        # Collinear: pick largest circle from 2 points
        best = None
        max_r = -1
        for i in range(3):
            for j in range(i+1, 3):
                c = circle_from([points[i], points[j]])
                if c[2] > max_r:
                    best = c
                    max_r = c[2]
        return best
    ux = ((x1**2 + y1**2)*(y2 - y3) + (x2**2 + y2**2)*(y3 - y1) + (x3**2 + y3**2)*(y1 - y2)) / d
    uy = ((x1**2 + y1**2)*(x3 - x2) + (x2**2 + y2**2)*(x1 - x3) + (x3**2 + y3**2)*(x2 - x1)) / d
    r = dist((ux, uy), (x1, y1))
    return (ux, uy, r)

def is_in_circle(p, circle):
    cx, cy, r = circle
    return dist(p, (cx, cy)) <= r + 1e-8

def welzl(P, R):
    if not P or len(R) == 3:
        return circle_from(R)
    p = P.pop()
    D = welzl(P, R)
    if is_in_circle(p, D):
        P.append(p)
        return D
    R.append(p)
    D2 = welzl(P, R)
    R.pop()
    P.append(p)
    return D2

n = int(input().strip())
points = [tuple(map(float, input().split())) for _ in range(n)]

random.shuffle(points)
circle = welzl(points[:], [])
diameter = circle[2] * 2

print(f"{diameter:.2f}")