import pygame


class Ship(pygame.sprite.Sprite):
    """飞船类，继承 Sprite"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen    # 获取游戏屏幕
        self.screen_rect = ai_game.screen.get_rect()    # 获取屏幕的rect
        self.settings = ai_game.settings    # 获取游戏设置

        self.image = pygame.image.load('images/ship.bmp')   # 加载飞船图片
        self.rect = self.image.get_rect()   # 获取图片的rect
        self.rect.midbottom = self.screen_rect.midbottom    # 设置图片的rect
        self.x = float(self.rect.x)

        self.moving_right = False   # 飞船向右移动标志
        self.moving_left = False    # 飞船向左移动标志

    def update(self):
        """更新飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """绘制飞船图片"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """重置飞船位置"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


