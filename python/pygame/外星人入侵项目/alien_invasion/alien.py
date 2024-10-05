import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """外星人类, 继承 Sprite"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen    # 获取游戏屏幕
        self.settings = ai_game.settings    # 获取游戏设置

        self.image = pygame.image.load('images/alien.bmp')  # 加载外星人图片
        self.rect = self.image.get_rect()   # 获取飞船图片的rect

        self.rect.x = self.rect.width   # 将飞船的水平位置设置为飞船图片的宽
        self.rect.y = self.rect.height  # 将飞船的垂直位置设置为飞船图片的高

        self.x = float(self.rect.x)     # 用于更精细化的控制飞船的水平位置

    def check_edges(self):
        """检查飞船是否碰到屏幕的左右边界"""
        screen_rect =self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= screen_rect.left)

    def update(self):
        """更新飞船的位置"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x


