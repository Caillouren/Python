# Lista experimental
# lista = [0, 2, 1, 4, 3, 5]
lista = ["Caio", "Avião", "Bola", "Diamante", "Cadeira"]

# def inserçãoDireta(lista):
#     for i in range(1, len(Biblioteca(disponiveis))):
#             chave = Biblioteca(disponiveis[i])
#             j = i
#             while j > 0 and Biblioteca(disponiveis[j - 1]) > chave:
#                 Biblioteca(disponiveis[j]) == Biblioteca(disponiveis[j - 1])
#                 j -= 1
#             Biblioteca(disponiveis[j]) == chave
#     return Biblioteca(disponiveis)

# Método de inserção direta
def inserçãoDireta(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i
        while j > 0 and lista[j - 1] > chave:
            lista[j] = lista[j - 1]
            j -= 1
        lista[j] = chave
    return lista
print(inserçãoDireta(lista))

# Método funcionando normalmente