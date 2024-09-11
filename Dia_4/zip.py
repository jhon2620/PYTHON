nombre = ['Ana','Hugo','Valeria']
edades = [65,29,42]
ciudades = ['Lima','Madrid','Mexico']

combinados = list(zip(nombre,edades,ciudades))

for nombre,edad,ciudad in combinados:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')

dic = {'C1':45,'C2':11}
print(min(dic.values()))