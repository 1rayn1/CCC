a = int(input())



for i in range(int(a/2)):
    print(("*"*(2*i+1)) + (" "*(2*a-(2*(2*i+1)))) + ("*"*(2*i+1)))
print("*"*(2*a))
for j in range(int(a/2)):
    i = int(a/2) - j - 1
    print(("*"*(2*i+1)) + (" "*(2*a-(2*(2*i+1)))) + ("*"*(2*i+1)))
