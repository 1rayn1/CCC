def creative_candy(a: str, b: str):
    i = j = 0
    na = nb = 0

    wins = {'R': 'G', 'G': 'B', 'B': 'R'}

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            na += 1
            nb += 1
            i += 1
            j += 1
        elif wins[a[i]] == b[j]:
            na += 1
            j += 1
        else:
            nb += 1
            i += 1

    na += len(a) - i
    nb += len(b) - j

    return na, nb


a = input().strip()
b = input().strip()
na, nb = creative_candy(a, b)
print(na)
print(nb)
