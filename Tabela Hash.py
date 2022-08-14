# Entrada
entrada = input().split(" ")
# Construção dos valores e listas
QtdContainers = entrada[0]
TamContainers = entrada[1]
tabela = []
# Criando os containers na lista tabela
for i in range(int(QtdContainers)):
    temp = [None] * int(TamContainers)
    tabela.append(temp)

# Definindo o número de inserções e as adicionando
QtdInserções = int(entrada[2])
for i in range(QtdInserções):
    chaves = entrada[3 + i]
    modulo = int(chaves) % int(QtdContainers)
    # Validando condições de None
    if tabela[modulo][0] == None:
        tabela[modulo][0] = chaves
    else:
        for j in range(int(TamContainers)):
            if tabela[modulo][j] == None:
                tabela[modulo][j] = chaves
                break
Output = []
# Criando o método de busca
for i in range(3 + int(QtdInserções), len(entrada)):
    temp_modulo = entrada[i]
    modulo_busca = int(temp_modulo) % int(QtdContainers)
    # Realizando a busca na tabela
    if tabela[modulo_busca][0] == entrada[i]:
        Output.append(1)
    else:
        for j in range(int(TamContainers)):
            if tabela[modulo_busca][j] == entrada[i]:
                Output.append(j + 1)
                break
            elif tabela[modulo_busca][0] == None:
                Output.append(j + 1)
                break
            elif j > len(TamContainers):
                Output.append(int(TamContainers))
                break
for i in list(Output):
    print(i, end=" ")