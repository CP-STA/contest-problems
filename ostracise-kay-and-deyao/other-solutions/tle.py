s = input()

while 'deyao' in s or 'kay' in s:
    s = s.replace('deyao', '')
    s = s.replace('kay', '')

print(s)