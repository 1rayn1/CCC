def numDivisors(n):
    count = 0
    for i in range(1,int(n**0.5)+1):
        if n% i == 0:
            count +=1
            if i != n//i:
                count +=1
    return count
        


a = int(input())
b = int(input())
c = 0
for i in range(a,b+1):
    if numDivisors(i) == 4:
        c += 1

print("The number of RSA numbers between " + str(a) + " and " + str(b) + " is " + str(c))
