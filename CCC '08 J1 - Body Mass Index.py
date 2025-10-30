x = float(input())
y = float(input())
z = x/y**2

if z > 25:
    print("Overweight")
elif z < 18.5:
    print("Underweight")
else:
    print("Normal weight")
