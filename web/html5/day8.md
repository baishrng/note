## 定位

作用：灵活的**改变**盒子在网页中的**位置**

实现：

1、**定位模式：position**

2、**边偏移：设置盒子的位置**

- left
- right
- top
- bottom

### 相对定位

**position: relative**

特点：

- 不脱标，占用自己原来位置
- 显示模式特点保持不变
- 设置边偏移则相对自己原来位置移动

拓展：很少单独使用相对定位，一般是与其他定位方式配合使用

```css
div {
  position: relative;
  top: 100px;
  left: 200px;
}	
```

### 绝对定位

**position: absolute**

使用场景：**子**级**绝对**定位，父级**相对**定位（**子绝父相**）

特点：

* 脱标，不占位
* 显示模式具备行内块特点
* 设置边偏移则相对最近的已经定位的祖先元素改变位置
* 如果祖先元素都未定位，则相对浏览器可视区改变位置

```css
.father {
  position: relative;
}

.father span {
  position: absolute;
  top: 0;
  right: 0;
}
```

### 定位居中

实现步骤：

1. 绝对定位
2. 水平、垂直边偏移为 **50%**
3. 子级向左、上移动**自身尺寸**的**一半**

* 左、上的外边距为 –尺寸的一半
* transform: translate(-50%, -50%)

```css
img {
  position: absolute;
  left: 50%;
  top: 50%;

  /* margin-left: -265px;
  margin-top: -127px; */

  /* 方便： 50% 就是自己宽高的一半 (水平，垂直)*/
  transform: translate(-50%, -50%);
}
```

### 固定定位

**position: fixed**

场景：元素的位置在网页滚动时不会改变

特点：

* 脱标，不占位
* 显示模式具备行内块特点
* 设置边偏移相对浏览器窗口改变位置

```css
div {
  position: fixed;
  top: 0;
  right: 0;

  width: 500px;
}
```

---

## 堆叠层级 z-index

默认效果：按照标签书写顺序，**后来者居上**

作用：设置**定位**元素的**层级顺序**，改变定位元素的显示顺序

属性名：**z-index**

属性值：**整数数字**（默认值为0，取值越大，层级越高）

```css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div {
            position: absolute;
            width: 200px;
            height: 200px;
        }

        .box1 {
            background-color: pink;
            /* 取值是整数，默认是0，取值越大显示顺序越靠上 */
            z-index: 1;
        }

        .box2 {
            background-color: skyblue;
            left: 100px;
            top: 100px;
            z-index: 2;
        }
    </style>
</head>
<body>
    <div class="box1">box1</div>
    <div class="box2">box2</div>
</body>
</html>
```

---

## 定位-总结

| 定位模式 | 属性值       | 是否脱标 | 显示模式             | 参照物                                              |
| -------- | ------------ | -------- | -------------------- | --------------------------------------------------- |
| 相对定位 | **relative** | 否       | 保持标签原有显示模式 | **自己原来**位置                                    |
| 绝对定位 | **absolute** | **是**   | **行内块**特点       | 1. **已经定位**的**祖先**元素 <br />2. 浏览器可视区 |
| 固定定位 | **fixed**    | **是**   | **行内块**特点       | **浏览器**窗口                                      |

---

## CSS 精灵

CSS 精灵，也叫 **CSS Sprites**，是一种网页**图片应用处理方式**。把网页中**一些背景图片**整合到**一张图片**文件中，再**background-position** 精确的定位出背景图片的位置。

优点：**减少**服务器被请求**次数**，**减轻**服务器的**压力**，**提高**页面加载**速度**

实现步骤：

1. 创建盒子，**盒子尺寸**与**小图**尺寸**相同**
2. 设置盒子**背景图**为精灵图
3. 添加 **background-position** 属性，改变**背景图位置**

​       3.1 使用 PxCook 测量小图片**左上角坐标**

​       3.2 取**负数**坐标为 background-position 属性值（向左上移动图片位置）

```css
div {
  width: 112px;
  height: 110px;
  background-color: pink;
  background-image: url(./imgs/abcd.jpg);
  background-position: -256px -276px;
}
```

---

## 案例-京东服务

#### HTML结构

```html
<div class="service">
  <ul>
    <li>
      <h5></h5>
      <p>品类齐全，轻松购物</p>
    </li>
    <li>
      <h5></h5>
      <p>多仓直发，极速配送</p>
    </li>
    <li>
      <h5></h5>
      <p>正品行货，精致服务</p>
    </li>
    <li>
      <h5></h5>
      <p>天天低价，畅选无忧</p>
    </li>
  </ul>
</div>
```

#### CSS样式

```html
<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  li {
    list-style: none;
  }

  .service {
    margin: 100px auto;
    width: 1190px;
    height: 42px;
    /* background-color: pink; */
  }

  .service ul {
    display: flex;
  }

  .service li {
    display: flex;
    padding-left: 40px;
    width: 297px;
    height: 42px;
    /* background-color: skyblue; */
  }

  .service li h5 {
    margin-right: 10px;
    width: 36px;
    height: 42px;
    /* background-color: pink; */
    background: url(./images/sprite.png) 0 -192px;
  }

  .service li:nth-child(2) h5 {
    background-position: -41px -192px;
  }

  .service li:nth-child(3) h5 {
    background-position: -82px -192px;
  }

  .service li:nth-child(4) h5 {
    background-position: -123px -192px;
  }

  .service li p {
    font-size: 18px;
    color: #444;
    font-weight: 700;
    line-height: 42px;
  }
</style>
```

---

## 字体图标

字体图标：**展示的是图标，本质是字体**

作用：在网页中添加**简单的、颜色单一**的小图标

优点

* **灵活性**：灵活地修改样式，例如：尺寸、颜色等
* **轻量级**：体积小、渲染快、降低服务器请求次数
* **兼容性**：几乎兼容所有主流浏览器
* **使用方便**：先下载再使用

---

## 字体图标 – 下载字体

iconfont 图标库：<https://www.iconfont.cn/> 

下载字体：

登录 → 素材库 → 官方图标库 → 进入图标库 → 选图标，加入购物车 → 购物车，添加至项目，确定 → 下载至本地 

---

## 字体图标 – 使用字体

1、引入字体样式表（iconfont.css）

```css
<link rel="stylesheet" href="./iconfont/iconfont.css">
```

2、标签使用字体图标类名

* iconfont：字体图标基本样式（字体名，字体大小等等）
* icon-xxx：图标对应的类名

```html
<span class="iconfont icon - xxx"></span>
```

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="./iconfont/iconfont.css">
    <style>
        .iconfont {
            font-size: 200px;
            color: red;
        }
    </style>
</head>
<body>
    <span>12</span>
    <span class="iconfont icon-shequhuodong"></span>
</body>
</html>
```

> 如果要调整字体大小，选择器的优先级要高于 iconfont 类

----

## 字体图标 – 上传矢量图

作用：项目**特有**的图标上传到 iconfont 图标库，生成字体

上传步骤：上传 → 上传图标 → 选择 svg 矢量图，打开 → 提交 → 系统审核

---

## CSS 修饰属性

### 垂直对齐方式 vertical-align

属性名：vertical-align

| 属性值     | 效果             |
| ---------- | ---------------- |
| baseline   | 基线对齐（默认） |
| top        | 顶部对齐         |
| **middle** | **居中对齐**     |
| bottom     | 底部对齐         |

>谁占的空间大，就给谁加 vertical-align 属性