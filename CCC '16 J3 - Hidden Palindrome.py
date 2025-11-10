def isPalindrome(s):
    r = s[::-1]
    if r == s:
        return True
    return False

a = input()
maxLength = 1

for i in range(len(a)):
    for j in range(len(a)):
        sub = a[i:j+1]
        if isPalindrome(sub):
            if(len(sub) > maxLength):
                maxLength = len(sub)
print(maxLength)