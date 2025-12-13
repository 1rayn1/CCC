keyword = input().strip().upper()
message = input()

shifts = [(ord(c) - ord('A')) for c in keyword]

out = []
k = 0
for ch in message:
    if ch.isalpha():
        val = ord(ch.upper()) - ord('A')
        shift = shifts[k % len(shifts)]
        enc_val = (val + shift) % 26
        enc_char = chr(enc_val + ord('A'))
        out.append(enc_char)
        k += 1
    else:
        continue

print("".join(out))