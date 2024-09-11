lista = [1,2,3,4]

for numero in range(5,10,2):#limite inicial, limite final, rango de avance
    print(numero)
    
lista = list(range(1,101))
print(lista)

lista = list(range(1,16))

suma_cuadrados = 0
for numero in range(1,16):
    cuadrado = numero ** 2
    suma_cuadrados += cuadrado
    
lista = ['a','b','c']
indice = 0

for indice,item in enumerate(lista):
    print(indice+1,item)
    indice += 1

for indice,item in enumerate(range(50,55)):
    print(indice+1,item)
    indice += 1

mis_tuples = list(enumerate(lista))
print(mis_tuples[1][0])

for texto in 'python':
    print(texto)

string = "Python"
lista_indices = list(enumerate(string))
print(lista_indices)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):
        print(indice)
