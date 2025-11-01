stop = False

lst = []

while stop is False:
    a = input()
    if a == "SCHOOL":
        break
    if a == "R":
        lst.append("L")
    elif a == "L":
        lst.append("R")
    else:
        lst.append(a)

lst.reverse()
lst.append("HOME")

stri = ""

for i in range(len(lst)):
    if lst[i] == "L":
        stri += "Turn LEFT "
    elif lst[i] == "R":
        stri += "Turn RIGHT "
    else:
        if lst[i] == "HOME":
            stri += "into your HOME."
            break
        else:
            stri += "onto " + lst[i] + " street.\n"



print(stri)
