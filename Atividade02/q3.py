def intersecao(lista1, lista2):
    intersec = []
    for x in lista1:
        if x in lista2:
            intersec.append(x)
    return intersec

def diferenca(lista1, lista2):
    intersec = intersecao(lista1, lista2)
    dif = []
    for x in lista1:
        if x not in intersec:
            dif.append(x)

    for y in lista2:
        if y not in intersec:
            dif.append(y)

    return dif

l1 = [1,2,3,4,5,6,7,8]
l2 = [2,4,6,8,10]

l3 = [1,3,5,7,9]
l4 = [2,3,5,10, 11]

l5 = [1,2,6,9]
l6 = [1,2,6,9]

print(diferenca(l1,l2))
print(diferenca(l3,l4))
print(diferenca(l5,l6))