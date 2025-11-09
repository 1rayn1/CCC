a = int(input())
b = int(input())
lst = []
count = 2
lst.append(a)
lst.append(b)
while True:
    count += 1
    lst.append(lst[count-3] - lst[count - 2])
    if lst[count-1] > lst[count-2]:
        break

print(count)