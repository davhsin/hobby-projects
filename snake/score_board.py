import pygame.font
from snake import Snake

class ScoreBoard:
    """計分板 顯示遊戲結果"""

    def __init__(self, snake_game):
        self.screen = snake_game.screen
        self.screen_rect = self.screen.get_rect()
        self.snake = Snake(self)

        self.width, self.height = 200, 50 
        self.text_bg_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font('freesansbold.ttf', 52)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

    def prepare_msg(self, snake_length):

        # GAME OVER 
        self.game_over_text = \
            self.font.render(
                'GAME OVER', 
                True, 
                self.text_color,
                self.text_bg_color)

        self.game_over_text_rect = self.game_over_text.get_rect()
        self.game_over_text_rect.center = self.rect.center 
        self.game_over_text_rect.y -= 100

        # Length: 
        self.length_text = \
             self.font.render(
                 f"Length: {str(snake_length)}",
                 True,
                 self.text_color,
                 self.text_bg_color)

        self.length_text_rect = self.length_text.get_rect()
        self.length_text_rect.x = 472
        self.length_text_rect.y = 400

        # Quit hint
        self.quit_text = \
            self.font.render(
                "Press q to quit", 
                True,
                self.text_color,
                self.text_bg_color)

        self.quit_text_rect = self.quit_text.get_rect()
        self.quit_text_rect.x = 420
        self.quit_text_rect.y = 480

    def draw_score_board(self):
        self.screen.fill(self.text_bg_color, self.rect)
        self.screen.blit(self.game_over_text, self.game_over_text_rect)
        self.screen.blit(self.length_text, self.length_text_rect)
        self.screen.blit(self.quit_text, self.quit_text_rect)
