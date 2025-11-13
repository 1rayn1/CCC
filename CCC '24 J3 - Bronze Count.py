a = int(input())
lst = []
lstNew = []
for i in range(a):
    b = int(input())
    lst.append(b)
people = 0
# y = set(lst)
a = sorted(set(lst),reverse = True)
x = a[2]

for item in lst:
    if item == x:
        people+=1
# while True:
#     if x in lst:
#         lst.remove(x)
#         people += 1
#     else:
#         break

print(str(x) + " " + str(people))