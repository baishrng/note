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

