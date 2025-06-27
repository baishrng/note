## 标准流

标准流也叫文档流，指的是标签在页面中**默认的排布规则**，例如：块元素独占一行，行内元素可以一行显示多个。 

---

## 浮动

作用：让块元素水平排列。

属性名：**float**

属性值

* **left**：左对齐
* **right**：右对齐

特点：

* 浮动后的盒子**顶对齐**
* 浮动后的盒子具备**行内块**特点
* 浮动后的盒子**脱标**，**不占用标准流的位置**（所以一个块中的标签要么都浮动，要么都不浮动）

```html
<style>
  /* 特点：顶对齐；具备行内块显示模式特点；浮动的盒子会脱标 */
  .one {
    width: 100px;
    height: 100px;
    background-color: brown;

    float: left;
  }

  .two {
    width: 200px;
    height: 200px;
    background-color: orange;

    /* float: left; */

    float: right;
  }
</style>

<div class="one">one</div>
<div class="two">two</div>
```

> 注意：如果父级的宽度不够，浮动的盒子会掉下来

示例：

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
            list-style: none;
        }

        .product {
            margin: 50px auto;
            width: 1226px;
            height: 628px;
            background-color: pink;
        }

        .product .left {
            float: left;
            width: 234px;
            height: 628px;
            background-color: skyblue;
        }

        .product .right {
            float: right;
            width: 978px;
            height: 628px;
            background-color: brown;
        }

        .right li {
            float: left;
            margin-right: 14px;
            margin-bottom: 14px;
            width: 234px;
            height: 300px;
            background-color: orange;
        }

        .right li:nth-child(4n) {
            margin-right: 0;
        }
    </style>
</head>
<body>
    <div class="product">
        <div class="left"></div>
        <div class="right">
            <ul>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
            </ul>
        </div>
    </div>
</body>
</html>
```

---

## 清除浮动

场景：浮动元素会**脱标**，如果**父级没有高度**，**子级无法撑开父级高度**（可能导致页面布局错乱）

解决方法：**清除浮动**（清除浮动带来的影响）

例如：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .one {
            margin: 10px auto;
            width: 1200px;
            /* height: 300px; */
            background-color: pink;
        }

        .left {
            float: left;
            width: 200px;
            height: 300px;
            background-color: skyblue;
        }

        .right {
            float: right;
            width: 950px;
            height: 300px;
            background-color: orange;
        }

        .two {
            height: 100px;
            background-color: brown;
        }
    </style>
</head>
<body>
    <div class="one">
        <div class="left"></div>
        <div class="right"></div>
    </div>
    <div class="two"></div>
</body>
</html>
```

#### 额外标签法

在**父元素内容的最后**添加一个**块级**元素，设置 CSS 属性 **clear: both** 

```html
<style>
.clearfix {
  clear: both;
}
</style>

<div class="father">
  <div class="left"></div>
  <div class="right"></div>
  <div class="clearfix"></div>
</div>
```

#### 单伪元素法

1. 准备 after 伪元素

```css
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}
```

2. 父级使用 clearfix 类

```html
<div class="father clearfix"></div>
```

#### 双伪元素法（推荐）

1. 准备 after 和 before 伪元素

```css
/* before 解决外边距塌陷问题 */
/* 双伪元素法 */
.clearfix::before,
.clearfix::after {
  content: "";
  display: table;
}

/* after 清除浮动 */
.clearfix::after {
  clear: both;
}
```

2. 父级使用 clearfix 类

```html
<div class="father clearfix"></div>
```

#### overfow法

父元素添加 CSS 属性 overflow: hidden

```css
.father {
  margin: 10px auto;
  width: 1200px;
  /* height: 300px; */
  background-color: pink;

  overflow: hidden;
}
```

---

## 浮动 – 总结

浮动属性 **float**，**left** 表示**左**浮动，**right** 表示**右**浮动

特点

- 浮动后的盒子**顶**对齐
- 浮动后的盒子具备**行内块**特点
- 父级**宽度**不够，浮动的**子级**会**换行**
- 浮动后的盒子**脱标**

清除浮动：子级浮动，**父级没有高度**，子级**无法**撑开**父级高度**，影响布局效果

1. 双伪元素法

拓展：浮动本质作用是实现**图文混排**效果

----

## Flex布局

| 描述                     | 属性            |
| ------------------------ | --------------- |
| 创建 flex 容器           | display: flex   |
| 主轴对齐方式             | justify-content |
| 侧轴对齐方式             | align-items     |
| 某个弹性盒子侧轴对齐方式 | align-self      |
| 修改主轴方向             | flex-direction  |
| 弹性伸缩比               | flex            |
| 弹性盒子换行             | flex-wrap       |
| 行对齐方式               | align-content   |

### 认识

Flex 布局也叫**弹性布局**，是浏览器**提倡的布局模型**，非常适合**结构化**布局，提供了强大的空间分布和对齐能力。

Flex 模型不会产生浮动布局中脱标现象，布局网页更简单、更灵活。

### 组成

设置方式：给**父**元素设置 **display: flex**，**子**元素可以**自动挤压或拉伸**

组成部分：

* 弹性容器
* 弹性盒子
* 主轴：默认在**水平**方向
* 侧轴 / 交叉轴：默认在**垂直**方向

弹性盒子沿着主轴方向排列

### 主轴对齐方式

属性名：**justify-content**

