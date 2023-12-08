import random

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao_total = 0

    def lancar_dados(self):
        return random.randint(1, 6), random.randint(1, 6)

    def somar_pontuacao(self, pontos):
        self.pontuacao_total += pontos

def jogar_partida(jogador1_nome, jogador2_nome):
    jogador1 = Jogador(jogador1_nome)
    jogador2 = Jogador(jogador2_nome)

    jogo = JogoDeDados(jogador1, jogador2)

    for rodada in range(3):
        print(f"\nRodada {rodada + 1}")
        resultado_rodada = jogo.jogar_rodada()
        print(f"{jogador1.nome} fez {resultado_rodada[0]} pontos")
        print(f"{jogador2.nome} fez {resultado_rodada[1]} pontos")

    print(f"\nO jogador {jogador1.nome} ganhou {jogador1.pontuacao_total} pontos")
    print(f"O jogador {jogador2.nome} ganhou {jogador2.pontuacao_total} pontos")

    vencedor = jogador1 if jogador1.pontuacao_total > jogador2.pontuacao_total else jogador2
    print(f"\nO vencedor é {vencedor.nome}")

class JogoDeDados:
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2

    def jogar_rodada(self):
        resultado_jogador1 = sum(self.jogador1.lancar_dados())
        resultado_jogador2 = sum(self.jogador2.lancar_dados())

        self.jogador1.somar_pontuacao(resultado_jogador1)
        self.jogador2.somar_pontuacao(resultado_jogador2)

        return resultado_jogador1, resultado_jogador2

if __name__ == "__main__":
    jogar_partida("Jogador1", "Jogador2")