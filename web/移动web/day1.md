## 平面转换 

作用：为元素**添加动态效果**，一般与**过渡**配合使用

概念：改变盒子在**平面**内的**形态**（位移、旋转、缩放、倾斜）

平面转换也叫 **2D 转换**，属性是 **transform**

示例：

```css
div {
  margin: 100px 0;

  width: 100px;
  height: 100px;
  background-color: pink;

  transition: all 1s;
}

/* 鼠标滑过：添加动态效果 */
div:hover {
  transform: translate(800px) rotate(360deg) scale(2) skew(180deg);
}
```

### 平移

属性：

```css
transform: translate(X轴移动距离, Y轴移动距离);
```

取值

* 像素单位数值
* 百分比（参照**盒子自身尺寸**计算结果）
* **正负**均可

技巧

* translate() **只写一个值**，表示沿着 **X** 轴移动
* 单独设置 X 或 Y 轴移动距离：translateX() 或 translateY()

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>平移效果</title>
    <style>
        .father {
            width: 500px;
            height: 300px;
            margin: 100px auto;
            border: 1px solid #000;
        }

        .son {
            width: 200px;
            height: 100px;
            background-color: pink;
            transition: all 0.5s;
        }

        /* 鼠标移入父盒子，son改变位置 */
        .father:hover .son {
            transform: translate(200px, 100px);

            /* 百分比：参照盒子自身尺寸计算结果 */
            transform: translate(50%, 100%);
            transform: translate(-50%, 100%);

            /* 只写一个数表示水平方向 */
            transform: translate(100px);

            transform: translateY(100px);
            transform: translateX(100px);
        }
    </style>
</head>
<body>
    <div class="father">
        <div class="son"></div>
    </div>
</body>
</html>
```

### 定位居中

- 方法一：


```css
position: absolute;
left: 50%;
top: 50%;
/* margin */
margin-left: -100px;
margin-top: -50px;

width: 200px;
height: 100px;
```

- 方法二：平移 → 百分比参照**盒子自身尺寸**计算结果 


```css
position: absolute;
left: 50%;
top: 50%;
transform: translate(-50%, -50%);
```

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>绝对定位元素居中效果</title>
    <style>
        .box {
            position: absolute;
            left: 50%;
            top: 50%;

            /* 向左向上移动自身尺寸的一半 */
            transform: translate(-50%, -50%);

            width: 200px;
            height: 100px;
            background-color: pink;
        }
    </style>
</head>
<body>
    <div class="box"></div>
</body>
</html>
```

### 案例—双开门效果

- HTML 结构

```html
<div class="father">
    <div class="left"></div>
    <div class="right"></div>
</div>
```

- CSS 样式

```css
* {
    margin: 0;
    padding: 0;
}

/* 1. 布局：父子结构，父级是大图，子级是左右小图 */
.father {
    display: flex;
    margin: 0 auto;
    width: 1366px;
    height: 600px;
    background-image: url(./images/bg.jpg);

    overflow: hidden;
}

.father .left,
.father .right {
    width: 50%;
    height: 600px;
    background-image: url(./images/fm.jpg);

    transition: all .5s;
}

.father .right {
    /* right 表示的取到精灵图右面的图片 */
    background-position: right 0;
}

/* 2. 鼠标悬停的效果：左右移动 */
.father:hover .left {
    transform: translate(-100%);
}

.father:hover .right {
    transform: translateX(100%);
}
```

### 旋转

- 属性

```css
transform: rotate(旋转角度);
```

* 取值：角度单位是 **deg** 
* 技巧
  * 取值**正负均可**
  * 取值为**正，顺**时针旋转
  * 取值为**负，逆**时针旋转

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>旋转效果</title>
    <style>
        img {
            width: 200px;
            transition: all 2s;
        }

        /* 鼠标悬停到图片上，添加旋转效果 */
        img:hover {
            /* 正数：顺时针旋转；负数：逆时针旋转 */
            transform: rotate(360deg);
            transform: rotate(-360deg);
        }
    </style>
