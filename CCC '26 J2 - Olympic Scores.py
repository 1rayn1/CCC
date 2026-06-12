a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
lst = [a,b,c,d,e]
lst = sorted(lst)
lst.pop(0)
lst.pop(-1)
sum = 0
for yes in lst:
    sum += yes
print(sum*f) 