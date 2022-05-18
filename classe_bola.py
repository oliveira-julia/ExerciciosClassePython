#Classe Bola: Crie uma classe que modele uma bola:
#Atributos: Cor, circunferência, material
#Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def __str__(self):
        return f'Bola de cor {self.cor}, feita de  {self.material} e de circunferência igual a {self.circunferencia} cm'

    def mostra_cor(self):
        print(f'a cor da bola é {self.cor}')

    def trocaCor(self, nova_cor):
        self.cor = nova_cor
        print (f'A cor da bola foi trocada para {self.cor}')

