def shift(x,n):
    if n == 0:
        return x
    return x + shift(x*10,n-1)

a = int(input())
b = int(input())
print(shift(a,b))