| 属性值            | 效果                                                         |
| ----------------- | ------------------------------------------------------------ |
| flex-start        | 默认值，弹性盒子从**起点**开始依次排列                       |
| flex-end          | 弹性盒子从**终点**开始依次排列                               |
| **center**        | 弹性盒子沿主轴**居中**排列                                   |
| **space-between** | 弹性盒子沿主轴均匀排列，空白间距均分在弹性盒子**之间**（父级剩余的尺寸分配间距） |
| **space-around**  | 弹性盒子沿主轴均匀排列，空白间距均分在弹性盒子**两侧**       |
| **space-evenly**  | 弹性盒子沿主轴均匀排列，弹性盒子与容器之间间距相等           |

### 侧轴对齐方式

* **`align-items`**：当前弹性容器内**所有**弹性盒子的侧轴对齐方式（给**弹性容器**设置）
* **`align-self`**：单独控制**某个弹性盒子**的侧轴对齐方式（给**弹性盒子**设置）

| 属性值      | 效果                                                         |
| ----------- | ------------------------------------------------------------ |
| **stretch** | 弹性盒子沿着侧轴线被**拉伸至铺满容器**（弹性盒子没有设置侧轴方向尺寸则默认拉伸） |
| **center**  | 弹性盒子沿侧轴**居中**排列                                   |
| flex-start  | 弹性盒子从**起点**开始依次排列                               |
| flex-end    | 弹性盒子从**终点**开始依次排列                               |

### 修改主轴方向

**主轴默认在水平方向，侧轴默认在垂直方向**

属性名：**flex-direction**

| 属性值           | 效果                       |
| ---------------- | -------------------------- |
| row              | 水平方向，从左向右（默认） |
| **column**       | **垂直方向，从上向下**     |
| row - reverse    | 水平方向，从右向左         |
| column - reverse | 垂直方向，从下向上         |

### 弹性伸缩比

作用：控制弹性盒子的**主轴**方向的**尺寸**。

属性名：**flex**

属性值：**整数数字**，表示占用**父级剩余尺寸的份数**。（给**弹性盒子**设置）

> 注意：默认情况下，主轴方向的尺寸靠内容撑开，侧轴默认拉伸

示例：

```html
<style>
  .box{
    display: flex;
    height: 300px;
    border: 1px solid #000;
  }

  .box div {
    height: 100px;
    background-color: pink;
  }

  .box div:nth-child(1) {
    width: 200px;
  }

  .box div:nth-child(2) {
    flex: 1;
  }

  .box div:nth-child(3) {
    flex: 2;
  }
</style>

<body>
  <div class="box">
    <div>1</div>
    <div>2</div>
    <div>3</div>
  </div>
</body>
```

### 弹性盒子换行

弹性盒子可以**自动挤压或拉伸**，默认情况下，所有弹性盒子都**在一行显示**。

属性名：**`flex-wrap`**

属性值

* wrap：换行
* nowrap：不换行（默认）

### 行对齐方式

属性名：**align-content** 

| 属性值            | 效果                                                         |
| ----------------- | ------------------------------------------------------------ |
| flex-start        | 默认值，弹性盒子从**起点**开始依次排列                       |
| flex-end          | 弹性盒子从**终点**开始依次排列                               |
| **center**        | 弹性盒子沿主轴**居中**排列                                   |
| **space-between** | 弹性盒子沿主轴均匀排列，空白间距均分在弹性盒子**之间**（父级剩余的尺寸分配间距） |
| **space-around**  | 弹性盒子沿主轴均匀排列，空白间距均分在弹性盒子**两侧**       |
| **space-evenly**  | 弹性盒子沿主轴均匀排列，弹性盒子与容器之间间距相等           |

注意：该属性对**单行**弹性盒子模型**无效**。（也就是说必须要设置`flex-wrap:wrap;`）

---

## 综合案例——抖音解决方案

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>抖音解决方案</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            list-style: none;
        }

        .box {
            border: 1px solid #ddd;
            border-radius: 10px;
            margin: 50px auto;
            width: 1200px;
            height: 418px;
        }

        .box ul {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-content: space-between;

            padding: 90px 40px 90px 60px;
            height: 418px;
        }

        .box li {
            display: flex;
            width: 500px;
            height: 88px;
        }

        .box .pic {
            margin-right: 15px;
        }

        .box .text h4 {
            line-height: 40px;
            font-size: 20px;
            color: #333;
            font-weight: 400;
        }

        li p {
            font-size: 14px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="box">
        <ul>
            <li>
                <div class="pic">
                    <img src="./images/1.svg" alt="">
                </div>
                <div class="text">
                    <h4>一键发布多端</h4>
                    <p>发布视频到抖音短视频、西瓜视频及今日头条</p>
                </div>
            </li>
            <li>
                <div class="pic">
                    <img src="./images/2.svg" alt="">
                </div>
                <div class="text">
                    <h4>管理视频内容</h4>
                    <p>支持修改已发布稿件状态和实时查询视频审核状态</p>
                </div>
            </li>
            <li>
                <div class="pic">
                    <img src="./images/3.svg" alt="">
                </div>
                <div class="text">
                    <h4>发布携带组件</h4>
                    <p>支持分享内容携带小程序、地理位置信息等组件，扩展内容及突出地域性</p>
                </div>
            </li>
            <li>
                <div class="pic">
                    <img src="./images/4.svg" alt="">
                </div>
                <div class="text">
                    <h4>数据评估分析</h4>
                    <p>获取视频在对应产品内的数据表现、获取抖音热点，及时进行表现评估</p>
                </div>
            </li>
        </ul>
    </div>
</body>
</html>
```

