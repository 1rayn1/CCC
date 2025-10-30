a = int(input())
b = int(input())

c = b - a
if c <= 20:
    f = 100
elif 21 <= c <= 30:
    f = 270
else:
    f = 500 

if b > a:
    print("You are speeding and your fine is $" + str(f) + ".")
else:
    print("Congratulations, you are within the speed limit!")
