a = int(input())

for i in range(a):
    b,c,d = input().split()
    b = int(b)
    c = int(c)
    d = int(d)
    if b * c == d:
        print("POSSIBLE DOUBLE SIGMA")
    else:
        print("16 BIT S/W ONLY")