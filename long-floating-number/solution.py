from decimal import Decimal
a = Decimal(input())
one = Decimal(1)
if a > one:
    print('larger')
elif a < one:
    print('smaller')
else:
    print('equal')
