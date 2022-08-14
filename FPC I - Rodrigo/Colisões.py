# Verificando colisões de objetos
x0A, y0A, x1A, y1A = [int(i) for i in input().split()]
x0B, y0B, x1B, y1B = [int(i) for i in input().split()]
# Checando as colisões
if x1A < x0B or x0A > x1B: #Investigando as coordenadas de "X"
    print("0")
elif y1A < y0B or y0A > y1B: #Investigando as coordenadas de "Y"
    print("0")
else:
    print("1")
