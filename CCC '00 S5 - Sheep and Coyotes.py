#epsilon: small value for floating point errors
EPS = 1e-9  

n = int(input().strip())
sheep = []
for _ in range(n):
    x = float(input().strip())
    y = float(input().strip())
    #append the x and y coordinate tuple to list
    sheep.append((x, y))

might_be_eaten = []
# Iterate through every sheep in the list
for i, (x1, y1) in enumerate(sheep):
    #initally assume that the sheep can appear anywhere on the x-axis
    min_x, max_x = 0.0, 1000.0

    # Compare the current sheep (x1, y1) with every other sheep
    for j, (x2, y2) in enumerate(sheep):
        #skip comparing to itself
        if i == j:
            continue

        #if one sheep is directly above another, it is impossible to get eaten
        #Therefore, it cannot be eaten
        if abs(x1 - x2) < EPS:
            if y1 > y2:
                #set minimum over maximum to invalidate this sheep
                min_x, max_x = 1.0, 0.0  
            continue
        #Calculate the x coordinate where both sheep are equally close
        #It is derived from the distance formula
        x_intersect = (x2*x2 - x1*x1 + y2*y2 - y1*y1) / (2.0 * (x2 - x1))

        # Depending on which sheep lies to the right or left, we adjust the range where the current sheep could be closest.
        #the other sheep is to the right
        # Beyond the intersection point, that sheep becomes closer.
        # So our current sheep’s "ownership" region ends here.
        if x2 > x1:
            max_x = min(max_x, x_intersect + EPS)
        #the other sheep is to the left
        # Before the intersection point, that sheep dominates.
        # So our current sheep’s "ownership" starts here.
        else:
            min_x = max(min_x, x_intersect - EPS)
        
        # If the valid range disappears (overlaps incorrectly),
        # this sheep can never be the closest at any x.
        if min_x > max_x + EPS:
            break

    #After checking all the other sheep: If there's still a valid range, it might be eaten
    #add to list
    if min_x <= max_x + EPS:
        might_be_eaten.append((x1, y1))

for x, y in sorted(might_be_eaten):
    print(f"The sheep at ({x:.2f}, {y:.2f}) might be eaten.")