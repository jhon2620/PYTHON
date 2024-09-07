x = 10
y = 4
print("Mis numeros son " + str(x) + " y " + str(y))
print("Mis numeros son {} y {} es igual a {}".format(x,y, x+y))
print(f"Mis numeros son {x} y {y} es igual a {x+y}")

x = 6
y = 2
z = 7

print(f"{x} mas {y} es igual a {x+y}")
print(f"{x} menos {y} es igual a {x-y}")
print(f"{x} por {y} es igual a {x*y}")
print(f"{x} dividido {y} es igual a {x/y}")

print(f"{z} dividido al piso de {y} es igual a {z//y}")
print(f"{z} modulo {y} es igual a {z%y}")
print(f"{x} elevado a la {y} es igual a {x**y}")
print(f"{x} elevado a la {3} es igual a {x**3}")
print(f"La raiz cuadrada de {x} es {x**0.5}")

m = x**0.5
#m = round(m)
m1 = round(m,2)
print(m1)
h=13.87
print(round(h))
print(int(h))
print(type(round(13/2,0)))