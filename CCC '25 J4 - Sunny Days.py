n = int(input().strip())
days = [input().strip() for _ in range(n)]

left = 0
rain = 0   # number of 'P' in current window
ans = 0

for right in range(n):
    if days[right] == 'P':
        rain += 1

    while rain > 1:
        if days[left] == 'P':
            rain -= 1
        left += 1

    ans = max(ans, right - left + 1)

if 'P' not in days:
    ans -= 1

print(ans)
