import os
from pathlib import Path

ruta = os.getcwd()
print(ruta)

ruta = os.chdir('C:\\Users\\JHON ES\\Pictures')
archivo = open('otro_archivo.txt')
print(archivo.read())

ruta = 'E:\\CURSOS\\PYTHON\\CLASES\\Python\\Dia_6'
elemento = os.path.basename(ruta)
print(elemento)
elemento = os.path.dirname(ruta)
print(elemento)
elemento = os.path.split(ruta)
print(elemento)

otro_archivo = open('C:\\Users\\JHON ES\\Pictures\\otro_archivo.txt')
print(otro_archivo.read())

carpeta = Path('/Users/JHON ES/Pictures')
archivo = carpeta / 'otro_archivo.txt'
mi_archivo = open(archivo)
print(mi_archivo.read())