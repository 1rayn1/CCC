start_day, num_days = map(int, input().split())

print("Sun Mon Tue Wed Thr Fri Sat")

for _ in range(start_day - 1):
    print("    ", end="")

current_day_of_week = start_day

for day in range(1, num_days + 1):
    print(f"{day:>3}", end="")
    if current_day_of_week == 7 or day == num_days:
        print()
        current_day_of_week = 1
    else:
        print(" ", end="")
        current_day_of_week += 1