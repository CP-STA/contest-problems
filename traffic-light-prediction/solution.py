g, y, r = map(int, input().split())
t = int(input())
t %= 60*60*24
b = t % (g+2*y+r)

if b < g:
    print("green")
elif b < g+y:
    print("yellow")
elif b < g+y+r:
    print("red")
elif b < g+y+r+y:
    print("yellow")
else:
    raise Exception("wtf")
