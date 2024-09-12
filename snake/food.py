import pygame
import random

class Food:
    """ 處理食物的狀態 """
    def __init__(self, snake_game):
        self.screen = snake_game.screen
        self.color = pygame.Color(255, 0, 0)
        self.coord = pygame.Rect(
            random.randint(1, 39) * 30, random.randint(1, 29) * 30, 30, 30) 

    def new_food(self):
        """隨機生成食物在某處"""
        self.coord.x = random.randint(1, 39) * 30   
        self.coord.y = random.randint(1, 29) * 30 

    def update(self):
        """ 在畫面上畫出食物 """
        self.food = pygame.draw.rect(
                self.screen, self.color, self.coord)
