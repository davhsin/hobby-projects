import sys
import pygame
from settings import Settings
from snake import Snake, Direction
from food import Food
from score_board import ScoreBoard

class SnakeGame:
    """ 管理整個遊戲的資源和行為"""

    def __init__(self):
        """ 初始化遊戲和載入資源 """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
           
        pygame.display.set_caption("Snake")
        
        self.snake = Snake(self)
        self.food = Food(self)
        self.score_board = ScoreBoard(self)
        self.game_active = True

    def check_keydown_events(self, event):
        """ keydown事件 """
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_DOWN and self.snake.dir != Direction.UP:
            self.snake.dir = Direction.DOWN
        elif event.key == pygame.K_RIGHT and self.snake.dir != Direction.LEFT:
            self.snake.dir = Direction.RIGHT
        elif event.key == pygame.K_LEFT and self.snake.dir != Direction.RIGHT:
            self.snake.dir = Direction.LEFT
        elif event.key == pygame.K_UP and self.snake.dir != Direction.DOWN:
            self.snake.dir = Direction.UP

    def check_events(self):
        """ 檢查遊戲的所有事件 """
        for event in pygame.event.get():      
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

    def update_screen(self):
        """ 更新畫面上的背景、蛇與食物 """
        # 填充遊戲背景
        self.screen.fill(self.settings.bg_color)

        # 更新食物位置 
        self.food.update()

        # 更新蛇的位置，若吃到食物身體變長，沒吃到就碰撞偵測
        self.update_snake()

        # 更新整個視窗
        pygame.display.flip()

    def update_snake(self):
        # 在地圖上更新蛇的位置
        self.snake.update_body(self.snake.dir)
        self.snake.draw_snake() 

        if (self.snake.body[0].x == self.food.coord.x and
            self.snake.body[0].y == self.food.coord.y):
            for _ in range(4):
                self.snake.body.append(
                    pygame.Rect(
                        self.snake.body[-1].x, self.snake.body[-1].y, 30, 30))
            self.food.new_food() 
        else:
            # 當蛇身長大於等於5時進行碰撞偵測
            if len(self.snake.body) >= 5: 
                if self.snake.body[0] in self.snake.body[1:]:
                    print("頭碰到身體")
                    self.game_active = False

            #  判斷是否出界
            if (self.snake.body[0].x > self.settings.screen_width or 
                self.snake.body[0].y > self.settings.screen_height or 
                self.snake.body[0].x < 0 or 
                self.snake.body[0].y < 0):
                print("超出邊界!")
                self.game_active = False

    def run_game(self):
        while True:
            self.check_events()

            if self.game_active:
                self.update_screen()
            else:
                """ Show Result """
                self.screen.fill(self.settings.bg_color)
                self.score_board.prepare_msg(len(self.snake.body))
                self.score_board.draw_score_board()
                pygame.display.flip()

            self.clock.tick(10)

if __name__ == '__main__' :
    s = SnakeGame()
    s.run_game() 
