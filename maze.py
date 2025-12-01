# Armazena e gerencia a estrutura do labirinto
# Leitura de um mapa a partir de um .txt, para importar mapas personalizados
# Aqui é importante ter funções para validar os movimentos do jogador


# Lê um arquivo TXT e retorna o labirinto como matriz 2D.
def carregar_labirinto(caminho):
    maze = []
    with open(caminho, "r") as f:
        for linha in f:
            maze.append(list(linha.rstrip("\n")))
    return maze

# Retorna True se a posição for acessível (não parede e dentro dos limites).
def is_walkable(maze, y, x):
    if y < 0 or y >= len(maze):
        return False
    if x < 0 or x >= len(maze[0]):
        return False
    return maze[y][x] != "#"

# Exibe o labirinto no terminal com jogador P e monstro M.
def imprimir_labirinto(maze, player=None, monster=None):
    for y in range(len(maze)):
        linha = ""
        for x in range(len(maze[0])):

            if player is not None and (y, x) == player.get_position():
                linha += "P"
            elif monster is not None and (y, x) == monster.get_position():
                linha += "M"
            else:
                linha += maze[y][x]

        print(linha)