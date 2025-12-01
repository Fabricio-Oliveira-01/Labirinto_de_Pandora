import pygame

#A ideia daqui eh a seguinte: utilizar de imagens com varios icons para gerar o mapa

class SpriteSheet:
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except pygame.error as e:
            print(f"Erro ao carregar a imagem: {filename}")
            raise SystemExit(e)

    def get_image(self, frame_coluna, frame_linha, width, height, scale=None):
        """
        Corta um pedaço da imagem (subsurface).
        """
        x = frame_coluna * width
        y = frame_linha * height

        # Define o retangulo cortado
        rect = pygame.Rect(x, y, width, height)
        
        # Armazena o recorte
        image = self.sheet.subsurface(rect)

        # Da o zoom
        if scale:
            image = pygame.transform.scale(image, scale)

        return image