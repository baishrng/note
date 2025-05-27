## 移动 web 基础

### 谷歌模拟器

模拟移动设备，方便查看页面效果

右键点检查，点击最上面一行的第二个按钮（元素左边那一个）

---

### 屏幕分辨率

- 屏幕分辨率：纵横向上的像素点数，单位是px

硬件分辨率 → 物理分辨率（出厂设置）  

缩放调节的分辨率 → 逻辑分辨率（软件/驱动设置）

分类：

* 物理分辨率：硬件分辨率（出厂设置）
* 逻辑分辨率：软件 / 驱动设置

结论：**制作网页参考 逻辑分辨率** 

---

### 视口

- 手机屏幕尺寸不同，网页宽度均为100%
- **网页的宽度和逻辑分辨率尺寸相同**

视口：**显示HTML网页的区域，用来约束HTML尺寸**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">

  <!– 视口标签 -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>Document</title>
</head>
<body>
  
</body>
</html>
```

* **width=device-width：视口宽度 = 设备宽度**
* initial-scale=1.0：缩放1倍（不缩放）

----

### 二倍图

概念：设计稿里面每个元素的尺寸的**倍数**

作用：防止图片在高分辨率屏幕下模糊失真

- 现阶段设计稿参考iPhone6/7/8，设备宽度375px产出设计稿。
- 二倍图设计稿尺寸：750px。

---

### 适配方案

* 宽度适配：宽度自适应
  * 百分比布局
  * Flex 布局

* 等比适配：宽高等比缩放
  * rem
  * vw

---

## rem

### 简介

* rem单位，是**相对单位**
* rem单位是相对于**HTML标签的字号**计算结果
* **1rem = 1HTML字号大小**

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>rem基本使用</title>
  <style>
    * {
      margin: 0;
      padding: 0;
    }

    /* 1. 给HTML标签加字号 */
    html {
      font-size: 30px;
    }

    /* 2. 使用rem单位书写尺寸 */
    .box {
      width: 5rem;
      height: 3rem;
      background-color: pink;
    }
  </style>
</head>
<body>
  <div class="box"></div>
</body>
</html>
```

----

### 媒体查询

媒体查询能够**检测视口的宽度**，然后编写**差异化的 CSS 样式**

当某个**条件成立，执行对应的CSS样式**

```css
@media（媒体特性）{
  选择器{
    CSS属性
  }
}
```

如：

```css
@media (width:320px) {
  html {
    background-color: green;
  }
}
```

---

### rem 布局

目前rem布局方案中，将网页等分成10份， HTML标签的字号为**视口宽度**的 **1/10**。

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>rem适配</title>
  <style>
    * {
      margin: 0;
      padding: 0;
    }

    /* 1. 使用媒体查询，给不同视口的屏幕设置不同的HTML字号 */
    @media (width:320.39px){
      html {
        font-size: 32.039px;
      }
    }
    @media (width:375.73px){
      html {
        font-size: 37.573px;
      }
    }
    @media (width:414.56px){
      html {
        font-size: 41.456px;
      }
    }

    /* 2. 使用rem单位书写尺寸 */
    .box {
      width: 5rem;
      height: 3rem;
      background-color: pink;
    }
  </style>
</head>
<body>
  <div class="box"></div>
</body>
</html>
```

---

### flexible.js

flexible.js 是手淘开发出的一个用来**适配移动端**的 **js 库**。

核心原理就是根据**不同的视口宽度**给网页中 html 根节点设置**不同**的 **font-size**。

```html
<body>
  ......
  <script src="./js/flexible.js"></script>
</body>
```

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>rem适配</title>
  <style>
    * {
      margin: 0;
      padding: 0;
    }

    /* 1. 使用媒体查询，给不同视口的屏幕设置不同的HTML字号 */
    /* @media (width:320.39px){
      html {
        font-size: 32.039px;
      }
    }
    @media (width:375.73px){
      html {
        font-size: 37.573px;
      }
    }
    @media (width:414.56px){
      html {
        font-size: 41.456px;
      }
    } */

    /* 2. 使用rem单位书写尺寸 */
    .box {
      width: 5rem;
      height: 3rem;
      background-color: pink;
    }
  </style>
</head>
<body>
  <div class="box"></div>

  <script src="./js/flexible.js"></script>
</body>
</html>
```

---

### rem 移动适配

rem单位尺寸

1.  **确定基准根字号**

* 查看**设计稿宽度** → 确定参考**设备宽度**(视口宽度) → 确定**基准根字号**（1/10视口宽度）

2.  rem单位的尺寸

* **rem单位的尺寸 = px单位数值 / 基准根字号**

---

## less

Less是一个**CSS预处理器**, Less文件后缀是**.less**。扩充了 CSS 语言, 使 CSS 具备一定的逻辑性、计算能力

**注意：浏览器不识别 Less 代码，目前阶段，网页要引入对应的 CSS 文件**

VS Code 插件：**Easy LESS**，保存 less文件后**自动**生成对应的 **CSS 文件**

### 注释

