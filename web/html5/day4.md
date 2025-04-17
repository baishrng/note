## 字体族

属性名：`font-family`

属性值：字体名

使用方法：

```css
font-family: 楷体;
```

```css
font-family: Microsoft YaHei, Heiti SC, tahoma, arial, Hiragino Sans GB, "\5B8B\4F53", sans-serif;
```

拓展（了解）：`font-family`属性值可以书写多个字体名，各个字体名用**逗号**隔开，执行顺序是**从左向右**依次查找（可以从其他网站复制）

` font-family` 属性**最后**设置一个**字体族名**，网页开发建议使用**无衬线字体**

---

## font 属性

font 复合属性

```css
div {
    /* 文字倾斜 */
    font-style: italic;
    /* 文字加粗 */
    font-weight: 700;
    /* 字体大小是30px */
    font-size: 30px;
    /* 行高为字号的2倍 */
    line-height: 2;
    /* 字体是楷体 */
    font-family: 楷体;
}
```

```css
div {
    /* font: 是否倾斜 是否加粗 字号/行高 字体; */
    font: italic 700 30px/2 楷体;
}
```

第二段代码的效果与第一段代码相同

**使用场景：设置网页文字公共样式**，例如：

```css
body {
    font: 12px/1.5 Microsoft YaHei,Heiti SC,tahoma,arial,Hiragano Sans GB,"\5B8B\4F53",sans-serif;
    color: #666;
}
```

复合属性：属性的**简写**方式，**一个属性**对应**多个值**的写法，各个属性值之间用**空格**隔开。

font: 是否倾斜  是否加粗  **字号/行高 字体（必须按顺序书写）**

```css
div {
    /* font: 是否倾斜 是否加粗 字号/行高 字体; */
    font: italic 700 30px/2 楷体;
}
```

注意：**字号和字体值必须书写**，否则 font 属性不生效（可以直接复制其他网站的）

---

## 文本缩进

属性名：`text-indent`

属性值：

​	1）数字 + px

​	2）**数字 + em**（推荐：1em = 当前标签的字号大小）

```css
p {
  text-indent: 2em;
}
```

---

## 文本对齐

作用：控制内容水平对齐方式

属性名：`text-align`

属性值

| 属性值     | 效果           |
| ---------- | -------------- |
| left       | 左对齐（默认） |
| **center** | 居中对齐       |
| right      | 右对齐         |

```css
text-align: center;
```

---

## 图片对齐

属性名：`text-align`

属性值

| 属性值     | 效果           |
| ---------- | -------------- |
| left       | 左对齐（默认） |
| **center** | 居中对齐       |
| right      | 右对齐         |

```css
text-align: center;
```

`text-align`本质是控制内容的对齐方式，属性要设置给内容的父级。

```html
<style>
    div {
        text-align: center;
    }
</style>
<div>
    <img src="./images/1.jpg" alt="">
</div>
```

---

## 文本修饰线

属性名： `text-decoration`

属性值

| 属性值        | 效果   |
| ------------- | ------ |
| **none**      | 无     |
| **underline** | 下划线 |
| line-through  | 删除线 |
| overline      | 上划线 |

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
       a {
        text-decoration: none;
       }
       div {
        text-decoration: underline;
       }
       p {
        text-decoration: line-through;
       }
       span {
        text-decoration: overline;
       }
    </style>
</head>
<body>
    <a href="#">a 标签</a>
    <div>下划线</div>
    <p>删除线</p>
    <span>上划线</span>
</body>
</html>
```

---

## color 文字颜色

属性名：`color`

属性值

| 颜色表示方式   | 属性值           | 说明                                                  | 使用场景                 |
| -------------- | ---------------- | ----------------------------------------------------- | ------------------------ |
| 颜色关键字     | 颜色英文单词     | red、green、blue...                                   | 学习测试                 |
| rgb 表示法     | rgb(r, g, b)     | r,g,b 表示红绿蓝三原色，取值：0 - 255                 | 了解                     |
| rgba 表示法    | rgba(r, g, b, a) | a 表示透明度，取值：0 - 1（0表示全透明，1表示不透明） | 开发使用，实现透明色     |
| 十六进制表示法 | #RRGGBB          | #000000, #ffcc00，简写: #000, #fc0                    | 开发使用（从设计稿复制） |

提示：只要属性值为颜色，都可以使用上述四种颜色表示方式，例如：背景色。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
       h1 {
        background-color: aqua;
        /* color: red; */
        /* color: rgb(0, 255, 0); */
        /* color: rgba(0, 0, 0, 0.3); */
        /* color: #0000ff; */
        color: #00f;
       }
    </style>
</head>
<body>
    <h1>h1 标签</h1>
</body>
</html>
```

