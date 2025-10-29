a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
count = 0
minimum = 9090909090

for i in range(e//a+1):
    for j in range(e//b+1):
        for k in range(e//c+1):
            for l in range(e//d+1):
                if i*a + j*b + k*c + l*d == e:
                    print(f"# of PINK is {i} # of GREEN is {j} # of RED is {k} # of ORANGE is {l}")
                    count += 1
                    if i+j+k+l < minimum:
                        minimum = i+j+l+k
print(f"Total combinations is {count}.")
print(f"Minimum number of tickets to print is {minimum}.")