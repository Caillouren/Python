# Input contendo a sequência de ordems do usuário
entrada = input().split()

# Testando comando entrada
for i in entrada:
    # Comando gerando do valor total
    if i == "INICIO":
        valor = []
        valor.append(0)
    elif i == "IO":
        pop_tados = valor.pop()
        valor.append(pop_tados + 30)
    elif i == "MEM":
        pop_tados = valor.pop()
        valor.append(pop_tados + 10)
    elif i == "PROCSUM":
        pop_tados = valor.pop()
        valor.append(pop_tados + 1)
    elif i == "PROCMULT":
        pop_tados = valor.pop()
        valor.append(pop_tados + 10)
    elif i == "LOOP":
        valorloop = 0
        valorloop = entrada.index(i) + 1
        valor.append(int(entrada[valorloop]))
        valor.append(0)
        # Remoção do loop da entrada para evitar repetições
        del entrada[entrada.index(i)]
    elif i == "FIMLOOP":
        pop_tados = valor.pop()
        pop_tados2 = valor.pop()
        multiloop = pop_tados * pop_tados2
        pop_tadosfimloop = valor.pop()
        valor.append(int(pop_tadosfimloop) + int(multiloop))
    # Fim da sequência de comandos
    elif i == "FIM":
        print(int(valor[0]))