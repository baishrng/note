class GameStats():
    """游戏状态类"""
    def __init__(self, ai_game):
        self.settings = ai_game.settings    # 获取游戏设置
        self.high_score = 0     # 游戏最高分数
        self.reset_stats()      # 重置状态变量

    def reset_stats(self):
        """重置状态变量"""
        self.ship_left = self.settings.ship_limit   # 剩余飞船数
        self.score = 0      # 游戏得分
        self.level = 1      # 玩家等级