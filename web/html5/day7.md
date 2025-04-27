## 1 项目目录

**网站根目录**是指存放网站的**第一层**文件夹，内部包含当前网站的**所有素材**，包含 HTML、CSS、图片、JavaScript等等。

**study**

- **images** 文件夹：存放**固定使用**的图片素材，例如：logo、样式修饰图等等
- **uploads** 文件夹：存放**非固定使用**的图片素材，例如：商品图、宣传图需要上传的图片
- **css** 文件夹：存放 CSS 文件（**link** 标签引入）
  - **base.css**：基础公共样式，例如：清除默认样式、设置网页基本样式
  - **index.css**：首页 CSS 样式
- **index.html**：首页 HTML 文件

* 首页引入CSS文件

```html
<!-- 顺序要求：先清除再设置 -->
<link rel="stylesheet" href="./css/base.css">
<link rel="stylesheet" href="./css/index.css">
```

---

## 2 版心居中

```css
.wrapper {
  margin: 0 auto;
  width: 1200px;
}

body {
  background-color: #f3f5f7;
}
```

---

## 3 网页制作思路

1. 布局思路：先整体再局部，从外到内，从上到下，从左到右
2. CSS 实现思路
   1. **画盒子**，调整盒子范围 → **宽高背景色**
   2. 调整盒子**位置** → **flex** 布局、**内外边距**
   3. **控制**图片、文字**内容**样式

---

## 4 header 区域-布局

通栏：**宽度**与**浏览器窗口**相同的**盒子**

标签结构：通栏 > 版心 > logo + 导航 + 搜索 + 用户

### HTML结构

```html
<!-- 头部区域 -->
<div class="header">
  <div class="wrapper">
    <!-- logo -->
    <div class="logo">logo</div>
    <!-- 导航 -->
    <div class="nav">导航</div>
    <!-- 搜索 -->
    <div class="search">search</div>
    <!-- 用户 -->
    <div class="user">用户</div>
  </div>
</div>
```

### CSS样式

```css
/* 头部区域 */
.header {
  height: 100px;
  background-color: #fff;
}

.header .wrapper {
  padding-top: 29px;
  display: flex;
}
```

---

## 5 header区域-logo

logo 功能：

* **单击跳转到首页**
* **搜索引擎优化**：**提升**网站百度搜索**排名**

实现方法：

* 标签结构：h1 > a > 网站名称（搜索关键字）

```html
<div class="logo">
  <h1><a href="#">学成在线</a></h1>
</div>
```

* CSS 样式

```css
/* logo */
.logo a {
  display: block;
  width: 195px;
  height: 41px;
  background-image: url(../images/logo.png);
  /* 隐藏文字 */
  font-size: 0;
}
```

---

## 6 header区域-导航

导航功能

- 单击跳转页面

实现方法：

* 标签结构：ul > **li * 3** > a
* 优势：**避免堆砌 a 标签**，网站搜索排名**降级**
* 布局思路
  * li 设置  右侧 margin
  *  a 设置  左右 padding

---

## 7 header区域-搜索布局

实现方法：

- 标签结构：.search > input + a / button

- 布局思路
  - div.search 标签 flex 布局，侧轴居中（垂直居中）
  - input 标签 flex: 1

### HTML结构

```html
<div class="search">
  <input type="text" placeholder="请输入关键词">
  <a href="#"></a>
</div>
```

### CSS样式

```css
.search input {
   flex: 1;
   border: 0;
   background-color: transparent;
   /* 去掉表单控件的焦点框 */
   outline: none;
}

/* ::placeholder 选中就是 placeholder 属性文字样式*/
.search input::placeholder {
  font-size: 14px;
  color: #999;
}

/* 父级是flex布局，子级变弹性盒子：加宽高生效 */
.search a {
  align-self: center;
  width: 16px;
  height: 16px;
  background-image: url(../images/search.png);
}
```

----

## 8 header区域-用户区域

实现方法：

- 标签结构：.user > a > img + span
- 布局技巧：图片、文字垂直方向居中

```css
vertical-align: middle;     /* 行内块和行内垂直方向对齐方式 */
```

### HTML结构

```html
<div class="user">
  <a href="#">
    <img src="./uploads/user.png" alt="">
    <span>播仔学前端</span>
  </a>
</div>
```

### CSS样式

```css
/* 用户 */
.user {
  margin-left: 32px;
  margin-top: 4px;
}

.user img {
  margin-right: 7px;
  /* vertical-align 行内块和行内垂直方向对齐方式 */
  vertical-align: middle;
}

.user span {
  font-size: 16px;
  color: #666;
}
```

---

## 9 banner区域-布局

结构：通栏banner > 版心 > .left + .right

### HTML结构

```html
<div class="banner">
  <div class="wrapper">
    <div class="left">left</div>
    <div class="right">right</div>
  </div>
</div>
```

### CSS样式

```css
/* banner 区域 */
.banner {
  height: 420px;
  background-color: #0092cb;
}

.banner .wrapper {
  display: flex;
  justify-content: space-between;
  height: 420px;
  background-image: url(../uploads/banner.png);
}
```

---

## 10 banner区域-侧导航

实现方法：

- 标签结构：.left > ul > li *9 > a
- 布局思路
  - a 默认状态：背景图为白色右箭头
  - a 鼠标悬停状态：背景图蓝色右箭头

