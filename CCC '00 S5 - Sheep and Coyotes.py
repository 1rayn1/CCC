
'''
import math
a = int(input())
start_radius = 500.00
count = 0
lst = []
possible = []

for _ in range(a):
    x = int(input())
    y = int(input())
    lst.append([x,y])


def find_sheeps_in_range(radius:float)->list:
    sheeps_in_range = []
    for i in range(100000):
        pos = i/100
        if (x-pos)**2 + y**2 < radius**2:
            sheeps_in_range.append((x,y))
    return sheeps_in_range

radius = start_radius
num_of_sheep_found = 0
while True:
    if radius > 1000 or radius < 1:
        break
    sheeps_in_range = find_sheeps_in_range(radius)
    num_of_sheep_found= len(sheeps_in_range)
    if num_of_sheep_found == 1 or num_of_sheep_found ==2:
        break
    if num_of_sheep_found == 0:
        radius = 1.5*radius
    else:
        radius =  radius/2  

if num_of_sheep_found == 1:
    print(sheeps_in_range)
if num_of_sheep_found == 2:
    sheep1= sheeps_in_range[0]
    sheep2= sheeps_in_range[1]
    if math.hypot(sheep1[0]-)

        # return math.hypot(x1 - x2, y1 - y2)

#x is the x of sheep
#y is the y of sheep
#pos is where the coyote comes out
'''


EPS = 1e-9  

n = int(input().strip())
sheep = []
for _ in range(n):
    x = float(input().strip())
    y = float(input().strip())
    sheep.append((x, y))

might_be_eaten = []

for i, (x1, y1) in enumerate(sheep):
    min_x, max_x = 0.0, 1000.0

    for j, (x2, y2) in enumerate(sheep):
        if i == j:
            continue

        if abs(x1 - x2) < EPS:
            if y1 > y2:
                min_x, max_x = 1.0, 0.0  
            continue

        x_intersect = (x2*x2 - x1*x1 + y2*y2 - y1*y1) / (2.0 * (x2 - x1))

        if x2 > x1:
            max_x = min(max_x, x_intersect + EPS)
        else:
            min_x = max(min_x, x_intersect - EPS)

        if min_x > max_x + EPS:
            break

    if min_x <= max_x + EPS:
        might_be_eaten.append((x1, y1))

for x, y in sorted(might_be_eaten):
    print(f"The sheep at ({x:.2f}, {y:.2f}) might be eaten.")