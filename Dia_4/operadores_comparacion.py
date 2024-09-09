mi_bool = 4 < 5 and 5 == 2 + 3 #Ambos deben ser igual para que sea true
mi_bool = 4 < 5 or 5 == 2 + 3 #Solo uno debe ser True para que sea true 
texto = "esta frase es breve"

mi_bool = ('frase' in texto) or ('python' in texto)
mi_bool = not ('a' == 'a')
print(mi_bool)

if 5 == 2:
    print('Es correcto')
else:
    print('No es correcto')
    
habla_ingles = True
sabe_python = False

lista = ['a', 'b', 'c']

for letra in lista:
    if letra.startswith('b'):
        numero_letra = lista.index(letra) + 1
        print(f'Letra {numero_letra}: {letra}')
    else:
        print('Nombre que comienza con b')
        
numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)
    
for letra in 'python':
    print(letra)
    
dic = {'clave1':'a','clave2':'b','clave3':'c'}

for item in dic:
    print(item)
    
for item in dic.items():
    print(item)
    
for item in dic.values():
    print(item)
    
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for suma in lista_numeros:
    if suma%2 == 0:
        suma_pares = suma_pares + suma
        print(suma_pares)
    else:
        suma_impares = suma_impares + suma
        print(suma_impares)
