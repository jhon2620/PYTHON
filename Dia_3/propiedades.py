poema = "mil pequeños peces blancos como si hirviera el color de agua"

print("sol" in poema)
print(len(poema))

mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2

mi_lista3.append('g')
eliminado = mi_lista3.pop(0)

print(mi_lista3)
print(eliminado)

lista = ['g','o','b','m','c']
lista.sort()#Ordena de manera alfabetica de A a Z
lista.reverse()#Ordena de manera alfabetica de Z a A
print(lista)

diccionario = {'c1':'valor1','c2':'valo2'}
print(diccionario)
resultado = diccionario['c2']
print(resultado)

dic = {'c1':55, 'c2':[10,'e',30],'c3':{'s1':100,'s2':200}}
print(dic['c3']['s2'])
valor = dic['c2'][1]
print(valor.upper())

dic = {1:'a',2:'b'}
print(dic)

dic[3] = 'c'
print(dic)

dic[2] = 'B'
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())