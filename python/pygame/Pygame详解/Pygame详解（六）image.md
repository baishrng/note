---
image模块
---

## **pygame.image**

用于图像传输的 Pygame 模块。

---

## **函数**

- pygame.image.load() — 从文件加载新图片
- pygame.image.save() — 将图像保存到磁盘上
- pygame.image.get_sdl_image_version() — 获取正在使用的 SDL_Image 库的版本号
- pygame.image.get_extended() — 检测是否支持载入扩展的图像格式
- pygame.image.tostring() — 将图像转换为字符串描述
- pygame.image.tobytes — 将图像传输到字节缓冲区
- pygame.image.fromstring() — 将字符串描述转换为图像
- pygame.image.frombytes — 从字节缓冲区创建新的 Surface
- pygame.image.frombuffer() — 创建一个与字符串描述共享数据的 Surface 对象
- pygame.image.load_basic — 从文件（或类似文件的对象）加载新的 BMP 图像
- pygame.image.load_extended — 从文件（或类似文件的对象）加载图像
- pygame.image.save_extended — 将 png/jpg 图像保存到文件（或类似文件的对象）

image 模块包含了加载和保存图像的函数，同时转换为 Surface 对象支持的格式。

注意：没有 Image 类；当一个图像被成功载入后，将转换为 Surface 对象。Surface 对象允许你在上边画线、设置像素、捕获区域等。

Image 是 Pygame 相当依赖的一个模块，支持载入的图像格式如下：

- JPG
- PNG
- GIF（无动画）
- BMP
- PCX
- TGA（无压缩）
- TIF
- LBM（和 PBM）
- PBM（和 PGM，PPM）
- XPM

支持保存为以下格式：

- BMP
- TGA
- PNG
- JPEG

---

## **函数详解**

### **pygame.image.load()**

从文件加载新图片。

load(filename) -> Surface

load(fileobj, namehint="") -> Surface

从文件加载一张图片，你可以传递一个文件路径或一个 Python 的文件对象。

Pygame 将自动判断图像的格式（比如 GIF 或位图）并创建一个新的 Surface 对象。有时它可能需要知道文件的后缀名（比如 GIF 图像应该以 “.gif” 为后缀）。如果你传入原始文件对象，你需要传入它对应的文件名到 namehint 参数中。

返回的 Surface 对象将包含与源文件相同的颜色格式，colorkey 和 alpha 透明度通道。你通常需要调用 Surface.convert() 函数进行转换，这样可以使得在屏幕上绘制的速度更快。

对于含有 alpha 通道的图片（支持部分位置透明，像 PNG 图像），需要使用 Surface.convert_alpha() 函数进行转换。

在某些环境下，Pygame 可能无法支持上述所有的图像格式，但至少无压缩的 BMP 格式是支持的。你可以调用 pygame.image.get_extended() 函数，如果返回 True，说明可以加载上述的格式（包含 PNG，JPG 和 GIF）。

你应该使用 os.path.join() 提高代码的兼容性：

```
asurf = pygame.image.load(os.path.join('data', 'Python.png'))
```

### **pygame.image.save()**

将图像保存到磁盘上。

save(Surface, filename) -> None

save(Surface, fileobj, namehint="") -> None

该函数将保存 Surface 对象到磁盘上，支持存储为 BMP，TGA，PNG 或 JPEG 格式的图像。如果 filename 没有指定后缀名，那么默认是保存为 TGA 格式。TGA 和 BMP 格式是无压缩的文件。

保存为 PNG 和 JPEG 格式是 Pygame 1.8 新增的。

### **pygame.image.get_extended()**

检测是否支持载入扩展的图像格式。

get_extended() -> bool

如果 Pygame 支持上述所有的扩展图像格式，则返回 True。

### **pygame.image.tostring()**

将图像转换为字符串描述。

tostring(Surface, format, flipped=False) -> bytes

将图像转换为一个字符串描述，可以被 Python 的其他图像模块通过 “fromstring” 转换回图像。一些 Python 图像模块喜欢“自下而上”的存储格式（例如 PyOpenGL）。如果 flipped 参数为 True，那么字符串将会垂直翻转以适用这类图像模块。

format 参数可以是下表中任何一个字符串。注意：只有 8 位的 Surface 对象可以使用 “P” 格式。其他格式可以用于任何 Surface 对象上。

| **字符串**   | **含义**                                            |
| :----------- | :-------------------------------------------------- |
| P            | 8 位调色板的 Surface 对象                           |
| RGB          | 24 位图像                                           |
| RGBX         | 32 位图像，不留空白                                 |
| RGBA         | 32 位图像，带 alpha 通道                            |
| ARGB         | 32 位图像，带 alpha 通道，并将 alpha 放在前边       |
| RGBA_PREMULT | 32 位图像，通过 alpha 通道缩放                      |
| ARGB_PREMULT | 32 位图像，通过 alpha 通道缩放，并将 alpha 放在前边 |

### **pygame.image.fromstring()**

将字符串描述转换为图像。

fromstring(bytes, size, format, flipped=False) -> Surface

该函数的使用跟 pygame.image.tostring() 相似。size 参数是一对表示宽度和高度的数字。一旦新的 Surface 对象创建成功，你就可以删除字符串描述。

size 和 format 参数指定的数据需要跟字符串描述相符，否则将抛出异常。

更快地将图片转换到 Pygame，请参考 pygame.image.frombuffer() 函数。

### **pygame.image.frombuffer()**

用于将字节缓冲区转换为图像对象的方法。它允许你从原始数据创建一个 `Surface`，这在处理图像数据时非常有用，比如从外部库或传感器获取图像数据。

frombuffer(buffer, size, format) -> Surface

- **buffer**: 包含图像数据的字节字符串（`bytes`）。这个数据应该是经过适当格式化的像素数据。

- **size**: 一个元组 `(width, height)`，指定图像的宽度和高度。

- format

  : 字符串，指定像素格式。常见的格式包括：

  - `'RGB'`: 表示每个像素由红、绿、蓝三色组成，每种颜色用一个字节表示。
  - `'RGBA'`: 表示每个像素包含红、绿、蓝和透明度四个分量。
  - `'RGBX'`: 表示红、绿、蓝和一个冗余的字节（通常是未用的）。

该函数的使用跟 pygame.image.fromstring() 类似，但没法垂直翻转原始数据。

该函数的速度会比 pygame.image.fromstring() 快很多，因为该函数不需要申请和拷贝任何像素数据。

示例：

```python
import pygame
import numpy as np

# 初始化 Pygame
pygame.init()

# 设置窗口大小
screen = pygame.display.set_mode((800, 600))

# 创建图像数据（示例：生成一个渐变图像）
width, height = 800, 600
size = (width, height)

# 使用 NumPy 创建 RGB 图像数据
data = np.zeros((height, width, 3), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        data[y, x] = [x % 256, y % 256, (x + y) % 256]  # 创建渐变色

# 将 NumPy 数组转换为字节缓冲区
buffer = data.tobytes()

# 从字节缓冲区创建 Surface
image_surface = pygame.image.frombuffer(buffer, size, 'RGB')

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新窗口
    screen.blit(image_surface, (0, 0))  # 绘制图像
    pygame.display.flip()

# 退出 Pygame
pygame.quit()
```

结果：

<img src="../../../img/python/pygame/Snipaste_2024-10-06_16-39-12.jpg" style="zoom:50%;" />

---

## 参考文献

https://www.pygame.org/docs/ref/image.html

https://www.kancloud.cn/lchy0987/pydic/3060858

chatgpt