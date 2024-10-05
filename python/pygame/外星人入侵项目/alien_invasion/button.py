import pygame


class Button():
    """按钮类"""
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen    # 获取游戏屏幕
        self.screen_rect = ai_game.screen.get_rect()    # 获取屏幕的rect
        self.width, self.height = 200, 50       # 设置按钮的尺寸
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)   # 设置文本的字体

        self.rect = pygame.Rect(0, 0, self.width, self.height)      # 创建按钮的rect
        self.rect.center = self.screen_rect.center      # 设置按钮的rect

        self._prep_msg(msg)     # 准备按钮的图片

    def _prep_msg(self, msg):
        """准备按钮的图片"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制按钮"""
        self.screen.fill(self.button_color, self.rect)  # 填充颜色(颜色，在哪儿填充)
        self.screen.blit(self.msg_image, self.msg_image_rect)   # 绘制图片
