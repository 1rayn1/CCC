number_of_initial_brooks = int(input())
brook_numbers = []
for _ in range(number_of_initial_brooks):
    brook_numbers.append(int(input()))

while True:
    command = int(input())
    if command == 77:
        break
    elif command == 99:
        brook_to_split = int(input())
        percent = int(input())
        left = brook_numbers[brook_to_split - 1] * percent / 100
        right = brook_numbers[brook_to_split - 1] * (1 - percent / 100)
        brook_numbers[brook_to_split - 1] = left
        brook_numbers.insert(brook_to_split, right)
    elif command == 88:
        brook_to_join = int(input())
        brook_numbers[brook_to_join - 1] += brook_numbers[brook_to_join]
        brook_numbers.pop(brook_to_join)

for value in brook_numbers:
    print(int(round(value)), end=" ")
print()