import pygame

from ship import Ship

class ScoreBoard():
    """分数展示类"""
    def __init__(self, ai_game):
        self.ai_game = ai_game      # 获取 AlienInvasion 实例
        self.screen = ai_game.screen    # 获取游戏屏幕
        self.screen_rect = ai_game.screen.get_rect()    # 获取屏幕的rect
        self.settings = ai_game.settings    # 获取游戏设置
        self.stats = ai_game.stats  # 获取游戏所有的状态变量

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)   # 设置字体

        self.prep_score()   # 准备分数图片
        self.prep_high_score()  # 准备最高分数图片
        self.prep_level()   # 准备等级图片
        self.prep_ships()   # 准备剩余飞船图片

    def prep_score(self):
        """准备分数图片"""
        round_score = round(self.stats.score, -1)   # 四舍五入分数，保留十位数
        score_str = f"{round_score:,}"      # 将分数转换为格式化字符串，在数字中增加 , 号

        # 创建图片(文本, 为True文本边缘更加光滑, 文本颜色, 图片背景颜色)
        self.score_img = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_img.get_rect()     # 获取图片的rect
        self.score_rect.right = self.screen_rect.right - 20     # 设置图片的rect
        self.score_rect.top = 20

    def prep_high_score(self):
        """准备最高分数图片"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_img = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        """准备等级图片"""
        self.level_str = str(self.stats.level)
        self.level_img = self.font.render(self.level_str, True, self.text_color, self.settings.bg_color)

        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.screen_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """准备剩余飞船图片"""
        self.ships = pygame.sprite.Group()      # 创建了一个精灵组
        for ship_num in range(self.stats.ship_left):
            ship = Ship(self.ai_game)
            ship.rect.x = ship_num * ship.rect.width + 10
            ship.rect.y = 10
            self.ships.add(ship)    # 将飞船实例加入组中，ship类必须继承 pygame.sprite.Sprite

    def show_score(self):
        """绘制分数"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """检查最高分数"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()  # 准备最高分数图片

