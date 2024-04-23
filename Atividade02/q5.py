def ordenar(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i][0] > lista[j][0]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

pessoas = [("Augusto", 30), ("Eliza", 25), ("Aang", 35), ("Joao", 12)]
print(ordenar(pessoas))