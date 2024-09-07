nombre = input("Cúal es tu nombre: ")
ventas = input("Ventas: $ ")

ganancia = float(ventas) * 0.13
ganancia = round(ganancia,2)

print(f"Ok {nombre}. este mes ganastes {ganancia}")