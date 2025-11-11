a = int(input())
count = 1
lst = []
unique = []
result = ""

for i in range(a):
    b = input()
    b = b + " "
    for j in range(len(b)-1):
        if b[j] == b[j+1]:
            count += 1
        else:
            lst.append(count)
            unique.append(b[j])
            count = 1
    for m in range(len(lst)):
        result += str(lst[m]) + " " + str(unique[m]) + " "
    print(result.strip())
    result = ""
    lst = []
    unique = []