import sys

sys.setrecursionlimit(10000)

def is_prefix_match(a, b):
    """
    Returns True if one string is a prefix of the other.
    This is the key pruning rule: if prefixes diverge, no future extension can fix it.
    """
    if len(a) < len(b):
        return b.startswith(a)
    else:
        return a.startswith(b)

def dfs(prefixA, prefixB, depth, seq, solution, m, visited, n, A, B):
    """
    Depth - limited DFS that tries all sequences of indices < m.
    prefixA, prefixB: current concatenated strings
    depth: how many indices chosen so far
    seq: the sequence of chosen indices
    solution: list used to store the first valid solution found
    visited: memoization set to avoid repeating states
    """

    # If a solution was already found, stop exploring
    if solution:
        return

    # Success condition: non-empty and equal
    if depth > 0 and prefixA == prefixB:
        solution.extend(seq)
        return

    # Depth limit: k < m
    if depth == m - 1:
        return

    # Memoization: avoid revisiting identical states
    state = (prefixA, prefixB, depth)
    if state in visited:
        return
    visited.add(state)

    # Try all n possible next indices
    for i in range(n):
        newA = prefixA + A[i]
        newB = prefixB + B[i]

        # Prune if prefixes diverge
        if not is_prefix_match(newA, newB):
            continue

        # Recurse with updated state
        dfs(newA, newB, depth + 1, seq + [i + 1], solution, m, visited, n, A, B)

        # If solution found deeper, stop immediately
        if solution:
            return


m = int(input().strip())
n = int(input().strip())

A = [input().strip() for _ in range(n)]
B = [input().strip() for _ in range(n)]

visited = set()
solution = []

# Start DFS with empty prefixes
dfs("", "", 0, [], solution, m, visited, n, A, B)


if not solution:
    print("No solution.")
else:
    print(len(solution))
    for x in solution:
        print(x)