import os

# Obtener la ruta absoluta de la carpeta donde está el script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta completa al archivo
file_path = os.path.join(current_dir, 'prueba.txt')

# archivo = open(file_path,'w')

# # archivo.write('''
# # hola
# # mundo
# # estoy
# # aqui''')

# lista = ['hola','mundo','aqui','estoy']
# for p in lista:
#     archivo.write(p + '\n')
    
# archivo = open(file_path,'a')
# archivo.write('bienvenido')
archivo = open(file_path,'r')
#'"r" solo de lectura
# "w" actualizar la info del archivo
# "a" añadir informacion al archivo'
    
archivo.close()

archivo = open('mi_archivo.txt','w')
archivo.write('Nuevo texto')
archivo.close()

archivo = open('mi_archivo.txt','r')
print(archivo.read())