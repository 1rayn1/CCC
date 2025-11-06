
DIGIT_WIDTH = 7  

SEGMENTS = {
    '0': [
        " * * *",
        "*     *",
        "*     *",
        "*     *",
        "",
        "*     *",
        "*     *",
        "*     *",
        " * * *"
    ],
    '1': [
        "",
        "      *",
        "      *",
        "      *",
        "",
        "      *",
        "      *",
        "      *",
        ""
    ],
    '2': [
        " * * *",
        "      *",
        "      *",
        "      *",
        " * * *",
        "*",
        "*",
        "*",
        " * * *"
    ],
    '3': [
        " * * *",
        "      *",
        "      *",
        "      *",
        " * * *",
        "      *",
        "      *",
        "      *",
        " * * *"
    ],
    '4': [
        "",
        "*     *",
        "*     *",
        "*     *",
        " * * *",
        "      *",
        "      *",
        "      *",
        ""
    ],
    '5': [
        " * * *",
        "*",
        "*",
        "*",
        " * * *",
        "      *",
        "      *",
        "      *",
        " * * *"
    ],
    '6': [
        " * * *",
        "*",
        "*",
        "*",
        " * * *",
        "*     *",
        "*     *",
        "*     *",
        " * * *"
    ],
    '7': [
        " * * *",
        "      *",
        "      *",
        "      *",
        "",
        "      *",
        "      *",
        "      *",
        ""
    ],
    '8': [
        " * * *",
        "*     *",
        "*     *",
        "*     *",
        " * * *",
        "*     *",
        "*     *",
        "*     *",
        " * * *"
    ],
    '9': [
        " * * *",
        "*     *",
        "*     *",
        "*     *",
        " * * *",
        "      *",
        "      *",
        "      *",
        " * * *"
    ]
}

def pad(line):
    return line.ljust(DIGIT_WIDTH)

def render_digits(s):
    lines = [""] * 9
    for i in range(9):
        row = [pad(SEGMENTS[d][i]) for d in s]
        lines[i] = " ".join(row).rstrip()
    return lines


n = int(input())
inputs = [input().strip() for _ in range(n)]
    
for idx, s in enumerate(inputs):
    output = render_digits(s)
    for line in output:
        print(line)
    if idx < n - 1:
        print()