### HTML结构

```html
<div class="left">
  <ul>
    <li><a href="#">前端开发</a></li>
    <li><a href="#">后端开发</a></li>
    <li><a href="#">移动开发</a></li>
    <li><a href="#">人工智能</a></li>
    <li><a href="#">商业预测</a></li>
    <li><a href="#">云计算&大数据</a></li>
    <li><a href="#">运维&测试</a></li>
    <li><a href="#">UI设计</a></li>
    <li><a href="#">产品</a></li>
  </ul>
</div>
```

### CSS样式

```css
/* 侧导航 */
.banner .left {
  padding: 3px 20px;
  width: 191px;
  height: 420px;
  background-color: rgba(0,0,0,0.42);
}

.banner .left a {
  /* 块级：宽度是父级的100% */
  display: block;
  height: 46px;
  background: url(../images/right.png) no-repeat right center;
  line-height: 46px;
  font-size: 16px;
  color: #fff;
}

.banner .left a:hover {
  background-image: url(../images/right-hover.png);
  color: #00a4ff;
}
```

---

## 11 banner区域-课程表布局

实现方法：

- 标签结构：.right > h3 + .content

### HTML布局

```html
<div class="right">
  <h3>我的课程表</h3>
  <div class="content">1</div>
</div>
```

### CSS样式

```css
/* 课程表 */
.banner .right {
  margin-top: 60px;
  width: 218px;
  height: 305px;
  background-color: #209dd5;
  border-radius: 10px;
}

.banner .right h3 {
  margin-left: 14px;
  height: 48px;
  line-height: 48px;
  font-size: 15px;
  color: #fff;
  font-weight: 400;
}

.banner .right .content {
  padding: 14px;
  height: 257px;
  background-color: #fff;
  border-radius: 10px;
}
```

---

## 12 banner区域-课程表内容

### HTML结构

```html
<dl>
  <dt>数据可视化课程</dt>
  <dd><span>正在学习</span>-<strong>echarts使用步骤</strong></dd>
</dl>
<dl>
  <dt>Vue3医疗项目课程  </dt>
  <dd><span>正在学习</span>-<strong>认识组合式API</strong></dd>
</dl>
<dl>
  <dt>React核心技术课程</dt>
  <dd><span>正在学习</span>-<strong>rudex配合TS使用</strong></dd>
</dl>
```

### CSS样式

```css
.banner .right dl {
  margin-bottom: 12px;
  border-bottom: 1px solid #e0e0e0;
}

.banner .right dt {
  margin-bottom: 8px;
  font-size: 14px;
  line-height: 20px;
  font-weight: 700;
}

.banner .right dd {
  margin-bottom: 8px;
  font-size: 12px;
  line-height: 16px;
}

.banner .right dd span {
  color: #00a4ff;
}

.banner .right dd strong {
  color: #7d7d7d;
  font-weight: 400;
}
```

---

## 13 banner区域-全部课程

### HTML结构

```html
<a href="#">全部课程</a>
```

### CSS样式

```css
.banner .right a {
  display: block;
  height: 32px;
  background-color: #00a4ff;
  text-align: center;
  line-height: 32px;
  font-size: 14px;
  color: #fff;
  border-radius: 15px;
}
```

---

## 14 精品推荐

实现方法：

- 标签结构：.recommend > h3 + ul + a.modify
- 布局思路：flex 布局

### HTML结构

```html
<ul>
  <li><a href="#">HTML</a></li>
  <li><a href="#">CSS</a></li>
  <li><a href="#">JavaScript</a></li>
  <li><a href="#">Node.js</a></li>
  <li><a href="#">Ajax</a></li>
  <li><a href="#">Vue2.0</a></li>
  <li><a href="#">Vue3.0</a></li>
  <li><a href="#">TypeScript</a></li>
  <li><a href="#">React</a></li>
</ul>
```

### CSS样式

```css
.recommend h3 {
  font-size: 18px;
  color: #00a4ff;
  font-weight: 400;
}

.recommend ul {
  /* 除去标题和修改兴趣的尺寸，父级剩余尺寸都给ul，实现把修改兴趣挤到最右侧 */
  flex: 1;
  display: flex;
}

.recommend ul li a {
  padding: 0 24px;
  border-right: 1px solid #e0e0e0;
  font-size: 18px;
}

.recommend ul li:last-child a {
  border-right: 0;
}

.recommend .modify {
  font-size: 16px;
  color: #00a4ff;
}
```

---

## 15 精品课程

实现方法：

- 标签结构：.hd + .bd
- 布局思路：盒子模型

### 15.1 精品课程-标题区域

思路：“标题”与“查看全部” 各个区域样式复用

标签结构：.hd > h3 + a.more

CSS 样式：a.more 设置箭头背景图

#### HTML结构

```html
<!-- 精品推荐课程 -->
<div class="course wrapper">
  <!-- 标题 -->
  <div class="hd">
    <h3>精品推荐</h3>
    <a href="#" class="more">查看全部</a>
  </div>
  <!-- 内容 -->
  <div class="bd">1</div>
</div>
```

#### CSS样式

