def altitude(h, t):
    t2 = t * t
    t3 = t2 * t
    t4 = t3 * t
    return -6 * t4 + h * t3 + 2 * t2 + t

h = int(input())
M = int(input())

for t in range(1, M + 1):
    if altitude(h, t) <= 0:
        print("The balloon first touches ground at hour:")
        print(t)
        break
else:
    print("The balloon does not touch ground in the given time.")