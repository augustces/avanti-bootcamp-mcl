def segMaior(lista):
    maior = max(lista)
    lista.remove(maior)
    maior = max(lista)
    return maior

l1 = [1,2,3,4,5,6,7,8]
l2 = [2,4,6,8,10]
l3 = [1,3,5,7,9]

print(segMaior(l1))
print(segMaior(l2))
print(segMaior(l3))