```css
/* 推荐课程 */
.course {
  margin-top: 15px;
}

/* 标题 - 公共类，与其他区域共用 */
.hd {
  display: flex;
  justify-content: space-between;
  height: 60px;
  line-height: 60px;
}

.hd h3 {
  font-size: 21px;
  font-weight: 400;
}

.hd .more {
  padding-right: 20px;
  background: url(../images/more.png) no-repeat right center;
  font-size: 14px;
  color: #999;
}
```

### 15.2 精品课程-内容区域

思路：“课程卡片”各个区域样式复用

标签结构：.bd > ul > li > a

 CSS 样式：flex 布局

#### HTML结构

```html
<ul>
  <li>
    <a href="#">
      <div class="pic"><img src="./uploads/course01.png" alt=""></div>
      <div class="text">
        <h4>JavaScript数据看板项目实战</h4>
        <p><span>高级</span> · <i>1125</i>人在学习</p>
      </div>
    </a>
  </li>
  <li>
    <a href="#">
      <div class="pic"><img src="./uploads/course02.png" alt=""></div>
      <div class="text">
        <h4>Vue.js实战——面经全端项目</h4>
        <p><span>高级</span> · <i>2726</i>人在学习</p>
      </div>
    </a>
  </li>
  <li>
    <a href="#">
      <div class="pic"><img src="./uploads/course03.png" alt=""></div>
      <div class="text">
        <h4>玩转Vue全家桶，iHRM人力资源项目</h4>
        <p><span>高级</span> · <i>9456</i>人在学习</p>
      </div>
    </a>
  </li>
  <li>
    <a href="#">
      <div class="pic"><img src="./uploads/course04.png" alt=""></div>
      <div class="text">
        <h4>Vue.js实战医疗项目——优医问诊</h4>
        <p><span>高级</span> · <i>7192</i>人在学习</p>
      </div>
    </a>
  </li>
  <li>
    <a href="#">
      <div class="pic"><img src="./uploads/course05.png" alt=""></div>
      <div class="text">
        <h4>小程序实战：小兔鲜电商小程序项目</h4>
        <p><span>高级</span> · <i>2703</i>人在学习</p>
      </div>
    </a>
  </li>
  <li>
    <a href="#">
      <div class="pic"><img src="./uploads/course06.png" alt=""></div>
      <div class="text">
        <h4>前端框架Flutter开发实战</h4>
        <p><span>高级</span> · <i>2841</i>人在学习</p>
      </div>
    </a>
  </li>
  <li>
    <a href="#">
      <div class="pic"><img src="./uploads/course07.png" alt=""></div>
      <div class="text">
        <h4>熟练使用React.js——极客园H5项目</h4>
        <p><span>高级</span> · <i>95682</i>人在学习</p>
      </div>
    </a>
  </li>
  <li>
    <a href="#">
      <div class="pic"><img src="./uploads/course08.png" alt=""></div>
      <div class="text">
        <h4>熟练使用React.js——极客园PC端项目</h4>
        <p><span>高级</span> · <i>904</i>人在学习</p>
      </div>
    </a>
  </li>
  <li>
    <a href="#">
      <div class="pic"><img src="./uploads/course09.png" alt=""></div>
      <div class="text">
        <h4>前端实用技术，Fetch API 实战</h4>
        <p><span>高级</span> · <i>1516</i>人在学习</p>
      </div>
    </a>
  </li>
  <li>
    <a href="#">
      <div class="pic"><img src="./uploads/course10.png" alt=""></div>
      <div class="text">
        <h4>前端高级Node.js零基础入门教程</h4>
        <p><span>高级</span> · <i>2766</i>人在学习</p>
      </div>
    </a>
  </li>
</ul>
```

#### CSS样式

```css
.bd li .pic {
  height: 156px;
}

.bd li .text {
  padding: 20px;
  height: 115px;
  background-color: #fff;
}

.bd li .text h4 {
  margin-bottom: 13px;
  height: 40px;
  font-size: 14px;
  line-height: 20px;
  font-weight: 400;
}

.bd li .text p {
  font-size: 14px;
  line-height: 20px;
  color: #999;
}

.bd li .text p span {
  color: #fa6400;
}

.bd li .text p i {
  font-style: normal;
}
```

---

## 16 前端开发工程师区域

整体标签结构：.hd（复用样式） + .bd

标题：

- 标签结构：h3 + ul + a.more
- tab 栏 / 选项卡：菜单个数与内容个数相同

内容：

- 标签结构：.left + .right > .top + .bottom

### HTML结构

