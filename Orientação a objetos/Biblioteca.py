# classes Biblioteca e Livro:
# - A Biblioteca contem uma lista de livros disponiveis e uma lista de livros alugados
# - A biblioteca possui um método para alugar um livro. Caso o livro já esteja alugado a pessoa nao poderá alugar este livro.
# - A biblioteca possui um método para devolver o livro.
# - A biblioteca possui um método que devolve o nome do livro mais alugado.

class Livro:
    codigo = None
    nome = None
    autor = None
    __qtdeAlugueis = 0

    def __init__(self, codigo, nome, autor):
        self.codigo = codigo
        self.nome = nome
        self.autor = autor

    def incrementaAluguel(self):
        self.__qtdeAlugueis += 1

    def getQtdeAlugueis(self):
        return self.__qtdeAlugueis

class Biblioteca:
    alugados = []
    disponiveis = []
    TodosLivros = []
    def inserir(self, livro):
        self.disponiveis.append(livro)

    def alugar(self, livro):
        ok = True
        mensagem = None
        if livro in self.disponiveis:
            for i in self.disponiveis:
                if i == livro:
                    i.incrementaAluguel()
                    self.alugados.append(i)
                    self.disponiveis.remove(i)
                    break
        elif livro in self.alugados:
            ok = False
            mensagem = "O livro ja esta alugado, infelizmente voce nao podera alugar"
        else:
            ok = False
            mensagem = "O livro nao existe"
        return (ok, mensagem)

    def devolver(self, codLivro):
        ok = True
        mensagem = None
        for livro in self.alugados:
            if livro.codigo == codLivro:
                self.disponiveis.append(livro)
                self.alugados.remove(livro)
                break
        else:
            ok = False
            mensagem = "O livro nao esta alugado"
        return (ok, mensagem)

    def livroMaisAlugado(self):
        ok = True
        mensagem = None
        maior = 0
        nome = None
        for livro in self.disponiveis:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        for livro in self.alugados:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        if maior == 0:
            ok = False
            mensagem = "Nenhum livro foi alugado ainda"
        else:
            mensagem = "O livro mais alugado e: %s (%d alugueis)"%(nome, maior)
            return (ok, mensagem)
    def LivrosOrdenadosPeloNome(self):
        for i in range(1, len(self.disponiveis)):
            chave = self.disponiveis[i]
            j = i
            while j > 0 and self.disponiveis[j - 1].nome > chave.nome:
                self.disponiveis[j] = self.disponiveis[j - 1]
                j -= 1
            self.disponiveis[j] = chave

        for i in range(1, len(self.alugados)):
            chave = self.alugados[i]
            j = i
            while j > 0 and self.alugados[j - 1].nome > chave.nome:
                self.alugados[j] = self.alugados[j - 1]
                j -= 1
            self.alugados[j] = chave

        self.TodosLivros = self.alugados + self.disponiveis
        for i in range(1, len(self.TodosLivros)):
            chave = self.TodosLivros[i]
            j = i
            while j > 0 and self.TodosLivros[j - 1].nome > chave.nome:
                self.TodosLivros[j] = self.TodosLivros[j - 1]
                j -= 1
            self.TodosLivros[j] = chave

entrada = input().split(",")
entrada.pop(0)

b = Biblioteca()

for i in range(0, len(entrada), 3):
    b.inserir(Livro(entrada[i], entrada[i + 1], entrada[i + 2]))

b.LivrosOrdenadosPeloNome()

for i in b.TodosLivros:
    print(i.codigo, end=" ")