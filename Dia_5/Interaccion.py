from random import shuffle

# Lista Inicial
palitos = ['-','--','---','----']

# mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

(mezclar(palitos))

# pedirle intento
def probar_surte():
    intento = ''
    
    while intento not in ['1','2','3','4']:
        intento = input('Elige un numero del 1 a 4: ')
    return int(intento)
intento1 = probar_surte()
print(intento1)

# Comprobar intento
def chequear_intento(lista,intento):
    if lista[intento - 1] == '-':
        print('A lavar los platos')
    else:
        print('Esta vez te has salvado')
    print(f'Te ha tocado {lista[intento - 1]}')

palitos_mezclados = mezclar(palitos)
seleccion = probar_surte()
chequear_intento(palitos_mezclados,seleccion)

