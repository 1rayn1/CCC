distance = int(input())
clubs = int(input())
club_powers = []
for _ in range(clubs):
    club_powers.append(int(input()))

# DP array: dp[i] = min strokes to reach i metres, -1 if unreachable
dp = [-1] * (distance + 1)
dp[0] = 0

#sample input:
#100 = distance
#3 = clubs
#66 = club 1
#33 = club 2
#1 = club 3
for i in range(distance + 1):
    if dp[i] != -1:
        for power in club_powers:
            next_dist = i + power
            if next_dist <= distance:
                if dp[next_dist] == -1 or dp[next_dist] > dp[i] + 1:
                    dp[next_dist] = dp[i] + 1

if dp[distance] != -1:
    print(f"Roberta wins in {dp[distance]} strokes.")
else:
    print("Roberta acknowledges defeat.")