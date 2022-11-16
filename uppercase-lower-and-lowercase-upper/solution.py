input()

s = input().strip()

d = ord('A') - ord('a')
a = []

def iu(c):
    h = ord('A')
    g = ord('Z')
    return h <= ord(c) and ord(c) <= g

for i in range(len(s)):
    if iu(s[i]):
        a.append(chr(ord(s[i]) - d))
    else:
        a.append(chr(ord(s[i]) + d))

print(''.join(a))