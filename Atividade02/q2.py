def numPrimo(n):
    if n < 2:
        return False
    for i in range(2,n-1):
        if n % i == 0:
            return False
    return True

def primosPresentes(lista):
    return [x for x in lista if numPrimo(x)]


l1 = [1,2,3,4,5,6,7,8]
l2 = [2,4,6,8,10]
l3 = [1,3,5,7,9]
print(primosPresentes(l1))
print(primosPresentes(l2))
print(primosPresentes(l3))
