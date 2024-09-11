dic  = {'clave1':100,'clave2':500}

a = dic.popitem()

print(a)
print(dic)

txt = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
b = txt.lstrip(',:%_#')
print(b)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)

def saludar_persona(nombre):
    '''
    Esta funcion sirve para saludar
    '''
    print('Hola ' + nombre)

saludar_persona('Jhon')

def saludar():
    print('¡Hola mundo!')

saludar()

def multiplicar(numero1,numero2):
    total = numero1 * numero2
    return total

resultado = multiplicar(5,10)
print(resultado)