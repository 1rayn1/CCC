a = str(input())
happy = int(a .count(":-)"))
sad = int(a .count(":-("))

if happy > sad:
    print("happy")
elif sad > happy:
    print("sad")
elif sad == 0 and happy == 0:
    print("none")
else:
    print("unsure")
