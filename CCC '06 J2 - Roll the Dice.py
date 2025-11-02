n = min(int(input()),9)
m = min(int(input()),9)

count = max(n + m - 9,0)

if count == 1:
    print("There is " + str(count) + " way to get the sum 10.")
else:
    print("There are " + str(count) + " ways to get the sum 10.")
