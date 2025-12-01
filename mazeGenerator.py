import random

def gerar_labirinto(largura, altura):
    # Gera um labirinto usando DFS (busca em profundidade) com backtracking:
    #       Parede: '#'
    #       Caminho: ' '
    #       Entrada: 'S' (Start)
    #       Saída: 'E' (Exit)
    # Cria uma matriz cheia de paredes
    # Começa em uma célula qualquer
    # Marca como visitada
    # Escolhe uma direção aleatória indo para uma célula não visitada, pulando uma célula
    # Remove a parede entre as duas células, ou seja, na célula pulada
    # Continua recursivamente
    # Quando não há mais células livres, volta (backtracking)


    # Garante que largura e altura sejam ímpares (melhor para labirintos)
    if largura % 2 == 0:
        largura += 1
    if altura % 2 == 0:
        altura += 1

    # Cria a grade cheia de paredes
    maze = [['#' for _ in range(largura)] for _ in range(altura)]

    # Ponto inicial
    start_y = 1
    start_x = 1

    # Marca o início como caminho
    maze[start_y][start_x] = ' '

    # Movimentos possíveis (cima, baixo, esquerda, direita), andando 2 passos por vez
    direcoes = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    def dfs(y, x):
        random.shuffle(direcoes) # Embaralha direções para variedade

        for dy, dx in direcoes:
            ny = y + dy
            nx = x + dx

            # Verifica os limites e se a célula ainda é uma parede
            if 1 <= ny < altura-1 and 1 <= nx < largura-1 and maze[ny][nx] == '#':
                # Remove a parede entre a célula atual e a próxima
                maze[y + dy//2][x + dx//2] = ' '
                maze[ny][nx] = ' '
                dfs(ny, nx)

    # Inicia o DFS
    dfs(start_y, start_x)

    # =====================================================================
    # Adiciona imperfeições (rotas alternativas)
    # =====================================================================

    # percent define quão “não perfeito” é o labirinto
    percent = 0.1 # 10% das paredes viram caminhos
    total_cells = (largura * altura) # Total de células na matriz
    to_open = int(total_cells * percent) # Define quantas paredes serão removidas

    # Substitui paredes por espaços, escolhendo posições aleatórias
    for _ in range(to_open):
        y = random.randint(1, altura - 2)
        x = random.randint(1, largura - 2)
        if maze[y][x] == '#':
            maze[y][x] = ' '

    # =====================================================================
    # Garante saída conectada ao labirinto
    # =====================================================================

    # Encontra a célula acessível mais à direita e, em caso de empate em x, a mais embaixo (maior y)
    melhor_y = -1
    melhor_x = -1

    for y in range(1, altura - 1):
        for x in range(1, largura - 1):
            if maze[y][x] == ' ':
                if x > melhor_x or (x == melhor_x and y > melhor_y):
                    melhor_x = x
                    melhor_y = y

    # Se não encontrou (improvável), força um ponto próximo ao começo
    if melhor_x == -1:
        melhor_y, melhor_x = 1, 1
        maze[melhor_y][melhor_x] = ' '

    # Coloca a saída na parede direita, alinhada com a célula escolhida
    maze[melhor_y][largura - 1] = 'E'

    # Marca a entrada
    maze[1][0] = 'S'

    return maze


def salvar_em_arquivo(maze, nome_arquivo):
    with open(nome_arquivo, "w") as f:
        for linha in maze:
            f.write("".join(linha) + "\n")