## Emmet  写法

Emmet写法：代码的**简写**方式，**输入缩写** VS Code 会**自动生成**对应的代码。

- html：

| 说明         | 标签结构                                     | Emmet           |
| ------------ | -------------------------------------------- | --------------- |
| 类选择器     | `<div class="box"></div>`                    | `标签名.类名`   |
| id 选择器    | `<div id="box"></div>`                       | `标签名 #id 名` |
| 同级标签     | `<div></div><p></p>`                         | `div+p`         |
| 父子级标签   | `<div><p></p></div>`                         | `div>p`         |
| 多个相同标签 | `<span>1</span><span>2</span><span>3</span>` | `span*3`        |
| 有内容的标签 | `<div>内容</div>`                            | `div {内容}`    |

- CSS：大多数简写方式为属性单词的**首字母**

| 说明       | CSS 属性                                           | Emmet           |
| ---------- | -------------------------------------------------- | --------------- |
| 宽度       | width                                              | `w`             |
| 宽度 500px | width: 500px;                                      | `w500`          |
| 背景色     | background-color                                   | `bgc`           |
| 多个属性   | width: 200px;height: 100px;background-color: #fff; | `w200+h100+bgc` |

----

## 背景属性

| 描述           | 属性                  |
| -------------- | --------------------- |
| 背景色         | background-color      |
| 背景图         | background-image      |
| 背景图平铺方式 | background-repeat     |
| 背景图位置     | background-position   |
| 背景图缩放     | background-size       |
| 背景图固定     | background-attachment |
| 背景复合属性   | background            |

### 背景图

网页中，使用背景图实现**装饰性**的图片效果。

属性名：`background-image`（bgi)

属性值：`url`(背景图 URL)

```css
div {
    width: 400px;
    height: 400px;
  	background-image: url(./images/1.png);
}
```

提示：**背景图默认有平铺（复制）效果**。

### 背景图平铺方式

属性名：**`background-repeat`**（bgr）

属性值

| 属性值    | 效果             |
| --------- | ---------------- |
| no-repeat | 不平铺           |
| repeat    | 平铺（默认效果） |
| repeat-x  | 水平方向平铺     |
| repeat-y  | 垂直方向平铺     |

```css
div {
    width: 400px;
    height: 400px;
    background-color: pink;
    background-image: url(./images/1.png);
    background-repeat: no-repeat;
}
```

### 背景图位置

属性名：**`background-position`**（bgp）

属性值：水平方向位置 垂直方向位置

- 关键字

| 关键字 | 位置 |
| ------ | ---- |
| left   | 左侧 |
| right  | 右侧 |
| center | 居中 |
| top    | 顶部 |
| bottom | 底部 |

- 坐标（数字 + px，正负都可以）

水平：正数向右；负数向左

垂直：正数向下；负数向上

提示：

- **关键字**取值方式写法，可以**颠倒**取值顺序
- 可以只写一个关键字，**另一个方向**默认为**居中**；**数字**只写**一**个值表示**水平**方向，垂直方向为**居中**

```css
div {
   width: 400px;
   height: 400px;
   background-color: pink;
   background-image: url(./images/1.png);
   background-repeat: no-repeat;
  
   background-position: center bottom;
   background-position: 50px -100px;
   background-position: 50px center;
 }
```

### 背景图缩放

作用：设置背景图大小

属性名：**`background-size`**（bgz）

常用属性值：

- **关键字**

  **`cover`**：等比例缩放背景图片以完全覆盖背景区，可能背景图片部分看不见

  **`contain`**：等比例缩放背景图片以完全装入背景区，可能背景区部分空白

- **百分比**：根据盒子尺寸计算图片大小（100% 图片的宽度与盒子的宽度一样，图片的高度等比例放大）

- 数字 + 单位（例如：px）

提示：工作中，**图片比例与盒子比例相同**，使用 cover 或 contain 缩放背景图效果相同。

```css
div {
   width: 500px;
   height: 400px;
   background-color: pink;
   background-image: url(./images/1.png);
   background-repeat: no-repeat;
   
   background-size: cover;
   background-size: contain;
 }
```

### 背景图固定

作用：背景不会随着元素的内容滚动。（一般用在背景大图的位置）

属性名：**`background-attachment`**（bga）

属性值：**`fixed`**

```css
 body {
   background-image: url(./images/bg.jpg);
   background-repeat: no-repeat;
   background-attachment: fixed;
 }
```

### 背景复合属性

