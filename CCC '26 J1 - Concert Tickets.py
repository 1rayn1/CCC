a = int(input())
b = int(input())
c = int(input())

remaining = b - c

if remaining >= a:
    print("Y " + str(remaining-a))
else:
    print("N")