m = int(input())
ye = set()
ye.add("0,0")
x = 0
y = 0
count = 0

for k in range(m):
        line = input()
        d = line[0]
        number = line[1:]
        dx = 0
        dy = 0
        if d == 'N':
            dy = 1
        elif d == 'S':
            dy = -1
        elif d == "E":
            dx = 1
        else:
            dx = -1
        for s in range(int(number)):
            x += dx
            y += dy
            key = str(x) + "," + str(y)
            if key in ye:
                 count += 1
            else:
                 ye.add(key)
print(count)