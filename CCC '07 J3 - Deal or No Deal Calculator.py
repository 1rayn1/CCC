cases = int(input())

lst = [100,500,1000,5000,10000,25000,50000,100000,500000,1000000]

for j in range(cases):
    b = int(input())
    del lst[b-1-j]

c = int(input())
avg = 0
for i in range(len(lst)):
    avg += lst[i]

avg = avg/len(lst)

if c > avg:
    print("deal")
else:
    print("no deal")