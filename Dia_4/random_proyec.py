from random import *

aleatorio = randint(1,10)

aleatorio = round(uniform(1,5),1)
print(aleatorio)

colores = ['azul','rojo','verde','amarillo']
aleatorio = choice(colores)
print(aleatorio)

numeros = list(range(5,50,5))

shuffle(numeros)

print(numeros)