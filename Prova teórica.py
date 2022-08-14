# Ativ 4
n = 48
def recursao(n):
    if n <= 10:
        return n * 2
    else:
         return recursao(n / 3)
print(recursao(n))

# Ativ 1
k = 7043
m = 347
modulo = k % m
print(modulo)