from math import floor
from math import ceil
from math import sqrt
a1, b1, c1, a2, b2, c2 = map(int, input().split())
a = a2 - a1
b = b2 - b1
c = c2 - c1

if b**2-4*a*c < 0:
    print('None')
    exit(0)

left = floor((-b-sqrt(b**2-4*a*c))/(2*a))
right = ceil((-b+sqrt(b**2-4*a*c))/(2*a))

solved = False
for x in range(left, right+1):
    if (a2*x**2+b2*x+c2) != 0 and (a1*x**2+b1*x+c1)//(a2*x**2+b2*x+c2) > 0 and (a1*x**2+b1*x+c1) % (a2*x**2+b2*x+c2) == 0:
        solved = True
        print(x, end=' ')
if solved:
    print('')
else:
    print('None')
