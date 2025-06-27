---
cursors 模块
---

## **pygame.cursors**

Pygame 中使用光标资源的模块。

---

## **函数**

- pygame.cursors.compile() —— 由纯字符串创建二进制光标数据
- pygame.cursors.load_xbm() —— 由一个xbm 文件载入光标数据
- [pygame.cursors.Cursor](https://www.pygame.org/docs/ref/cursors.html#pygame.cursors.Cursor)() —— 代表光标的 pygame 对象

Pygame 提供对系统硬件光标的控制。Pygame 支持黑白光标（位图光标）、系统变量光标和彩色光标。您可以使用 pygame.mouse模块中的函数来控制光标，从而与鼠标协同工作。

该光标模块包含加载和解码各种光标格式的函数。通过这些函数，您可以轻松地将光标存储到外部文件中，或直接存储为编码后的 python 字符串。

该模块包含多个标准光标。pygame.mouse.set_cursor()将鼠标光标设置为一个新光标的函数需要几个参数。所有这些参数都存储在一个元组中，你可以像这样调用：

```python
pygame.mouse.set_cursor(*pygame.cursors.arrow)
```

以下变量可以传递给 pygame.mouse.set_cursor 函数：

- `pygame.cursors.arrow`
- `pygame.cursors.diamond`
- `pygame.cursors.broken_x`
- `pygame.cursors.tri_left`
- `pygame.cursors.tri_right`

本模块还包含一些格式化字符串的游标。在使用之前，您需要将这些游标传递给 pygame.cursors.compile() 函数。调用示例如下

```python
cursor = pygame.cursors.compile(pygame.cursors.textmarker_strings)
pygame.mouse.set_cursor((8, 16), (0, 0), *cursor)
```

使用 pygame.cursors.compile() 可以将下列字符串转换为游标位图：

- `pygame.cursors.thickarrow_strings`
- `pygame.cursors.sizer_x_strings`
- `pygame.cursors.sizer_y_strings`
- `pygame.cursors.sizer_xy_strings`
- `pygame.cursor.textmarker_strings`

---

## **函数详解**

### **pygame.cursors.compile()**

由纯字符串创建二进制光标数据。

compile(strings, black='X', white='.', xor='o') -> data, mask

一串连续的字符串可以被用于创建对应系统光标的二进制光标数据。返回值要和 pygame.mouse.set_cursor() 所需要的参数格式相同。

如果你正在创建自己的光标字符串，你可使用任何值来代表白色和黑色像素。一些系统允许你根据系统颜色自己设置一种特殊的切换色，也被称为 xor 色。如果系统不支持 xor 光标，则光标颜色将会变为纯黑色。

字符串的长度必须全部相等，而且可以被 8 整除。一个光标字符串设定示例，如下所示：

```
thickarrow_strings = (               #sized 24x24
  "XX                      ",
  "XXX                     ",
  "XXXX                    ",
  "XX.XX                   ",
  "XX..XX                  ",
  "XX...XX                 ",
  "XX....XX                ",
  "XX.....XX               ",
  "XX......XX              ",
  "XX.......XX             ",
  "XX........XX            ",
  "XX........XXX           ",
  "XX......XXXXX           ",
  "XX.XXX..XX              ",
  "XXXX XX..XX             ",
  "XX   XX..XX             ",
  "     XX..XX             ",
  "      XX..XX            ",
  "      XX..XX            ",
  "       XXXX             ",
  "       XX               ",
  "                        ",
  "                        ",
  "                        ")
```

示例：

```python
import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置窗口
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Custom Cursor Example")

# 定义光标位图，确保每行宽度为8的倍数
thickarrow_strings = (               #sized 24x24
  "XX                      ",
  "XXX                     ",
  "XXXX                    ",
  "XX.XX                   ",
  "XX..XX                  ",
  "XX...XX                 ",
  "XX....XX                ",
  "XX.....XX               ",
  "XX......XX              ",
  "XX.......XX             ",
  "XX........XX            ",
  "XX........XXX           ",
  "XX......XXXXX           ",
  "XX.XXX..XX              ",
  "XXXX XX..XX             ",
  "XX   XX..XX             ",
  "     XX..XX             ",
  "      XX..XX            ",
  "      XX..XX            ",
  "       XXXX             ",
  "       XX               ",
  "                        ",
  "                        ",
  "                        ")

# 编译光标
cursor = pygame.cursors.compile(thickarrow_strings, black='X', white='.')

# 创建光标，(宽度, 高度)和热区坐标
pygame.mouse.set_cursor((24, 24), (0, 2), *cursor)

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 清屏
    screen.fill((255, 255, 255))

    # 刷新显示
    pygame.display.flip()

# 退出 Pygame
pygame.quit()
sys.exit()
```

### **pygame.cursors.load_xbm()**

由一个xbm 文件载入光标数据。

load_xbm(cursorfile) -> cursor_args

load_xbm(cursorfile, maskfile) -> cursor_args

该方法将根据 XBM 文件的某一个简单子集载入光标。XBM 文件从传统上是被用于保存 UNIX 系统内光标，它们是被用于代表一些简单图像的 ASCII 码。

一些时候，白色和黑色值将会分开在两个独立的 XBM 文件中。你可以通过传递第二个 maskfile 参数将两个图像载入到同一个光标中。

Cursorfile 和 maskfile 参数可以是带有 readlines 方法的 filenames 或者 filelike 对象。

返回值 cursor_args 可以被直接传递给 pygame.mouse.set_cursor() 方法。

### pygame.cursors.**Cursor**

代表光标的 pygame 对象

Cursor(size, hotspot, xormasks, andmasks) -> Cursor

Cursor(hotspot, surface) -> Cursor

Cursor(constant) -> Cursor

Cursor(Cursor) -> Cursor

Cursor() -> Cursor

- [pygame.cursors.Cursor.copy](https://www.pygame.org/docs/ref/cursors.html#pygame.cursors.Cursor.copy)() — 复制当前光标
- [pygame.cursors.Cursor.type](https://www.pygame.org/docs/ref/cursors.html#pygame.cursors.Cursor.type)() — 获取游标类型
- [pygame.cursors.Cursor.data](https://www.pygame.org/docs/ref/cursors.html#pygame.cursors.Cursor.data)() — 获取游标数据

创建系统游标

从列表中选择一个常量，传入 pygame.cursors.Cursor(constant) 即可。请注意，并非所有系统都支持所有系统游标，您可能会得到一个替代游标。例如，在 MacOS 上，WAIT/WAITARROW 应显示为一个箭头，而 SIZENWSE/SIZENESW/SIZEALL 应显示为一只闭合的手。而在 Wayland 上，每个 SIZE 光标都应显示为一只手。

| Pygame 光标常数                | 描述                          |
| ------------------------------ | ----------------------------- |
| pygame.SYSTEM_CURSOR_ARROW     | 箭头                          |
| pygame.SYSTEM_CURSOR_IBEAM     | 工字钢                        |
| pygame.SYSTEM_CURSOR_WAIT      | 等待                          |
| pygame.SYSTEM_CURSOR_CROSSHAIR | 十字线                        |
| pygame.SYSTEM_CURSOR_WAITARROW | 小等待光标(如果没有，请等待） |
| pygame.SYSTEM_CURSOR_SIZENWSE  | 双箭头指向，西北和东南        |
| pygame.SYSTEM_CURSOR_SIZENESW  | 双箭头指向，东北和西南        |
| pygame.SYSTEM_CURSOR_SIZEWE    | 双箭头，西和东                |
| pygame.SYSTEM_CURSOR_SIZENS    | 双箭头， 南北                 |
| pygame.SYSTEM_CURSOR_SIZEALL   | 四箭头，南北东西              |
| pygame.SYSTEM_CURSOR_NO        | 斜杠                          |
| pygame.SYSTEM_CURSOR_HAND      | 手                            |

**不传递参数创建游标**

除了上述可用的游标常量外，您还可以调用 pygame.cursors.Cursor() 来创建游标（调用 pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW) 与调用 pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW) 相同）。调用其中一个游标实际上是使用默认的本地图像创建一个系统游标。

**创建颜色光标**

要创建颜色光标，请使用热点和曲面创建光标。热点是一个 (x,y) 坐标，用于确定光标中确切点的位置。热点位置必须在曲面的范围内。

**创建位图光标**

当鼠标光标可见时，将使用给定的位掩码数组以黑白位图的形式显示。size 是一个包含光标宽度和高度的序列，hotspot 是一个包含光标热点位置的序列。

光标有宽度和高度，但鼠标位置由一组点坐标表示。因此，传入光标热点变量的值可以帮助 pygame 确定光标的具体位置。

xormasks 是一串字节，包含光标 xor 数据掩码。最后，andmasks 是包含光标位掩码数据的字节序列。要创建这些变量，我们可以使用 pygame.cursors.compile()create binary cursor data from simple strings 函数。

宽度和高度必须是 8 的倍数，掩码数组的大小必须符合给定的宽度和高度。否则会出现异常。

#### **copy**()

复制当前光标

copy() -> Cursor

返回一个新的光标对象，其数据和热点与原始光标对象相同。

#### **type**

获取游标类型

type -> string

类型将是 “系统”、“位图 ”或 “颜色”。

#### **data**

获取游标数据

data -> tuple

返回用于创建游标对象的数据，以元组形式封装。

---

## 示例

```python
# pygame setup
import pygame as pg

pg.init()
screen = pg.display.set_mode([600, 400])
pg.display.set_caption("Example code for the cursors module")

# 创建系统光标
system = pg.cursors.Cursor(pg.SYSTEM_CURSOR_NO)

# 创建位图光标
bitmap_1 = pg.cursors.Cursor(*pg.cursors.arrow)
bitmap_2 = pg.cursors.Cursor(
    (24, 24), (0, 0), *pg.cursors.compile(pg.cursors.thickarrow_strings)
)

# 创建色彩光标
surf = pg.Surface((40, 40)) # you could also load an image 
surf.fill((120, 50, 50))        # and use that as your surface
color = pg.cursors.Cursor((20, 20), surf)

cursors = [system, bitmap_1, bitmap_2, color]
cursor_index = 0

pg.mouse.set_cursor(cursors[cursor_index])

clock = pg.time.Clock()
going = True
while going:
    clock.tick(60)
    screen.fill((0, 75, 30))
    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            going = False

        # if the mouse is clicked it will switch to a new cursor
        if event.type == pg.MOUSEBUTTONDOWN:
            cursor_index += 1
            cursor_index %= len(cursors)
            pg.mouse.set_cursor(cursors[cursor_index])

pg.quit()
```

