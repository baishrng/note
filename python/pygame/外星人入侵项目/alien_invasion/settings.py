class Settings():
    """设置类"""
    def __init__(self):
        self.screen_width = 800     # 屏幕宽度
        self.screen_height = 600    # 屏幕高度
        self.bg_color = (230, 230, 230)     # 背景颜色

        self.ship_limit = 3     # 飞船上限

        self.bullet_width = 3       # 子弹宽度
        self.bullet_height = 15     # 子弹高度
        self.bullet_color = (60, 60, 60)    # 子弹颜色
        self.bullets_allowed = 3    # 允许同时出现在屏幕上的子弹数

        self.fleet_drop_speed = 10  # 外星人组向下移动的距离

        self.score_scale = 1.5      # 分数上升的比例

        self.spaceup_scale = 1.1    # 速度提升比例
        self.initialize_dynamic_settings()      # 初始化动态设置

    def initialize_dynamic_settings(self):
        """初始化动态设置"""
        self.ship_speed = 1.5       # 飞船速度
        self.bullet_speed = 2.5     # 子弹速度
        self.alien_speed = 1.0      # 外星人速度
        self.alien_points = 50      # 每个外星人分数

        self.fleet_direction = 1  # 1 表示向右移动， -1 表示向左移动

    def increase_speed(self):
        """提升难度"""
        self.ship_speed *= self.spaceup_scale
        self.bullet_speed *= self.spaceup_scale
        self.alien_speed *= self.spaceup_scale
        self.alien_points = int(self.alien_points * self.score_scale)   # 提升每个外星人分数
        # print(self.alien_points)
