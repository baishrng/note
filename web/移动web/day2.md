## 空间转换

* 空间：是从坐标轴角度定义的 **X 、Y 和 Z** 三条坐标轴构成了一个立体空间，**Z 轴位置与视线方向相同。**（正数方向指向用户）
* 空间转换也叫 **3D转换**
* **属性：transform**

### 平移

属性：

 ```css
transform: translate3d(x, y, z);
transform: translateX();
transform: translateY();
transform: translateZ();
 ```

取值（**正负**均可） ：

- 像素单位数值
- 百分比（参照**盒子自身尺寸**计算结果）

提示：

- 默认情况下，Z 轴平移没有效果

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>空间平移</title>
  <style>
    .box {
      width: 200px;
      height: 200px;
      margin: 100px auto;
      background-color: pink;
      transition: all 0.5s;
    }

    .box:hover {
      /* 电脑是平面，默认无法观察 Z 轴平移效果 */
      /* transform: translate3d(100px, 200px, 300px); */

      /* 3d 小括号里面必须逗号隔开三个数 */
      /* transform: translate3d(100px, 200px); */

      transform: translateX(100px);
      transform: translateY(-100%);
      transform: translateZ(300px);
    }
  </style>
</head>
<body>
  <div class="box"></div>
</body>
</html>
```

### 视距

作用：指定了**观察者**与 **Z=0** 平面的**距离**，为元素添加**透视效果**

透视效果：**近大远小、近实远虚**

属性：(添加给**父级**，取值范围 **800px-1200px**)

```css
perspective: 视距;
```

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>透视效果</title>
  <style>
    /* 视距属性必须添加给 直接父级 */
    .father {
      perspective: 1000px;
    }

    .son {
      width: 200px;
      height: 200px;
      margin: 100px auto;
      background-color: pink;
      transition: all 0.5s;
    }

    .son:hover {
      transform: translateZ(-300px);
      transform: translateZ(300px);
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

### 旋转

- Z 轴：transform：rotateZ()，沿着 Z 轴旋转

- X 轴：transform：rotateX()，沿着 X 轴旋转

- Y 轴：transform：rotateY()，沿着 Y 轴旋转

示例1：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>空间旋转-Z轴</title>
  <style>
    .box {
      width: 300px;
      margin: 100px auto;
    }

    img {
      width: 300px;
      transition: all 2s;
    }

    img:hover {
      transform: rotateZ(360deg);
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

示例2：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>空间旋转-X轴</title>
  <style>
    .box {
      width: 300px;
      margin: 100px auto;
    }

    img {
      width: 300px;
      transition: all 2s;
    }

    .box {
      /* 透视效果：近大远小，近实远虚 */
      perspective: 1000px;
    }

    img:hover {
      transform: rotateX(60deg);
      transform: rotateX(-60deg);
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

示例3：

```htlm
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>空间旋转-Y轴</title>
  <style>
    .box {
      width: 300px;
      margin: 100px auto;
    }

    img {
      width: 300px;
      transition: all 2s;
    }

    .box {
      /* 透视效果：近大远小，近实远虚 */
      perspective: 1000px;
    }

    img:hover {
      transform: rotateY(60deg);
      transform: rotateY(-60deg);
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

### 左手法则

作用：根据**旋转方向**确定取值**正负**

使用：**左手**握住旋转轴, **拇指指向正值方向**, 其他四个手指**弯曲**方向为旋转**正值**方向 

（就是旋转轴顺时针方向为正，逆时针方向为负，旋转轴的箭头需指向自己）

### rotate3d-了解

* rotate3d(x, y, z, 角度度数) ：用来设置**自定义旋转轴的位置**及旋转的角度
* x，y，z 取值为0-1之间的数字

### 立体呈现

作用：设置元素的**子**元素是位于 **3D 空间**中还是**平面**中

属性名：transform-style

属性值：

* flat：子级处于**平面**中
* **preserve-3d**：子级处于 **3D 空间**

> 属性设置为父级

呈现立体图形步骤：

1. **父元素**添加**transform-style: preserve-3d**； 
2. 子级**定位** 
3.  调整子盒子的**位置（位移或旋转）**

> 提示：空间内，转换元素都有自已独立的坐标轴，互不干扰

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>立体呈现</title>
  <style>
    .cube {
      width: 200px;
      height: 200px;
      margin: 100px auto;
      /* background-color: pink; */
      transition: all 2s;

      transform-style: preserve-3d;
      position: relative;

      /* transform: rotateY(89deg); */
    }

    .cube div {
      position: absolute;
      left: 0;
      top: 0;
      width: 200px;
      height: 200px;
    }

    .froot {
      background-color: orange;
      transform: translateZ(100px);
    }

    .back {
      background-color: green;
      transform: translateZ(-100px);
    }

    .cube:hover {
      transform: rotateY(90deg);
    }
  </style>
</head>
<body>
  <div class="cube">
    <div class="froot">前面</div>
    <div class="back">后面</div>
  </div>
</body>
</html>
```

### 案例—3D 导航

案例步骤：

1. 搭建**立方体**
   1. 绿色是立方体的前面
   2. 橙色是立方体的上面
2. 鼠标**悬停**，立方体**旋转**

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>3D 导航</title>
  <style>
    ul {
        margin: 0;
        padding: 0;
        list-style: none;
      }

      .nav {
        width: 300px;
        height: 40px;
        margin: 50px auto;
      }

      .nav ul {
        display: flex;
      }

    .nav li {
      position: relative;
      width: 100px;
      height: 40px;
      line-height: 40px;
      transition: all 0.5s;

      transform-style: preserve-3d;

      /* 为了看到橙色和绿色的移动过程，给立方体添加旋转 */
      /* transform: rotateX(-20deg) rotateY(30deg); */
    }

    .nav li a {
      position: absolute;
      left: 0;
      top: 0;
      display: block;
      width: 100%;
      height: 100%;
      text-align: center;
      text-decoration: none;
      color: #fff;
    }

    .nav li a:first-child {
      background-color: green;
      transform: translateZ(20px);
    }

    /* 立方体每个面都有独立的坐标轴，互不影响 */
    .nav li a:last-child {
      background-color: orange;
      transform: translateY(-50%) rotateX(90deg);
    }

    .nav li:hover {
      transform: rotateX(-90deg);
    }
  </style>
</head>
<body>
  <div class="nav">
    <ul>
      <li>
        <a href="#">首页</a>
        <a href="#">Index</a>
      </li>
      <li>
        <a href="#">登录</a>
        <a href="#">login</a>
      </li>
      <li>
        <a href="#">注册</a>
        <a href="#">register</a>
      </li>
    </ul>
  </div>
</body>

</html>
```

### 缩放

属性

```css
transform: scale3d(x, y, z);
transform: scaleX();
transform: scaleY();
transform: scaleZ();
```

取值**大于1**表示**放大**，取值**小于1**表示**缩小**

----

## 动画

* 过渡：实现**两个状态**间的变化过程
* 动画：实现**多个状态**间的变化过程，**动画过程可控**（重复播放、最终画面、是否暂停）

### 动画实现步骤

1. 定义动画

```css
/* 方式一 */
@keyframes 动画名称 {
  from {}
  to {}
}

/* 方式二 */
@keyframes 动画名称 {
  0% {}
  10% {}
  ......
  100% {}
}
```

`{}`里存放当前状态的CSS

百分比：表示的意思是动画时长的百分比

2. 使用动画

```css
animation: 动画名称 动画花费时长;
```

动画花费时长以秒（s）为单位

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>动画实现步骤</title>
  <style>
    .box {
      width: 200px;
      height: 100px;
      background-color: pink;

      animation: change 1s;
    }

    /* 动画一：宽度从200变化到800 */
    /* @keyframes change {
      from {
        width: 200px;
      }
      to {
        width: 800px;
      }
    } */

    /* 动画二：从 200*100 变化到 300*300 变化到800*500 */
    /* 百分比：表示的意思是动画时长的百分比 */
    @keyframes change {
      0% {
        width: 200px;
        height: 100px;
      }
      20% {
        width: 300px;
        height: 300px;
      }
      100% {
        width: 800px;
        height: 500px;
      }
    }
  </style>
</head>
<body>
  <div class="box"></div>
</body>
</html>
```

### animation复合属性

```css
animation: 动画名称 动画时长 速度曲线 延迟时间 重复次数 动画方向 执行完毕时状态;
```

提示：

* **动画名称**和**动画时长**必须赋值
* 取值**不**分先后顺序
* 如果有**两个时间**值，**第一个**时间表示**动画时长**，**第二个**时间表示**延迟时间**

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>animation复合属性</title>
  <style>
    .box {
      width: 200px;
      height: 100px;
      background-color: pink;

      /* linear：匀速 */
      animation: change 1s linear;

      /* steps：分步动画，工作中，配合精灵图实现精灵动画 */
      animation: change 1s steps(3);

      /* 如果有两个时间，第一个是动画时长，第二个是延迟时间 */
      animation: change 1s 2s;

      /* 重复次数，infinite：无限循环 */
      animation: change 1s 3;
      animation: change 1s infinite;

      /* alternate：反向 */
      animation: change 1s infinite alternate;

      /* 动画执行完毕时的状态， forwards：结束状态； backwards：开始状态（默认） */
      animation: change 1s forwards;
      animation: change 1s backwards;
    }

    /* 宽度 从 200 变化到 800 */
    @keyframes change {
      from {
        width: 200px;
      }
      to {
        width: 800px;
      }
    }
  </style>
</head>
<body>
  <div class="box"></div>
</body>
</html>
```

### animation拆分写法

| 属性                              | 作用               | 取值                                         |
| --------------------------------- | ------------------ | -------------------------------------------- |
| **animation - name**              | **动画名称**       |                                              |
| **animation - duration**          | **动画时长**       | 以秒（s）为单位                              |
| animation - delay                 | 延迟时间           |                                              |
| animation - fill - mode           | 动画执行完毕时状态 | forwards：最后一帧状态 backwards：第一帧状态 |
| animation - timing - function     | 速度曲线           | **steps (数字)：逐帧动画**                   |
| **animation - iteration - count** | **重复次数**       | **infinite 为无限循环**                      |
| **animation - direction**         | **动画执行方向**   | **alternate 为反向**                         |
| animation - play - state          | 暂停动画           | paused 为暂停，通常配合:**hover** 使用       |

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>animation拆分写法</title>
  <style>
    .box {
      width: 200px;
      height: 100px;
      background-color: pink;

      /* 动画名称 */
      animation-name: change;
      /* 动画时长 */
      animation-duration: 1s;
      /* 播放次数 */
      animation-iteration-count: infinite;
    }

    .box:hover {
      /* 暂停动画 */
      animation-play-state: paused;
    }

    /* 宽度 从 200 变化到 800 */
    @keyframes change {
      0% {
        width: 200px;
      }
      100% {
        width: 800px;
      }
    }
  </style>
</head>
<body>
  <div class="box"></div>
</body>
</html>
```

### 走马灯

- 列表添加动画效果
- 鼠标移入区域，列表动画暂停

- 无缝动画原理：复制**开头图片**到**结尾**位置（**图片累加宽度 = 区域宽度**）

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>走马灯</title>
  <style>
    * {
      margin: 0;
      padding: 0;
    }

    li {
      list-style: none;
    }

    img {
      display: block;
      width: 200px;
    }
    
    .box {
      width: 600px;
      height: 112px;
      border: 5px solid #000;
      margin: 100px auto;
      overflow: hidden;
    }

    .box ul {
      display: flex;
      animation: move 6s infinite linear;
    }

    .box:hover ul {
      animation-play-state: paused;
    }

    /* 定义位移动画；ul使用动画；鼠标悬停暂停动画 */
    @keyframes move {
      0% {
        transform: translate(0);
      }
      100% {
        transform: translate(-1400px);
      }
    }
  </style>
</head>
<body>
  <div class="box">
    <ul>
      <li><img src="./images/1.jpg" alt="" /></li>
        <li><img src="./images/2.jpg" alt="" /></li>
        <li><img src="./images/3.jpg" alt="" /></li>
        <li><img src="./images/4.jpg" alt="" /></li>
        <li><img src="./images/5.jpg" alt="" /></li>
        <li><img src="./images/6.jpg" alt="" /></li>
        <li><img src="./images/7.jpg" alt="" /></li>
        <!-- 替身：填补显示区域的露白 -->
        <li><img src="./images/1.jpg" alt="" /></li>
        <li><img src="./images/2.jpg" alt="" /></li>
        <li><img src="./images/3.jpg" alt="" /></li>
    </ul>
  </div>
</body>
</html>
```

### 逐帧动画

| 属性                          | 作用     | 取值                       |
| ----------------------------- | -------- | -------------------------- |
| animation - timing - function | 速度曲线 | **steps (数字)：逐帧动画** |

- 核心原理：

1.steps() 逐帧动画 

2.CSS 精灵图

- 制作步骤：


1.准备显示区域

​	盒子尺寸与**一张精灵小图尺寸**相同

2.定义动画

​	**移动背景图（移动距离 = 精灵图宽度）**

3.使用动画

​	**steps(N)，N 与精灵小图个数相同** 

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>精灵动画</title>
  <style>
    div {
      width: 140px;
      height: 140px;
      border: 1px solid #000;
      background: url(./imgs/bg.png);
      animation: run 1s steps(12) infinite;
    }

    div:hover {
      animation-play-state: paused;
    }

    @keyframes run {
      from {
        background-position: 0 0;
      }
      to {
        background-position: -1680px 0;
      }
    }
  </style>
</head>
<body>
  <div></div>
</body>
</html>
```

### 多组动画

```css
animation: 
  动画一,
  动画二,
  ... ...
	动画N
;
```

例如：

```css
animation:
  run 1s steps(12） infinite,
  move 3s linear forwards
;
```

示例：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>多组动画</title>
  <style>
    div {
      width: 140px;
      height: 140px;
      /* border: 1px solid #000; */
      background: url(./imgs/bg.png);
      animation: 
        run 1s steps(12) infinite,
        move 3s forwards;
    }

    div:hover {
      animation-play-state: paused;
    }

    /* 当动画的开始状态样式 跟 盒子默认样式相同，可以省略动画开始状态的代码 */
    @keyframes run {
      /* from {
        background-position: 0 0;
      } */
      to {
        background-position: -1680px 0;
      }
    }

    @keyframes move {
      /* 0% {
        transform: translate(0);
      } */
      100% {
        transform: translate(800px);
      }
    }
  </style>
</head>
<body>
  <div></div>
</body>
</html>
```

---

## 综合案例—全民出游

- HTML结构

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>全名出游季</title>
  <link rel="stylesheet" href="./css/style.css">
</head>
<body>
  <!-- 云 -->
  <div class="cloud">
    <img src="./images/yun1.png" alt="">
    <img src="./images/yun2.png" alt="">
    <img src="./images/yun3.png" alt="">
  </div>
  <!-- 热气球 -->
  <div class="balloon"><img src="./images/san.png" alt=""></div>
  <!-- 标签 -->
  <div class="tags">
    <img src="./images/1.png" alt="">
    <img src="./images/2.png" alt="">
    <img src="./images/3.png" alt="">
    <img src="./images/4.png" alt="">
  </div>
  <!-- 文字 -->
   <div class="text"><img src="./images/font1.png" alt=""></div>
</body>

</html>
```

- css样式

```css
* {
    margin: 0;
    padding: 0;
}

/* 大背景 */
/* 默认状态HTML和body的高度是0，所以导致cover缩放背景图不成功 */
html {
    height: 100%;
}

body {
    height: 100%;
    background: url(../images/f1_1.jpg) no-repeat center 0 / cover;
}

/* 云 */
.cloud img {
    position: absolute;
    left: 50%;
}

.cloud img:nth-child(1) {
    margin-left: -250px;
    top: 20px;
    animation: cloud 1s infinite linear alternate;
}

.cloud img:nth-child(2) {
    margin-left: 400px;
    top: 100px;
    animation: cloud 1s infinite linear alternate 0.4s;
}

.cloud img:nth-child(3) {
    margin-left: -550px;
    top: 200px;
    animation: cloud 1s infinite linear alternate 0.6s;
}

@keyframes move-up-down {
    0% {
        transform: translateY(0);
    }
    100% {
        transform: translateY(-30px);
    }
}

/* 热气球 */
.balloon img {
    position: absolute;
    left: 550px;
    top: 150px;
    animation: move-up-down 1s infinite alternate;
}

/* 标签 */
.tags img {
    position: absolute;
    width: 80px;
}

.tags img:nth-child(1) {
    left: 550px;
    bottom: 50px;
    animation: move-up-down 1s infinite alternate;  
}

.tags img:nth-child(2) {
    left: 750px;
    bottom: 50px;
    animation: move-up-down 1s infinite alternate 0.25s;
}

.tags img:nth-child(3) {
    left: 950px;
    bottom: 50px;
    animation: move-up-down 1s infinite alternate 0.5s;
}

.tags img:nth-child(4) {
    left: 1150px;
    bottom: 50px;
    animation: move-up-down 1s infinite alternate 0.75s;
}


@keyframes cloud {
    0% {
        transform: translate(0);
    }
    100% {
        transform: translate(20px);
    }
}

/* 文字 */
.text img{
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    animation: text 1s;
}

/* 默认 → 小 → 大 → 小 → 默认 */
@keyframes text {
    0% {
        transform: translate(-50%, -50%) scale(1);
    }
    20% {
        transform: translate(-50%, -50%) scale(0.1);
    }
    40% {
        transform: translate(-50%, -50%) scale(1.4);
    }
    70% {
        transform: translate(-50%, -50%) scale(0.8);
    }
    100% {
        transform: translate(-50%, -50%) scale(1);
    }
}
```

