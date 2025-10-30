t = int(input())
s = int(input())
h = int(input())
#, the height of the tines, t
#, the spacing between tines, and s
#, the length of the handle. h
print(("*" + " " * s + "*" + " " * s + "*" +"\n")*t, end="")
print("*"*(2*s+3))
print((" "*(s+1)+ "*\n")*h,end="")
