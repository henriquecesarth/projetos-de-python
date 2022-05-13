import pygame
from button import Button
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
                                                             
def run_game(): #Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # cria o botão Play
    play_button = Button(ai_settings, screen, "Play")
    # cria uma instância para armazenar dados estatísticos do jogo e cria painel de pontuação
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # cria uma espaçonave, um grupo de projéteis e um grupo de alienigenas
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # cria frota de alienigenas
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # inicia o laço principal do jogo
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen,stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
            

run_game()