属性名：**`background`**（bg）

属性值：背景色 背景图 背景图平铺方式 背景图位置/背景图缩放  背景图固定（**空格**隔开各个属性值，**不区分顺序**）

```css
div {
   width: 400px;
   height: 400px;
   background: pink url(./images/1.png) no-repeat right center/cover;
 }
```

---

## 显示模式

显示模式：标签（元素）的显示方式。

作用：布局网页的时候，根据标签的显示模式选择**合适**的标签摆放内容。

- 块级元素（如`div`）
  - **独占**一行
  - 宽度默认是**父**级的**100%**
  - 添加**宽高**属性**生效**
- 行内元素（如`span`）
  - 一行可以显示多个
  - 设置宽高属性不生效
  - 宽高尺寸由内容撑开
- 行内块元素（如`img`）
  - 一行可以显示多个
  - 设置宽高属性生效
  - 宽高尺寸也可以由内容撑开

示例：

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div {
            width: 100px;
            height: 100px;
        }


        .div1 {
            background-color: red;
        }

        .div2 {
            background-color: orange;
        }

        span {
            width: 100px;
            height: 100px;
        }

        .span1 {
            background-color: red;
        }

        .span2 {
            background-color: orange;
        }

        img {
            width: 50px;
            height: 50px;
        }
    </style>
</head>

<body>
    <div class="div1">div 标签1</div>
    <div class="div2">div 标签2</div>

    <span class="span1">span1234567</span>
    <span class="span2">span2</span>

    <img src="./imgs/logo.png" alt="">
    <img src="./imgs/logo.png" alt="">
</body>

</html>
```

---

## 转换显示模式

属性名：**`display`**

属性值：

| 属性值         | 效果   |
| -------------- | ------ |
| block          | 块级   |
| inline - block | 行内块 |
| inline         | 行内   |

工作中常用的使前两个

----

## 综合案例——热词

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>热词</title>
    <style>
        a {
            display: block;
            color: #fff;
            text-align: center;
            text-decoration: none;
            width: 200px;
            height: 80px;
            background-color: #3064bb;
            font-size: 18px;
            text-align: center;
            line-height: 80px;
        }

        a:hover {
            background-color: #608dd9;
        }
    </style>
</head>
<body>
    <a href="#">HTML</a>
    <a href="#">CSS</a>
    <a href="#">JavaScript</a>
    <a href="#">Vue</a>
    <a href="#">React</a>
</body>
</html>
```

----

## 综合案例——banner 效果

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>banner 效果</title>
    <style>
        .banner {
            height: 500px;
            background-image: url(./imgs/bk.png);
            background-repeat: no-repeat;
            background-color: #f3f3f4;
            background-position: left bottom;
            text-align: right;
            color: #333;
        }

        .banner h2{
            font-size: 36px;
            height: 100px;
            line-height: 100px;
            font-weight: 400;
        }

        .banner p {
            font-size: 20px;
        }

        .banner a {
            display: inline-block;
            width: 125px;
            height: 40px;
            background-color: #f06b1f;
            text-align: center;
            line-height: 40px;
            font-size: 20px;
            text-decoration: none;
            color: #fff;
        }
    </style>
</head>

<body>
    <div class="banner">
        <h2>
            让创意产生价值
        </h2>
        <p>
            让每一个创作都可以发光发热！为创作都可以像榜样，让才华横溢的创作者和渴望创意资源的用户
        </p>
        <a href="#">我要报名</a>

    </div>
</body>

</html>
```

---

## 结构伪类选择器

作用：根据元素的**结构关系**查找元素。

| 选择器           | 说明                                      |
| ---------------- | ----------------------------------------- |
| `E:first-child`  | 查找第一个 E 元素                         |
| `E:last-child`   | 查找最后一个 E 元素                       |
| `E:nth-child(N)` | 查找第 N 个 E 元素（第一个元素 N 值为 1） |

```css
li:first-child {
  background-color: green;
}

li:last-child {
  background-color: red;
}

