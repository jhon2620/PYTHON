text = "Este es el texto de Federico"
resultado_1 = text.upper()
resultado_2 = text.lower()
resultado_3 = text.split()
resultado_4 = text.split("t")
resultado_5 = text.find("s")
resultado_6 = text.replace("e", "x")
print("1.- " + resultado_1)
print("2.- " + resultado_2)
print("3.- " + str(resultado_3))
print("4.- " + str(resultado_4))
print("5.- " + str(resultado_5))
print("6.- " + resultado_6)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = "-".join([a,b,c,d])
print("7.- " + e)