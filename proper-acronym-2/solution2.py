import sys
sys.setrecursionlimit(5000)
def is_subsequence(a, b):
    if a == '':
        return True
    for i in range(len(b)):
        if a[0] == b[i]:
            return is_subsequence(a[1:], b[i+1:])
    return False

input()
words = input().split()
initials = ''.join(map(lambda x: x[0], words))
T = input().strip()
print('Yes' if is_subsequence(T, initials) else 'No')
