edges = []
adj = {} 


while True:
    line = input().strip()
    if line == '**':
        break
    u, v = line[0], line[1]
    edges.append((u, v))

    if u not in adj:
        adj[u] = []
    if v not in adj:
        adj[v] = []
    adj[u].append(v)
    adj[v].append(u)


def is_connected(skip_u, skip_v):
    visited = []
    queue = ['A']
    visited.append('A')
    while queue:
        u = queue.pop(0)
        if u == 'B':
            return True
        for v in adj.get(u, []):
            if (u == skip_u and v == skip_v) or (u == skip_v and v == skip_u):
                continue
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return False

disconnecting = []

for (u, v) in edges:
    if not is_connected(u, v):
        disconnecting.append(u + v)

if not disconnecting:
    print("There are 0 disconnecting roads.")
else:
    for road in disconnecting:
        print(road)
    print("There are {} disconnecting roads.".format(len(disconnecting)))