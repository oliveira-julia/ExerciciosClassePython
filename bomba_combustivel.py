#Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

#Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
#tipoCombustivel.
#valorLitro
#quantidadeCombustivel
#Possua no mínimo esses métodos:
#abastecerPorValor( ) – método onde é informado o valor a ser abastecido
# e mostra a quantidade de litros que foi colocada no veículo
#abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível
# e mostra o valor a ser pago pelo cliente.
#alterarValor( ) – altera o valor do litro do combustível.
#alterarCombustivel( ) – altera o tipo do combustível.
#alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
#OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, reservatorio, marcaCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self._reservatorio = reservatorio
        self.marcaCombustivel = marcaCombustivel
        self.precoFinal = 0

    def __str__(self):
        return f'''A bomba está abastecendo {self.tipoCombustivel}, por R${self.valorLitro} o litro, 
               temos ainda {self._reservatorio} litros, da marca {self.marcaCombustivel} disponiveis no posto'''

    def abastecePorValor(self, valor):
        valor = valor / self.valorLitro
        self.precoFinal = valor
        print(f"Voce abasteceu {valor:.2f} litros")
        self._reservatorio -= valor

    def abastecePorLitro(self,litros):
        valorPorLitros = litros * self.valorLitro
        self.precoFinal = valorPorLitros
        print (f"Voce deve pagar R${valorPorLitros}")
        self._reservatorio -= litros

    def alteraValor(self,valorBomba):
        self.valorLitro = valorBomba
        print(f"O novo valor por litro foi fixado na bomba é {self.valorLitro}")

    def alteraTipoCombustivel(self,combustivel):
        self.tipoCombustivel = combustivel
        print(f"O combustivel disponivel na bomba é {self.tipoCombustivel}")

    def alteraReservatorio(self,reserva):
        self._reservatorio = reserva
        print(f"A quantidade de combustivel disponivel na bomba é {self._reservatorio}")

    def alteraMarca (self, marca):
        self.marcaCombustivel = marca
        print(f'''A distribuidora do combustivel é :''')

