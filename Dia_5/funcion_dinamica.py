def chequear_3_cifras(lista):
    #return lista in range(100,1000)
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False

def chequear_3_cifras_1(lista):
    
    lista_3_cifras = []
    
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

def todos_positivos(lista):
    for n in lista:
        if n < 0:
            return False
    return True
lista_numeros = [20,-30,20]

def suma_menores(lista):
    f = 0
    for n in lista:
        if 0 < n < 1000:
            f += n
    return f
lista_numeros = [20,30,40]

def cantidad_pares(lista):
    c = 0
    for n in lista:
        if n % 2 == 0:
            c += 1
    return c

lista_numeros = [10, 3, 6, 7, 12, 5, 18]

resultado = chequear_3_cifras_1([555,99,600])
print(resultado)

muestra = todos_positivos(lista_numeros)
print(muestra)