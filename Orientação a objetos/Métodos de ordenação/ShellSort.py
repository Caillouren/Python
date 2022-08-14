# Lista experimental
# lista = [0, 2, 1, 4, 3, 5]
lista = ["Caio", "Avião", "Bola", "Diamante", "Cadeira"]

# Método ShellSort
def shellsort(lista):
    n = len(lista)
    h = int(n / 2)
    while h > 0:
        for i in range(h, n):
            c = lista[i]
            j = i
            while j >= h and c < lista[j - h]:
                lista[j] = lista[j - h]
                j -= h
                lista[j] = c
        h = int(h / 2.2)
    return lista
print(shellsort(lista))

# Corrigir para funcionar com string-lists