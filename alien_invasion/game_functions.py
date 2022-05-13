import json
import sys, pygame
from alien import Alien
from bullet import Bullet
from time import sleep


def check_keydown_events(event, ai_settings, screen, ship, bullets, stats, aliens, sb): # Responde se pressionarmos a tecla
    if event.key == pygame.K_RIGHT: # move a espaçonave para a direita
        ship.moving_right = True
    elif event.key == pygame.K_LEFT: # move a espaçonave para a esquerda
        ship.moving_left = True
    elif event.key == pygame.K_SPACE: # cria um novo projétil e o adiciona  ao grupo de projéteis
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        start_game(ai_settings, screen, stats, sb, aliens, bullets, ship)
    elif event.key == pygame.K_ESCAPE:
        pause_game(stats)

def pause_game(stats):
    if stats.game_pause:
        stats.game_active = True
        stats.game_pause = False
    elif not stats.game_pause:
        stats.game_active = False
        stats.game_pause = True

def check_keyup_events(event, ship): # Responde se soltarmos a tecla
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets): # responde a eventos de pressionamento de teclas e de mouse.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, stats, aliens, sb)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y): # inicia um novo jogo quando o jogador clicar em Play.
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, sb, aliens, bullets, ship)
        
def start_game(ai_settings, screen, stats, sb, aliens, bullets, ship):
        # reinicia as configurações do jogo
        ai_settings.initialize_dynamic_settings()
        # oculta o cursor do mouse
        pygame.mouse.set_visible(False)
        # reinicia os dados estatísticos do jogo
        stats.reset_stats()
        stats.game_active = True
        # reinicia as imagens do painel de pontuação
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        # esvazia a lista de alienígenas e de projéteis
        aliens.empty()
        bullets.empty()
        # cria uma nova frota e centraliza a espaçonave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def fire_bullet(ai_settings, screen, ship, bullets): # dispara um projétil se o limite ainda não foi alcançado
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    # redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    # redesenha todos os projéteis atrás da espaçonave e dos alienigenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # desenha a informação sobre pontuação 
    sb.show_score()
    # desenha o botão Play se o jogo estiver inativo
    if not stats.game_active and not stats.game_pause:
        play_button.draw_button()
    # deixa a tela mais recente visivel
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets): # Atualiza a posição dos projéteis e se livra dos projéteis antigos
    bullets.update()
    # livra-se ods projéteis  que desapareceram
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # verifica se algum projétil atingiu os alienigenas
    # em caso afirmativo, livra-se do projétil e do alienigena
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets): # responde as colisões entre projéteis e alienigenas
    # remove qualquer projétil e alienigena que tenham colidido
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points*len(aliens)
            sb.prep_score()
            check_high_score(stats, sb)
    if len(aliens) == 0: # destrói os projéteis existentes e cria uma nova frota
        bullets.empty()
        ai_settings.increase_speed()
        # aumenta o nível
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)

def get_number_aliens_x(ai_settings, alien_width): #determina o número de alienigenas que cabem em uma linha
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height): # Determina o número de linhas com alienigenas que cabem na tela
    available_space_y = (ai_settings.screen_height - (4*alien_height) - ship_height)
    number_rows = int(available_space_y/ (2*alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number): #cria um alienigena e o posiciona na linha
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_number*alien_width
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)
    
def create_fleet(ai_settings, screen, ship, aliens): # cria uma frota completa de alienigenas
    # cria um alienigena e calcula o número de alienigenas numa linha
    # o espaçamento entre os alienigenas é igual a largura de um alienigena
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # cria frota de alienigenas
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x): # cria um alienigena e o posiciona na linha
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
    
def check_fleet_edges(ai_settings, aliens): # responde apropriadamente se algum alienigena alcançou uma borda
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens): # faz toda a frota descer e muda sua direção
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets): # responde ao fato de a espaçonave ter sido atingida por um alienigena
    if stats.ships_left > 0:
        # decrementa ships_left
        stats.ships_left -= 1
        # atualiza o painel de pontuações 
        sb.prep_ships()
        # esvazia a lista de alienígenas e de projéteis
        aliens.empty()
        bullets.empty()
        # cria uma nova frota e centraliza a espaçonave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # faz pausa
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        save_high_score(stats)
        
def save_high_score(stats):
    filename = 'high_score.json'
    with open(filename, 'w') as f_obj:
        json.dump(stats.high_score, f_obj)


def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets): # verifica se algum alienigena alcançou a parte inferior da tela
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom: # trata esse caso do mesmo modo  que é feito quando a espacionave é atingida
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets): # atualiza as posições de todos os aliens da tropa
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # verifica se houve colisões entre alienigenas e a espaçonave
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
    # verifica se há algum alienigena que atingiu a parte inferior da tela
    check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)
    
def check_high_score(stats, sb): # verifica se há uma nova pontuação máxima
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
