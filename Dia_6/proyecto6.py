import os
from pathlib import Path
from os import system

mruta = Path("E:/CURSOS/PYTHON/CLASES/Python/Dia_6/Recetas")
#mruta = Path(Path.home(),"Recetas") solo se usa cuando la carpeta se encuentra en C:\Users\JHON ES

def contar_recetas(ruta):
    i = 0
    for txt in Path(ruta).glob("**/*.txt"):
        i += 1
    return i

def inicio ():
    system('cls')
    print('*' * 50)
    print('*' * 5 + "Bienvenido al administrador de recetas" + '*' * 5)
    print('*' * 50)
    print(f'Las Recetas se encuentran en mi {mruta}')
    print(f'Total recetas: {contar_recetas(mruta)}')

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print('*' * 5 + 'Elige una Opción' + '*' * 5)
        print('''      
            [1] - Leer receta
            [2] - Crear receta nueva
            [3] - Crear categoria nueva
            [4] - Eliminar receta
            [5] - Eliminar categoria
            [6] - Salir programa''')
        eleccion_menu = input('\nElige una Opción: ')
    return int(eleccion_menu)

def mostrar_categorias(ruta):
    print('Categorias: ')
    rcategorias = Path(ruta)
    lcategorias = []
    i = 1
    for carpeta in rcategorias.iterdir():
        carpeta_str = str(carpeta.home)
        print(f'[{i}] - {carpeta_str}')
        lcategorias.append(carpeta)
        i += 1
    return lcategorias

def elegir_categoria(lista):
    eleccion_correcta = 'x'
    
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input('\nElige una categoria: ')
        
    return lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print('Recetas: ')
    rrecetas = Path(ruta)
    lrectas = []
    i = 1
    for receta in rrecetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f'[{i}] - {receta_str}')
        lrectas.append(receta)
        i += 1
    return lrectas

def elegir_recetas(lista):
    eleccion_receta = 'x'
    
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input('\nElige una receta: ')
        
    return lista[int(eleccion_receta) - 1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False
    
    while not existe:
        print('Escribe el nombre de tu receta: ')
        nombre_receta = input() + '.txt'
        print('Escribe tu nueva receta: ')
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)
        
        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f'Tu receta {nombre_receta} ha sido creada')
            existe = True
        else:
            print('Lo siento, esa receta ya existe')

def crear_categoria(ruta):
    existe = False
    
    while not existe:
        print('Escribe el nombre de la nueva categoria: ')
        nombre_categoria = input() + '.txt'
        ruta_nueva = Path(ruta, nombre_categoria)
        
        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f'Tu nueva categoria {nombre_categoria} ha sido creada')
            existe = True
        else:
            print('Lo siento, esa categoria ya existe')

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f'La receta {receta.name} ha sido eliminada')

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f'La categoria {categoria.name} ha sido eliminada')
    
def volver_inicio():
    eleccion_regresar = 'x'
    
    while eleccion_regresar.lower()  != 'v':
        eleccion_regresar = input("\nPresione V para volver al menu: ")
    
# Mostrar menu de incio

finalizar_programa = False

while not finalizar_programa:
    menu = inicio()

    if menu == 1:
        mis_cateogrias = mostrar_categorias(mruta)
        mi_categoria = elegir_categoria(mis_cateogrias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print('no hay recetas eb esra categoria. ')
        else:
            mi_receta = elegir_recetas(mis_recetas)
            leer_receta(mi_receta)
        volver_inicio()
        pass
    elif menu == 2:
        mis_cateogrias = mostrar_categorias(mruta)
        mi_categoria = elegir_categoria(mis_cateogrias)
        crear_receta(mi_categoria)
        volver_inicio()
        pass
    elif menu == 3:
        crear_categoria(mruta)
        volver_inicio()
        pass
    elif menu == 4:
        mis_cateogrias = mostrar_categorias(mruta)
        mi_categoria = elegir_categoria(mis_cateogrias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()
        pass
    elif menu == 5:
        mis_cateogrias = mostrar_categorias(mruta)
        mi_categoria = elegir_categoria(mis_cateogrias)
        eliminar_categoria(mi_categoria)
        volver_inicio()
        pass
    elif menu == 6:
        finalizar_programa = True
        pass
