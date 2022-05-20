# Imports iniciais
import matplotlib.pyplot as plt
from math import floor

# Programa principal
while True:
    menu = int(input("1- Cadastrar funcionário \n2- Gerar relatório\n3- Sair\nEscolha uma opção: "))
    if menu == 1:
        # Lista temporária para adição do novo funcionário
        temp = []

        # Inputs de preenchimento (Formulário)
        cpf = int(input("CPF: "))
        nome = input("Nome: ")
        sexo = input("Sexo(M/F): ")
        salario = input("Salário(R$): ")

        # Append do novo funcionário na lista temporária
        novo_cadastro = (f'{cpf} {nome.capitalize()} {sexo.upper()} {salario}')
        temp.append(novo_cadastro)

        # Abertura compacta do txt e realização do cadastro
        with open('funcionários.txt', 'a') as cadastro:
            cadastro.writelines(temp)
            cadastro.write('\n')

    elif menu == 2:
        # Abertura compacta e leitura do conteúdo do .txt
        with open('funcionários.txt', 'r') as leitura:
            conteudo = leitura.readlines()

        # Criação da lista de trabalho
        valores = []
        for i in range(len(conteudo)):
            valores.append(conteudo[i].split())

        # Criação das listas contendo os salários
        salario_homens = []
        salario_mulheres = []

        # Loop for para adição dos salários por gênero
        for i in range(len(conteudo)):
            # Condicionais para geração do relatório
            if valores[i][2] == 'M':
                salario_homens.append(int(valores[i][3]))
            if valores[i][2] == 'F':
                salario_mulheres.append(int(valores[i][3]))

        # Calculo da média salário de cada grupo
        media_homens = (sum(salario_homens) / len(salario_homens))
        media_mulheres = (sum(salario_mulheres) / len(salario_mulheres))
        m_h = floor(media_homens)
        m_m = floor(media_mulheres)

        # Criação do gráfico via Matplotlib
        generos = ["Homens", "Mulheres"]
        salarios = [m_h, m_m]

        plt.bar(generos, salarios)
        
        # Legenda do eixo Y
        plt.ylabel("Média salarial")
        # Título do gráfico
        plt.title("Média salarial dos funcionários")
        # Chamamos o gráfico
        plt.show()

    elif menu == 3:
        break