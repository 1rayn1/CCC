a = int(input())
b = input()

x = b.count("A")
y = b.count("B")

if x > y:
    print("A")
elif x < y:
    print("B")
else:
    print("Tie")