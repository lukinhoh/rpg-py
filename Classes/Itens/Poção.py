#Importações
from Classes.Jogador.Jogador import Jogador

#Variáveis
jogador = Jogador()

class Poção:

    def __init__(self, potion = 20, qnt=1):
        self.potion = potion
        self.qnt = qnt
        jogador.inventario -= qnt
        if jogador.vida < 100:
            jogador.vida += potion
            if jogador.vida > 100:
                jogador.vida = 100
