# Criação do dicionário
Filmes = {}

# Loop-while que receberá os filmes e seus anos
while True:
    Filme = input("Digite o nome de um filme: ")
    Ano = int(input("Em que ano ele foi lançado? "))
    Filmes[Filme] = Ano
    # Condicional que determina o limite de filmes
    if len(Filmes) == 2:
        print(f"Os filmes e seus respectivos anos de lançamentos foram: {Filmes}")
        break
    else:
        continue