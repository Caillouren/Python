# Lista contendo as "notas"
notas = []

# Lista que irá conter as notas acima da média
notas_acima = []

# Criando Loop-While para manter o programa rodando
while True:
    # Input que receberá as notas
    x = float(input("Digite mais um nota nota: "))

    # Condicional que terminará o programa, "input == -1"
    if x == -1:
        print(f"As notas inseridas, em sequência, foram: {notas},")

        # Print contendo o cálculo de média dos elementos contidos na lista "notas"
        print(f"E a média de suas notas foi: {sum(notas)/len(notas):.2f}.")

        # Loop que realizara a contabilização das notas inseridas na lista "notas" que estão acima da média
        for i in list(notas):
            if i > sum(notas)/len(notas):
                notas_acima.append(i)
        print(f"Além do número de notas que foram acima da média: {len(notas_acima)}")

        break

    # Condicional que mantém o loop em funcionamento adicionando os inputs a uma lista
    else:
        notas.append(x)
        continue