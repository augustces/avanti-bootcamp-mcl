def impares(lista):
    return [x for x in lista if x % 2 != 0]

l1 = [1,2,3,4,5,6,7,8]
l2 = [2,4,6,8,10]
l3 = [1,3,5,7,9]

print(impares(l1))
print(impares(l2))
print(impares(l3))
