from search_algorithms import A_Estrela

class Monster:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    #self equivale ao this-> (Acessar objetos) enquanto o init ja inicia o objeto com a classe

    def get_position(self): #Getter. Vai entender pq eh assim.
        return self.y, self.x

    def move (self, player, maze):
        start = (self.y, self.x) #Inicio do monstro
        goal = (player.y, player.x) #Local do player

        path = A_Estrela(maze, start, goal) #A* vem aqui, na lista path
        self.path = path

        if path and len(path) > 1: #Se existe caminho e nao esta na posicao do jogador...

            next_step = path[1] #... o monstro atualiza a posicao
            self.y, self.x = next_step