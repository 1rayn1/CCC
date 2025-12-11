#The length of the indices that make up the answer has to be under m.
#eg. if it is (2,1,1,4), it passes, since it has 4 elements
m = int(input())
#The length of the two sets
#eg. if its 3, then there can be 3 elements: (a,b,c)
n = int(input())
one = {}
two = {}
for _ in range(n):
    a = input()
    one.add(a)
for _ in range(n):
    b = input()
    two.add(b)

for i in range(n):
    print()