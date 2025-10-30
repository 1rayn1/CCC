def find(x):

    s = int(x**0.5)
    for i in range(s):
        if x %(s-i)==0:
            return ("Minimum perimeter is "+ str(int((2*((s-i)+(x/(s-i)))))) + 
                  " with dimensions " + str(s-i) + " x " + str(int(x/(s-i)))) + "\n"

b = ""
while True:
    x = int(input())
    if x == 0:
        break
    else:
        b = b+(find(x))
            
print(b)