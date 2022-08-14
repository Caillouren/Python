# Lista experimental
# lista = [0, 2, 1, 4, 3, 5]
lista = ["Caio", "Avião", "Bola", "Diamante", "Cadeira"]

# Método BubbleSort
def bubbleSort(lista, n):
    troca = True
    while troca:
        troca = False
        for i in range(n-1):
            if lista[i] > lista[i + 1]:
                chave = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = chave
                troca = True
    return lista
print(bubbleSort(lista, n))

# Fazer funcionar