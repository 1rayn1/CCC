a = input()

signs = {
    "+" : "tighten",
    "-" : "loosen"
}

strings = ""
sign = ""
num = ""

for c in a:
    if c.isalpha():
        if (sign != ""):
            print(f"{strings} {signs[sign]} {num}")
            strings = num = sign = ""
        strings += c
    elif c.isdigit():
        num += c
    else:
        sign = c

print(f"{strings} {signs[sign]} {num}")