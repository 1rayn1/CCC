import re

case = int(input())
output = ""
for _ in range(case):
    a = input()
    temp = ""
    sum_val = 0
    
    for ch in a:
        if ch.isupper():
            temp += ch
    
    numbers = re.findall(r'-?\d+', a)
    sum_val = sum(int(num) for num in numbers)
    
    temp += str(sum_val)
    output += temp + "\n"

print(output)