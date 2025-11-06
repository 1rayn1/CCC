def count_ways(n, memo={}):
    if n == 0:
        return 1
    if n < 0:
        return 0
    
    if n in memo:
        return memo[n]
    
    memo[n] = count_ways(n - 1, memo) + count_ways(n - 2, memo) + count_ways(n - 3, memo)
    return memo[n]


total_ways = count_ways(100)

print(total_ways)