a = int(input())
b = int(input())
c = int(input())
d = int(input())

count = 0
string = ""

for i in range(d//a + 1):
    for j in range(d//b + 1):
        for k in range(d//c + 1):
            if 0 < i*a + j*b + k*c <= d:
                count += 1
                string += (f"{i} Brown Trout, {j} Northern Pike, {k} Yellow Pickerel") + "\n"

print(string)
print("Number of ways to catch fish: " + str(count))