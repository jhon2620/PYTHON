def ceros_vecinos(*args):
    contador = 0
    for num in args:
        if contador + 1  == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False

print(ceros_vecinos(0,6,8,5,0,5,6,4,0,1,5,3,6,5,0))