---

## 综合案列——新闻详情

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>新闻详情</title>
    <style>
        h1 {
            font-size: 30px;
            color: #333333;
            text-align: center;
            font-weight: 400;
        }

        .meta {
            font-size: 14px;
            color: #999999;
        }

        p {
            font-size: 18px;
            color: #333333;
            text-indent: 2em;
        }

        .img {
            text-align: center;
        }

        img {
            width: 600px;
            height: 400px;
        }
    </style>
</head>

<body>
    <h1>在希望的田野上 | 湖北秋收开镰 各地多举措保增产增收</h1>
    <div class="meta">来源：央视网 | 2022 年 10 月 12 日 12:12:12</div>
    <p><strong>央视网消息：</strong>眼下湖北全省秋收开镰已有一周多的时间。水稻收割已经超过四成，玉米收割七成。湖北省通过大力推广新品种水稻，建高标准农田等一系列措施，为秋粮稳产提供有力支撑。<p>
    <p>中稻占据了湖北全年粮食产量的一半以上。在湖北的主产区荆门市，370 万亩中稻已经收割四成以上。</p>
    <div class="img"><img src="./imgs/钢铁侠.jpg" alt=""></div>
    <p>王化林说的新品种，是湖北省研发的杂交水稻 “华夏香丝”，不仅产量高，还具有抗病、抗倒、抗高温的特性。在荆门漳河镇的一工程农田内，像 “华夏香丝” 这样抗旱节水的品种还有 20
        多个，这些水稻新品将在荆门全面推广，确保来年增产增收。</p>
    <p>此外，湖北还大力推进高标准农田建设。截至今年 6 月，已建成 3980 万亩高标准农田，目前，湖北全省仍有 1800 多万亩中稻正在有序收割中，预计 10 月中旬收割完毕。</p>
</body>

</html>
```

---

## 综合案例——CSS简介

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSS简介</title>
    <style>
        h1 {
            color: #333333;
        }
        p {
            text-indent: 2em;
            font-size: 14px;
            color: #444444;
            line-height: 30px;
        }
        a {
            color: #0069c2;
        }
        li {
            line-height: 30px;
            font-size: 14px;
            color: #444444;
        }
    </style>
</head>

<body>
    <h1>CSS（层叠样式表）</h1>
    <p>层叠样式表（Cascading Style Sheets，缩写为 CSS），是一种 <a href="#">样式表</a> 语言，用来描述 HTML 或 XML（包括如 SVG、MathML、XHTML 之类的 XML 分支语言）文档的呈现。CSS 描述了在屏幕、纸质、音频等其它媒体上的元素应该如何被渲染的问题。</p>
    <p><strong>CSS 是开放网络的核心语言之一</strong>，由 W3C 规范，实现跨浏览器的标准化。CSS 节省了大量的工作。样式可以通过定义保存在外部.css 文件中，同时控制多个网页的布局，这意味着开发者不必经历在所有网页上编辑布局的麻烦。CSS 被分为不同等级：CSS1 现已废弃，CSS2.1 是推荐标准，CSS3 分成多个小模块且正在标准化中。</p>
    <ul>
        <li>CSS 介绍：如果你是 Web 开发的新手，请务必阅读我们的 CSS 基础文章以学习 CSS 的含义和用法。</li>
        <li>CSS 教程：我们的 CSS 学习区包含了丰富的教程，它们覆盖了全部基础知识，能使你在 CSS 之路上从初出茅庐到游刃有余。</li>
        <li>CSS 参考：针对资深 Web 开发者的 <a href="">详细参考手册</a> ，描述了 CSS 的各个属性与概念。</li>
    </ul>
</body>

</html>
```

---

## 复合选择器

