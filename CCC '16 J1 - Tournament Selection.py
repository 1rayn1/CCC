w = 0
for i in range(6):
    a = input("")
    if a == "W":
        w +=1
if w >=5:
    print(1)
elif w == 3 or w==4:
    print(2)
elif w == 1 or w==2:
    print(3)
else:
    print(-1)
