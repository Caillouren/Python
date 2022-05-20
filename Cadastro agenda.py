# Arquivo .txt
a = open('/Users/Caio_/Documents/Mykael/contatos.txt', 'a')
temp = []
while True:
    # Inputs e construção do append
    nome = input('Nome: ')
    tele = input('Telefone: ')
    novo = (f'{nome} {tele:>2}')
    temp.append(novo)
    # Condição de parada
    if nome == 'sair':
        temp.pop()
        break
    else:
        continue
for i in list(temp):
    a.writelines(i)
    a.write('\n')

a.close()