定义：由**两个或多个基础选择器**，通过不同的方式组合而成。

作用：**更准确、更高效**的选择目标元素（标签）。

```html
<span>span 标签</span>
<div>
    <span>文字颜色是绿色</span>
</div>
```

### 后代选择器

后代选择器：选中某元素的**后代**元素。（选中所有后代元素，包括儿子元素、孙子元素、重孙子元素等）

选择器写法：**父选择器  子选择器** { CSS 属性}，父子选择器之间用**空格**隔开。

```html
<style>
    div span {
        color: red;
    }
</style>

<span> span 标签</span>
<div>
    <span>这是 div 的儿子 span</span>
</div>
```

### 子代选择器

子代选择器：选中某元素的子代元素（最近的子级）。

选择器写法：**父选择器 > 子选择器** { CSS 属性}，父子选择器之间用 **>** 隔开。

```css
<style>
    div > span {
      color: red;
    }
</style>
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
        div > span {
            color: red;
        }
    </style>
</head>
<body>
    <span>span 1</span>
    <div>
        <span>这是 div 的儿子</span>
        <p>
            <span>这是 div 的孙子</span>
        </p>
    </div>
    
</body>
</html>
```

### 并集选择器

并集选择器：选中**多组**标签设置**相同**的样式。

选择器写法：**选择器1, 选择器2, …, 选择器N** { CSS 属性}，选择器之间用 **,** 隔开。

```html
<style>
    div,
    p,
    span {
        color: red;
    }
</style>
<div> div 标签</div>
<p>p 标签</p>
<span>span 标签</span>
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
        div,
        p,
        span {
            color: red;
        }
    </style>
</head>

<body>
    <h1>h1 标签</h1>
    <div>div 标签</div>
    <p>p 标签</p>
    <span>span 标签</span>
</body>

</html>
```

### 交集选择器

交集选择器：选中**同时**满足**多个条件**的元素。

```html
<p class="box">p 标签，使用了类选择器 box</p>
<p>p 标签</p>
<div class="box">div 标签，使用了类选择器 box</div>
```

选择器写法：**选择器1选择器2** { CSS 属性}，**选择器之间连写**，没有任何符号。

```css
p.box {
 color: red;
}
```

注意：如果交集选择器中有标签选择器，**标签选择器必须书写在最前面**。

---

## 伪类选择器

伪类选择器：伪类表示元素**状态**，选中元素的某个状态设置样式。

### 鼠标悬停状态

鼠标悬停状态：选择器:**hover** { CSS 属性 }

```css
<style>
    a:hover {
        color: red;
    }

    .box:hover {
        color: green;
    }
</style>
<a href="#">a 标签</a>
<div class="box">div 标签</div>
```

任何标签都可以设置 **鼠标悬停状态**

### 伪类-超链接（拓展）

超链接一共有**四**个状态

| 选择器   | 作用           |
| -------- | -------------- |
| :link    | 访问前         |
| :visited | 访问后         |
| :hover   | 鼠标悬停       |
| :active  | 点击时（激活） |

提示：如果要给超链接设置以上四个状态，需要按 **LVHA** 的顺序书写。

示例：

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        a:link {
            color: red;
        }

        a:visited {
            color: green;
        }

        a:hover {
            color: blue;
        }

        a:active {
            color: orange;
        }
    </style>
</head>

<body>
    <a href="#">a 标签，测试伪类</a>
</body>

</html>
```

在工作中，按下面代码的写法：

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
         a {
            color: red;
         }

         a:hover {
            color: green;
         }
    </style>
</head>

<body>
    <a href="#">a 标签，测试伪类</a>
</body>

</html>
```

----

## CSS 特性

CSS特性：化简代码 / 定位问题，并解决问题

- 继承性
- 层叠性
- 优先级

### 继承性

继承性：**子**级默认继承**父**级的**文字控制属性**。

