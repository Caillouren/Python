# Criação do dicionário
Semana = {}

# Lista contendo os dias
Dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']

# Adicionando os pratos ao dicionário
for i in range(len(Dias)):
    Prato = input(f"Qual o prato do(a) {Dias[i]}? ")
    Semana[Dias[i]] = Prato

# Imprimindo o dicionário
print(f'As refeições da semana foram: {Semana}')
