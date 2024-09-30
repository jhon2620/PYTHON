from pathlib import Path, PureWindowsPath

carpeta = Path("E:/CURSOS/PYTHON/CLASES/Python/Dia_6/prueba.txt")

print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

if not carpeta.exists():
    print('Este archivo no existe')
else:
    print('Genial, existe')
    
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)