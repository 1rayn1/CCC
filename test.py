a = input()
lst = []
stri = ""
for i in range(len(a)):
    lst.append(a[i])

lst.sort(reverse = True)
print(lst)
"""
for i in range(len(a)):
    stri += lst.pop()

print(stri)"""