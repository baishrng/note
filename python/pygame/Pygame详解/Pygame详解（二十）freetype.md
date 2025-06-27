---
freetype 模块
---

# **pygame.freetype**

增强的 pygame 模块，用于加载和渲染计算机字体。

`pygame.freetype` 模块是 `pygame.font` 模块的替代品，用于加载和渲染字体。它具有原模块的所有功能，此外还增加了许多新特性。同时，它完全不依赖于 SDL_ttf 库，而是直接实现于 FreeType 2 库。请注意，`pygame.freetype` 模块与 `pygame.font` 模块不兼容。如果您需要向后兼容，请使用 `pygame.ftfont` 模块作为 `pygame.font` 模块的替代方案。

`pygame.freetype` 支持所有由 FreeType 支持的字体文件格式，包括 TTF、Type1、CFF、OpenType、SFNT、PCF、FNT、BDF、PFR 和 Type42 字体。所有具有 UTF-32 代码点的字形都可以访问（请参阅 `Font.ucs4`）。

大多数与字体相关的工作都是通过 `Font` 实例完成的。该模块本身仅提供初始化和创建 `Font` 对象的功能。您可以使用 `SysFont()` 函数从系统中加载字体。

对位图字体提供了额外的支持。可以列出可用的位图大小（请参阅 `Font.get_sizes()`）。对于仅位图字体，`Font` 可以为您设置大小（请参阅 `Font.size` 属性）。

目前，未定义的字符编码会被替换为 `.notdef`（未定义）字符。未来版本中，如何处理未定义的编码可能会变得可配置。

Pygame 附带了一个内置的默认字体。您可以通过将 `None` 作为字体名称传递给 `Font` 构造函数来访问它。

`pygame.freetype.Font` 提供了额外的渲染特性，包括从支持的字体文件创建新的 Font 实例、直接渲染到表面（请参阅 `Font.render_to()`）、字符间距调整（请参阅 `Font.kerning`）、垂直布局（请参阅 `Font.vertical`）、渲染文本的旋转（请参阅 `Font.rotation`）和粗体样式（请参阅 `Font.strong`）。一些属性是可配置的，例如粗体样式的强度（请参阅 `Font.strength`）和下划线位置调整（请参阅 `Font.underline_adjustment`）。文本可以通过文本框的右上角或文本基线定位（请参阅 `Font.origin`）。最后，可以单独调整字体的垂直和水平大小（请参阅 `Font.size`）。您可以参考 `pygame.examples.freetype_misc` 示例来查看这些功能的实际应用。

请注意，`pygame` 包在加载时不会自动导入 `freetype`，必须显式导入此模块才能使用。

例如：

```python
import pygame
import pygame.freetype
```



---

# 函数 & 类

| 函数                                                         | 描述                                          |
| ------------------------------------------------------------ | --------------------------------------------- |
| [pygame.freetype.get_error](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.get_error) | 返回最新的 FreeType 错误。                    |
| [pygame.freetype.get_version](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.get_version) | 返回 FreeType 版本。                          |
| [pygame.freetype.init](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.init) | 初始化底层的 FreeType 库。                    |
| [pygame.freetype.quit](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.quit) | 关闭底层的 FreeType 库。                      |
| [pygame.freetype.get_init](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.get_init) | 如果 FreeType 模块当前已初始化，则返回 True。 |
| [pygame.freetype.was_init](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.was_init) | 已弃用：请改用 get_init()。                   |
| [pygame.freetype.get_cache_size](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.get_cache_size) | 返回字形的大小。                              |
| [pygame.freetype.get_default_resolution](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.get_default_resolution) | 返回默认的每英寸像素大小。                    |
| [pygame.freetype.set_default_resolution](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.set_default_resolution) | 设置该模块的默认每英寸像素大小。              |
| [pygame.freetype.SysFont](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.SysFont) | 从系统字体创建一个 Font 对象。                |
| [pygame.freetype.get_default_font](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.get_default_font) | 获取默认字体的文件名。                        |
| [pygame.freetype.Font](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font) | 从支持的字体文件创建一个新的 Font 实例。      |

---

# 函数详解

## pygame.freetype.**get_error**()

返回最新的 FreeType 错误。

get_error() -> str

