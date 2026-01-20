L = int(input())

for _ in range(L):
    n = int(input())
    names = [input().strip() for _ in range(n)]

    level = {} 
    max_level = 0

    root = names[-1]
    level[root] = 1

    if n > 1:
        level[names[0]] = 2
        previous = names[0]
        max_level = max(max_level, level[names[0]] - 1)
    else:
        previous = root

    for j in range(1, n):
        name = names[j]
        if name not in level or level[name] == 0:
            level[name] = level[previous] + 1
            max_level = max(max_level, level[name] - 1)
        previous = name

    print(n * 10 - max_level * 20)