mi_tuple = (1,2,3,4)
print(mi_tuple)

t = (1,2,3)
x,y,z = t
print(x,y,z)

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)

print(t.index(2))

mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}
otro_set.add(4)
otro_set.discard(2)#descarta el elemento no lo elimina
otro_set.pop()#elimina de manera aleatoria
otro_set.clear#vaciar al set
print(otro_set)

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)#unir set