</head>
<body>
    <img src="./imgs/rotate.png" alt="">
</body>
</html>
```

### 改变转换原点

> 默认情况下，转换原点是**盒子中心点** 

属性：

```css
transform-origin: 水平原点位置 垂直原点位置;
```

取值：

* **方位名词**（left、top、right、bottom、center）
* 像素单位数值
* 百分比

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>转换原点</title>
    <style>
        img {
            width: 200px;
            border: 1px solid #000;
            transition: all 1s;

            transform-origin: right bottom;
        }

        img:hover {
            transform: rotate(360deg);
        }
    </style>
</head>
<body>
    <img src="./imgs/rotate.png" alt="">
</body>
</html>
```

### 案例—时钟

```css
transform-origin: center bottom;
```

```css
.hour {
  width: 6px;
  height: 50px;
  background-color: #333;
  margin-left: -3px;
  transform: rotate(15deg);
  transform-origin: center bottom;
}

.minute {
  width: 5px;
  height: 65px;
  background-color: #333;
  margin-left: -3px;
  transform: rotate(90deg);
  transform-origin: center bottom;
}

.second {
  width: 4px;
  height: 80px;
  background-color: red;
  margin-left: -2px;
  transform: rotate(240deg);
  transform-origin: center bottom;
}
```

### 多重转换

多重转换技巧：**先平移再旋转**

```css
transform: translate() rotate();
```

* 多重转换原理：以第一种转换方式坐标轴为准转换形态
  * 旋转会改变网页元素的坐标轴向
  * 先写旋转，则后面的转换效果的轴向以旋转后的轴向为准，会影响转换结果

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>多重转换</title>
    <style>
        .box {
            width: 800px;
            height: 200px;
            border: 1px solid #000;
        }

        img {
            width: 200px;
            transition: all 2s;
        }

        /* 鼠标移入box，图片边走边转 */
        .box:hover img {
            /* 先平移再旋转 */
            transform: translate(600px) rotate(360deg);

            /* 旋转会改变坐标轴向 */
            /* 多种转换：以第一种转换形态的坐标轴为准 */
            /* transform: rotate(360deg) translate(600px); */

            /* 层叠性 */
            transform: translate(600px);
            transform: rotate(360ddeg);
        }
    </style>
</head>
<body>
    <div class="box">
        <img src="./imgs/tyre.png" alt="">
    </div>
</body>
</html>
```

### 缩放

- 属性：

```css
transform: scale(缩放倍数);
transform: scale(X轴缩放倍数, Y轴缩放倍数);
```

* 技巧
  * 通常，只为 scale() 设置**一个值**，表示 X 轴和 Y 轴**等比例缩放**
  * 取值**大于1**表示**放大**，取值**小于1**表示**缩小**

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>缩放效果</title>
    <style>
        .box {
            width: 300px;
            height: 210px;
            margin: 100px, auto;
            background-color: pink;
        }

        .box img {
            width: 100%;
            transition: all 0.5s;
        }

        .box:hover img {
            /* 修改宽高尺寸，从左上角开始缩放 */
            /* width: 500px;
            height: 400px; */

            /* 大于1，表示放大 */
            transform: scale(2);
            /* 小于1，表示缩小 */
            transform: scale(0.5);
            /* 等于1，不变 */
            transform: scale(1);
        }
    </style>
</head>
<body>
    <div class="box">
        <img src="./imgs/1.jpg" alt="">
    </div>
</body>
</html>
```

### 播放特效

方法一：