get_error() -> None

要获取 FreeType2 库中最后发生的错误描述，可以使用 `pygame.freetype.get_error()` 函数。如果没有发生错误，则返回 `None`。该函数提供了对错误状态的检查，以帮助调试和处理字体渲染相关的问题。

## pygame.freetype.**get_version**()

返回 FreeType 版本。

get_version(linked=True) -> (int, int, int)

要获取当前使用的 FreeType 库的版本，可以调用 `pygame.freetype.get_version(linked=True)`。默认情况下，`linked=True` 会返回链接的 FreeType 版本，而如果设置为 `linked=False`，则会返回编译的 FreeType 版本。

请注意，`freetype` 模块依赖于 FreeType 2 库，因此它无法与原始的 FreeType 1.0 编译。元组的第一个元素将始终是 "2"。

在 Pygame 2.2.0 中，添加了 `linked` 关键字参数，并且默认行为已更改为返回链接的版本，而不是编译版本。

## pygame.freetype.**init**()

初始化底层的 FreeType 库。

init(cache_size=64, resolution=72) -> None

在使用 `freetype` 模块的任何功能之前，必须调用该函数来初始化底层的 FreeType 库。虽然 `pygame.init()` 会自动调用此函数（如果 `freetype` 模块已经被导入），但你仍然可以安全地多次调用它。

此外，你可以选择指定一个默认的 *cache_size*，这代表 Glyph 缓存中可以同时缓存的最大字形数量。如果设置的值过小，模块会自动进行性能调优。你还可以提供一个默认的像素 *resolution*（以每英寸点数为单位），用于调整字体缩放。

## pygame.freetype.**quit**()

关闭底层的 FreeType 库。

quit() -> None

该函数用于关闭 `freetype` 模块。在调用此函数后，您不应再调用与 `freetype` 模块相关的任何类、方法或函数，因为它们可能会失败或产生不可预测的结果。无论模块是否已初始化，调用此函数都是安全的。

## pygame.freetype.**get_init**()

如果 FreeType 模块当前已初始化，则返回 True。

get_init() -> bool

如果 `pygame.freetype` 模块当前已初始化，则返回 `True`。

## pygame.freetype.**get_cache_size**()

*返回字形缓存大小*

get_cache_size() -> long

请参见 [`pygame.freetype.init()` 初始化底层 FreeType 库。](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.init)

## pygame.freetype.**get_default_resolution**()

*返回每英寸的默认像素大小*

get_default_resolution() -> long

返回该模块的默认像素大小（以每英寸点数为单位）。默认值为 72 DPI。

## pygame.freetype.**set_default_resolution**()

*设置该模块的默认像素大小（以每英寸点数为单位）*

set_default_resolution([resolution])

设置该模块的默认像素大小（以每英寸点数为单位）。如果省略可选参数或参数为零，则分辨率将重置为 72 DPI。

## pygame.freetype.**SysFont**()

*从系统字体创建一个字体对象*

SysFont(name, size, bold=False, italic=False) -> Font

返回一个从系统字体加载的新字体对象。该字体将匹配请求的 *粗体* 和 *斜体* 标志。Pygame 使用一小部分常见字体别名。如果请求的特定字体不可用，可能会使用一个合理的替代字体。如果找不到合适的系统字体，将回退到加载默认的 pygame 字体。

字体 *名称* 还可以是一个可迭代的字体名称集合、一个以逗号分隔的字符串或一个以逗号分隔的字节串，此时将按顺序搜索这些名称。

*在 pygame 2.0.1 中新增：* 接受字体名称的可迭代对象。

## pygame.freetype.**get_default_font**()

*获取默认字体的文件名*

get_default_font() -> string

返回默认 pygame 字体的文件名。这个文件名不是文件的完整路径。该文件通常与字体模块在同一目录中，但也可以打包在单独的归档文件中。

---

# 类详解

## pygame.freetype.**Font**

*从支持的字体文件创建一个新的 Font 实例。*

Font(file, size=0, font_index=0, resolution=0, ucs4=False) -> Font

Font(pathlib.Path) -> Font

参数文件可以是一个表示字体文件名的字符串、一个包含字体的类文件对象，或者为 None；如果为 None，则使用默认的 Pygame 字体。

