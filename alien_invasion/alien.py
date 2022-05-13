import pygame
from pygame.sprite import Sprite

class Alien(Sprite): # uma classe q ue representa um únicco alien da frota
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # carrega a imagem do alienigena e define seu atributo rect
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        # inicia cada alienigena proximo à parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # armazena a posição exata do alienigena 
        self.x = float(self.rect.x)

    def blitme(self): # desenha ao alienigena em sua posição atual
        self.screen.blit(self.image, self.rect)

    def check_edges(self): # Devolve true se o alienigena estiver na borda da tela
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self): #move o alienigena para a direita.
        self.x += self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction
        self.rect.x = self.x