```css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>缩放效果</title>
    <style>
        li {
            list-style: none;
        }

        img {
            width: 100%;
        }

        .box {
            width: 200px;
            height: 300px;
            margin: 50px auto;
        }

        .box p {
            color: #3b3b3b;
            padding: 10px 10px 0 10px;
        }

        /* 1. 摆放播放按钮：图片区域的中间 */
        .box li {
            overflow: hidden;
        }

        .pic {
            position: relative;
        }

        .pic::after{
            position: absolute;
            left: 50%;
            top: 50%;
            margin-left: -29px;
            margin-top: -29px;
            content: '';
            width: 58px;
            height: 58px;
            background: url(./imgs/play.png);
            transform: scale(5);
            opacity: 0;

            transition: all 0.5s;
        }

        /* 2. hover效果：大按钮，看不见：透明是0 → 小按钮，看得见：透明度1 */
        .box li:hover .pic::after {
            transform: scale(1);
            opacity: 1;
        }
    </style>
</head>
<body>
    <div class="box">
        <ul>
            <li>
                <div class="pic">
                    <img src="./imgs/1.jpg" alt="">
                </div>
                <p>小猫小猫</p>
            </li>
        </ul>
    </div>
</body>
</html>
```

方法二：

```css
li {
  list-style: none;
}

img {
  width: 100%;
}

.box {
  width: 200px;
  height: 300px;
  margin: 50px auto;
}

.box p {
  color: #3b3b3b;
  padding: 10px 10px 0 10px;
}

/* 1. 摆放播放按钮：图片区域的中间 */
.box li {
  overflow: hidden;
}

.pic {
  position: relative;
}

.pic::after{
  position: absolute;
  left: 50%;
  top: 50%;
  /* margin-left: -29px;
  margin-top: -29px; */
  transform: translate(-50%, -50%) scale(5);
  content: '';
  width: 58px;
  height: 58px;
  background: url(./imgs/play.png);
  /* transform: scale(5); */
  opacity: 0;

  transition: all 0.5s;
}

/* 2. hover效果：大按钮，看不见：透明是0 → 小按钮，看得见：透明度1 */
.box li:hover .pic::after {
  transform: translate(-50%, -50%) scale(1);
  opacity: 1;
}
```

### 倾斜

属性：

```css
transform: skew();
```

取值：角度度数 **deg**（正数向左倾斜，负数向右倾斜）

---

## 渐变

渐变是**多个颜色**逐渐变化的效果，一般用于设置**盒子背景** 

分类：

- 线性渐变
- 径向渐变

### 线性渐变

属性：

```css
background-image: linear-gradient(
  渐变方向,
  颜色1 终点位置,
  颜色2 终点位置,
  ......
);
```

取值：

* 渐变方向：**可选**
  * **to 方位名词**
  * **角度度数**
* 终点位置：**可选**
  * **百分比**

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
        width: 200px;
        height: 200px;
        background-color: green;

        background-image: linear-gradient(
            red,
            green
        );
        background-image: linear-gradient(
            to right,
            red,
            green
        );
        background-image: linear-gradient(
            45deg,
            red,
            green
        );
        background-image: linear-gradient(
            red 80%,
            green
        );
       }
    </style>
</head>
<body>
    <div></div>
</body>
</html>
```

### 案例—产品展示

```css
background-image: linear-gradient(
 transparent,
 rgba(0, 0, 0, 0.6)
 );
```

HTML 结构

```html
<div class="box">
  <img src="./images/product.jpeg" alt="" />
  <div class="title">OceanStor Pacific 海量存储斩获2021 Interop金奖</div>
  <div class="mask"></div>
</div>
```

CSS 样式

```css
.box {
  position: relative;
  width: 300px;
  height: 212px;
}

.box img {
  width: 300px;
}

.box .title {
  position: absolute;
  left: 15px;
  bottom: 20px;
  z-index: 2;
  width: 260px;
  color: #fff;
  font-size: 20px;
  font-weight: 700;
}

.box .mask {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-image: linear-gradient(
    transparent,
    rgba(0, 0, 0, 0.5)
  );
  opacity: 0;

  transition: all 0.5s;
}

