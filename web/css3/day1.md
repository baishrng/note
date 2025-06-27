## CSS 体验

如：

```css
p {
	属性名: 属性值;
}

div {
	属性名: 属性值;
}
```

示例：

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        p {
            color: red;
            font-size: 14px;
        }
    </style>
    <title>Document</title>
</head>

<body>
    <p>则是一行争产大小的字</p>
    <small>这是一啊很难过小子</small>
</body>

</html>
```

---

## CSS 引入位置

### 内部样式表

学习使用

CSS 代码写在 style 标签里面，示例：

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        p {
            color: red;
            font-size: 14px;
        }
    </style>
    <title>Document</title>
</head>

<body>
    <p>则是一行争产大小的字</p>
    <small>这是一啊很难过小子</small>
</body>

</html>
```

### 外部样式表

开发使用

CSS 代码写在单独的 CSS 文件中（.css）

在 HTML 使用 link 标签引入，使用方法：

```html
<link rel="stylesheet" href="./my.css">
```

示例：

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/style.css">
    <title>Document</title>
</head>

<body>
    <p>这是 p 标签</p>
    <div>这是 div 标签</div>
</body>

</html>
```

```css
/* style.css */

p {
    color: red;
}
```

### 行内样式

配合 JavaScript 使用

CSS 写在标签的 style 属性值里

```html
<div style="color: red; font-size:20px;">这是 div 标签</div>
```

----

## CSS 选择器

### 标签选择器

使用标签名作为选择器 → 选中同名标签设置相同的样式

例如：p, h1, div, a, img......

```HTML
<style>
   p {
     color: red;
   }
 </style>
```

注意：标签选择器无法差异化同名标签的显示效果。

### 类选择器

作用：查找标签，差异化设置标签的显示效果。

步骤：

​	1）定义类选择器 → .类名

​	2）使用类选择器 → 标签添加 class="类名“

注意：

- 类名自定义，不要用纯数字或中文，尽量用英文命名
- 一个类选择器可以供多个标签使用
- 一个标签可以使用多个类名，类名之间用空格隔开

开发习惯：类名见名知意，多个单词可以用 - 连接，例如：news-hd

使用方法：

```html
<style>
    /* 定义类选择器 */
    .red {
        color: red;
    }
</style>
<!-- 使用类选择器 -->
<div class="red">这是 div 标签</div>
```

示例：

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .color-red {
            color: red;
        }
        .size {
            font-size: 25px;
        }
    </style>
    <title>Document</title>
</head>

<body>
    <p class="color-red">这是 p 标签</p>
    <p class="red">这也是一个 p 标签</p>
    <!-- 一个标签可以使用多个类名，类名用空格隔开 -->
    <div class="color-red size">this is a div tag.</div>
</body>

</html>
```

### id选择器

作用：查找标签，差异化设置标签的显示效果。

场景：id 选择器一般配合 JavaScript 使用，很少用来设置 CSS 样式

步骤：

​	1）定义 id 选择器 → #id名

​	2）使用 id 选择器 → 标签添加 id= "id名"

规则：

- 同一个 id 选择器在一个页面只能使用一次

使用方法：

```html
<style>
    /* 定义 id 选择器 */
    #red {
        color: red;
    }
</style>
<!-- 使用 id 选择器 -->
<div id="red">这是 div 标签</div>
```

### 通配符选择器

作用：查找页面所有标签，设置相同样式。

通配符选择器： *，不需要调用，浏览器自动查找页面所有标签，设置相同的样式

使用方法：

```html
* {
   color: red;
 }
```

经验：

- 通配符选择器可以用于清除标签的默认样式，例如：标签默认的外边距、内边距，如：

```html
* {
  margin: 0;
  padding: 0;
}
```

示例：

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {
            color: red;
        }
    </style>
    <title>Document</title>
</head>

<body>
    <h1>这是 h1 标签</h1>
    <div>这是一个 div 标签</div>
    <p>这是一个 p 标签</p>
</body>

</html>
```

----

## 画盒子

| 属性名           | 作用   |
| ---------------- | ------ |
| width            | 宽度   |
| height           | 高度   |
| background-color | 背景色 |

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .red {
            width: 100px;
            height: 100px;
            background-color: brown;
        }

        .orange {
            width:200px;
            height: 200px;
            background-color: orange;
        }
    </style>
</head>
<body>
    <span>
    <div class="red">div1</div>
    <div class="orange">div2</div>
    </span>
</body>
</html>
```

---

## 文字控制属性

| 描述         | 属性            |
| ------------ | --------------- |
| 字体大小     | font-size       |
| 字体粗细     | font-weight     |
| 字体倾斜     | font-style      |
| 行高         | line-height     |
| 字体族       | font-family     |
| 字体复合属性 | font            |
| 文本缩进     | text-indent     |
| 文本对齐     | text-align      |
| 修饰线       | text-decoration |

- **字体大小**

属性名：`font-size`

属性值：文字尺寸，PC 端网页最常用的单位 px，如果不加 px 则不会生效

```css
 p {
   font-size: 30px;
 }
```

经验：谷歌浏览器默认字号是16px

- **字体粗细**

属性名：`font-weight`

属性值

```
1、数字（开发使用）
	正常	400
	加粗	700
	
2、关键字
	正常 normal
	加粗 blod
```

```html
/* 不加粗 */
 font-weight: 400;
 /* 加粗 */
 font-weight: 700;
```

示例：

```html
<h1 style="font-weight: 400;">这是标题</h1>
<p style="font-weight: 700;">这是文本</p>
```

- **字体样式（是否倾斜）**

作用：清除文字默认的倾斜效果

属性名：`font-style`

属性值：

​	正常（不倾斜）：normal 

​	倾斜：italic

```html
<em style="font-style: normal;">em 标签，改为不倾斜的</em>
<p style="font-style: italic;">这是倾斜的</p>
```

- **行高**

作用：设置多行文本的间距

属性名：`line-height`

属性值：

​	1）数字 + px

​	2）数字（当前标签font-size属性值的倍数）

```html
line-height: 30px;

 /* 当前标签字体大小为16px */
 line-height: 2;
```

行高的测量方法：从一行文字的最顶端（最底端）量到下一行文字的最顶端（最底端）。

- **行高-垂直居中**

垂直居中技巧：行高属性值等于盒子高度属性值

注意：该技巧适用于单行文字垂直居中效果

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div {
            height: 100px;
            background-color: skyblue;

            line-height: 100px;
        }
    </style>
</head>
<body>
    <div>文字</div>
</body>
</html>
```

