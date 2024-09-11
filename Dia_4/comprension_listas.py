palabra = 'python'

listas = [letra for letra in palabra]

lista = [n for n in range(0,21,2)]
lista1 = [n/2 for n in range(0,21,2)]
lista2 = [n for n in range(0,21,2) if n * 2 > 10]
lista2 = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]

pies = [10,20,30,40,50]
metros = [p * 3.281 for p in pies]
print(metros)

print(listas)
print(lista)
print(lista1)
print(lista2)