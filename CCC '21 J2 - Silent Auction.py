a = int(input())
top = 0
top_l = ""
for i in range(a):
    c = input()
    b = int(input())
    if b > top:
        top = b
        top_l = c

print(top_l)