li:nth-child(3) {
  background-color: pink;
}
```

### :nth-child(公式)

作用：根据元素的**结构关系**查找**多个**元素。

| 功能                  | 公式       |
| --------------------- | ---------- |
| 偶数标签              | 2n         |
| 奇数标签              | 2n+1；2n-1 |
| 找到 5 的倍数的标签   | 5n         |
| 找到第 5 个以后的标签 | n+5        |
| 找到第 5 个以前的标签 | -n+5       |

提示：公式中的n取值从 **0** 开始。

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        /* li:nth-child(2n) {
            background-color: red;
        } */

        /* li:nth-child(2n+1) {
            background-color: red;
        } */

        /* li:nth-child(5n) {
            background-color: red;
        } */

        /* li:nth-child(n+5) {
            background-color: red;
        } */

        li:nth-child(-n+5) {
            background-color: red;
        }
    </style>
</head>
<body>
    <ul>
        <li>li 1</li>
        <li>li 2</li>
        <li>li 3</li>
        <li>li 4</li>
        <li>li 5</li>
        <li>li 6</li>
        <li>li 7</li>
        <li>li 8</li>
        <li>li 9</li>
        <li>li 10</li>
    </ul>
</body>
</html>
```

----

## 伪元素选择器

作用：创建**虚拟**元素（伪元素），用来摆放**装饰性**的内容。（创建子级）

| 选择器    | 说明                                      |
| --------- | ----------------------------------------- |
| E::before | 在 E 元素**里面**最**前**面添加一个伪元素 |
| E::after  | 在 E 元素**里面**最**后**面添加一个伪元素 |

注意点：

- **必须**设置 **`content: ""`**属性，用来 设置**伪元素的内容**，如果没有内容，则引号**留空**即可
- 伪元素默认是**行内**显示模式
- **权重**和**标签选择器**相同

```css
div::before {
  content: "before 伪元素";
}
div::after {
  content: "after 伪元素";
}
```

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div {
            width: 300px;
            height: 300px;
            background-color: pink;
        }

        div::before {
            content: "老鼠";
        }

        div::after {
            content: "大米";
        }
    </style>
</head>
<body>
    <!-- 标签内容：老鼠爱大米 -->
    <div>爱</div>
</body>
</html>
```

----

## PxCook

PxCook（**像素大厨**） 是一款切图设计工具**软件**。支持**PSD**文件的文字、颜色、距离**自动智能识别**。

- **开发面板**（自动智能识别）
- 设计面板（手动测量尺寸和颜色）

---

## 盒子模型

### 组成

作用：布局网页，摆放盒子和内容。

盒子模型重要组成部分：

* 内容区域 – `width & height`
* 内边距 – **`padding`**（出现在内容与盒子边缘之间）
* 边框线 – **`border `**
* 外边距 – **`margin`**（出现在盒子外面）

```css
div {
  margin: 50px;	
  border: 5px solid brown;
  padding: 20px;
  width: 200px;
  height: 200px;
  background-color: pink;
}
```

### 边框线——四周

属性名：**border**（bd）

属性值：边框线粗细  线条样式  颜色（**不**区分顺序）

常用线条样式：

| 属性值 | 线条样式 |
| ------ | -------- |
| solid  | 实线     |
| dashed | 虚线     |
| dotted | 点线     |

```css
div {
  border: 5px solid brown;
  width: 200px;
  height: 200px;
  background-color: pink;
}
```

### 边框线——单边

设置单方向边框线

属性名：**`border-方位名词`**（bd+方位名词首字母，例如，bdl）

属性值：边框线粗细  线条样式  颜色（不区分顺序）

```css
div {
  border-top: 2px solid red;
  border-right: 3px dashed green;
  border-bottom: 4px dotted blue;
  border-left: 5px solid orange;
  
  width: 200px;
  height: 200px;
  background-color: pink;
}
```

### 内边距

作用：设置 **内容** 与 **盒子边缘** 之间的距离。

- 属性名：**`padding / padding-方位名词`**

```css
div {
  /* 四个方向 内边距相同 */
  padding: 30px;
  /* 单独设置一个方向内边距 */
  padding-top: 10px;
  padding-right: 20px;
  padding-bottom: 40px;
  padding-left: 80px;
  
  width: 200px;
  height: 200px;
  background-color: pink;
}
```

> 提示：添加 padding 会撑大盒子。

* padding 多值写法

| 取值个数 | 示例                            | 含义                                   |
| -------- | ------------------------------- | -------------------------------------- |
| 一个值   | `padding: 10px;`                | 四个方向内边距均为 10px                |
| 四个值   | `padding: 10px 20px 40px 80px;` | 上: 10px; 右: 20px; 下: 40px; 左: 80px |
| 三个值   | `padding:10px 40px 80px;`       | 上: 10px; 左右: 40px; 下: 80px         |
| 两个值   | `padding:10px 80px;`            | 上下: 10px; 左右: 80px                 |

技巧：从上开始顺时针赋值，当前方向没有数值则与对面取值相同

### 尺寸计算

默认情况：盒子尺寸 = 内容尺寸 + border 尺寸 + 内边距尺寸

结论：给盒子加 border / padding 会撑大盒子

解决：

* **手动做减法**，减掉 border / padding 的尺寸
* 內减模式：**box-sizing: border-box**

示例：

```css
/* 手动做减法 */
div {
  background-color: pink;

  padding: 20px 40px 60px;
  width: 120px;
  height: 120px;
}

