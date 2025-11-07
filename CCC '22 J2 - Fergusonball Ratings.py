a = int(input())
lst = []
count = 0
for i in range(a):
    z = 0
    x = int(input())
    y = int(input())
    z += x*5 - 3*y
    lst.append(z)
    if z > 40:
        count += 1

if count == a:
    print(str(count) + "+")
else:
    print(str(count))
