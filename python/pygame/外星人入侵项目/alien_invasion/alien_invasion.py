import pygame
import sys
from time import sleep

from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard
from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien



class AlienInvasion:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        pygame.init()   # 初始化pygame库，必写语句
        self.clock = pygame.time.Clock()
        self.settings = Settings()  # 创建设置示例，游戏用到的所有与设置有关的变量或常量均在里面

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))    # 设置界面及大小
        pygame.display.set_caption('外星人入侵')     # 设置界面标题

        self.stats = GameStats(self)    # 创建状态实例，保存游戏过程中产生的状态变量
        self.ship = Ship(self)      # 创建飞船实例
        self.bullets = pygame.sprite.Group()    # 创建子弹组
        self.aliens = pygame.sprite.Group()     # 创建外星人组
        self.game_active = False    # 判断游戏是否正在运行
        self.play_button = Button(self, 'Play')     # 游戏开始按钮
        self.sb = ScoreBoard(self)      # 与分数展示相关的实例

        self._create_fleet()    # 创建满屏外星人

    def run_game(self):
        """游戏循环"""
        while True:
            self._check_events()    # 查看事件

            if self.game_active:
                self.ship.update()      # 更新飞船
                self._update_bullets()      # 更新子弹组
                self._update_aliens()   # 跟新外星人组

            self._update_screen()   # 更新屏幕（界面）
            self.clock.tick(60)     # 设置游戏帧率

    def _check_fleet_edges(self):
        """检查外星人是否碰到界面的左右边"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()      # 改变外星人水平移动的方向
                break

    def _check_aliens_buttom(self):
        """检查外星人是否碰倒界面的的底部"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()    # 处理飞船碰撞
                break

    def _check_bullet_alien_collision(self):
        """检查子弹与外星人是否发生碰撞"""
        # 检查是否有子弹集中外星人
        # 如有，则删除子弹和外星人
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, False, True)

        # 计分
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)    # 加上消灭外星人的分数(消灭外星人数*每个外星人分数)
            self.sb.prep_score()    # 重新准备分数图片
            self.sb.check_high_score()  # 重新准备最高分数图片

        # 如何外星人被全部消灭
        if not self.aliens:
            self.bullets.empty()    # 清空屏幕上的子弹
            self._create_fleet()    # 重新创建满屏的外星人
            self.settings.increase_speed()  # 增加子弹、外星人移动等速度

            self.stats.level += 1   # 等级提升
            self.sb.prep_level()    # 重新准备等级图片

    def _check_events(self):
        """检查事件、处理事件"""
        for event in pygame.event.get():    # 获取事件
            if event.type == pygame.QUIT:   # 如果事件为点击屏幕右上角的退出按钮
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 如果事件类型为键盘按下
                self._check_keydown_events(event)   # 处理键盘按下事件
            elif event.type == pygame.KEYUP:    # 如果事件类型为键盘松开
                self._check_keyup_events(event)     # 处理键盘松开事件
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 如果事件类型为鼠标按下
                mouse_pos = pygame.mouse.get_pos()      # 获取鼠标按下的位置
                self._check_play_button(mouse_pos)  # 处理鼠标按下事件

    def _check_keydown_events(self, event):
        """处理键盘按下事件"""
        if event.key == pygame.K_RIGHT:     # 右键按下
            self.ship.moving_right = True   # 飞创向右移动标志为真
        elif event.key == pygame.K_LEFT:    # 左键按下
            self.ship.moving_left = True    # 飞创向左移动标志为真
        elif event.key == pygame.K_q:   # 大写的Q按下
            sys.exit()
        elif event.key == pygame.K_SPACE:   # 空格键按下
            self._fire_bullet()     # 发出子弹

    def _check_keyup_events(self, event):
        """处理键盘松开事件"""
        if event.key == pygame.K_RIGHT:     # 右键松开
            self.ship.moving_right = False  # 飞创向右移动标志为假
        elif event.key == pygame.K_LEFT:    # 左键松开
            self.ship.moving_left = False   # 飞创向左移动标志为假

    def _check_play_button(self, mouse_pos):
        """处理鼠标按下事件"""
        # 如果鼠标点击位置与游戏开始按钮碰撞 且 此时游戏处于处于停止状态
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active:
            self.settings.initialize_dynamic_settings()     # 重置设置
            self.game_active = True     # 使游戏运行标志为真
            self.stats.reset_stats()    # 重置状态变量，如分数、等级
            self.sb.prep_score()    # 重新准备分数图片
            self.sb.prep_level()    # 重新准备最高分数图片
            self.sb.prep_ships()    # 重新准备剩余飞船图片

            self.bullets.empty()    # 清空屏幕上的子弹
            self.aliens.empty()     # 清空屏幕上的外星人

            self._create_fleet()    # 重新创建满屏的外星人
            self.ship.center_ship() # 改变飞船位置，使飞船置于屏幕底部的中间

            pygame.mouse.set_visible(False)     # 隐藏光标

    def _change_fleet_direction(self):
        """改变外星人的水平移动方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed  # 使所有外星人向下移动固定距离
        self.settings.fleet_direction *= -1     # 改变水平移动方向

    def _create_fleet(self):
        """创建满屏的外星人，与屏幕的四边均留有一定的距离"""
        alien = Alien(self)     # 创建外星人实例
        alien_width, alien_height = alien.rect.size     # 获取外星人的尺寸

        current_x, current_y = alien_width, alien_height    # 设置外星人的初始位置
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width    # x轴位置向右移动

            current_x = alien_width     # 重置x轴位置
            current_y += 2 * alien_height   # y轴位置向下移动

    def _create_alien(self, x_position, y_position):
        """创建一个外星人"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)  # 将外星人实例加入到外星人组中，然后在_update_screen()方法中统一绘制

    def _ship_hit(self):
        """处理飞船碰撞"""
        # 判断剩余飞船数
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1   # 剩余飞船数减一
            self.sb.prep_ships()    # 重新准备剩余飞船图片

            self.bullets.empty()    # 清空屏幕上的子弹
            self.aliens.empty()     # 清空屏幕上的外星人

            self._create_fleet()    # 重新创建满屏的外星人
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.game_active = False    # 游戏停止
            pygame.mouse.set_visible(True)      # 使光标可见

    def _fire_bullet(self):
        """发出子弹"""
        # 判断屏幕上的子弹数是否已经达到上限
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)    # 将子弹实例加入到子弹组中，然后在_update_screen()中统一绘制

    def _update_bullets(self):
        """更新子弹位置和状态"""
        self.bullets.update()   # 更新子弹位置

        self._check_bullet_alien_collision()    # 检查子弹与外星人是否发生碰撞

        # 检查子弹是否从顶部射出界面（因为要对组里的元素做处理，所以这里用的copy()副本）
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))  # 最好不要有输出语句，会降低游戏体验（测试时可以用）

    def _update_aliens(self):
        """更新外星人位置和状态"""
        self._check_fleet_edges()   # 检查外星人是否碰到界面的左右边
        self.aliens.update()    # 外星人组自带的更新位置的方法

        # 检查飞船与外星人是否发生碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()    # 处理飞船碰撞

        self._check_aliens_buttom()     # 检查外星人是否碰到底部

    def _update_screen(self):
        """更新屏幕"""
        self.screen.fill(self.settings.bg_color)  # 设置背景颜色

        # 绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()  # 绘制飞船
        self.aliens.draw(self.screen)   # 绘制所有外星人

        self.sb.show_score()    # 绘制分数、最高分数和等级等

        if not self.game_active:
            self.play_button.draw_button()  # 绘制游戏开始按钮

        pygame.display.flip()  # 刷新界面

if __name__ == '__main__':
    ai =  AlienInvasion()
    ai.run_game()