| 描述         | 属性            | 效果                                                         |
| ------------ | --------------- | ------------------------------------------------------------ |
| 字体大小     | font-size       | 文字 & 文字                                                  |
| 字体粗细     | font-weight     | 文字 & 文字                                                  |
| 字体倾斜     | font-style      | 文字 & 文字                                                  |
| 行高         | line-height     | 文字                                                         |
| 字体族       | font-family     | 文字 & 文字                                                  |
| 字体复合属性 | font            | 复合属性                                                     |
| 文本缩进     | text-indent     | 玉兰颇受明清时期文人的欢迎，尤其在明代万历年间，玉兰被大量种植。 |
| 文本对齐     | text-align      | 对齐方式                                                     |
| 修饰线       | text-decoration | 文字 & 文字 & 文字 & 文字                                    |
| 颜色         | color           | 文字 & 文字                                                  |

**注意：如果标签有默认文字样式会继承失败。（例：如果标签默认有字体颜色，但没有其他文字样式，则还是会继承其他的文字样式）**

例如：a 标签的颜色、标题的字体大小。

```css
body {
    font: 12px/1.5 Microsoft YaHei,Heiti SC,tahoma,arial,Hiragano Sans GB,"\5B8B\4F53",sans-serif;
    color: #666;
}
```

### 层叠性

特点：

- 相同的属性会**覆盖**：**后面**的 CSS 属性覆盖**前面**的 CSS 属性
- 不同的属性会**叠加**：不同的 CSS 属性**都生效**

```html
<style>
    div {
        color: red;
        font-weight: 700;
    }

    div {
        color: green;
        font-size: 30px;
    }
</style>
<div>div 标签</div>
```

注意：**选择器类型相同则遵循层叠性**，否则按选择器**优先级**判断。

### 优先级

优先级：也叫权重，当一个标签使用了**多种**选择器时，基于不同种类的选择器的**匹配规则**。

```html
<style>
    div {
        color: red;
    }

    .box {
        color: green;
    }
</style>
<div class="box">div 标签</div>
```

规则：**选择器优先级高的样式生效。**

公式：通配符选择器 < 标签选择器 < 类选择器 < id选择器 < 行内样式 < !important

**（选中标签的范围越大，优先级越低）**

示例：

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        /* !important 提权功能，提高权重/优先级到 最高，慎用 */
        div {
            color: red !important;
        }

        * {
            color: green;
        }

        .box {
            color: blue;
        }

        #test {
            color: orange;
        }
    </style>
</head>

<body>
    <div class="box" id="test" style="color: purple;">div 标签</div>
</body>

</html>
```

叠加计算：如果是**复合选择器**，则需要权重叠加计算。

公式：（每一级之间**不存在进位**）

（**行内**样式,  **id**选择器个数,  **类**选择器个数,  **标签**选择器个数）

规则：

- **从左向右**依次比较选个数，**同一级**个数**多**的优先级**高**，如果个数相同，则向后比较
- `!important` 权重最高
- 继承权重最低

示例-1：

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        /* （行内样式,  id选择器个数,  类选择器个数,  标签选择器个数） */
        /* (0, 0, 2, 1) */
        .c1 .c2 div {
            color: blue;
        }

        /* (0, 1, 0, 1) */
        div #box3 {
            color: green;
        }

        /* (0, 1, 1, 0) */
        #box1 .c3 {
            color: orange;
        }
    </style>
</head>

<body>
    <div id="box1" class="c1">
        <div id="box2" class="c2">
            <div id="box3" class="c3">
                这行文本是什么颜色？
            </div>
        </div>
    </div>
</body>

</html>
```

```
结果为：orange
```

示例-2：

```html
<style>
  div p {
  color: red;
  }

  .father {
  color: blue;
  }
</style>

<body>
    <div class="father">
        <p class="son">
            文字
        </p>
    </div>
</body>
```

```
结果为：red
```

示例-3：

```html
<style>
    /* （行内样式,  id选择器个数,  类选择器个数,  标签选择器个数） */
    /* (0, 2, 0, 0) */
    #father #son {
        color: blue;
    }

    /* (0, 1, 1, 1) */
    #father p.c2 {
        color: black;
    }

    /* (0, 0, 2, 2) */
    div.c1 p.c2 {
        color: red;
    }

    /* 继承 */
    #father
        {
        color: green !important;
    }

    /* 继承 */
    div#father.c1 {
        color: yellow;
    }
</style>

<body>
    <div id="father" class="c1">
        <p id="son" class="c2">
            文字
        </p>
    </div>
</body>
```

```
结果为：blue
```

