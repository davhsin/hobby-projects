import pygame
from enum import Enum

class Direction(Enum):
    LEFT = 'left',
    RIGHT = 'right',
    UP = 'up',
    DOWN = 'down',
    STOP = 'stop'

class Snake:
    """ 處理有關蛇的狀態 """

    def __init__(self, snake_game) -> None:
        """ 初始化蛇的屬性 """
        
        # 取得surface，之後在上面畫圖
        self.screen = snake_game.screen

        # 紀錄蛇的全身
        self.body: list[pygame.Rect] = []

        # 初始化蛇的顏色
        self.color = pygame.Color(53, 222, 0)

        # 初始化蛇的頭部 
        self.body.append(pygame.Rect(600, 450, 30, 30))

        # 初始化蛇的方向，一開始是靜止的
        self.dir = Direction.STOP 

    def draw_snake(self) -> None:
        """ 畫出整隻蛇 """
        for per_rect in self.body:
            # 畫身體 
            pygame.draw.rect(self.screen, self.color, per_rect)
            # 畫邊框 
            border_width = 2  
            border_rect = per_rect.inflate(border_width * 2, border_width * 2)
            pygame.draw.rect(self.screen, (0, 0, 0), border_rect, border_width)

    def update_body(self, dir) -> None:
        """先新增頭部至list最前方，再刪除尾巴。"""
        self.body.insert(
            0, pygame.Rect(self.body[0].x, self.body[0].y, 30, 30)) 
        self.body.pop()

        """ 根據方向鍵改變方向 """
        if dir == Direction.UP:
            self.body[0].y -= 30 
        elif dir == Direction.DOWN:
            self.body[0].y += 30 
        elif dir == Direction.LEFT:
            self.body[0].x -= 30
        elif dir == Direction.RIGHT:
            self.body[0].x += 30
