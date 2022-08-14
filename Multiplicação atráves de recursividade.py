x, y = input().split()
x = int(x)
y = int(y)

def multi(x,y):
    if y == 1:
        return x
    else:
        return x + multi(x,y-1)
print(multi(x, y))