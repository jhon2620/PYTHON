def suma(a,b):
    return a + b

print(suma(5,6))

def suma_1(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(suma_1(5,6,5))

def numeros_persona(nombre,*args):
    suma_numeros = 0
    for arg in args:
        suma_numeros += arg
    return f"{nombre}, la suma de tus números es {suma_numeros}"