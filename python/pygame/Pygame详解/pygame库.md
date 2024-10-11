## Pygame

| **模块 & 类**   | **描述**                                                     |
| --------------- | ------------------------------------------------------------ |
| *最有用的内容*  |                                                              |
| **Color**       | 用于颜色表示的 pygame 对象                                   |
| **display**     | 控制显示窗口和屏幕的 pygame 模块                             |
| **draw**        | 绘制形状的 pygame 模块                                       |
| **event**       | 与事件和队列交互的 pygame 模块                               |
| **font**        | 用于加载和渲染字体的 pygame 模块                             |
| **image**       | 用于图像传输的 pygame 模块                                   |
| **key**         | 使用键盘的 pygame 模块                                       |
| **locals**      | pygame 常量                                                  |
| **mixer**       | 用于加载和播放声音的 pygame 模块                             |
| **mouse**       | 使用鼠标的 pygame 模块                                       |
| **Rect**        | 用于存储矩形坐标的 pygame 对象                               |
| **Surface**     | 用于表示图像的 pygame 对象                                   |
| **time**        | 监测时间的 pygame 模块                                       |
| **music**       | 控制流媒体音频的 pygame 模块                                 |
| **pygame**      | 顶级的 pygame 软件包                                         |
| *高级内容*      |                                                              |
| **cursors**     | 用于光标资源的 pygame 模块                                   |
| **joystick**    | 用于与手柄、游戏手柄和轨迹球交互的 Pygame 模块。             |
| **mask**        | 用于图像掩码的 pygame 模块。通常用于碰撞检测或透明度管理。用于快速实现完美的碰撞检测，Mask 可以精确到 1 个像素级别的判断。 |
| **sprite**      | 包含基本游戏对象类的 pygame 模块                             |
| **transform**   | 用于对图像进行变换和处理的模块。它提供了多种功能，可以缩放、旋转、翻转和裁剪图像 |
| **BufferProxy** | pygame 对象，通过数组协议导出表面缓冲区。允许你直接访问和修改图像或表面（surface）的像素数据，提供了更高效的方式来进行图像处理。 |
| **freetype**    | 用于加载和渲染计算机字体的增强型 pygame 模块。与传统的 `pygame.font` 模块相比，`pygame.freetype` 提供了更灵活的功能和更好的性能，特别是在处理 TrueType 字体时。 |
| **gfxdraw**     | 绘制形状的 pygame 模块（实验性的）                           |
| **midi**        | 用于与 midi 输入和输出交互的 pygame 模块。                   |
| **PixelArray**  | 用于直接访问 surfaces 像素的 pygame 对象。可以高效地读取和修改图像的每个像素，适用于需要进行像素级处理的应用，例如图像编辑、特效制作等。 |
| **pixelcopy**   | 用于复制像素数据的 pygame 模块。可以快速地将像素从一个表面（Surface）复制到另一个表面，或从图像文件加载像素数据。这对于需要进行图像处理和编辑的程序非常有用。 |
| **sndarray**    | 用于访问声音采样数据的 pygame 模块。用于处理声音数据的 NumPy 数组。这使得音频处理更加灵活和高效，尤其适合需要对音频数据进行直接操作的应用。 |
| **surfarray**   | 使用数组接口访问 surface 像素数据的 pygame 模块。允许你将图像数据转换为 NumPy 数组，以便进行高效的处理和操作。这对于图像处理、特效和游戏开发中的许多其他用途都非常有用。 |
| **math**        | 用于向量类的 pygame 模块。提供了一些用于处理二维和三维数学运算的类和函数 |
| *其他*          |                                                              |
| **camera**      | 用于相机的 pygame 模块                                       |
| **controller**  | SDL2 版本中用于处理游戏手柄和控制器输入的模块。这个模块提供了访问和管理连接的游戏控制器的功能。 |
| **examples**    | 示例程序模块                                                 |
| **fastevent**   | 与事件和队列交互的 pygame 模块                               |
| **scrap**       | 支持剪贴板的 pygame 模块。                                   |
| **tests**       | Pygame 单元测试套件软件包                                    |
| **touch**       | 专门用于处理触摸输入的模块，特别是在支持触摸屏的设备上。它允许开发者访问和管理触摸事件，例如检测触摸位置、手势等。 |
| **version**     | 包含版本信息的小模块                                         |

pygame官方文档：https://www.pygame.org/docs/

---

## pygame-menu

pygame菜单类，需要单独下载这个库