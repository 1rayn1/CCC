def steps(fs,bs,ts):
    i = fs+bs
    if ts%(i) <= fs:
        m = (fs-bs)*(ts//i) + ts%i
    else:
        m = (fs-bs)*(ts//i) + 2*fs -ts%i
    return m


a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())



m=steps(a,b,s)
n=steps(c,d,s)

if m > n:
    print("Nikky")
elif m < n:
    print("Byron")
else:
    print("Tied")