import json


class GameStats(): # armazena os dados estatísticos da Invasão Alienigena
    def __init__(self, ai_settings): # inicializa os dados estatísticos
        self.ai_settings = ai_settings
        self.reset_stats()
        # inicia a Invasão Alienigena em um estado inativo
        self.game_active = False
        self.game_pause = False
        # a pontuação máxima jamais deverá ser reiniciada
        self.load_stats()

    def reset_stats(self): # inicializa os dados estatísticos que podem mudar durante o jogo
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
    
    def load_stats(self):
        filename = 'high_score.json'
        with open(filename) as f_obj:
            self.high_score = json.load(f_obj)
