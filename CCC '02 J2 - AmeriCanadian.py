while True:
    s = input()
    if s == "quit!":
        break
    if len(s) >= 4 and s[-2:] == "or" and s[-3] not in "aeiuoy":
        s = s[:-2] + "our"
    print(s)