import pygame
from pygame.sprite import Sprite

class Bullet(Sprite): # uma classe que administra projéteis disparados pela nave
    def __init__(self,ai_settings, screen, ship) : # Cria um objeto para o projétil na posução atual da nave
        super().__init__()
        self.screen = screen
        # cria um retângulo para o projétil em (0,0) e, em seguida, define a posição correta
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # armazena a posição do projétil como um valor decimal
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self): # Move o projétil para cima na tela
        #atualiza a posição decimal do projétil
        self.y -= self.speed_factor
        # atualiza a posição de rect
        self.rect.y = self.y
    
    def draw_bullet(self): # desenha o projétil na tela
        pygame.draw.rect(self.screen, self.color, self.rect)
        