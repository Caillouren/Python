class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def getAnoNascimento(self, DataAtual):
        return DataAtual - self.idade

user = Pessoa("Caio", 20)
print(user.getAnoNascimento(2022))
