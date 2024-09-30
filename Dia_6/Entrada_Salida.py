import os

# Obtener la ruta absoluta de la carpeta donde está el script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta completa al archivo
file_path = os.path.join(current_dir, 'prueba.txt')

mi_archivo = open(file_path)

todas = mi_archivo.readlines()
todas = todas.pop()
print(todas)

# for l in mi_archivo:
#     print("Aqui dice: " + l)
    
# una_linea = mi_archivo.readline()
# print(una_linea.upper())

# una_linea = mi_archivo.readline()
# print(una_linea.rstrip())

# una_linea = mi_archivo.readline()
# print(una_linea)

mi_archivo.close()