可选地，可以指定一个大小参数来设置默认大小，以点为单位，这决定了呈现字符的大小。大小也可以显式传递给每个方法调用。由于缓存系统的工作方式，在构造函数中指定默认大小并不意味着在每次函数调用中手动传递大小会有性能提升。如果字体是位图且未给定大小，则默认大小设置为该字体的第一个可用大小。

如果字体文件包含多个字体，可以通过索引参数选择要加载的字体。对于超出范围的字体索引值，将引发异常。

可选的分辨率参数设置了用于缩放该字体实例字形的像素大小（以每英寸点数为单位）。如果为 0，则使用由 init() 设置的默认模块值。Font 对象的分辨率只能通过重新初始化 Font 实例来更改。

可选的 ucs4 参数是一个整数，设置默认文本翻译模式：0（假）识别 UTF-16 补充对，任何其他值（真）将 Unicode 文本视为 UCS-4，不使用补充对。请参见 Font.ucs4。

---

## 属性 & 方法

| 属性 & 方法                                                  | 描述                               |
| ------------------------------------------------------------ | ---------------------------------- |
| [pygame.freetype.Font.name](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.name) | *正确的字体名称。*                 |
| [pygame.freetype.Font.path](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.path) | 字体文件路径。                     |
| [pygame.freetype.Font.size](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.size) | 用于渲染的默认点大小。             |
| [pygame.freetype.Font.get_rect](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_rect) | 返回渲染文本的大小和偏移量。       |
| [pygame.freetype.Font.get_metrics](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_metrics) | 返回给定文本的字形度量值           |
| [pygame.freetype.Font.height](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.height) | 字体在字体单位中的未缩放高度。     |
| [pygame.freetype.Font.ascender](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.ascender) | 字体在字体单位中的未缩放上升值。   |
| [pygame.freetype.Font.descender](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.descender) | 字体在字体单位中的未缩放下降值。   |
| [pygame.freetype.Font.get_sized_ascender](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_sized_ascender) | 字体在像素中的缩放上升值。         |
| [pygame.freetype.Font.get_sized_descender](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_sized_descender) | 字体在像素中的缩放下降值。         |
| [pygame.freetype.Font.get_sized_height](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_sized_height) | 字体在像素中的缩放高度。           |
| [pygame.freetype.Font.get_sized_glyph_height](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_sized_glyph_height) | 字体在像素中的缩放边界框高度。     |
| [pygame.freetype.Font.get_sizes](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_sizes) | 返回嵌入位图的可用大小。           |
| [pygame.freetype.Font.render](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render) | 返回渲染的文本作为一个表面。       |
| [pygame.freetype.Font.render_to](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_to) | 将文本渲染到现有表面上。           |
| [pygame.freetype.Font.render_raw](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_raw) | 返回渲染的文本作为字节字符串。     |
| [pygame.freetype.Font.render_raw_to](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_raw_to) | 将文本渲染为 int 数组              |
| [pygame.freetype.Font.style](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.style) | 字体样式标志                       |
| [pygame.freetype.Font.underline](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.underline) | 字体下划线样式标志的状态           |
| [pygame.freetype.Font.strong](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.strong) | 字体粗体样式标志的状态             |
| [pygame.freetype.Font.oblique](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.oblique) | 字体斜体样式标志的状态             |
| [pygame.freetype.Font.wide](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.wide) | 字体宽体样式标志的状态             |
| [pygame.freetype.Font.strength](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.strength) | 与粗体或宽体字体样式相关的强度     |
| [pygame.freetype.Font.underline_adjustment](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.underline_adjustment) | 下划线位置调整系数                 |
| [pygame.freetype.Font.fixed_width](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.fixed_width) | 获取字体是否为固定宽度             |
| [pygame.freetype.Font.fixed_sizes](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.fixed_sizes) | 字体可用位图大小的数量             |
| [pygame.freetype.Font.scalable](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.scalable) | 获取字体是否可缩放                 |
| [pygame.freetype.Font.use_bitmap_strikes](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.use_bitmap_strikes) | 允许在大纲字体文件中使用嵌入式位图 |
| [pygame.freetype.Font.antialiased](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.antialiased) | 字体抗锯齿模式                     |
| [pygame.freetype.Font.kerning](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.kerning) | 字符分隔模式                       |
| [pygame.freetype.Font.vertical](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.vertical) | 字体垂直模式                       |
| [pygame.freetype.Font.rotation](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.rotation) | 文本逆时针旋转的角度（度）         |
| [pygame.freetype.Font.fgcolor](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.fgcolor) | 默认前景颜色                       |
| [pygame.freetype.Font.bgcolor](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.bgcolor) | 默认背景颜色                       |
| [pygame.freetype.Font.origin](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.origin) | 字体呈现为文本原点模式             |
| [pygame.freetype.Font.pad](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.pad) | 填充边界模式                       |
| [pygame.freetype.Font.ucs4](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.ucs4) | 启用 UCS-4 模式                    |
| [pygame.freetype.Font.resolution](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.resolution) | 每英寸像素分辨率（DPI）            |

