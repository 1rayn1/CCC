n = int(input())

code_to_char = {}

for _ in range(n):
    line = input().split()
    char = line[0]
    code = line[1]
    code_to_char[code] = char
encoded = input().strip()
current = ""
decoded = ""

for bit in encoded:
    current += bit
    if current in code_to_char:
        decoded += code_to_char[current]
        current = ""

print(decoded)