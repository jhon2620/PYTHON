monedas = 5

while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas -= 1

respuesta = 's'

while respuesta == 's':
    respuesta = input('quieres seguir? (s/n')
    break
else:
    print('Gracias')
    
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if numero >=0:
        print(numero)
    else:
        break