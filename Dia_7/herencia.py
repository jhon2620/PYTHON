class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    
    def nacer(self):
        print('Este animal ha dicho')
        
    def hablar(self):
        print('Este animal emite un sonido')
        
class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad,color)
        self.altura_vuelo = altura_vuelo
    def hablar(self):
        print('pio')
    
    def volar(self, metros):
        print(f'El pajaro vuela {metros} metros')

# piolin = Pajaro(2,'amarillo')
# piolin.nacer()
# print(piolin.color)
# piolin.hablar()
# piolin.volar(5)

class Padre:
    def hablar(self):
        print('Hola')
        
class Madre:
    def reir(self):
        print('ja ja')
    def hablar(self):
        print('que tal')

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.reir()
mi_nieto.hablar()