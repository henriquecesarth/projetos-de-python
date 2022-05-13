import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen): # inicializa a espaçonave e define sua posição inicial.
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # carrega a imagem da espacionave e obtém seu rect
        self.image = pygame.image.load('images/ship_mini.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # inicia cada nova espacionave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)
        # flag de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self): # Atualiza a posição da espaçonave de acordo com a flag de movimento
        # atualiza o valor do centro da espaçonave, e não o retângulo
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # atualiza o objeto rect de acordo com self.center
        self.rect.centerx = self.center


    def blitme(self): # desenha a espacionave em sua posição atual
        self.screen.blit(self.image, self.rect)

    def center_ship(self): #centraliza a espaçonave na tela
        self.center = self.screen_rect.centerx
