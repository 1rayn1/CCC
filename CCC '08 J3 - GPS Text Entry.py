row1 = ['A', 'B', 'C', 'D', 'E', 'F']
row2 = ['G', 'H', 'I', 'J', 'K', 'L']
row3 = ['M', 'N', 'O', 'P', 'Q', 'R']
row4 = ['S', 'T', 'U', 'V', 'W', 'X']
row5 = ['Y', 'Z', ' ', '-', '.', 'enter']

previousx = 0
previousy = 0
x = 0
y = 0
a = input()
count = 0
for i in range(len(a)):
    if a[i] in row1:
        y = 1
        x = row1.index(a[i])
    elif a[i] in row2:
        y = 2
        x = row2.index(a[i])
    elif a[i] in row3:
        y = 3
        x = row3.index(a[i])
    elif a[i] in row4:
        y = 4
        x = row4.index(a[i])
    elif a[i] in row5:
        y = 5
        x = row5.index(a[i])

    count += abs(x-previousx)
    count += abs(y-previousy)

    previousx = x
    previousy = y

count += abs(previousx - 6)

count += abs(previousy - 5)

count -= 2

print(count)