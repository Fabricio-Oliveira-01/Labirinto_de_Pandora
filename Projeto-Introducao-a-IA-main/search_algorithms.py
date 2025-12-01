import heapq #Organiza a lista para o menor item ficar em cima

def heuristica(a,b):
#Distância de Manhattan. Abs serve para o modulo do valor
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def A_Estrela(labirinto, inicio, objetivo):

    fronteira = []
    veio_deonde = {} #std::map
    custoReal = {} #std::map

    #O formato eh: (PRIORIDADE, ITEM)
    heapq.heappush(fronteira, (0, inicio))
    veio_deonde[inicio] = None
    custoReal[inicio] = 0

    #O que vem agora pode funcionar ou nao. Dilema da beleza e paciencia
    #Se funcionar, beleza. Se nao, paciencia
    while fronteira:

        _, atual = heapq.heappop(fronteira)
        # O _ ignora a prioridade. O pop tira o item de menor valor da lista

        #Encontrado o objetivo, volta para saber o caminho
        if atual == objetivo:

            caminho = []
            passo = objetivo

            while passo is not None:

                caminho.append(passo)
                passo = veio_deonde[passo]

                #inverte o caminho
            caminho.reverse()
            return caminho            

        #O for vai olhar para todas as direcoes da posicao
        for dy, dx in [(0,1), (0,-1,), (1,0),(-1,0)]:

            vizinho_y = atual[0] + dy
            vizinho_x = atual[1] + dx
            noVizinho = (vizinho_y, vizinho_x)

            #Linha para verificar os limites
            if 0 <= vizinho_y < len(labirinto) and 0 <= vizinho_x < len(labirinto[0]):

                if labirinto[vizinho_y][vizinho_x] != '#':

                    custoNovo = custoReal[atual] + 1

                    if noVizinho not in custoReal or custoNovo < custoReal[noVizinho]:

                        #F(n) = G(n) + H(n)
                        custoReal[noVizinho] = custoNovo
                        prioridade = custoNovo + heuristica(noVizinho, objetivo)
                        heapq.heappush(fronteira, (prioridade, noVizinho))
                        veio_deonde[noVizinho] = atual
                        #Deixa registrado de onde veio//Backtracking

    return []