/* 內减模式 */
div {
  background-color: pink;

  padding: 20px 40px 60px;
  width: 200px;
  height: 200px;
  box-sizing: border-box;
}
```

### 外边距

作用：拉开两个盒子之间的距离

属性名：**`margin`**

提示：与 padding 属性值写法、含义相同。外边距不会撑大盒子尺寸。

技巧：**版心居中 – 左右 margin 值 为 auto（盒子要有宽度）**

示例：

```css
div {
  background-color: pink;
  width: 1000px;
  height: 200px;

  margin: 50px auto;
}
```

---

## 清除默认样式

清除标签默认的样式，比如：默认的内外边距。

目前有俩种写法：

- 京东写法

```css
* {
    margin: 0;
    padding: 0;
}
```

- 淘宝写法

```css
blockquote, body, button, dd, dl, dt, fieldset, form, 
h1, h2, h3, h4, h5, h6, hr, input, legend, li, ol, p, pre, td, 
textarea, th, ul {
    margin: 0;
    padding: 0;
}
```

示例：

```css
/* 清除默认内外边距 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
/* 清除列表项目符号 */
li {
  list-style: none;
}
```

---

## 元素溢出

作用：控制溢出元素的内容的显示方式。

属性名：**`overflow`**

属性值：

| 属性值     | 效果                                       |
| ---------- | ------------------------------------------ |
| **hidden** | **溢出隐藏**                               |
| scroll     | 溢出滚动（无论是否溢出，都显示滚动条位置） |
| auto       | 溢出滚动（溢出才显示滚动条位置）           |

示例：

```css
div {
  width: 200px;
  height: 200px;
  background-color: pink;

  /* overflow: hidden; */
  /* overflow: scroll; */
  overflow: auto;
}
```

---

## 外边距问题

### 合并现象

场景：**垂直**排列的兄弟元素，上下 **margin** 会**合并**

现象：取两个 margin 中的**较大值生效**

```css
.one {
  margin-bottom: 50px;
}
.two {
  margin-top: 20px;
}
```

### 塌陷问题

场景：**父子级**的标签，**子级**的添加 **上外边距** 会产生**塌陷**问题

现象：**导致父级一起向下移动**

```css
.son {
  margin-top: 50px;
  width: 100px;
  height: 100px;
  background-color: orange;
}
```

解决方法：

* **取消子级margin，父**级设置**padding**（推荐）
* **父**级设置 **overflow: hidden**
* **父**级设置 **border-top**

示例：

```css
.father {
  width: 300px;
  height: 300px;
  background-color: pink;
  /* 方法一 */
  padding-top: 50px;
  box-sizing: border-box; 
  /* 方法二 */
  overflow: hidden;
  /* 方法三 */
  border-top: 0px solid #000;
  box-sizing: border-box;
}

