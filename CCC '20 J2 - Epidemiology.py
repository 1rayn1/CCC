a = int(input())
b = int(input())
c = int(input())
d = b
day = 0

while b <= a:
    d *= c
    b += d
    day += 1
print(day)