* 单行注释
  * 语法：**// 注释内容**
  * 快捷键：**ctrl + /**
* 块注释
  * 语法：**/* 注释内容 */**
  * 快捷键： **Shift + Alt + A**

### 运算

* 加、减、乘直接书写计算表达式
* **除法**需要添加 **小括号** 或 .
* 表达式存在多个单位以第一个单位为准

示例：

.less文件

```less
.box {
    width: 100 + 20px;
    width: 100 - 80px;
    width: 100 * 2px;

    // 除法 / → (计算表达式) 或 ./ → 推荐（）
    width: (68 / 37.5rem);
    width: 29 ./ 37.5rem;

    // 如果表达式有多个单位，最终css里面以第一个单位为准
    height: (29px / 37.5rem);
}
```

.css文件

```css
.box {
  width: 120px;
  width: 20px;
  width: 200px;
  width: 1.81333333rem;
  width: 0.77333333rem;
  height: 0.77333333px;
}
```

### 嵌套

作用：快速生成**后代**选择器

```css
.父级选择器 {
    // 父级样式
   .子级选择器 {
        // 子级样式
    }
}
```

```css
.father {
    color: red;
   .son {
        width: 100px;
    }
}
```

提示：用 & 表示当前选择器，不会生成后代选择器，通常配合伪类或伪元素使用

```css
.father {
    color: red;
    &:hover {
        color: green;
    }
}
```

```css
.father {
    color: red;
}
.father:hover {
    color: green;
}
```

示例：

less文件

```less
.father {
    color: red;
    .son {
        width: 200px;
        a {
            color: green;
            // & 表示的是当前选择器，代码写到谁的大括号里面就表示谁 → 不会生成后代选择器
            // 应用：配合hover伪类或nth-child结构伪类使用
            &:hover {
                color: blue;
            }
        }
    }
}
```

css文件

```css
.father {
  color: red;
}
.father .son {
  width: 200px;
}
.father .son a {
  color: green;
}
.father .son a:hover {
  color: blue;
}
```

### 变量

概念：**容器，存储数据**

作用：存储数据，方便**使用**和**修改**

语法：

* 定义变量：**@变量名: 数据;** 
* 使用变量：**CSS属性：@变量名;**

```less
// 定义变量
@myColor: pink;

// 使用变量
.box {
  color: @myColor;
}

a {
  color: @myColor;
}
```

示例：

less文件

```less
// 1. 定义变量
@myColor: green;

// 2. 使用变量
div {
    color: @myColor;
}

p {
    background-color: @myColor;
}

a {
    color: @myColor;
}
```

css文件

```css
div {
  color: green;
}
p {
  background-color: green;
}
a {
  color: green;
}
```

### 导入

作用：导入 less 公共样式文件

语法：导入: **@import “文件路径”;**

提示：如果是 **less 文件可以省略后缀**

```less
@import './base.less';
@import './common';
```

### 导出

写法：在 less 文件的**第一行**添加 **// out: 存储URL**

提示：文件夹名称后面添加 /

```less
// out: ./index.css
// out: ./css/
```

### 禁止导出

写法：在 less 文件**第一行**添加:  **// out: false** 

---

## 综合案例—极速问诊

### HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>极速问诊</title>
    <link rel="stylesheet" href="./css/index.css">
    <link rel="stylesheet" href="./iconfont/iconfont.css">
</head>
<body>
    <!-- 头部 -->
     <header>
        <a href="#" class="back">
            <span class="iconfont icon-left"></span>
        </a>
        <h3>极速问诊</h3>
        <a href="#" class="note">问诊记录</a>
     </header>

     <!-- banner -->
    <div class="banner">
        <img src="./assets/entry.png" alt="">
        <p><span>20s</span> 快速匹配专业医生</p>
    </div>

    <!-- 问诊类型 -->
    <div class="type">
        <ul>
            <li>
                <a href="#">
                    <div class="pic"><img src="./assets/type01.png" alt=""></div>
                    <div class="txt">
                        <h4>三甲图文问诊</h4>
                        <p>三甲主治及以上级别医生</p>
                    </div>
                    <span class="iconfont icon-right"></span>
                </a>
            </li>
            <li>
                <a href="#">
                    <div class="pic"><img src="./assets/type02.png" alt=""></div>
                    <div class="txt">
                        <h4>普通图文问诊</h4>
                        <p>二甲主治及以上级别医生</p>
                    </div>
                    <span class="iconfont icon-right"></span>
                </a>
            </li>
        </ul>
    </div>

    <script src="./js/flexible.js"></script>
</body>
</html>
```

### LESS

```less
// out: ../css/index.css

@import "./base.less";

// 定义变量
@rootsize: 37.5rem;

// 头部
header {
    display: flex;
    justify-content: space-between;
    height: (44 / @rootsize);
    // background-color: pink;
    padding: 0 (15 / @rootsize);
    line-height: (44 / @rootsize);

    .back .icon-left {
        font-size: (22 / @rootsize);
    }

    h3 {
        font-size: (17 / @rootsize);
    }

    .note {
        font-size: (15 / @rootsize);
        color: #2CB5A5;
    }
}

// banner 
.banner {
    margin-top: (30 / @rootsize);
    margin-bottom: (34 / @rootsize);
    text-align: center;

    img {
        margin-bottom: (18 / @rootsize);
        width: (240 / @rootsize);
        height: (206 / @rootsize);
    }

    p {
        font-size: (16 / @rootsize);
        span {
            color: #16C2A3;
        }
    }
}

// 问诊类型
.type {
    padding: 0 (15 / @rootsize);

    ul li {
        margin-bottom: (15 / @rootsize);
        padding: 0 (15 / @rootsize);
        height: (78 / @rootsize);
        border: 1px solid #EDEDEDE5;
        border-radius: (4 / @rootsize);
        a {
            // 内容在78里面垂直居中 
            height: (78 / @rootsize);
            display: flex;
            align-items: center;
            img {
                width: (40 / @rootsize);
                height: (40 / @rootsize);
                margin-right: (14 / @rootsize);
            }
            .txt {
                flex: 1;
                h4 {
                    font-size: (16/ @rootsize);
                    color: #3C3E42;
                    line-height: (24 / @rootsize);
                }
                p {
                    font-size: (13 / @rootsize);
                    color: #848484;
                    line-height: (20 / @rootsize);
                }
            }
            .icon-right {
                font-size: (16 / @rootsize);
            }
        }
    }
}
```

