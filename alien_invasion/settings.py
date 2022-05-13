class Settings(): #Uma classe para armazenar todas as configurações da Invasão Alienigena
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        # Configurações da espaçonave 
        self.ship_limit = 3
        # configurações dos projéteis
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10
        # configurações dos aliens
        self.fleet_drop_speed = 10
        # a taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.5
        # a taxa com que os pontos para cada alienigena aumentam
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self): # inicializa as configurações que mudam no decorrer do jogo
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1.2
        # fleet_direction igual a 1 -> direita; igual a -1 -> esquerda
        self.fleet_direction = 1 
        # pontuação 
        self.alien_points = 50

    def increase_speed(self): # aumenta  as configurações de velocidade
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale) 
        print(self.alien_points)