---

## 属性详解

### **name**

*正确的字体名称.*

name -> string

只读。返回字体文件中记录的真实（长）字体名称。

### **path**

*字体文件路径*

path -> unicode

只读。返回已加载字体文件的路径。

### **size**

*渲染时使用的默认点尺寸*。

size -> float

size -> (float, float)

获取或设置用于文本度量和渲染的默认大小。它可以是一个以 Python `int` 或 `float` 表示的单一点大小，或一个字体的 ppem（宽度，高度）`元组`。大小值必须为非负值。零大小或宽度表示未定义的大小。在这种情况下，必须将大小作为方法参数提供，否则将引发异常。零宽度但非零高度将引发 ValueError。

对于可缩放字体，单个数值等同于宽度等于高度的元组。可以通过将高度设置大于宽度来垂直拉伸字体，或通过将宽度设置大于高度来水平拉伸字体。对于嵌入位图，请使用[`get_sizes()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_sizes)列出的名义宽度和高度来选择可用的大小。

对于不可缩放的位图字体，字体大小在方法调用时必须与[`get_sizes()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_sizes)返回的可用大小之一匹配。如果不匹配，将引发异常。如果大小是单个数值，则首先将其与点大小值匹配。如果没有匹配，则选择具有相同名义宽度和高度的可用大小。

### **height**

字体在字体单位中的未缩放高度。

height -> int

只读属性。获取字体的高度。这是字体中所有字形的平均值。

### **ascender**

字体在字体单位中的未缩放上升度。

ascender -> int

只读属性。返回从字体基线到边界框顶部的单位数。

### **descender**

字体在字体单位中的未缩放降度。

descender -> int

只读属性。返回字体降度的单位高度。降度是从字体基线到边界框底部的单位数。

### **style**

字体的样式标志

style -> int

获取或设置字体的默认样式。该默认样式将用于所有文本渲染和大小计算，除非在具体的渲染或 [`get_rect()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_rect) 调用中被覆盖。样式值可以是以下常量之一或多个的按位或：

```
STYLE_NORMAL
STYLE_UNDERLINE
STYLE_OBLIQUE
STYLE_STRONG
STYLE_WIDE
STYLE_DEFAULT
```

这些常量可以在 FreeType 常量模块中找到。可选地，默认样式可以通过访问各个样式属性（下划线、斜体、粗体）来修改或获取。

`STYLE_OBLIQUE` 和 `STYLE_STRONG` 风格仅适用于可缩放字体。如果尝试为位图字体设置这两种样式之一，将引发 `AttributeError`。对于由 `Font.__new__()` 返回的非活动字体，如果尝试设置这两种样式之一，将引发 `RuntimeError`。

将 `STYLE_DEFAULT` 赋值给 [`style`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.style) 属性不会改变属性，因为该属性定义了默认值。[`style`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.style) 属性将永远不会返回 `STYLE_DEFAULT`。

### **underline**

字体下划线样式标志的状态。

underline -> bool

获取或设置在绘制文本时字体是否带下划线。该默认样式值将用于所有文本渲染和大小计算，除非在具体的渲染或 [`get_rect()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_rect) 调用中通过 'style' 参数进行覆盖。

### **strong**

字体粗体样式标志的状态。

strong -> bool

