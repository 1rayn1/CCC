'''
interactions = int(input())

time = 0
received = {}
total_wait = {}

for _ in range(interactions):
    a, b = input().split()

    if a == 'W':
        time += int(b) - 1

    elif a == 'R':
        received[b] = time
        time += 1

    elif a == 'S':
        wait_time = time - received[b]
        total_wait[b] = total_wait.get(b, 0) + wait_time
        del received[b]
        time += 1

# Print results sorted by friend number
all_friends = set(total_wait.keys()) | set(received.keys())
for friend in sorted(all_friends, key=lambda x: int(x)):
    if friend in received:
        print(friend, -1)
    else:
        print(friend, total_wait[friend])
'''


interactions = int(input())

time = 0
received = {}
total_wait = {}

for _ in range(interactions):
    a, b = input().split()

    if a == 'W':
        time += int(b) - 1
    elif a == 'R':
        #add the friend number as the key, and the time where he sent it as the value
        received[b] = time
        time += 1
    elif a == 'S':
        #look for the friend number in the recieved dictionary, and return the difference of the time values
        #add both to friend_time

        #so here we have two inputs, a and b where a signifies S, and b is the friend number.
        #look through the recieved to find friend b.

        wait_time = time - received[b]
        total_wait[b] = total_wait.get(b, 0) + wait_time
        del received[b]
        time += 1

    
# Print results sorted by friend number
all_friends = set(total_wait.keys()) | set(received.keys())
for friend in sorted(all_friends, key=lambda x: int(x)):
    if friend in received:
        print(friend, -1)
    else:
        print(friend, total_wait[friend])

'''
Sample Input:
14
R 12
W 2
R 23
W 3
R 45
S 45
R 45
S 23
R 23
W 2
S 23
R 34
S 12
S 34
'''

'''
12 13
23 8
34 2
45 -1
'''