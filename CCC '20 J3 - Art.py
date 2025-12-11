times = int(input())
x = []
y = []
for _ in range(times):
    a,b = map(int,input().split(","))
    x.append(a)
    y.append(b)

print(str(min(x)-1) + "," + str(min(y)-1))
print(str(max(x)+ 1) + "," + str(max(y) + 1))