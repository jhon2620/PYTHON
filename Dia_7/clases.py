class Pajaro:
    
    pass

mi_pajaro = Pajaro()
# print(mi_pajaro)
# print(type(mi_pajaro))

class Pajaro:
    alas = True
    
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    
    def piar(self):
        print(f'pio, mi color es {self.color}')
    
    def volar(self, metros):
        print(f'El pajaro ha volado {metros} metros')
        self.piar()
        
    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')
    
    #Tipos de Metodos
    
    @classmethod # no nececita declarar el constructor de la clase para llamarlo
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
        cls.alas = False
        print(Pajaro.alas)
    
    @staticmethod
    def mirar():
        print('Pajaro mira')

print('\n')
Pajaro.poner_huevos(5)
Pajaro.mirar()
print('\n')
piolin = Pajaro('amarillo','canario')

piolin.alas = False
piolin.piar()
piolin.volar(12)

mi_pajaro = Pajaro('negro', 'Tucan')

# print(mi_pajaro.color)
# print(f'mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}')