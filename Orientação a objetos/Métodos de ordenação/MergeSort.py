alugados = ["Não sei"]
disponiveis = ["Descubra"]
receba = alugados + disponiveis

lista1 = 0
lista2 = 0
while True:
    if self.alugados[lista1] < self.disponiveis[lista2]:
        self.receba.append(self.alugados[lista1])
        lista1 += 1
    if lista1 == len(self.alugados):
        for i in range((len(self.disponiveis))- lista2):
            self.receba.append(self.disponiveis[lista2])
            lista2 += 1
        break
    if lista2 != len(self.disponiveis):
        if self.alugados[lista1] > self.disponiveis[lista2]:
            self.receba.append(self.disponiveis[lista2])
            lista2 += 1
        if  lista2 == len(self.disponiveis):
            for i in range((len(self.alugados))- lista1):
                self.receba.append(self.alugados[lista1])
                lista1 += 1
            break