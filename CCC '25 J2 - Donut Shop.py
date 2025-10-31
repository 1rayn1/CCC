a = int(input())
b = int(input())

for i in range(b):
    c = input()
    d = int(input())
    if c == "+":
        a += d
    elif c == "-":
        a -= d
        
print(a)