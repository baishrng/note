---
time 模块
---

## pygame.time

Pygame 中用于监控时间的模块。

---

## 函数

- pygame.time.get_ticks() —— 获取以毫秒为单位的时间
- pygame.time.wait() —— 暂停程序一段时间
- pygame.time.delay() —— 暂停程序一段时间
- pygame.time.set_timer() —— 在事件队列上重复创建一个事件
- pygame.time.Clock() —— 创建一个对象来帮助跟踪时间

Pygame中的时间以毫秒（1/1000秒）表示。大多数平台的时间分辨率有限，大约为10毫秒。该分辨率（以毫秒为单位) 以常量 TIMER_RESLUTION 给出。

---

## 函数详解

### **pygame.time.get_ticks()**

获取以毫秒为单位的时间

get_ticks() -> milliseconds

返回自 pygame_init() 调用以来的毫秒数。在pygame初始化之前，这将始终为0。

### pygame.time.wait()

暂停程序一段时间

wait(milliseconds) -> time

将暂停一段给定的毫秒数。此函数会暂停进程以与其他程序共享处理器。等待几毫秒的程序将消耗非常少的处理器时间。它比pygame.time.delay() 函数稍微准确一些。

这将返回实际使用的毫秒数。

### **pygame.time.delay()**

暂停程序一段时间

delay(milliseconds) -> time

将暂停给定的毫秒数。此功能将使用处理器（而不是休眠），使用 pygame.time.wait() 以使延迟更准确。

这将返回实际使用的毫秒数。

### pygame.time.set_timer()

在事件队列上重复创建一个事件

set_timer(event, millis) -> None

set_timer(event, millis, loops=0) -> None

将事件类型设置为每隔给定的毫秒数显示在事件队列中。第一个事件将在经过一段时间后才会出现。

每种事件类型都可以附加一个单独的计时器。在 pygame.USEREVENT 和 pygame.NUMEVENTS 中使用该值更好。

要禁用事件的计时器，请将milliseconds参数设置为0。

### pygame.time.Clock()

创建一个对象来帮助跟踪时间

Clock() -> Clock

- pygame.time.Clock.tick() —— 更新时钟
- pygame.time.Clock.tick_busy_loop() —— 更新时钟
- pygame.time.Clock.get_time() —— 在上一个tick中使用的时间
- pygame.time.Clock.get_rawtime() —— 在上一个tick中使用的实际时间
- pygame.time.Clock.get_fps() —— 计算时钟帧率

创建一个新的Clock对象，可用于跟踪一段时间。时钟还提供了几个功能来帮助控制游戏的帧速率。

#### tick()

更新时钟

tick(framerate=0) -> milliseconds

该方法每帧应调用一次。它将计算从上次调用到现在已经过去了多少毫秒。

如果您传递了可选的帧速率参数，函数将延迟以保持游戏运行速度低于给定的每秒滴答数。这有助于限制游戏的运行速度。每帧调用一次 Clock.tick(40)，程序的运行速度就不会超过每秒 40 帧。

请注意，该函数使用的 SDL_Delay 函数并非在每个平台上都准确，但不会占用太多 CPU。如果您想要一个精确的计时器，并且不介意占用 CPU，请使用 tick_busy_loop。

#### tick_busy_loop()

更新时钟

tick_busy_loop(framerate=0) -> milliseconds

应该每帧调用一次此方法。它将计算自上一次调用以来经过的毫秒数。

如果您传递可选的帧率参数，该函数将延迟以使游戏运行速度低于每秒给定的滴答数。这可以用于帮助限制游戏的运行时速度。通过每帧调用 一次 Clock.tick_busy_ioop(40)，程序将永远不会超过每秒40帧。

请注意，该函数使用 pygame.time.delay()将程序暂停一段时间，这将在繁忙循环中消耗大量 CPU，以确保计时更加精确。

#### get_time()

在上一个tick中使用的时间

get_time() -> milliseconds

前两次调用 Clock.tick() 之间的毫秒数。

#### get_rawtime()

在上一个tick中使用的实际时间

get_rawtime() -> milliseconds

类似于 Clock.get_time()，但不包括 Clock.tick() 延迟限制帧速率时使用的任何时间。

#### get_fps()

计算时钟帧率

get_fps() -> float

计算游戏的帧速率（以每秒帧数为单位）。它是通过平均最后十次调用来计算的 Clock.tick() 。

---

## 示例

```python
import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置窗口尺寸
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Time Example")

# 创建一个时钟对象
clock = pygame.time.Clock()

# 主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 退出 Pygame
            pygame.quit()
            sys.exit()

    # 清屏
    screen.fill((0, 0, 0))

    # 显示内容
    pygame.display.flip()

    # 控制每秒帧数
    clock.tick(60)  # 设定为 60 FPS
```

---

## 参考文献

https://www.pygame.org/docs/ref/time.html

https://www.kancloud.cn/lchy0987/pydic/3060865

chatgpt