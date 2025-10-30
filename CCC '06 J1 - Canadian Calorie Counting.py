a = int(input())
b = int(input())
c = int(input())
d = int(input())
def burger():
    if a == 1:
        return(461)
    elif a ==2:
        return(431)
    elif a ==3:
        return(420)
    else:
        return(0)
    
def side():
    if b == 1:
        return(100)
    elif b ==2:
        return(57)
    elif b == 3:
        return(70)
    else:
        return(0)

def drink():
    if c == 1:
        return(130)
    elif c ==2:
        return(160)
    elif c ==3:
        return(118)
    else:
        return(0)

def des():
    if d==1:
        return(167)
    elif d == 2:
        return(266)
    elif d ==3:
        return(75)
    else:
        return(0)

print("Your total Calorie count is "+ str(burger() + side() + drink() + des())+".")