.son {
  width: 100px;
  height: 100px;
  background-color: orange;
  /* 方法二 和 方法三 */
  margin-top: 50px;
}
```

---

## 行内元素 – 内外边距问题

场景：**行内**元素添加 **margin 和 padding**，无法改变元素**垂直**位置

解决方法：给行内元素添加 **line-height** 可以改变垂直位置

```css
span {
  /* margin 和 padding 属性，无法改变垂直位置 */
  margin: 50px;
  padding: 20px;
  /* 行高可以改变垂直位置 */
  line-height: 100px;
}
```

---

## 盒子模型 – 圆角

作用：设置元素的外边框为圆角。

属性名：**`border-radius`**

属性值：**数字+px** / 百分比

提示：属性值是圆角半径

- 多值写法

| 取值个数 | 示例                                | 含义                                           |
| -------- | ----------------------------------- | ---------------------------------------------- |
| 一个值   | border-radius: 10px;                | 四个角均为 10px                                |
| 四个值   | border-radius: 10px 20px 40px 80px; | 左上: 10px; 右上: 20px; 右下: 40px; 左下: 80px |
| 三个值   | border-radius: 10px 40px 80px;      | 左上: 10px; 右上 + 左下: 40px; 右下: 80px      |
| 两个值   | border-radius: 10px 80px;           | 左上 + 右下: 10px; 右上 + 左下: 80px           |

技巧：从左上角开始顺时针赋值，当前角没有数值则与对角取值相同。

示例：

```css
border-radius: 20px;
border-radius: 10px 20px 40px 80px;
border-radius: 10px 40px 80px;
border-radius: 10px 80px;
```

- 正圆形状：给**正方形**盒子设置圆角属性值为 **宽高的一半 / 50%**.（最大值为50%，超过50%没有效果）

```css
img {
  width: 200px;
  height: 200px;
  
  border-radius: 100px;
  border-radius: 50%;
}
```

- 胶囊形状：给**长方形**盒子设置圆角属性值为 盒子高度的一半 

```css
div {
  width: 200px;
  height: 80px;
  background-color: orange;
  border-radius: 40px;
}
```

---

## 盒子模型 – 阴影（拓展）

作用：给元素设置**阴影**效果

属性名：**box-shadow**

属性值：**X 轴偏移量  Y 轴偏移量**  模糊半径  扩散半径  颜色  内外阴影

注意： 

* X 轴偏移量 和 Y 轴偏移量 **必须**书写
* **默认是外阴影**，内阴影需要添加 **inset**

```css
div {
  width: 200px;
  height: 80px;
  background-color: orange;
  box-shadow: 2px 5px 10px 0 rgba(0, 0, 0, 0.5) inset;
}
```

---

## 综合案例——产品卡片

CSS 书写顺序：

1. 盒子模型属性
2. 文字样式
3. 圆角、阴影等修饰属性

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background-color: #f1f1f1;
        }

        .product {
            width: 270px;
            height: 253px;
            background-color: #fff;
            margin: 50px auto;
            padding-top: 40px;
            text-align: center;
            border-radius: 10px;
        }

        img {
            width: 80px;
            height: 80px;
            border-radius: 50%;
        }

        .product h4 {
            margin-top: 20px;
            margin-bottom: 12px;
            font-size: 18px;
            color: #333;
            font-weight: 400;
        }

        .product p {
            font-size: 12px;
            color: #555;
        }
    </style>
</head>
<body>
    <div class="product">
        <img src="./imgs/1.jpg" alt="">
        <h4>抖音直播 SDK</h4>
        <p>包含抖音直播看播功能</p>
    </div>
</body>
</html>
```

---

## 综合案例——新闻列表

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>新闻列表</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            list-style: none;
            text-decoration: none;
        }

        .news {
            margin: 30px auto;
            width: 360px;
            height: 180px;
        }

        .news .head {
            background-color: #eee;
            height: 34px;
            border: 1px solid #dbdee1;
            border-left: 0px solid #fff;
        }

        .news .head a {
            margin-top: -1px;
            display: block;
            background-color: #fff;
            width: 48px;
            height: 34px;
            border-top: 3px solid #ff8400;
            border-right: 1px solid #dbdee1;
            text-align: center;
            line-height: 32px;
            font-size: 14px;
            color: #333;
        }

        .news .body {
            padding: 5px;
        }

        .news .body li {
            background-image: url(./imgs/square.png);
            background-repeat: no-repeat;
            background-position: 0 center;
            padding-left: 15px;
        }

        .news .body li a {
            background: url(./imgs/img.gif) no-repeat 0 center;
            padding-left: 20px;
            font-size: 12px;
            color: #666;
            line-height: 24px;
        }

        .news .body li a:hover {
            color: #ff8400;
        }
    </style>
</head>
<body>
    <div class="news">
        <div class="head"><a href="#">新闻</a></div>
        <div class="body">
            <ul>
                <li><a href="#">点赞 “新农人” 温暖的伸手</a></li>
                <li><a href="#">在希望的田野上...</a></li>
                <li><a href="#">“中国天眼” 又有新发现 已在《自然》杂志发表</a></li>
                <li><a href="#">急！这个领域，缺人！月薪 4 万元还不好招！啥情况？</a></li>
                <li><a href="#">G9 “带货” 背后：亏损面持续扩大，竞争环境激烈</a></li>
                <li><a href="#">多地力推二手房 “带押过户”，有什么好处？</a></li>
            </ul>
        </div>
    </div>
</body>
</html>
```

