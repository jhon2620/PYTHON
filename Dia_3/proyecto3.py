text = input("Ingrese el Text: ")
primera = input("Primera Letra: ")
segunda = input("Segunda Letra: ")
tercera = input("Tercera Letra: ")

print("\n" + text + "\nLetra: " + primera + "\nLetra: " + segunda + "\nLetra: " + tercera)
text = text.lower()
cprimera = text.count(primera)
csegunda = text.count(segunda)
ctercera = text.count(tercera)

palabras = text.split()
cpalabras = len(palabras)
print("\nCuántas veces aparece la \"" + primera + "\": " + str(cprimera))
print("Cuántas veces aparece la \"" + segunda + "\": " + str(csegunda))
print("Cuántas veces aparece la \"" + tercera + "\": " + str(ctercera))
print("\nCuántas palabras hay en total: " + str(cpalabras))
primeral = text[0]
ultimal = text[-1]
print("Cuántas es la primera letra: " + primeral)
print("Cuántas es la ultima letra: " + ultimal)

palabras.reverse()
rtext = ' '.join(palabras)
print("\nTexto de forma inversa: " + rtext)

python = 'python' in text
dic = {True:"si", False:"no"}
comprobar = dic[python]
print("\nTexto contiene la palabra 'Python': " + comprobar)