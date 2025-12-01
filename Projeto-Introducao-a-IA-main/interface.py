import pygame
import sys
import os
from spritesheet import SpriteSheet

TILE_SIZE = 32 

class Graphics:
    def __init__(self, largura_mapa, altura_mapa):
        pygame.init()
        pygame.font.init() 
        
        self.largura_tela = largura_mapa * TILE_SIZE
        self.altura_tela = altura_mapa * TILE_SIZE
        self.tela = pygame.display.set_mode((self.largura_tela, self.altura_tela))
        pygame.display.set_caption('O Labirinto de Pandora')
        self.clock = pygame.time.Clock()

        # Fontes para cronometro e mensagens
        self.fonte_ui = pygame.font.SysFont('arial', 24, bold=True)
        self.fonte_msg = pygame.font.SysFont('arial', 60, bold=True)

        print("Carregando texturas...")
        self.assets = {}

        # Criacao dos ambientes
        try:
            sheet_env = SpriteSheet(os.path.join("assets", "ParedesFundo.png"))
            self.assets['floor'] = sheet_env.get_image(1, 3, 16, 16, scale=(TILE_SIZE, TILE_SIZE))
            self.assets['wall'] = sheet_env.get_image(4, 0, 16, 16, scale=(TILE_SIZE, TILE_SIZE))
        except SystemExit:
            self.criar_asset_temporario('floor', (50, 50, 50))
            self.criar_asset_temporario('wall', (150, 150, 150))

        # Criacao dos itens (a chavezinha no final)
        try:
            sheet_items = SpriteSheet(os.path.join("assets", "EntradaSaida.png"))
            self.assets['exit'] = sheet_items.get_image(3, 0, 16, 16, scale=(TILE_SIZE, TILE_SIZE))
        except SystemExit:
             self.criar_asset_temporario('exit', (255, 215, 0))

        # Criacao do jogador e do monstro
        self.carregar_personagem('player', 'player.png', (0, 0, 255))
        self.carregar_personagem('monster', 'monster.png', (255, 0, 0))

    def carregar_personagem(self, nome_asset, nome_arquivo, cor_fallback):
        caminho = os.path.join("assets", nome_arquivo)
        if os.path.exists(caminho):
            img = pygame.image.load(caminho).convert_alpha()
            self.assets[nome_asset] = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        else:
            self.criar_asset_temporario(nome_asset, cor_fallback)

    def criar_asset_temporario(self, nome, cor):
        surf = pygame.Surface((TILE_SIZE, TILE_SIZE))
        surf.fill(cor)
        self.assets[nome] = surf

    def processar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.fechar()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w: return 'w'
                if event.key == pygame.K_s: return 's'
                if event.key == pygame.K_a: return 'a'
                if event.key == pygame.K_d: return 'd'
                if event.key == pygame.K_q: self.fechar()
        return None

    def desenhar_tudo(self, maze, player, monster, exit_pos, tempo_decorrido):
        # 1. Desenha o Jogo
        for y in range(len(maze)):
            for x in range(len(maze[0])):
                pos = (x * TILE_SIZE, y * TILE_SIZE)
                self.tela.blit(self.assets['floor'], pos)
                if maze[y][x] == '#':
                    self.tela.blit(self.assets['wall'], pos)
                elif (y, x) == exit_pos:
                     self.tela.blit(self.assets['exit'], pos)

        self.tela.blit(self.assets['player'], (player.x * TILE_SIZE, player.y * TILE_SIZE))
        self.tela.blit(self.assets['monster'], (monster.x * TILE_SIZE, monster.y * TILE_SIZE))

        # Cria o cronometro
        texto_tempo = f"Tempo: {tempo_decorrido:.2f}s"
        sombra = self.fonte_ui.render(texto_tempo, True, (0, 0, 0))
        superficie_texto = self.fonte_ui.render(texto_tempo, True, (255, 255, 255))
        
        self.tela.blit(sombra, (12, 12)) 
        self.tela.blit(superficie_texto, (10, 10))

        pygame.display.flip()
        self.clock.tick(60)

    def mostrar_mensagem_final(self, texto, cor):
        superficie_texto = self.fonte_msg.render(texto, True, cor)
        rect_texto = superficie_texto.get_rect(center=(self.largura_tela/2, self.altura_tela/2))
        
        # Cria o fundo escuro
        s = pygame.Surface((self.largura_tela, 100))  
        s.set_alpha(200) 
        s.fill((0,0,0))           
        self.tela.blit(s, (0, self.altura_tela/2 - 50))

        self.tela.blit(superficie_texto, rect_texto)
        pygame.display.flip()
        
        # Linha para nao travar o Windowns
        tempo_inicial = pygame.time.get_ticks()
        while pygame.time.get_ticks() - tempo_inicial < 3000:
            pygame.event.pump()
            self.clock.tick(60)
            
        self.fechar()

    def fechar(self):
        pygame.quit()
        sys.exit()

def encontrar_entrada(maze):
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == "S": return (y, x)
    return (1, 1)

def encontrar_saida(maze):
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == "E": return (y, x)
    return (len(maze)-2, len(maze[0])-2)