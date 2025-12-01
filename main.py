from mazeGenerator import gerar_labirinto
from player import Player
from monster import Monster
from interface import Graphics, encontrar_entrada, encontrar_saida

import sys
import time 

def main():
    largura = 31
    altura  = 21

    # Gera o labirinto
    maze = gerar_labirinto(largura, altura)
    start_y, start_x = encontrar_entrada(maze)
    exit_y, exit_x = encontrar_saida(maze) # exit_y é Linha, exit_x é Coluna
    
    player = Player(start_x, start_y)
    monster = Monster(exit_x, exit_y)
    gui = Graphics(largura, altura)

    # Cronometro
    inicio_jogo = 0
    jogo_comecou = False
    tempo_decorrido = 0

    while True:
        comando = gui.processar_eventos()

        # Inicia cronometro no primeiro movimento
        if comando and not jogo_comecou:
            jogo_comecou = True
            inicio_jogo = time.time()

        if jogo_comecou:
            tempo_decorrido = time.time() - inicio_jogo

        # Move o player
        if comando:
            moved = player.move(comando, maze)
            monster.move(player, maze)
            
            # Verificacao. Pode apagar depois
            if moved:
                print(f"Player: {player.y},{player.x} | Saída: {exit_y},{exit_x}")

        if (player.y, player.x) == (exit_y, exit_x):
            print("VENCEU")
            gui.mostrar_mensagem_final(f"VITÓRIA! ({tempo_decorrido:.2f}s)", (255, 215, 0))

        if (player.y, player.x) == (monster.y, monster.x):
            print("GAME OVER")
            gui.mostrar_mensagem_final("VOCÊ MORREU!", (255, 0, 0))

        # Desenha na tela
        gui.desenhar_tudo(maze, player, monster, (exit_y, exit_x), tempo_decorrido)

if __name__ == "__main__":
    main()