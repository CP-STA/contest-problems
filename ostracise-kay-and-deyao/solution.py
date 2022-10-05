# by Deyao Chen
s = input()
a = ['a' for i in range(len(s))] 
p = 0
i = 0

while i < len(s):
    a[p] = s[i]
    i += 1
    p += 1
    if p >= 5 and ''.join(a[p-5: p]) == 'deyao':
        p -= 5
    if p >= 3 and ''.join(a[p-3: p]) == 'kay':
        p -= 3

print(''.join(a[0:p]))