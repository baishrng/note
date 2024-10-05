import pygame
from pygame import Rect
from pygame.sprite import Sprite


class Bullet(Sprite):
    """子弹类, 继承 Sprite"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen    # 获取游戏屏幕
        self.settings = ai_game.settings    # 获取游戏设置
        self.color = self.settings.bullet_color     # 设置子弹颜色

        self.rect = Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)     # 创建子弹的rect
        self.rect.midtop = ai_game.ship.rect.midtop     # 设置子弹的rect

        self.y = float(self.rect.y)     # 用于更精细化的控制子弹的垂直位置

    def update(self):
        """更新子弹的位置"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """绘制子弹"""
        # 绘制矩形(参数说明：在哪儿上面绘制，矩形的颜色， 矩形的位置)
        pygame.draw.rect(self.screen, self.color, self.rect)