```html
<!-- 前端 -->
<div class="wrapper">
  <!-- 标题 -->
  <div class="hd">
    <h3>前端开发工程师</h3>
    <ul>
      <li><a href="#" class="active">热门</a></li>
      <li><a href="#">初级</a></li>
      <li><a href="#">中级</a></li>
      <li><a href="#">高级</a></li>
    </ul>
    <a href="#" class="more">查看全部</a>
  </div>
  <div class="bd">
    <div class="left">
      <img src="./uploads/web_left.png" alt="">
    </div>
    <div class="right">
      <div class="top"><img src="./uploads/web_top.png" alt=""></div>
      <div class="bottom">
        <ul>
          <li>
            <a href="#">
              <div class="pic"><img src="./uploads/web01.png" alt=""></div>
              <div class="text">
                <h4>JS高级javaScript进阶面向对象ES6</h4>
                <p><span>高级</span> · <i>101937</i>人在学习</p>
              </div>
            </a>
          </li>
          <li>
            <a href="#">
              <div class="pic"><img src="./uploads/web02.png" alt=""></div>
              <div class="text">
                <h4>零基础玩转微信小程序</h4>
                <p><span>高级</span> · <i>133781</i>人在学习</p>
              </div>
            </a>
          </li>
          <li>
            <a href="#">
              <div class="pic"><img src="./uploads/web03.png" alt=""></div>
              <div class="text">
                <h4>JavaScript基础——语法解析+项目实战</h4>
                <p><span>高级</span> · <i>8927</i>人在学习</p>
              </div>
            </a>
          </li>
          <li>
            <a href="#">
              <div class="pic"><img src="./uploads/web04.png" alt=""></div>
              <div class="text">
                <h4>前端框架Vue2+Vue3全套视频</h4>
                <p><span>高级</span> · <i>26022</i>人在学习</p>
              </div>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

### CSS样式

```css
/* 前端 */
.hd ul {
  display: flex;
}

.hd li {
  margin-right: 60px;
  font-size: 16px;
}

.hd li .active {
  color: #00a4ff;
}

.bd {
  display: flex;
  justify-content: space-between;
}

.bd .left {
  width: 228px;
  /* background-color: pink; */
}

.bd .right {
  width: 957px;
  /* background-color: pink; */
}

.bd .right .top {
  margin-bottom: 15px;
  height: 100px;
}
```

---

## 17 版权区域（footer）

标签结构：通栏 > 版心 > .left + .right > dl

### HTML结构

```html
<div class="left">
  <a href="#"><img src="./images/logo.png" alt=""></a>
  <p>学成在线致力于普及中国最好的教育它与中国一流大学和机构合作提供在线课程。
    © 2017年XTCG Inc.保留所有权利。-沪ICP备15025210号</p>
  <a href="#" class="download">下载APP</a>
</div>
<div class="right">
  <dl>
    <dt>关于学成网</dt>
    <dd><a href="#">关于</a></dd>
    <dd><a href="#">管理团队</a></dd>
    <dd><a href="#">工作机会</a></dd>
    <dd><a href="#">客户服务</a></dd>
    <dd><a href="#">帮助</a></dd>
  </dl>
  <dl>
    <dt>新手指南</dt>
    <dd><a href="#">如何注册</a></dd>
    <dd><a href="#">如何选课</a></dd>
    <dd><a href="#">如何拿到毕业证</a></dd>
    <dd><a href="#">学分是什么</a></dd>
    <dd><a href="#">考试未通过怎么办</a></dd>
  </dl>
  <dl>
    <dt>合作伙伴</dt>
    <dd><a href="#">合作机构</a></dd>
    <dd><a href="#">合作导师</a></dd>
  </dl>
</div>
```

### CSS样式

```css
.footer .left p {
  margin-top: 24px;
  margin-bottom: 14px;
  font-size: 12px;
  line-height: 17px;
  color: #666;
}

.footer .left .download {
  display: block;
  width: 120px;
  height: 36px;
  border: 1px solid #00a4ff;
  text-align: center;
  line-height: 34px;
  font-size: 16px;
  color: #00a4ff;
}

.footer .right {
  display: flex;
}

.footer .right dl {
  margin-left: 130px;
}

.footer .right dt {
  margin-bottom: 12px;
  font-size: 16px;
  line-height: 23px;
}