.box:hover .mask {
  opacity: 1;
}
```

### 径向渐变

作用：给按钮添加**高光**效果

属性：

```css
background-image: radial-gradient(
  半径 at 圆心位置,
  颜色1 终点位置,
  颜色2 终点位置,
  ......
);
```

取值：

* 半径可以是**2条**，则为**椭圆**
* 圆心位置取值：像素单位数值 / 百分比 / 方位名词

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
            background-color: pink;
            border-radius: 50%;

            background-image: radial-gradient(
                50px at center center,
                red,
                pink
            );
            background-image: radial-gradient(
                50px 20px at center center,
                red,
                pink
            );
            background-image: radial-gradient(
                50px at 50px 30px,
                red,
                pink
            );
            background-image: radial-gradient(
                50px at 50px 30px,
                red,
                pink 50%
            );
        }

        button {
            width: 100px;
            height: 40px;
            background-color: green;
            border: 0;
            border-radius: 5px;
            color: #fff;

            background-image: radial-gradient(
                30px at 30px 20px,
                rgba(255, 255, 255, 0.2),
                transparent
            );
        }
    </style>
</head>

<body>
    <div></div>
    <button>按钮</button>
</body>

</html>
```

---

## 综合案例—喜马拉雅

### 导航-频道

#### 箭头旋转

```css
.x-header-nav .nav-item:hover .icon-down {
  transform: rotate(-180deg);
}
```

#### 频道列表

```css
.channel-layer {
  position: absolute;
  top: 60px;
  left: 50%;
  z-index: -2;
  width: 1080px;
  height: 120px;
  padding: 10px;
  margin-left: -540px;
  color: #72727b;
  background-color: #f5f5f5;
  border: 1px solid #e4e4e4;
  border-top: none;
  transition: all 0.5s;
  transform: translateY(-120px);
}

/* TODO 2. 弹窗频道 */
.x-header-nav .nav-item:hover .channel-layer {
  transform: translateY(0);
}
```

### 渐变按钮

#### 搜索按钮

```css
.x-header-search form .btn {
  position: absolute;
  top: 0;
  right: 0;
  width: 60px;
  height: 40px;
  line-height: 40px;
  text-align: center;
  background-color: #f86442;
  border-top-right-radius: 20px;
  border-bottom-right-radius: 20px;
  background-image: linear-gradient(
    to right,
    rgba(255, 255, 255, 0.3),
    #f86442
  );
}
```

#### 登录按钮

```css
/* TODO 7. 渐变按钮 */
.card .card-info .login {
  padding: 3px 34px;
  color: #fff;
  background-color: #ff7251;
  border-radius: 30px;
  box-shadow: 0 4px 8px 0 rgb(252 88 50 / 50%);
  background-image: linear-gradient(
    to right,
    rgba(255, 255, 255, 0.2),
    #ff7251
  );
}
```

#### 客户端按钮

```css
/* TODO 8. 径向渐变 */
.download .dl .dl-btn {
  width: 68px;
  height: 34px;
  line-height: 34px;
  color: #fff;
  text-align: center;
  border-radius: 4px;
  background-image: radial-gradient(
    50px at 10px 10px,
    rgba(255, 255, 255, 0.5),
    transparent
  );
}
```

### 轮播图

```css
/* TODO 4. 摆放图片 */
.banner .banner-list .banner-item.left {
  z-index: 0;
  transform: translate(-160px) scale(0.8);
  transform-origin: left center;
}

.banner .banner-list .banner-item.right {
  z-index: 0;
  transform: translate(160px) scale(0.8);
  transform-origin: right center;
}
```

### 猜你喜欢

```css
/* TODO 5. 播放按钮和遮罩 */
.album-item .album-item-box::after {
  position: absolute;
  left: 0;
  top: 0;
  content: '';
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,.5) url(../assets/play.png) no-repeat center / 20px;
  opacity: 0;
  transition: all .5s;
}

.album-item .album-item-box:hover::after {
  opacity: 1;
  background-size: 50px;
}


/* TODO 6. 图片缩放 */
.album-item .album-item-box:hover img {
  transform: scale(1.1);
}
```

