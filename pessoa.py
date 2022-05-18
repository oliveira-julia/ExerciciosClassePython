#Classe Pessoa: Crie uma classe que modele uma pessoa:

#Atributos: nome, idade, peso e altura
#Métodos: Envelhercer, engordar, emagrecer, crescer.
#Obs: Por padrão, a cada ano que nossa pessoa envelhece,
#sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self. altura = altura

    def __str__(self):
        return f'Nome {self.nome}, altura {self.altura} metros, idade {self.idade} anos, peso {self.peso}Kg'

    def envelhece(self, anos):
        if self.idade < 21:
            self.idade += anos
            self.altura += 0.05 * anos
        else:
            self.idade += anos

    def engorda (self, peso):
        self.peso += peso

    def emagrece (self, peso):
        self.peso -= peso

    def cresce (self, altura):
        self.altura += altura

