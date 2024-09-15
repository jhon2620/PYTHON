def letras_unicas(palabras):
    mi_set = set()
    
    for letra in palabras:
        mi_set.add(letra)
    mi_lista = list(mi_set)
    mi_lista.sort()
    
    return mi_lista

print(letras_unicas('cascarrabias'))