.footer .right a {
  font-size: 14px;
  color: #666;
  line-height: 24px;
}
```

---

## 18 完整代码

### HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- 顺序要求：先清除再设置 -->
    <link rel="stylesheet" href="./css/base.css">
    <link rel="stylesheet" href="./css/style.css">
    <title>学成在线</title>
</head>
<body>
    <!-- 头部区域 -->
     <div class="header">
        <div class="wrapper">
            <!-- logo -->
             <div class="logo">
                <h1><a href="#">学成在线</a></h1>
             </div>
            <!-- 导航 -->
             <div class="nav">
                <ul>
                    <li><a href="#" class="active">首页</a></li>
                    <li><a href="#">课程</a></li>
                    <li><a href="#">职业规划</a></li>
                </ul>
             </div>
            <!-- 搜索 -->
             <div class="search">
                <input type="text" placeholder="输入关键词">
                <a href="#"></a>
             </div>
            <!-- 用户 -->
             <div class="user">
                <a href="#">
                    <img src="./学成在线素材-图片/uploads/user.png" alt="">
                    <span>白生学前端</span>
                </a>
             </div>
        </div>
     </div>

     <!-- banner 区域 -->
    <div class="banner">
        <div class="wrapper">
            <div class="left">
                <ul>
                    <li><a href="">前端开发</a></li>
                    <li><a href="">后端开发</a></li>
                    <li><a href="">移动开发</a></li>
                    <li><a href="">人工智能</a></li>
                    <li><a href="">商业预测</a></li>
                    <li><a href="">云计算&大数据</a></li>
                    <li><a href="">运维&测试</a></li>
                    <li><a href="">UI设计</a></li>
                    <li><a href="">产品</a></li>
                </ul>
            </div>
            <div class="right">
                <h3>我的课程表</h3>
                <div class="content">
                    <dl>
                        <dt>数据可视化课程</dt>
                        <dd>
                            <span>正在学习</span>-<strong>echarts使用步骤</strong>
                        </dd>
                    </dl>
                    <dl>
                        <dt>Vue3医疗项目课程</dt>
                        <dd>
                            <span>正在学习</span>-<strong>认识组合式API</strong>
                        </dd>
                    </dl>
                    <dl>
                        <dt>React核心技术课程</dt>
                        <dd>
                            <span>正在学习</span>-<strong>rudex配合TS使用</strong>
                        </dd>
                    </dl>
                    <a href="#">全部课程</a>
                </div>
            </div>
        </div>
    </div>

    <!-- 推荐区域 -->
    <div class="recommend wrapper">
        <h3>精品推荐</h3>
        <ul>
            <li><a href="#">HTML</a></li>
            <li><a href="#">CSS</a></li>
            <li><a href="#">JavaScript</a></li>
            <li><a href="#">Node.js</a></li>
            <li><a href="#">Ajax</a></li>
            <li><a href="#">Vue2.0</a></li>
            <li><a href="#">Vue3.0</a></li>
            <li><a href="#">TypeScript</a></li>
            <li><a href="#">React</a></li>
        </ul>
        <a href="#" class="modify">修改兴趣</a>
    </div>

    <!-- 课程区域 -->
    <div class="course wrapper">
        <!-- 标题 -->
        <div class="hd">
            <h3>精品推荐</h3>
            <a href="#" class="more">查看全部</a>
        </div>

        <!-- 内容 -->
        <div class="bd">
            <ul>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./学成在线素材-图片/uploads/course01.png" alt=""></div>
                        <div class="text">
                            <h4>JavaScript数据看板项目实战</h4>
                            <p><span>高级</span> · <i>1125</i>人在学习</p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./学成在线素材-图片/uploads/course02.png" alt=""></div>
                        <div class="text">
                            <h4>Vue.js实战——面经全端项目</h4>
                            <p><span>高级</span> · <i>2726</i>人在学习</p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./学成在线素材-图片/uploads/course03.png" alt=""></div>
                        <div class="text">
                            <h4>玩转Vue全家桶，iHRM人力资源项目</h4>
                            <p><span>高级</span> · <i>9456</i>人在学习</p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./学成在线素材-图片/uploads/course04.png" alt=""></div>
                        <div class="text">
                            <h4>Vue.js实战医疗项目——优医问诊</h4>
                            <p><span>高级</span> · <i>7192</i>人在学习</p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./学成在线素材-图片/uploads/course05.png" alt=""></div>
                        <div class="text">
                            <h4>小程序实战：小兔鲜电商小程序项目</h4>
                            <p><span>高级</span> · <i>2703</i>人在学习</p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./学成在线素材-图片/uploads/course06.png" alt=""></div>
                        <div class="text">
                            <h4>前端框架Flutter开发实战</h4>
                            <p><span>高级</span> · <i>2841</i>人在学习</p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./学成在线素材-图片/uploads/course07.png" alt=""></div>
                        <div class="text">
                            <h4>熟练使用React.js——极客园H5项目</h4>
                            <p><span>高级</span> · <i>95682</i>人在学习</p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./学成在线素材-图片/uploads/course08.png" alt=""></div>
                        <div class="text">
                            <h4>熟练使用React.js——极客园PC端项目</h4>
                            <p><span>高级</span> · <i>904</i>人在学习</p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./学成在线素材-图片/uploads/course09.png" alt=""></div>
                        <div class="text">
                            <h4>前端实用技术，Fetch API 实战</h4>
                            <p><span>高级</span> · <i>1516</i>人在学习</p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./学成在线素材-图片/uploads/course10.png" alt=""></div>
                        <div class="text">
                            <h4>前端高级Node.js零基础入门教程</h4>
                            <p><span>高级</span> · <i>2766</i>人在学习</p>
                        </div>
                    </a>
                </li>
            </ul>
        </div>
    </div>

    <!-- 前端 -->
    <div class="wrapper">
        <!-- 标题 -->
        <div class="hd">
            <h3>前端工程师</h3>
            <ul>
                <li><a href="#" class="active">热门</a></li>
                <li><a href="#">初级</a></li>
                <li><a href="#">中级</a></li>
                <li><a href="#">高级</a></li>
            </ul>
            <a href="#" class="more">查看全部</a>
        </div>
        <!-- 内容 -->
        <div class="bd">
            <div class="left"><img src="./学成在线素材-图片/uploads/web_left.png" alt=""></div>
            <div class="right">
                <div class="top"><img src="./学成在线素材-图片/uploads/web_top.png" alt=""></div>
                <div class="bottom">
                    <ul>
                        <li>
                            <a href="#">
                                <div class="pic"><img src="./学成在线素材-图片/uploads/web01.png" alt=""></div>
                                <div class="text">
                                    <h4>JS高级javaScript进阶面向对象ES6</h4>
                                    <p><span>高级</span> · <i>101937</i>人在学习</p>
                                </div>
                            </a>
                        </li>
                        <li>
                            <a href="#">
                                <div class="pic"><img src="./学成在线素材-图片/uploads/web02.png" alt=""></div>
                                <div class="text">
                                    <h4>零基础玩转微信小程序</h4>
                                    <p><span>高级</span> · <i>133781</i>人在学习</p>
                                </div>
                            </a>
                        </li>
                        <li>
                            <a href="#">
                                <div class="pic"><img src="./学成在线素材-图片/uploads/web03.png" alt=""></div>
                                <div class="text">
                                    <h4>JavaScript基础——语法解析+项目实战</h4>
                                    <p><span>高级</span> · <i>8927</i>人在学习</p>
                                </div>
                            </a>
                        </li>
                        <li>
                            <a href="#">
                                <div class="pic"><img src="./学成在线素材-图片/uploads/web04.png" alt=""></div>
                                <div class="text">
                                    <h4>前端框架Vue2+Vue3全套视频</h4>
                                    <p><span>高级</span> · <i>26022</i>人在学习</p>
                                </div>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- Python+大数据开发 -->
    <div class="wrapper">
        <!-- 标题 -->
        <div class="hd">
            <h3>Python+大数据开发</h3>
            <ul>
                <li><a href="#" class="active">热门</a></li>
                <li><a href="#">初级</a></li>
                <li><a href="#">中级</a></li>
                <li><a href="#">高级</a></li>
            </ul>
            <a href="#" class="more">查看全部</a>
        </div>
        <!-- 内容 -->
        <div class="bd">
            <div class="left"><img src="./学成在线素材-图片/uploads/python_left.png" alt=""></div>
            <div class="right">
                <div class="top"><img src="./学成在线素材-图片/uploads/python_top.png" alt=""></div>
                <div class="bottom">
                    <ul>
                        <li>
                            <a href="#">
                                <div class="pic"><img src="./学成在线素材-图片/uploads/python01.png" alt=""></div>
                                <div class="text">
                                    <h4>Django视频教程_Django入门视频教程</h4>
                                    <p><span>高级</span> · <i>9037</i>人在学习</p>
                                </div>
                            </a>
                        </li>
                        <li>
                            <a href="#">
                                <div class="pic"><img src="./学成在线素材-图片/uploads/python02.png" alt=""></div>
                                <div class="text">
                                    <h4>python实战项目从0开发一个Django博客系统</h4>
                                    <p><span>高级</span> · <i>988320</i>人在学习</p>
                                </div>
                            </a>
                        </li>
                        <li>
                            <a href="#">
                                <div class="pic"><img src="./学成在线素材-图片/uploads/python03.png" alt=""></div>
                                <div class="text">
                                    <h4>Python+大数据进阶教程6天掌握NoSQL实时计算基础</h4>
                                    <p><span>高级</span> · <i>8863</i>人在学习</p>
                                </div>
                            </a>
                        </li>
                        <li>
                            <a href="#">
                                <div class="pic"><img src="./学成在线素材-图片/uploads/python04.png" alt=""></div>
                                <div class="text">
                                    <h4>数据分析入门教程|300分钟用Matplotlib打造疫情展示地图</h4>
                                    <p><span>高级</span> · <i>54093</i>人在学习</p>
                                </div>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <!-- 人工智能开发 -->
    <div class="ai wrapper">
        <!-- 标题 -->
        <div class="hd">
            <h3>人工智能开发</h3>
            <ul>
                <li><a href="#" class="active">热门</a></li>
                <li><a href="#">初级</a></li>
                <li><a href="#">中级</a></li>
                <li><a href="#">高级</a></li>
            </ul>
            <a href="#" class="more">查看全部</a>
        </div>
        <!-- 内容 -->
        <div class="bd">
            <ul>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./学成在线素材-图片/uploads/ai01.png" alt=""></div>
                        <div class="text">
                            <h4>4天快速入门Python数据挖掘</h4>
                            <p><span>高级</span> · <i>83556</i>人在学习</p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./学成在线素材-图片/uploads/ai02.png" alt=""></div>
                        <div class="text">
                            <h4>计算机视觉入门及案例实战</h4>
                            <p><span>高级</span> · <i>42234</i>人在学习</p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./学成在线素材-图片/uploads/ai03.png" alt=""></div>
                        <div class="text">
                            <h4>AI深度学习自然语言处理NLP零基础入门</h4>
                            <p><span>高级</span> · <i>33848</i>人在学习</p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./学成在线素材-图片/uploads/ai05.png" alt=""></div>
                        <div class="text">
                            <h4>Python进阶课程-Web基础开发</h4>
                            <p><span>高级</span> · <i>61644</i>人在学习</p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./学成在线素材-图片/uploads/ai06.png" alt=""></div>
                        <div class="text">
                            <h4>AI-OpenCV图像处理10小时零基础入门</h4>
                            <p><span>高级</span> · <i>34922</i>人在学习</p>
                        </div>
                    </a>
                </li>  
            </ul>
        </div>
    </div>

    <!-- JavaEE -->
    <div class="javaee wrapper">
        <!-- 标题 -->
        <div class="hd">
            <h3>JavaEE</h3>
            <ul>
                <li><a href="#" class="active">热门</a></li>
                <li><a href="#">初级</a></li>
                <li><a href="#">中级</a></li>
                <li><a href="#">高级</a></li>
            </ul>
            <a href="#" class="more">查看全部</a>
        </div>
        <!-- 内容 -->
        <div class="bd">
            <ul>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./学成在线素材-图片/uploads/ai01.png" alt=""></div>
                        <div class="text">
                            <h4>4天快速入门Python数据挖掘</h4>
                            <p><span>高级</span> · <i>83556</i>人在学习</p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./学成在线素材-图片/uploads/java02.png" alt=""></div>
                        <div class="text">
                            <h4>详细分析LinkedList数据链表的实现原理</h4>
                            <p><span>高级</span> · <i>25855</i>人在学习</p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./学成在线素材-图片/uploads/java03.png" alt=""></div>
                        <div class="text">
                            <h4>全面深入Mysql数据库优化_java进阶教程</h4>
                            <p><span>高级</span> · <i>94577</i>人在学习</p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./学成在线素材-图片/uploads/java04.png" alt=""></div>
                        <div class="text">
                            <h4>全面解剖RocketMQ和项目实战_Java进阶教程</h4>
                            <p><span>高级</span> · <i>47554</i>人在学习</p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./学成在线素材-图片/uploads/java04.png" alt=""></div>
                        <div class="text">
                            <h4>三天系统学习ZooKeeper</h4>
                            <p><span>高级</span> · <i>110510</i>人在学习</p>
                        </div>
                    </a>
                </li>  
            </ul>
        </div>
    </div>

    <!-- 版权区域 -->
    <div class="footer">
        <div class="wrapper">
            <div class="left">
                <a href="#"><img src="./学成在线素材-图片/images/logo.png" alt=""></a>
                <p>学成在线致力于普及中国最好的教育它与中国一流大学和机构合作提供在线课程。 © 2017年XTCG Inc.保留所有权利。-沪ICP备15025210号</p>
                <a href="#" class="download">下载APP</a>
            </div>
            <div class="right">
                <dl>
                    <dt>合作伙伴</dt>
                    <dd><a href="#">关于</a></dd>
                    <dd><a href="#">管理团队</a></dd>
                    <dd><a href="#">工作机会</a></dd>
                    <dd><a href="#">客户服务</a></dd>
                    <dd><a href="#">帮助</a></dd>
                </dl>
                <dl>
                    <dt>合作伙伴</dt>
                    <dd><a href="#">如何注册</a></dd>
                    <dd><a href="#">如何选课</a></dd>
                    <dd><a href="#">如何拿到毕业证</a></dd>
                    <dd><a href="#">学分是什么</a></dd>
                    <dd><a href="#">考试未通过怎么办</a></dd>
                </dl>
                <dl>
                    <dt>合作伙伴</dt>
                    <dd><a href="#">合作机构</a></dd>
                    <dd><a href="#">合作导师</a></dd>
                </dl>
            </div>
        </div>
    </div>
</body>
</html>
```

