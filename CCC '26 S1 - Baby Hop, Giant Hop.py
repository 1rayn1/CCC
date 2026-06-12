A = int(input()) #start
B = int(input()) #end
K = int(input()) #giant hop dist
T = int(input()) #fewest or second fewest

d = abs(B - A)
q, r = divmod(d, K)

if r == 0:
    best = q
else:
    best = min(q + r, q + 1 + K - r)

if T == 1:
    print(best)
else:
    if best == 0:
        print(2)
    elif r == 0:
        print(q + min(2, K - 1))
    elif abs(2 * r - K - 1) == 1:
        print(best + 1)
    else:
        print(best + 2)