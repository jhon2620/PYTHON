import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 6 < suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

dado1, dado2 = lanzar_dados()

resultado = evaluar_jugada(dado1, dado2)
print(resultado)

def reducir_lista(lista):
    duplicados = list(set(lista))
    duplicados.remove(max(duplicados))
    return duplicados

def promedio(lista):
    return sum(lista) / len(lista) if lista else 0

lista_numeros = [1, 2, 15, 7, 2]

import random

def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])

def probar_suerte(resultado_moneda, lista):
    if resultado_moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista

lista_numeros = [10, 20, 30, 40, 50]