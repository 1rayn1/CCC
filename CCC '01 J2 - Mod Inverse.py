a = int(input())
b = int(input())
count = 0
boolean = False

for i in range(1,b):
    if (a*i)%b == 1:
        count = i
        boolean = True
        break
if boolean is True:
    print(count)
else:
    print("No such integer exists.")