### CSS

base.css

```css
/* 基础公共样式：清除默认样式 + 设置通用样式 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

li {
  list-style: none;
}

body {
  font: 14px/1.5 "Microsoft Yahei", "Hiragino Sans GB", "Heiti SC", "WenQuanYi Micro Hei", sans-serif;
  color: #333;
}

a {
  color: #333;
  text-decoration: none;
}
```

style.css

```CSS
/* 版心 */
.wrapper {
    margin: 0 auto;
    width: 1200px;
}

body {
    background-color: #f3f5f7;
}

/* 头部区域 */
.header {
    height: 100px;
    background-color: #fff;
}

.header .wrapper {
    display: flex;
    padding-top: 29px;
}

/* logo区域 */
.logo a {
    display: block;
    width: 195px;
    height: 41px;
    background-image: url(../学成在线素材-图片/images/logo.png);
    /* 隐藏文字 */
    font-size: 0;
}

/* 导航区域 */
.nav {
    margin-left: 102px;
}

.nav ul {
    display: flex;
}

.nva li {
    margin-right: 24px;
}

.nav li a {
    display: block;
    padding:6px 8px;
    font-size: 19px;
    line-height: 27px;
}

.nav li .active,
.nav li .active:hover { /* active 类选择器，表示默认选中的a */
    border-bottom: 2px solid #00a4ff;
}


/* 搜索区域 */
.search {
    display: flex;
    margin-left: 64px;
    padding-left: 19px;
    padding-right: 12px;
    width: 412px;
    height: 40px;
    background-color: #f3f5f7;
    border-radius: 20px;
}

.search input {
    flex: 1;
    border: 0 solid #000;
    background-color: transparent;  /* 设置为透明 */
    outline: none;  /*去掉表单控件的焦点框  */
}

.search input::placeholder {    /* ::placeholder 选中的就是placeholder属性文字样式 */
    font-size: 14px;
    color: #999;
}

.search a {     /*父级时flex布局，子级变弹性盒子：加宽高生效*/
    align-self: center;
    width: 16px;
    height: 16px;
    background: url(../学成在线素材-图片/images/search.png) no-repeat;
}

/* 用户区域 */
.user {
    margin-left: 32px;
    margin-top: 4px;
}

.user img {
    margin-right: 7px;
    vertical-align: middle;     /* 行内块和行内垂直方向对齐方式 */
}

.user span {
    font-size: 16px;
    color: #666;
}

/* banner 区域 */
.banner {
    height: 420px;
    background-color: #0092cb;
}

.banner .wrapper {
    display: flex;
    justify-content: space-between;
    height: 420px;
    background: url(../学成在线素材-图片/uploads/banner.png);
}

.banner .left {
    padding: 3px 20px;
    width: 191px;
    height: 420px;
    background-color: rgba(0, 0, 0, 0.4);
}

.banner .left a {
    display: block;
    height: 46px;
    background: url(../学成在线素材-图片/images/right.png) no-repeat right center;
    line-height: 46px;
    font-size: 16px;
    color: #fff;
}

.banner .left a:hover {
    color: #00a4ff;
    background: url(../学成在线素材-图片/images/right-hover.png) no-repeat right center;
}

.banner .right {
    margin-top: 60px;
    width: 218px;
    height: 305px;
    background-color: #209dd5;
    border-radius: 10px;
}

.banner .right h3 {
    margin-left: 14px;
    height: 48px;
    line-height: 48px;
    font-size: 15px;
    font-weight: 400;
    color: #fff;
}

.banner .right .content {
    padding: 14px;
    height: 257px;
    background-color: #fff;
    border-radius: 10px;
}

.banner .right dl {
    margin-bottom: 12px;
    border-bottom: 1px solid #e0e0e0;
}

.banner .right dt {
    margin-bottom: 8px;
    font-size: 14px;
    line-height: 20px;
    font-weight: 700;
}

.banner .right dd {
    margin-bottom: 8px;
    font-size: 12px;
    line-height: 16px;
}

.banner .right dd span {
    color: #00a4ff;
}

.banner .right dd strong {
    color: #7d7d7d ;
    font-weight: 400;
}

.banner .right .content a {
    display: block;
    height: 32px;
    background-color: #00a4ff;
    border-radius: 15px;
    text-align: center;
    line-height: 32px;
    font-size: 14px;
    color: #fff;
}

/* 推荐区域 */
.recommend {
    display: flex;
    height: 60px;
    background-color: #fff;
    box-shadow: 0px 1px 2px 0px rgba(211, 211, 211, 0.5);
    margin-top: 11px;
    padding: 0 20px;
    line-height: 60px;
}

.recommend h3 {
    font-size: 18px;
    color: #00a4ff;
    font-weight: 400;
}

.recommend ul {
    display: flex;
    /* 除去标题和修改兴趣的尺寸，父级剩余尺寸都给ul，实现把修改兴趣挤到最右侧 */
    flex: 1;
}

.recommend ul li a{
    padding: 0 24px;
    border-right: 1px solid #e0e0e0;
    font-size: 18px;
}

.recommend ul li:last-child a {
    border-right: 0 solid #000;
}

.recommend .modify {
    font-size: 16px;
    color: #00a4ff;
}

/* 课程区域 */
.course {
    margin-top: 15px;
}

/* 标题 - 公共类，与其他区域共用 */
.hd {   
    display: flex;
    justify-content: space-between;
    height: 60px;
    line-height: 60px;
}

.hd h3 {
    font-size: 21px;
    font-weight: 400;
}

.hd .more { 
    font-size: 14px;
    color: #999;
    background: url(../学成在线素材-图片/images/more.png) no-repeat center right;
    padding-right: 20px;
}

/* 课程内容-公共类 */
.bd ul {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

.bd li {
    margin-bottom: 14px;
    width: 228px;
    height: 271px;
    background-color: pink;
}

.bd li .pic {
    height: 156px;
}

.bd li .text {
    padding: 20px;
    height: 115px;
    background-color: #fff;
}

.bd li .text h4 {
    height: 40px;
    margin-bottom: 13px;
    font-weight: 400;
    font-size: 14px;
    line-height: 20px;
}

.bd li .text p {
    line-height: 20px;
    font-size: 14px;
    color: #999;
}

.bd li .text span {
    color: #fa6400;
}

.bd li .text p i {
    font-style: normal;
}

/* 前端 */
.hd ul {
    display: flex;
}

.hd ul li {
    margin-right: 60px;
    font-size: 16px;
}

.hd li .active {
    color: #00a4ff;
}

.bd {
    display: flex;
    justify-content: space-between;
}

.bd .left {
    width: 228px;
}

.bd .right {
    width: 957px;
}

.bd .right .top {
    margin-bottom: 15px;
    height: 100px;
}


/* 人工智能开发 */
.ai .bd {
    flex-direction: column;
}

/* JavaEE */
.javaee .bd {
    flex-direction: column;
}

/* 版权 */
.footer {
    margin-top: 60px;
    padding-top: 60px;
    height: 273px;
    background-color: #fff;
}

.footer .wrapper {
    display: flex;
    justify-content: space-between;
}

.footer .left {
    width: 440px;
}

.footer .left p {
    margin-top: 24px;
    margin-bottom: 14px;
    font-size: 12px;
    line-height: 17px;
    color: #666;
}

.footer .left .download {
    display: block;
    width: 120px;
    height: 36px;
    border: 1px solid #00a4ff;
    text-align: center;
    line-height: 34px;
    font-size: 16px;
    color: #00a4ff;
}

.footer .right {
    display: flex;
}

.footer .right dl {
    margin-left: 130px;
}

.footer .right dt {
    margin-bottom: 12px;
    font-size: 16px;
    line-height: 23px;
}

.footer .right a {
    font-size: 14px;
    color: #666;
    line-height: 24px;
}
```

