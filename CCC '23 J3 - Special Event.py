counts = [0] * 5
case = int(input())
for _ in range(case):
    availability = input()
    for i in range(5):
        if availability[i] == 'Y':
            counts[i] += 1

max_attendees = max(counts)

best_days = [i + 1 for i, c in enumerate(counts) if c == max_attendees]


print(",".join(map(str, best_days)))