获取或设置在绘制文本时字体是否为粗体。该默认样式值将用于所有文本渲染和大小计算，除非在具体的渲染或 [`get_rect()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_rect) 调用中通过 'style' 参数进行覆盖。

### **oblique**

字体斜体样式标志的状态。

oblique -> bool

获取或设置字体是否以斜体渲染。该默认样式值将用于所有文本渲染和大小计算，除非在具体的渲染或 [`get_rect()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_rect) 调用中通过 *style* 参数进行覆盖。

斜体样式仅支持可缩放（轮廓）字体。尝试在位图字体上设置此样式将引发 AttributeError。如果字体对象处于非活动状态（由 `Font.__new__()` 返回），则设置此属性将引发 RuntimeError。

### **wide**

字体宽度样式标志的状态

wide -> bool

获取或设置在绘制文本时字体是否会水平拉伸。它产生的效果类似于 [`pygame.font.Font` 创建的新字体对象](https://www.pygame.org/docs/ref/font.html#pygame.font.Font) 的粗体样式。此样式在旋转文本时不可用。

### **strength**

与粗体或宽体字体样式相关的强度。

strength -> float

字体字形在粗体或宽体转换中放大的大小，以未转换大小的分数表示。对于宽体样式，仅增加水平维度；而对于粗体文本，水平和垂直维度均被放大。宽体强度为 0.08333（1/12）时，相当于 [`pygame.font.Font` 创建新字体对象](https://www.pygame.org/docs/ref/font.html#pygame.font.Font) 的粗体样式。默认值为 0.02778（1/36）。

强度样式仅支持可缩放（轮廓）字体。在位图字体上尝试设置此属性将引发 AttributeError。如果字体对象处于非活动状态（通过 `Font.__new__()` 返回），则对该属性的赋值将引发 RuntimeError。

### **underline_adjustment**

下划线位置的调整因子

underline_adjustment -> float

获取或设置一个因子，当其为正值时，会与字体的下划线偏移量相乘，以调整下划线位置。负值则将下划线转变为删除线或上划线。该因子与字形的升部相乘。接受的值范围在 -2.0 到 2.0 之间（包括 -2.0 和 2.0）。值为 0.5 时，与 Tango 的下划线效果非常相近；值为 1.0 时则模仿 [`pygame.font.Font` 创建新字体对象](https://www.pygame.org/docs/ref/font.html#pygame.font.Font) 的下划线效果。

### **fixed_width**

获取字体是否为等宽字体。

fixed_width -> bool

只读属性。返回 `True` 如果字体包含等宽字符（例如 Courier、Bitstream Vera Sans Mono、Andale Mono）。

### **fixed_sizes**

字体可用的位图大小数量。

fixed_sizes -> int

只读属性。返回字体包含位图字符图像的点大小数量。如果为零，则该字体不是位图字体。可缩放字体可能包含作为样式的预渲染点大小。

### **scalable**

获取字体是否为可缩放字体。

scalable -> bool

只读属性。返回 `True` 如果字体包含轮廓字形。如果是这样，点大小不受可用位图大小的限制。

### **use_bitmap_strikes**

允许在轮廓字体文件中使用嵌入的位图。

use_bitmap_strikes -> bool

某些可缩放字体包含特定点大小的嵌入位图。此属性控制是否使用这些位图样式。将其设置为 `False` 可禁用任何位图样式的加载。将其设置为 `True`（默认值）则允许在没有其他样式（仅有 [`wide`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.wide) 或 [`underline`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.underline)）的情况下进行非旋转渲染。对于位图字体，此属性将被忽略。

另请参见 [`fixed_sizes`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.fixed_sizes) 和 [`get_sizes()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_sizes)。

### **antialiased**

字体抗锯齿模式。

antialiased -> bool

获取或设置字体的抗锯齿模式。所有字体的默认值为 `True`，这意味着使用全 8 位混合进行渲染。

将其设置为 `False` 可进行单色渲染。这应该会带来小幅速度提升，并减少缓存内存大小。

### **kerning**

字符字间距模式。

kerning -> bool

获取或设置字体的字间距模式。所有字体的默认值为 `False`，这意味着在渲染时不使用字间距调整。

将其设置为 `True`，在定位字形时，如果字体支持，将在字符对之间添加字间距调整。

### **vertical**

字体垂直模式。

vertical -> bool

获取或设置字符是否垂直排列，而不是水平排列。这在渲染汉字或其他一些垂直书写的文字时可能会很有用。

将其设置为 `True` 可切换到垂直文本布局。默认值为 `False`，即水平排列。

请注意，[`Font`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font) 类不会自动确定脚本方向。必须明确选择垂直布局。

另外，需要注意的是，某些字体格式（尤其是基于位图的格式）可能不包含绘制垂直字形所需的度量信息，因此在这些情况下进行绘制可能会导致未定义的结果。

### **rotation**

文本逆时针旋转角度。

rotation -> int

获取或设置渲染文本的基线角度。角度以整数度数表示。默认角度为 0，水平文本沿 X 轴渲染，垂直文本沿 Y 轴渲染。正值将这些轴逆时针旋转相应的度数，负值则对应顺时针旋转。旋转值会被归一化到 0 到 359 的范围内（例如，390 -> 390 - 360 -> 30，-45 -> 360 + -45 -> 315，720 -> 720 - (2 * 360) -> 0）。

只有可缩放的（轮廓）字体可以旋转。尝试更改位图字体的旋转会引发 AttributeError。尝试更改由 `Font.__new__()` 返回的非活动字体实例的旋转也会引发错误。

### **fgcolor**

默认前景色。

fgcolor -> Color

获取或设置默认的字形渲染颜色。初始值为不透明黑色 (0, 0, 0, 255)。该设置适用于 [`render()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render) 和 [`render_to()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_to)。

### **bgcolor**

默认背景色。

bgcolor -> Color

获取或设置默认的背景渲染颜色。初始值未设置，因此文本默认以透明背景渲染。该设置适用于 [`render()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render) 和 [`render_to()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_to)。

### **origin**

字体渲染到文本原点模式。

origin -> bool

如果设置为 `True`，则 [`render_to()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_to) 和 [`render_raw_to()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_raw_to) 将把 *dest* 位置视为文本原点，而不是边界框的左上角。有关详细信息，请参见 [`get_rect()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_rect)。

### **pad**

填充边界模式。

pad -> bool

如果设置为 `True`，则文本边界矩形将被扩展，以匹配 [`font.Font`](https://www.pygame.org/docs/ref/font.html#pygame.font.Font) 的大小。否则，边界矩形仅足够大以容纳文本。

### **ucs4**

启用 UCS-4 模式。

ucs4 -> bool

获取或设置 Unicode 文本的解码方式。默认情况下，freetype 模块对 Unicode 文本执行 UTF-16 代理对解码。这允许在使用 UCS-2 Unicode 类型构建的 Python 解释器（例如 Windows）中，介于 0x10000 和 0x10FFFF 之间的 32 位转义序列（'Uxxxxxxxx'）表示其对应的 UTF-32 代码点。这也意味着 UTF-16 代理区域内的字符值（0xD800 到 0xDFFF）被视为代理对的一部分。格式不正确的代理对将引发 UnicodeEncodeError。将 ucs4 设置为 `True` 将关闭代理对解码，允许访问具有四字节 Unicode 字符支持的 Python 解释器的完整 UCS-4 字符范围。

### **resolution**

每英寸像素分辨率（DPI）。

resolution -> int

只读。获取此 [`Font`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font) 实例中用于缩放字体字形的像素大小。

---

## 方法详解

### **get_rect**()

返回渲染文本的大小和偏移量。

get_rect(text, style=STYLE_DEFAULT, rotation=0, size=0) -> rect

获取文本的最终尺寸和原点（以像素为单位），可选的 *size* 以磅为单位，*style* 和 *rotation*。对于其他相关的渲染属性，以及未提供的任何可选参数，将使用 [`Font`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font) 实例设置的默认值。

返回一个 [`Rect`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect) 实例，包含文本边界框的宽度和高度以及文本原点的位置。原点在对单独渲染的文本片段进行对齐时非常有用。它提供文本开始时的基线位置和偏移。有关示例，请参见 [`render_to()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_to) 方法。

如果 *text* 是字符（字节）字符串，则假定其编码为 `LATIN1`。

可选地，*text* 可以为 `None`，这将返回先前调用的 [`get_rect()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_rect)、[`render()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render)、[`render_to()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_to)、[`render_raw()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_raw) 或 [`render_raw_to()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_raw_to) 的文本边界矩形。有关更多详细信息，请参见 [`render_to()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_to)。

### **get_metrics**()

返回给定文本的字形度量。

get_metrics(text, size=0) -> [(...), ...]

返回 *text* 中每个字符的字形度量。

字形度量以元组列表的形式返回。每个元组提供单个字符字形的度量。字形度量包括：

```
(min_x, max_x, min_y, max_y, horizontal_advance_x, horizontal_advance_y)
```

边界框的 min_x、max_x、min_y 和 max_y 值以整数类型的网格拟合像素坐标返回。推进值为浮点数。

计算使用字体的默认点大小进行。如果需要，您可以通过 *size* 参数指定其他点大小。

度量值会根据当前的旋转、加粗和斜体设置进行调整。

如果 text 是字符（字节）字符串，则假定其编码为 `LATIN1`。

### **get_sized_ascender**()

字体在像素中的缩放上升度。

get_sized_ascender(<size>=0) -> int

返回从字体基线到边界框顶部的单位数。该值未经过加粗或旋转调整。

### **get_sized_descender**()

字体在像素中的缩放降度。

get_sized_descender(<size>=0) -> int

返回从字体基线到边界框顶部的像素数。该值未经过加粗或旋转调整。

### **get_sized_height**()

字体在像素中的缩放高度。

get_sized_height(<size>=0) -> int

返回字体的高度。这是字体中所有字形的平均值。该值未经过加粗或旋转调整。

### **get_sized_glyph_height**()

字体在像素中的缩放边界框高度。

get_sized_glyph_height(<size>=0) -> int

返回字体中字形的边界框高度（以像素为单位）。这是所有字形的平均值，未经过加粗或旋转调整。

### **get_sizes**()

返回嵌入位图的可用尺寸。

get_sizes() -> [(int, int, int, float, float), ...]

get_sizes() -> []

返回一个包含元组记录的列表，每个元组代表一个支持的点大小。每个元组包含以下信息：点大小、以像素为单位的高度、以像素为单位的宽度、以分数像素表示的水平ppem（名义宽度）以及以分数像素表示的垂直ppem（名义高度）。

### **render**()

返回渲染文本为一个表面。

render(text, fgcolor=None, bgcolor=None, style=STYLE_DEFAULT, rotation=0, size=0) -> (Surface, Rect)

返回一个新的 [`Surface`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface)，在其上以 `fgcolor` 指定的颜色渲染文本。如果没有给定前景色，则使用默认的前景色 [`fgcolor`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.fgcolor)。如果给定了 `bgcolor`，则该表面将填充此颜色。当未给定背景颜色时，表面背景为透明， alpha 值为零。通常返回的表面具有 32 位像素大小。然而，如果 `bgcolor` 为 `None` 且抗锯齿禁用，将返回一个单色 8 位颜色键表面，并将颜色键设置为背景颜色。

返回值是一个元组：新表面和一个边界矩形，给出渲染文本的大小和起始位置。

如果传入空字符串，则返回的矩形宽度为零，高度为字体的高度。

可选的 *fgcolor*、*style*、*rotation* 和 *size* 参数覆盖 [`Font`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font) 实例设置的默认值。

如果 *text* 是字符（字节）字符串，则假定其编码为 `LATIN1`。

可选地，*text* 可以为 `None`，这将渲染先前调用的 [`get_rect()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_rect)、[`render()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render)、[`render_to()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_to)、[`render_raw()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_raw) 或 [`render_raw_to()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_raw_to) 中传递的文本。有关详细信息，请参见 [`render_to()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_to)。

### **render_to**()

在现有表面上渲染文本。

render_to(surf, dest, text, fgcolor=None, bgcolor=None, style=STYLE_DEFAULT, rotation=0, size=0) -> Rect

将字符串 *text* 渲染到 [`pygame.Surface`](https://www.pygame.org/docs/ref/surface.html#pygame.Surface) 对象 *surf* 上，位置为 *dest*，这是一个 (x, y) 表示表面坐标的元组。如果 x 或 y 不是整数，则会尽可能转换为整数。任何以 x 和 y 位置元素为前两项的序列都是可以接受的，包括一个 [`Rect`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect) 实例。与 [`render()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render) 一样，可选的 *fgcolor*、*style*、*rotation* 和 *size* 参数可用。

如果提供了背景颜色 *bgcolor*，则首先用该颜色填充文本边界框。然后进行文本的渲染。背景填充和文本渲染都涉及完整的 alpha 渲染。也就是说，前景、背景和目标表面的 alpha 值都会影响渲染。

返回值是一个矩形，给出渲染文本在表面内的大小和位置。

如果传入空字符串作为文本，则返回的 [`Rect`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect) 的宽度为零，高度为字体的高度。该矩形将测试为 False。

可选地，*text* 可以设置为 `None`，这将重新渲染之前传递给 [`render_to()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_to)、[`get_rect()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_rect)、[`render()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render)、[`render_raw()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_raw) 或 [`render_raw_to()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_raw_to) 的文本。主要是这个功能有助于将 [`render_to()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_to) 与 [`get_rect()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_rect) 结合使用。一个示例：

```python
def word_wrap(surf, text, font, color=(0, 0, 0)):
    font.origin = True
    words = text.split(' ')
    width, height = surf.get_size()
    line_spacing = font.get_sized_height() + 2
    x, y = 0, line_spacing
    space = font.get_rect(' ')
    for word in words:
        bounds = font.get_rect(word)
        if x + bounds.width + bounds.x >= width:
            x, y = 0, y + line_spacing
        if x + bounds.width + bounds.x >= width:
            raise ValueError("word too wide for the surface")
        if y + bounds.height - bounds.y >= height:
            raise ValueError("text to long for the surface")
        font.render_to(surf, (x, y), None, color)
        x += bounds.width + space.width
    return x, y
```

当调用 [`render_to()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_to) 并且使用与 [`get_rect()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_rect) 相同的字体属性 ― [`size`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.size)、[`style`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.style)、[`strength`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.strength)、[`wide`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.wide)、[`antialiased`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.antialiased)、[`vertical`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.vertical)、[`rotation`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.rotation)、[`kerning`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.kerning) 和 [`use_bitmap_strikes`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.use_bitmap_strikes)，则 [`render_to()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_to) 将使用 [`get_rect()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_rect) 计算的布局。否则，如果在调用 [`get_rect()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.get_rect) 之后传入了一个文本字符串或上述任一属性发生了变化，`render_to()` 将重新计算布局。

如果 *text* 是一个字符（字节）字符串，则其编码被假定为 `LATIN1`。

### **render_raw**()

将渲染的文本返回为字节字符串。

render_raw(text, style=STYLE_DEFAULT, rotation=0, size=0, invert=False) -> (bytes, (int, int))

类似于 [`render()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render)，但返回的像素作为 8 位灰度值的字节字符串。前景颜色为 255，背景颜色为 0，这对于前景图案的 alpha 蒙版非常有用。

### **render_raw_to**()

将文本渲染为整数数组。

render_raw_to(array, text, dest=None, style=STYLE_DEFAULT, rotation=0, size=0, invert=False) -> Rect

渲染到一个暴露数组结构接口的数组对象。该数组必须是二维的，包含整数项。默认的 *dest* 值为 `None`，相当于位置 (0, 0)。请参见 [`render_to()`](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.render_to)。与其他渲染方法一样，*text* 可以为 `None`，以渲染之前传递给另一个方法的文本字符串。

返回值是一个 [`pygame.Rect()` pygame 对象，用于存储矩形坐标](https://www.pygame.org/docs/ref/rect.html#pygame.Rect)，给出渲染文本的大小和位置。

---

# 示例

```python
import pygame
import pygame.freetype

# 初始化 Pygame
pygame.init()

# 设置窗口
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame FreeType Example")

# 创建字体对象
font = pygame.freetype.Font(None, size=24)

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充背景
    screen.fill((0, 0, 0))

    # 渲染文本
    font.render_to(screen, (100, 100), "Hello, World!", (255, 255, 255))

    # 更新屏幕
    pygame.display.flip()

# 退出 Pygame
pygame.quit()
```



---

# 参考文献

https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font.size