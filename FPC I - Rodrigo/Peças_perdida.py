# Exercício da peça perdida
def soma(lista):
    s = 0
    for i in lista:
        s += i
    return s
N = int(input())
# Usando list comprehension de python para ler uma linha
pecas_incompletas = [int(i) for i in input().split()]
soma_incompleta = soma(pecas_incompletas)
pecas_completas = list(range(1, N + 1))
# Soma_completa = soma(pecas_completas)
soma_completa = int(N * (N + 1) / 2)
print(soma_completa - soma_incompleta)
