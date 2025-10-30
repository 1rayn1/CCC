n = int(input())
count = 0
for i in range(6):
    for j in range(i,6):
        if i +j == n:
            count += 1

print(count)
