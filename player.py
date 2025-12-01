class Player:
    # self é equivalente ao this do C++, se referindo ao nome do objeto que chamou o método
    def __init__(self, x, y): # __init__ já inicializa um objeto quando a classe é criada, equivalente ao construtor de C++
        self.x = x
        self.y = y

    def get_position(self):
        return self.y, self.x

    def move(self, direction, maze):
        # Movimentos propostos
        dy = 0
        dx = 0

        if direction == 'w':  # Cima
            dy = -1
        elif direction == 's':  # Baixo
            dy = 1
        elif direction == 'a':  # Esquerda
            dx = -1
        elif direction == 'd':  # Direita
            dx = 1

        new_y = self.y + dy
        new_x = self.x + dx

        # Verificar limites do mapa
        if new_y < 0 or new_y >= len(maze) or new_x < 0 or new_x >= len(maze[0]):
            return False  # Parede invisível nas bordas, turno perdido

        # Verificar parede
        if maze[new_y][new_x] == '#':
            return False  # bateu na parede, turno perdido

        # Se chegou até aqui, pode mover
        self.y = new_y
        self.x = new_x
        return True