## 01-banner

结构：通栏 > 版心 >  轮播图（ul.pic）+ 侧导航（subnav > ul）+ 圆点指示器（ol） 

布局：定位（子绝父相）

圆点结构：ol > li > i（li 是大圆，i 是小圆）

### 轮播图

#### HTML结构

```html
<!-- banner -->
  <div class="banner">
    <div class="wrapper">
      <!-- 图片 -->
      <ul class="pic">
        <li><a href="#"><img src="./uploads/banner1.png" alt=""></a></li>
        <li><a href="#"><img src="./uploads/banner1.png" alt=""></a></li>
        <li><a href="#"><img src="./uploads/banner1.png" alt=""></a></li>
      </ul>
    </div>
</div>
```

#### CSS样式

```css
/* banner */
.banner {
  height: 500px;
  background-color: #F5F5F5;
}

.banner .wrapper {
  position: relative;
  height: 500px;
  background-color: pink;
  overflow: hidden;
}

/* 图片 */
.banner .pic {
  display: flex;
  /* flex 布局，父级宽度不够，子级被挤小，不想挤小，增大父级尺寸 */
  width: 3720px;
}
```

### 侧导航

#### HTML结构

```html
<!-- 侧导航 ul -->
<div class="subnav">
  <ul>
    <li>
      <div><a href="#" class="classify">生鲜</a><a href="#">水果</a><a href="#">蔬菜</a></div>
      <span class="iconfont icon-arrow-right-bold"></span>
    </li>
    <li>
      <div><a href="#" class="classify">美食</a><a href="#">面点</a><a href="#">干果</a></div>
      <span class="iconfont icon-arrow-right-bold"></span>
    </li>
    <li>
      <div><a href="#" class="classify">餐厨</a><a href="#">数码产品</a></div>
      <span class="iconfont icon-arrow-right-bold"></span>
    </li>
    <li>
      <div><a href="#" class="classify">电器</a><a href="#">床品</a><a href="#">四件套</a><a href="#">被枕</a></div>
      <span class="iconfont icon-arrow-right-bold"></span>
    </li>
    <li>
      <div><a href="#" class="classify">居家</a><a href="#">奶粉</a><a href="#">玩具</a><a href="#">辅食</a></div>
      <span class="iconfont icon-arrow-right-bold"></span>
    </li>
    <li>
      <div><a href="#" class="classify">洗护</a><a href="#">洗发</a><a href="#">洗护</a><a href="#">美妆</a></div>
      <span class="iconfont icon-arrow-right-bold"></span>
    </li>
    <li>
      <div><a href="#" class="classify">孕婴</a><a href="#">奶粉</a><a href="#">玩具</a></div>
      <span class="iconfont icon-arrow-right-bold"></span>
    </li>
    <li>
      <div><a href="#" class="classify">服饰</a><a href="#">女装</a><a href="#">男装</a></div>
      <span class="iconfont icon-arrow-right-bold"></span>
    </li>
    <li>
      <div><a href="#" class="classify">杂货</a><a href="#">户外</a><a href="#">图书</a></div>
      <span class="iconfont icon-arrow-right-bold"></span>
    </li>
    <li>
      <div><a href="#" class="classify">品牌</a><a href="#">品牌制造</a></div>
      <span class="iconfont icon-arrow-right-bold"></span>
    </li>
    
  </ul>
</div>
```

#### CSS样式

```css
/* 侧导航 */
.subnav {
  position: absolute;
  left: 0;
  top: 0;
  width: 250px;
  height: 500px;
  background-color: rgba(0,0,0,0.42);
}

.subnav li {
  display: flex;
  justify-content: space-between;
  padding-left: 30px;
  padding-right: 12px;
  height: 50px;
  /* background-color: pink; */
  line-height: 50px;
  color: #fff;

  cursor: pointer;
}

/* a所有都是小字，分类是大字 */
.subnav li a {
  margin-right: 5px;
  font-size: 14px;
  color: #fff;
}

.subnav li .classify {
  margin-right: 14px;
  font-size: 16px;
}

.subnav li .iconfont {
  font-size: 14px;
}

.subnav li:hover {
  background-color: #00BE9A;
}
```

### 圆点指示器

#### HTML结构

```html
<!-- 圆点指示器 -->
<ol>
  <li class="current"><i></i></li>
  <li><i></i></li>
  <li><i></i></li>
</ol>
```

#### CSS样式

```css
/* 圆点指示器 */
.banner ol {
  position: absolute;
  bottom: 17px;
  right: 16px;
  display: flex;
}

.banner ol li {
  margin-left: 8px;
  width: 22px;
  height: 22px;
  /* background-color: pink; */
  border-radius: 50%;
  cursor: pointer;
}

.banner ol i {
  display: block;
  margin: 4px;
  width: 14px;
  height: 14px;
  background-color: rgba(255,255,255,0.5);
  border-radius: 50%;
}

/* 选中：li半透明； i白色 */
.banner ol .current {
  background-color: rgba(255,255,255,0.5);
}

.banner ol .current i {
  background-color: #fff;
}
```

---

## 02-新鲜好物

结构：标题（title） + 内容（bd） 

提示：多区域样式共用（考虑公共样式）

### 标题

#### HTML结构

```html
<!-- 新鲜好物 -->
<div class="goods wrapper">
  <!-- 标题 -->
  <div class="title">
    <div class="left">
      <h3>新鲜好物</h3>
      <p>新鲜出炉 品质靠谱</p>
    </div>
    <div class="right">
      <a href="#" class="more">查看全部<span class="iconfont icon-arrow-right-bold"></span></a>
    </div>
  </div>
</div>
```

#### CSS样式

```css
/* 新鲜好物 */
/* 标题 -- 公共样式 */
.title {
  display: flex;
  justify-content: space-between;
  margin-top: 40px;
  margin-bottom: 30px;
  height: 42px;
  /* background-color: pink; */
}

.title .left {
  display: flex;
}

.title .left h3 {
  margin-right: 35px;
  font-size: 30px;
}

.title .left p {
  align-self: flex-end;
  color: #A1A1A1;
}

.title .right .more {
  line-height: 42px;
  color: #A1A1A1;
}

.title .right .more .iconfont {
  margin-left: 10px;
}
```

### 内容

#### HTML结构

```html
<!-- 内容 -->
<div class="bd">
  <ul>
    <li>
      <a href="#">
        <div class="pic"><img src="./uploads/goods1.png" alt=""></div>
        <div class="txt">
          <h4>KN95级莫兰迪色防护口罩</h4>
          <p>¥<span>79</span></p>
        </div>
      </a>
    </li>
    <li>
      <a href="#">
        <div class="pic"><img src="./uploads/goods2.png" alt=""></div>
        <div class="txt">
          <h4>紫檀外独板三层普洱茶盒</h4>
          <p>¥<span>566</span></p>
        </div>
      </a>
    </li>
    <li>
      <a href="#">
        <div class="pic"><img src="./uploads/goods3.png" alt=""></div>
        <div class="txt">
          <h4>法拉蒙高颜值记事本可定制</h4>
          <p>¥<span>58</span></p>
        </div>
      </a>
    </li>
    <li>
      <a href="#">
        <div class="pic"><img src="./uploads/goods4.png" alt=""></div>
        <div class="txt">
          <h4>科技布布艺沙发</h4>
          <p>¥<span>3579</span></p>
        </div>
      </a>
    </li> 
  </ul>
</div>
```

#### CSS样式

```css
/* 好物内容 -- 公共样式 */
.bd ul {
  display: flex;
  justify-content: space-between;
}

.bd li {
  width: 304px;
  height: 404px;
  background-color: #EEF9F4;
}

.bd li .pic {
  width: 304px;
  height: 304px;
}

.bd li .txt {
  text-align: center;
}

.bd li h4 {
  margin-top: 18px;
  margin-bottom: 8px;
  font-size: 20px;
}

.goods .bd p {
  font-size: 18px;
  color: #AA2113;
}

.goods .bd p span {
  margin-left: 3px;
  font-size: 22px;
}
```

---

## 03-人气推荐

### HTML结构

```html
<!-- 人气推荐 -->
<div class="recommend wrapper">
  <!-- 标题 -->
  <div class="title">
    <div class="left">
      <h3>人气推荐</h3>
      <p>人气爆款 不容错过</p>
    </div>
  </div>
  <!-- 内容 -->
  <div class="bd">
    <ul>
      <li>
        <a href="#">
          <div class="pic"><img src="./uploads/recommend1.png" alt=""></div>
          <div class="txt">
            <h4>特惠推荐</h4>
            <p>我猜得到 你的需要</p>
          </div>
        </a>
      </li>
      <li>
        <a href="#">
          <div class="pic"><img src="./uploads/recommend2.png" alt=""></div>
          <div class="txt">
            <h4>爆款推荐</h4>
            <p>人气好物推荐</p>
          </div>
        </a>
      </li>
      <li>
        <a href="#">
          <div class="pic"><img src="./uploads/recommend3.png" alt=""></div>
          <div class="txt">
            <h4>节日礼品一站买全</h4>
            <p>编辑尽心整理推荐</p>
          </div>
        </a>
      </li>
      <li>
        <a href="#">
          <div class="pic"><img src="./uploads/recommend4.png" alt=""></div>
          <div class="txt">
            <h4>鲜花园艺</h4>
            <p>给生活增加仪式感</p>
          </div>
        </a>
      </li>
      
    </ul>
  </div>
</div>
```

### CSS样式

```css
/* 人气推荐 */
.recommend .bd li {
  background-color: #fff;
}

.recommend .bd p {
  color: #A1A1A1;
}
```

---

## 04-热门品牌

标题结构：左侧（left）+ 右侧箭头（显示在标题外部：定位）

### 布局

#### HTML结构

```html
<!-- 热门品牌 -->
<div class="brand">
  <div class="wrapper">
    <!-- 标题 -->
    <div class="title">
      <div class="left">
        <h3>热门品牌</h3>
        <p>国际经典 品质认证</p>
      </div>

      <div class="button">1</div>
    </div>
  </div>
</div>
```

#### CSS样式

```css
/* 热门品牌 */
.brand {
  margin-top: 60px;
  height: 468px;
  background-color: #F5F5F5;
}

.brand .wrapper {
  overflow: hidden;
  height: 468px;
  /* background-color: pink; */
}

.brand .title {
  position: relative;
  margin-bottom: 40px;
}

.brand .button {
  position: absolute;
  right: 0;
  bottom: -25px;

  /* 让a在一行显示，宽高生效 */
  display: flex;
}
```

### 内容

#### HTML结构

```html
<div class="button">
  <a href="#" class="prev">
    <i class="iconfont icon-arrow-left-bold"></i>
  </a>
  <a href="#" class="next">
    <i class="iconfont icon-arrow-right-bold"></i>
  </a>
</div>




<!-- 内容 -->
<div class="bd">
  <ul>
    <li><a href="#"><img src="./uploads/hot1.png" alt=""></a></li>
    <li><a href="#"><img src="./uploads/hot2.png" alt=""></a></li>
    <li><a href="#"><img src="./uploads/hot3.png" alt=""></a></li>
    <li><a href="#"><img src="./uploads/hot4.png" alt=""></a></li>
    <li><a href="#"><img src="./uploads/hot5.png" alt=""></a></li>
  </ul>
</div>
```

#### CSS样式

```css
.brand .button a {
  margin-left: 12px;
  width: 20px;
  height: 20px;
  text-align: center;
  line-height: 20px;
  color: #fff;
}

.brand .button .prev {
  background-color: #ddd;
}

.brand .button .next {
  background-color: #00BE9A;
}

.brand .bd li {
  width: 244px;
  height: 306px;
}
```

---

## 05-生鲜

标题结构：右侧（right）> 菜单（ul）+ 查看全部

内容（content）： .left + .right > 商品（ul）

### 标题

#### HTML结构

```html
<!-- 生鲜 -->
<div class="fresh wrapper">
  <!-- 标题 -->
  <div class="title">
    <div class="left">
      <h3>生鲜</h3>
    </div>
    <div class="right">
      <ul>
        <li><a href="#" class="active">热门</a></li>
        <li><a href="#">蔬菜</a></li>
        <li><a href="#">肉禽蛋</a></li>
        <li><a href="#">水果</a></li>
        <li><a href="#">海鲜</a></li>
        <li><a href="#">零食</a></li>
        <li><a href="#">饮料</a></li>
      </ul>
      <a href="#" class="more">查看全部<span class="iconfont icon-arrow-right-bold"></span></a>
    </div>
  </div>
</div>
```

#### CSS样式

```css
/* 生鲜 */
.fresh .title {
  margin-top: 60px;
  margin-bottom: 20px;
}

.title .right {
  display: flex;
}

.title .right ul {
  display: flex;
  margin-top: 10px;
  margin-right: 58px;
}

.title .right ul a {
  display: block;
  margin-left: 6px;
  padding: 0 7px;
  height: 20px;
  /* background-color: pink; */
  line-height: 20px;
}

.title .right ul .active {
  background-color: #00BE9A;
  color: #fff;
}
```

### 内容布局

#### HTML结构

```html
<!-- 内容 -->
<div class="content">
  <div class="left">
    <a href="#"><img src="./uploads/fresh_left.png" alt=""></a>
  </div>
  <div class="right">
    <ul>
      <li>1</li>
      <li>2</li>
      <li>3</li>
      <li>4</li>
      <li>5</li>
      <li>6</li>
      <li>7</li>
      <li>8</li>
    </ul>
  </div>
</div>
```

#### CSS样式

```css
/* 生鲜内容 */
.content {
  display: flex;
  justify-content: space-between;
}

.content .left {
  width: 248px;
  height: 610px;
  /* background-color: pink; */
}

.content .right {
  width: 968px;
  height: 610px;
  /* background-color: pink; */
}

.content .right ul {
  display: flex;
  flex-wrap: wrap;
}

.content .right li {
  position: relative;
  padding: 10px 21px 0;
  width: 242px;
  height: 305px;
  border: 2px solid #fff;

  /* 为了隐藏绿色cover */
  overflow: hidden;
}
```

### 产品内容

### HTML结构

```html
<ul>
  <li>
    <a href="#">
      <div class="pic"><img src="./uploads/fresh1.png" alt=""></div>
      <div class="txt">
        <div class="info">
          <h4>双味千层，手抓饼烤肉组合</h4>
          <p>240g/袋 4片装</p>
          <p>加热即食</p>
        </div>
        <p class="price">¥<span>89.99</span></p>
      </div>
    </a>
  </li>
  <li>
    <a href="#">
      <div class="pic"><img src="./uploads/fresh2.png" alt=""></div>
      <div class="txt">
        <div class="info">
          <h4>云南甘蔗慢熬红糖馒头</h4>
          <p>220g/袋 5个装</p>
          <p>加热即食</p>
        </div>
        <p class="price">¥<span>9.00</span></p>
      </div>
    </a>
  </li>
  <li>
    <a href="#">
      <div class="pic"><img src="./uploads/fresh3.png" alt=""></div>
      <div class="txt">
        <div class="info">
          <h4>日式风味小圆饼</h4>
          <p>圆形【海盐味】</p>
          <p>糖果零食</p>
        </div>
        <p class="price">¥<span>588.00</span></p>
      </div>
    </a>
  </li>
  <li>
    <a href="#">
      <div class="pic"><img src="./uploads/fresh4.png" alt=""></div>
      <div class="txt">
        <div class="info">
          <h4>全麦奶油浓香小面包</h4>
          <p>50g*12袋</p>
          <p>美味西点</p>
        </div>
        <p class="price">¥<span>69.00</span></p>
      </div>
    </a>
  </li>
  <li>
    <a href="#">
      <div class="pic"><img src="./uploads/fresh5.png" alt=""></div>
      <div class="txt">
        <div class="info">
          <h4>秘制外皮五福摩提大福点心</h4>
          <p>150g/盒</p>
          <p>美味西点</p>
        </div>
        <p class="price">¥<span>39.99</span></p>
      </div>
    </a>
  </li>
  <li>
    <a href="#">
      <div class="pic"><img src="./uploads/fresh6.png" alt=""></div>
      <div class="txt">
        <div class="info">
          <h4>水果面膜韩国蜂蜜柚子茶</h4>
          <p>560g/瓶</p>
          <p>冲调饮品</p>
        </div>
        <p class="price">¥<span>39.99</span></p>
      </div>
    </a>
  </li>
  <li>
    <a href="#">
      <div class="pic"><img src="./uploads/fresh7.png" alt=""></div>
      <div class="txt">
        <div class="info">
          <h4>浓情比利时巧克力礼盒装</h4>
          <p>205克/盒</p>
          <p>糖果零食</p>
        </div>
        <p class="price">¥<span>120.00</span></p>
      </div>
    </a>
  </li>
  <li>
    <a href="#">
      <div class="pic"><img src="./uploads/fresh8.png" alt=""></div>
      <div class="txt">
        <div class="info">
          <h4>抹茶奶油小蛋糕礼盒装</h4>
          <p>220克/盒</p>
          <p>美味西点</p>
        </div>
        <p class="price">¥<span>60.00</span></p>
      </div>
    </a>
  </li>
</ul>
```

#### CSS样式

```css
/* 产品内容 */
.content .pic {
  width: 200px;
  height: 180px;
}

.content .info {
  margin-top: 14px;
  margin-bottom: 5px;
  height: 60px;
  line-height: 19px;
}

.content .price {
  color: #AF2F22;
}

.content .price span {
  margin-left: 5px;
  font-size: 22px;
}
```

### 过渡效果

#### HTML结构

```html
<div class="cover">
  <p>找相似</p>
  <p></p>
  <p>发现更多宝贝<span class="iconfont icon-arrow-right-bold"></span></p>
</div>
```

#### CSS样式

```css
/* 产品底部绿色区域 */
.content li .cover {
  position: absolute;
  left: 0;
  /* bottom: 0; */
  bottom: -86px;
  padding-top: 15px;
  width: 242px;
  height: 84px;
  background-color: #00BE9A;
  text-align: center;
  color: #fff;
  transition: all 0.5s;
}

.content .cover p:nth-child(1) {
  font-size: 18px;
}

.content .cover p:nth-child(2) {
  margin: 3px auto 6px;
  width: 120px;
  height: 1px;
  background-color: rgba(255,255,255,0.11);
}

.content .cover p:nth-child(3) {
  font-size: 13px;
} 

.content .cover p:nth-child(3) .iconfont {
  font-size: 14px;
}

/* 鼠标悬停到li，显示cover，改变位置 */
.content .right li:hover .cover {
  bottom: 0;
}

.content .right li:hover {
  border: 2px solid #00BE9A;
}
```

---

## 06-最新专题

### 布局

#### HTML结构

```html
<!-- 最新专题 -->
<div class="topic wrapper">
  <div class="title">
    <div class="left">
      <h3>最新专题</h3>
    </div>
    <div class="right">
      <a href="#" class="more">查看全部<span class="iconfont icon-arrow-right-bold"></span></a>
    </div>
  </div>
  <div class="topic-bd">
    <ul>
      <li>1</li>
      <li>2</li>
      <li>3</li>
    </ul>
  </div>
</div>
```

#### CSS样式

```css
/* 最新专题 */
.topic {
  margin-bottom: 40px;
}

.topic .title {
  margin-top: 100px;
}

.topic-bd ul {
  display: flex;
  justify-content: space-between;
}

.topic-bd li {
  width: 405px;
  height: 355px;
  background-color: pink;
}
```

### 内容

#### HTML结构

```html
<ul>
  <li>
    <a href="#">
      <div class="pic">
        <img src="./uploads/topic1.png" alt="">
      </div>
      <div class="txt">
        <div class="left">
          <p>
            <i class="iconfont icon-favorites-fill"></i>
            <span>1220</span>
          </p>
          <p>
            <i class="iconfont icon-browse"></i>
            <span>1800</span>
          </p>
        </div>
        <div class="right">
          <p>
            <i class="iconfont icon-comment"></i>
            <span>246</span>
          </p>
        </div>
      </div>
    </a>
  </li>
  <li>
    <a href="#">
      <div class="pic">
        <img src="./uploads/topic2.png" alt="">
      </div>
      <div class="txt">
        <div class="left">
          <p>
            <i class="iconfont icon-favorites-fill"></i>
            <span>1220</span>
          </p>
          <p>
            <i class="iconfont icon-browse"></i>
            <span>1800</span>
          </p>
        </div>
        <div class="right">
          <p>
            <i class="iconfont icon-comment"></i>
            <span>246</span>
          </p>
        </div>
      </div>
    </a>
  </li>
  <li>
    <a href="#">
      <div class="pic">
        <img src="./uploads/topic3.png" alt="">
      </div>
      <div class="txt">
        <div class="left">
          <p>
            <i class="iconfont icon-favorites-fill"></i>
            <span>1220</span>
          </p>
          <p>
            <i class="iconfont icon-browse"></i>
            <span>1800</span>
          </p>
        </div>
        <div class="right">
          <p>
            <i class="iconfont icon-comment"></i>
            <span>246</span>
          </p>
        </div>
      </div>
    </a>
  </li>
</ul>
```

#### CSS样式

```css
.topic-bd ul {
  display: flex;
  justify-content: space-between;
}

.topic-bd li {
  width: 405px;
  height: 355px;
  background-color: pink;
}

.topic-bd .pic {
  position: relative;
  width: 405px;
  height: 288px;
}

.topic-bd .txt {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 15px;
  width: 405px;
  height: 67px;
  /* background-color: skyblue; */
  font-size: 14px;
  color: #666;
}

.topic-bd .txt .left {
  display: flex;
}

.topic-bd .txt .left p {
  margin-right: 20px;
}

.topic-bd .txt .left p:nth-child(1) i {
  color: #AA2113;
}
```

### 定位文字

#### HTML结构

```html
<div class="pic">
  <img src="./uploads/topic2.png" alt="">
  <!-- 定位区域 -->
  <div class="cover">
    <div class="left">
      <h4>吃这些美食才不算辜负自己</h4>
      <p>餐厨起居洗护好物</p>
    </div>
    <div class="right">￥<span>29.9</span><span>起</span></div>
  </div>
</div>
```

#### CSS样式

```css
/* 定位区域 - 文字 */
.topic-bd .cover {
  position: absolute;
  left: 0;
  bottom: 0;

  display: flex;
  justify-content: space-between;
  align-items: center;

  padding: 0 15px;
  width: 405px;
  height: 90px;
  background-image: linear-gradient(180deg, rgba(137,137,137,0.00) 0%, rgba(0,0,0,0.90) 100%);
}

.topic-bd .cover .left {
  color: #fff;
}

.topic-bd .cover .left h4 {
  margin-bottom: 6px;
  font-size: 20px;
}

.topic-bd .cover .right {
  padding: 0 7px;
  height: 25px;
  background-color: #fff;
  color: #AA2113;
  font-size: 15px;
}

.topic-bd .cover .right span {
  font-size: 18px;
}
```

---

## 07-完整代码

### index.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="小兔鲜儿官网，致力于打造全球最大的食品、生鲜电商购物平台。">
    <meta name="keywords" content="小兔鲜儿,食品,生鲜,服装,家电,电商,购物">
    <title>小兔鲜儿-新鲜、惠民、快捷！</title>
    <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="./iconfont/iconfont.css">
    <link rel="stylesheet" href="./css/base.css">
    <link rel="stylesheet" href="./css/common.css">
    <link rel="stylesheet" href="./css/index.css">
</head>

<body>
    <!-- 快捷导航 -->
    <div class="shortcut">
        <div class="wrapper">
            <ul>
                <li><a href="" class="login">请先登录</a></li>
                <li><a href="">免费注册</a></li>
                <li><a href="">我的订单</a></li>
                <li><a href="">会员中心</a></li>
                <li><a href="">帮助中心</a></li>
                <li><a href="">在线客服</a></li>
                <li><a href=""><span class="iconfont icon-mobile-phone"></span>手机版</a></li>
            </ul>
        </div>
    </div>

    <!-- 头部 -->
    <div class="header wrapper">
        <!-- logo -->
        <div class="logo">
            <h1><a href="#">小兔鲜儿</a></h1>
        </div>
        <!-- 导航 -->
        <div class="nav">
            <ul>
                <li><a href="#">首页</a></li>
                <li><a href="#">生鲜</a></li>
                <li><a href="#">美食</a></li>
                <li><a href="#">餐厨</a></li>
                <li><a href="#">电器</a></li>
                <li><a href="#">居家</a></li>
                <li><a href="#">洗护</a></li>
                <li><a href="#">孕婴</a></li>
                <li><a href="#">服装</a></li>
            </ul>
        </div>
        <!-- 搜索 -->
        <div class="search">
            <span class="iconfont icon-search"></span>
            <input type="text" placeholder="搜一搜">
        </div>
        <!-- 购物车 -->
        <div class="cart">
            <span class="iconfont icon-cart-full"></span>
            <i>2</i>
        </div>
    </div>

    <!-- banner -->
    <div class="banner">
        <div class="wrapper">
            <!-- 图片 -->
            <ul class="pic">
                <li><a href="#"><img src="./uploads/banner1.png" alt=""></a></li>
                <li><a href="#"><img src="./uploads/banner1.png" alt=""></a></li>
                <li><a href="#"><img src="./uploads/banner1.png" alt=""></a></li>
            </ul>
            <!-- 侧导航 -->
            <div class="subnav">
                <ul>
                    <li>
                        <div><a href="#" class="classify">生鲜</a><a href="#">水果</a><a href="#">蔬菜</a></div>
                        <span class="iconfont icon-arrow-right-bold"></span>
                    </li>
                    <li>
                        <div><a href="#" class="classify">美食</a><a href="#">面点</a><a href="#">干果</a></div>
                        <span class="iconfont icon-arrow-right-bold"></span>
                    </li>
                    <li>
                        <div><a href="#" class="classify">餐厨</a><a href="#">数码产品</a></div>
                        <span class="iconfont icon-arrow-right-bold"></span>
                    </li>
                    <li>
                        <div><a href="#" class="classify">电器</a><a href="#">床品</a><a href="#">四件套</a><a href="#">被枕</a>
                        </div>
                        <span class="iconfont icon-arrow-right-bold"></span>
                    </li>
                    <li>
                        <div><a href="#" class="classify">居家</a><a href="#">奶粉</a><a href="#">玩具</a><a href="#">辅食</a>
                        </div>
                        <span class="iconfont icon-arrow-right-bold"></span>
                    </li>
                    <li>
                        <div><a href="#" class="classify">洗护</a><a href="#">洗发</a><a href="#">洗护</a><a href="#">美妆</a>
                        </div>
                        <span class="iconfont icon-arrow-right-bold"></span>
                    </li>
                    <li>
                        <div><a href="#" class="classify">孕婴</a><a href="#">奶粉</a><a href="#">玩具</a></div>
                        <span class="iconfont icon-arrow-right-bold"></span>
                    </li>
                    <li>
                        <div><a href="#" class="classify">服饰</a><a href="#">女装</a><a href="#">男装</a></div>
                        <span class="iconfont icon-arrow-right-bold"></span>
                    </li>
                    <li>
                        <div><a href="#" class="classify">杂货</a><a href="#">户外</a><a href="#">图书</a></div>
                        <span class="iconfont icon-arrow-right-bold"></span>
                    </li>
                    <li>
                        <div><a href="#" class="classify">品牌</a><a href="#">品牌制造</a></div>
                        <span class="iconfont icon-arrow-right-bold"></span>
                    </li>
                </ul>
            </div>
            <!-- 圆点指示器 -->
            <ol>
                <li class="current"><i></i></li>
                <li><i></i></li>
                <li><i></i></li>
            </ol>
        </div>
    </div>

    <!-- 新鲜好物 -->
    <div class="goods wrapper">
        <!-- 标题 -->
        <div class="title">
            <div class="left">
                <h3>新鲜好物</h3>
                <p>新鲜出炉 品质靠谱</p>
            </div>
            <div class="right">
                <a href="#" class="more">查看全部<span class="iconfont icon-arrow-right-bold"></span></a>
            </div>
        </div>
        <!-- 内容 -->
        <div class="bd">
            <ul>
                <li><a href="#">
                        <div class="pic"><img src="./uploads/goods1.png" alt=""></div>
                        <div class="txt">
                            <h4>KN95级莫兰迪色防护口罩</h4>
                            <p>¥ <span>79</span></p>
                        </div>
                    </a></li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./uploads/goods2.png" alt=""></div>
                        <div class="txt">
                            <h4>紫檀外独板三层普洱茶盒</h4>
                            <p>¥<span>566</span></p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./uploads/goods3.png" alt=""></div>
                        <div class="txt">
                            <h4>法拉蒙高颜值记事本可定制</h4>
                            <p>¥<span>58</span></p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./uploads/goods4.png" alt=""></div>
                        <div class="txt">
                            <h4>科技布布艺沙发</h4>
                            <p>¥<span>3579</span></p>
                        </div>
                    </a>
                </li>
            </ul>
        </div>
    </div>

    <!-- 人气推荐 -->
    <div class="recommend wrapper">
        <!-- 标题 -->
        <div class="title">
            <div class="left">
                <h3>人气推荐</h3>
                <p>人气爆款 不容错过</p>
            </div>
        </div>
        <!-- 内容 -->
        <div class="bd">
            <ul>
                <li><a href="#">
                        <div class="pic"><img src="./uploads/recommend1.png" alt=""></div>
                        <div class="txt">
                            <h4>KN95级莫兰迪色防护口罩</h4>
                            <p>我猜得到 你的需要</p>
                        </div>
                    </a></li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./uploads/recommend2.png" alt=""></div>
                        <div class="txt">
                            <h4>爆款推荐</h4>
                            <p>人气好物推荐</p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./uploads/recommend3.png" alt=""></div>
                        <div class="txt">
                            <h4>节日礼品一站买全</h4>
                            <p>编辑尽心整理推荐</p>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic"><img src="./uploads/recommend4.png" alt=""></div>
                        <div class="txt">
                            <h4>鲜花园艺</h4>
                            <p>给生活增加仪式感</p>
                        </div>
                    </a>
                </li>
            </ul>
        </div>
    </div>

    <!-- 热门品牌 -->
    <div class="brand">
        <div class="wrapper">
            <!-- 标题 -->
            <div class="title">
                <div class="left">
                    <h3>热门品牌</h3>
                    <p>国际经典 品质认证</p>
                </div>
                <div class="button">
                    <a href="#" class="prev">
                        <span class="iconfont icon-arrow-left-bold"></span>
                    </a>
                    <a href="#" class="next">
                        <span class="iconfont icon-arrow-right-bold"></span>
                    </a>
                </div>
            </div>
            <!-- 内容 -->
            <div class="bd">
                <ul>
                    <li><a href="#"><img src="./uploads/hot1.png" alt=""></a></li>
                    <li><a href="#"><img src="./uploads/hot2.png" alt=""></a></li>
                    <li><a href="#"><img src="./uploads/hot3.png" alt=""></a></li>
                    <li><a href="#"><img src="./uploads/hot4.png" alt=""></a></li>
                    <li><a href="#"><img src="./uploads/hot5.png" alt=""></a></li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 生鲜 -->
    <div class="fresh wrapper">
        <!-- 标题 -->
        <div class="title">
            <div class="left">
                <h3>生鲜</h3>
            </div>
            <div class="right">
                <ul>
                    <li><a href="#" class="active">热门</a></li>
                    <li><a href="#">热门</a></li>
                    <li><a href="#">热门</a></li>
                    <li><a href="#">热门</a></li>
                    <li><a href="#">热门</a></li>
                    <li><a href="#">热门</a></li>
                    <li><a href="#">热门</a></li>
                </ul>
                <a href="#" class="more">查看全部<span class="iconfont icon-arrow-right-bold"></span></a>
            </div>
        </div>
        <!-- 内容 -->
        <div class="content">
            <div class="left">
                <a href="#"><img src="./uploads/fresh_left.png" alt=""></a>
            </div>
            <div class="right">
                <ul>
                    <li>
                        <a href="#">
                            <div class="pic"><img src="./uploads/fresh1.png" alt=""></div>
                            <div class="txt">
                                <div class="info">
                                    <h4>双味千层，手抓饼烤肉组合</h4>
                                    <p>240g/袋 4片装</p>
                                    <p>加热即食</p>
                                </div>
                                <p class="price">¥ <span>89.99</span></p>
                            </div>
                        </a>
                        <div class="cover">
                            <p>找相似</p>
                            <p></p>
                            <p>发现更多宝贝<span class="iconfont icon-arrow-right-bold"></span></p>
                        </div>
                    </li>
                    <li>
                        <a href="#">
                            <div class="pic"><img src="./uploads/fresh2.png" alt=""></div>
                            <div class="txt">
                                <div class="info">
                                    <h4>云南甘蔗慢熬红糖馒头</h4>
                                    <p>220g/袋 5个装</p>
                                    <p>加热即食</p>
                                </div>
                                <p class="price">¥<span>9.00</span></p>
                            </div>
                        </a>
                        <div class="cover">
                            <p>找相似</p>
                            <p></p>
                            <p>发现更多宝贝<span class="iconfont icon-arrow-right-bold"></span></p>
                        </div>
                    </li>
                    <li>
                        <a href="#">
                            <div class="pic"><img src="./uploads/fresh3.png" alt=""></div>
                            <div class="txt">
                                <div class="info">
                                    <h4>日式风味小圆饼</h4>
                                    <p>圆形【海盐味】</p>
                                    <p>糖果零食</p>
                                </div>
                                <p class="price">¥<span>588.00</span></p>
                            </div>
                        </a>
                        <div class="cover">
                            <p>找相似</p>
                            <p></p>
                            <p>发现更多宝贝<span class="iconfont icon-arrow-right-bold"></span></p>
                        </div>
                    </li>
                    <li>
                        <a href="#">
                            <div class="pic"><img src="./uploads/fresh4.png" alt=""></div>
                            <div class="txt">
                                <div class="info">
                                    <h4>全麦奶油浓香小面包</h4>
                                    <p>50g*12袋</p>
                                    <p>美味西点</p>
                                </div>
                                <p class="price">¥<span>69.00</span></p>
                            </div>
                        </a>
                        <div class="cover">
                            <p>找相似</p>
                            <p></p>
                            <p>发现更多宝贝<span class="iconfont icon-arrow-right-bold"></span></p>
                        </div>
                    </li>
                    <li>
                        <a href="#">
                            <div class="pic"><img src="./uploads/fresh5.png" alt=""></div>
                            <div class="txt">
                                <div class="info">
                                    <h4>秘制外皮五福摩提大福点心</h4>
                                    <p>150g/盒</p>
                                    <p>美味西点</p>
                                </div>
                                <p class="price">¥<span>39.99</span></p>
                            </div>
                        </a>
                        <div class="cover">
                            <p>找相似</p>
                            <p></p>
                            <p>发现更多宝贝<span class="iconfont icon-arrow-right-bold"></span></p>
                        </div>
                    </li>
                    <li>
                        <a href="#">
                            <div class="pic"><img src="./uploads/fresh6.png" alt=""></div>
                            <div class="txt">
                                <div class="info">
                                    <h4>水果面膜韩国蜂蜜柚子茶</h4>
                                    <p>560g/瓶</p>
                                    <p>冲调饮品</p>
                                </div>
                                <p class="price">¥<span>39.99</span></p>
                            </div>
                        </a>
                        <div class="cover">
                            <p>找相似</p>
                            <p></p>
                            <p>发现更多宝贝<span class="iconfont icon-arrow-right-bold"></span></p>
                        </div>
                    </li>
                    <li>
                        <a href="#">
                            <div class="pic"><img src="./uploads/fresh7.png" alt=""></div>
                            <div class="txt">
                                <div class="info">
                                    <h4>浓情比利时巧克力礼盒装</h4>
                                    <p>205克/盒</p>
                                    <p>糖果零食</p>
                                </div>
                                <p class="price">¥<span>120.00</span></p>
                            </div>
                        </a>
                        <div class="cover">
                            <p>找相似</p>
                            <p></p>
                            <p>发现更多宝贝<span class="iconfont icon-arrow-right-bold"></span></p>
                        </div>
                    </li>
                    <li>
                        <a href="#">
                            <div class="pic"><img src="./uploads/fresh8.png" alt=""></div>
                            <div class="txt">
                                <div class="info">
                                    <h4>抹茶奶油小蛋糕礼盒装</h4>
                                    <p>220克/盒</p>
                                    <p>美味西点</p>
                                </div>
                                <p class="price">¥<span>60.00</span></p>
                            </div>
                        </a>
                        <div class="cover">
                            <p>找相似</p>
                            <p></p>
                            <p>发现更多宝贝<span class="iconfont icon-arrow-right-bold"></span></p>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </div>

    <!-- 最新专题 -->
    <div class="topic wrapper">
        <!-- 标题 -->
        <div class="title">
            <div class="left">
                <h3>最新专题</h3>
            </div>
            <div class="right">
                <a href="#" class="more">查看全部<span class="iconfont icon-arrow-right-bold"></span></a>
            </div>
        </div>
        <!-- 内容 -->
        <div class="topic-bd">
            <ul>
                <li>
                    <a href="#">
                        <div class="pic">
                            <img src="./uploads/topic1.png" alt="">
                            <!-- 定位区域 -->
                            <div class="cover">
                                <div class="left">
                                    <h4>吃这些美食才不算辜负自己</h4>
                                    <p>餐厨起居洗护好物</p>
                                </div>
                                <div class="right">
                                    ￥<span>29.9<span>起</span></span>
                                </div>
                            </div>
                        </div>
                        <div class="txt">
                            <div class="left">
                                <p>
                                    <i class="iconfont icon-favorites-fill"></i>
                                    <span>1220</span>
                                </p>
                                <p>
                                    <i class="iconfont icon-browse"></i>
                                    <span>180</span>
                                </p>
                            </div>
                            <div class="right">
                                <p>
                                    <i class="iconfont icon-comment"></i>
                                    <span>246</span>
                                </p>
                            </div>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic">
                            <img src="./uploads/topic2.png" alt="">
                        </div>
                        <div class="txt">
                            <div class="left">
                                <p>
                                    <i class="iconfont icon-favorites-fill"></i>
                                    <span>1220</span>
                                </p>
                                <p>
                                    <i class="iconfont icon-browse"></i>
                                    <span>1800</span>
                                </p>
                            </div>
                            <div class="right">
                                <p>
                                    <i class="iconfont icon-comment"></i>
                                    <span>246</span>
                                </p>
                            </div>
                        </div>
                    </a>
                </li>
                <li>
                    <a href="#">
                        <div class="pic">
                            <img src="./uploads/topic3.png" alt="">
                        </div>
                        <div class="txt">
                            <div class="left">
                                <p>
                                    <i class="iconfont icon-favorites-fill"></i>
                                    <span>1220</span>
                                </p>
                                <p>
                                    <i class="iconfont icon-browse"></i>
                                    <span>1800</span>
                                </p>
                            </div>
                            <div class="right">
                                <p>
                                    <i class="iconfont icon-comment"></i>
                                    <span>246</span>
                                </p>
                            </div>
                        </div>
                    </a>
                </li>
            </ul>
        </div>
    </div>

    <!-- 底部 -->
    <div class="footer">
        <div class="wrapper">
            <!-- 服务 -->
            <div class="service">
                <ul>
                    <li>
                        <h5></h5>
                        <p>价格亲民</p>
                    </li>
                    <li>
                        <h5></h5>
                        <p>物流快捷</p>
                    </li>
                    <li>
                        <h5></h5>
                        <p>品质新鲜</p>
                    </li>
                    <li>
                        <h5></h5>
                        <p>售后无忧</p>
                    </li>
                </ul>
            </div>
            <!-- 帮助中心 -->
            <div class="help">
                <div class="left">
                    <dl>
                        <dt>购物指南</dt>
                        <dd><a href="#">购物流程</a></dd>
                        <dd><a href="#">支付方式</a></dd>
                        <dd><a href="#">售后规则</a></dd>
                    </dl>
                    <dl>
                        <dt>配送方式</dt>
                        <dd><a href="#">配送运费</a></dd>
                        <dd><a href="#">配送范围</a></dd>
                        <dd><a href="#">配送时间</a></dd>
                    </dl>
                    <dl>
                        <dt>关于我们</dt>
                        <dd><a href="#">平台规则</a></dd>
                        <dd><a href="#">联系我们</a></dd>
                        <dd><a href="#">问题反馈</a></dd>
                    </dl>
                    <dl>
                        <dt>售后服务</dt>
                        <dd><a href="#">售后政策</a></dd>
                        <dd><a href="#">退款说明</a></dd>
                        <dd><a href="#">取消订单</a></dd>
                    </dl>
                    <dl>
                        <dt>服务热线</dt>
                        <dd><a href="#">在线客服<span class="iconfont icon-customer-service"></span></a></dd>
                        <dd><a href="#">客服电话 400-0000-000</a></dd>
                        <dd><a href="#">工作时间 周一至周日 8:00-18:00</a></dd>
                    </dl>
                </div>
                <div class="right">
                    <ul>
                        <li>
                            <div class="pic"><img src="./images/wechat.png" alt=""></div>
                            <p>微信公众号</p>
                        </li>
                        <li>
                            <div class="pic"><img src="./images/app.png" alt=""></div>
                            <p>APP下载二维码</p>
                        </li>
                    </ul>
                </div>
            </div>
            <!-- 版权 -->
            <div class="copyright">
                <p><a href="#">关于我们</a> |
                    <a href="#">帮助中心</a> |
                    <a href="#">售后服务</a> |
                    <a href="#">配送与验收</a> |
                    <a href="#">商务合作</a> |
                    <a href="#">搜索推荐</a> |
                    <a href="#">友情链接</a>
                </p>
                <p>CopyRight © 小兔鲜</p>
            </div>
        </div>
    </div>
</body>

</html>
```

### base.css

```css
/* 去除常见标签默认的 margin 和 padding */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* 设置网页统一的字体大小、行高、字体系列相关属性 */
body {
  font: 16px/1.5  "Microsoft Yahei",
    "Hiragino Sans GB", "Heiti SC", "WenQuanYi Micro Hei", sans-serif;
  color: #333;
}

/* 去除列表默认样式 */
ul,
ol {
  list-style: none;
}

/* 去除默认的倾斜效果 */
em,
i {
  font-style: normal;
}

/* 去除a标签默认下划线，并设置默认文字颜色 */
a {
  text-decoration: none;
  color: #333;
}

/* 设置img的垂直对齐方式为居中对齐，去除img默认下间隙 */
img {
  width: 100%;
  height: 100%;
  vertical-align: middle;
}

/* 去除input默认样式 */
input {
  border: none;
  outline: none;
  color: #333;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  font-weight: 400;
}
```

### common.css

```css
/* 头尾各个页面相同的样式 */
.wrapper {
    width: 1240px;
    margin: 0 auto;
}

/* 快捷导航 */
.shortcut {
    height: 52px;
    background-color: #333;
}

.shortcut .wrapper {
    display: flex;
    justify-content: flex-end;
    height: 52px;
}

.shortcut ul {
    display: flex;
    line-height: 52px;
}

.shortcut li a {
    padding: 0 15px;
    border-right: 1px solid #999;
    font-size: 14px;
    color: #fff;
}

.shortcut li:last-child a {
    border-right: 0 solid #000;
}

.shortcut li .iconfont {
    color: #fff;
    margin-right: 4px;
    vertical-align: middle;
}

.shortcut li .login {
    color: #5EB69C;
}

/* 头部 */
.header {
    display: flex;
    height: 88px;
    /* background-color: pink; */
    margin-top: 22px;
    margin-bottom: 22px;
}

/* logo */
.logo {
    margin-right: 40px;
    width: 200px;
    height: 88px;
}

.logo a {
    display: block;
    width: 200px;
    height: 88px;
    background: url(../images/logo.png);
    font-size: 0;
}

/* 导航 */
.nav {
    margin-top: 33px;
    margin-right: 28px;
}

.nav ul {
    display: flex;
}

.nav ul li {
    margin-right: 47px;
}

.nav li a {
    padding-bottom: 10px;
}

.nav li a:hover {
    border-bottom: 2px solid #5EB69C;
    color: #5EB69C;
}

/* 搜索 */
.search {
    display: flex;
    width: 170px;
    height: 34px;
    border-bottom: 2px solid #F4F4F4;
    margin-top: 33px;
    margin-left: 45px;
}

.search .iconfont {
    margin-right: 8px;
    font-size: 20px;
    color: #ccc;
    vertical-align: middle;
}

.search input {
    flex: 1;
    width: 0;   /* 重置默认宽度 */
    margin-bottom: 10px;
}

.search input::placeholder {
    color: #ccc;
}

/* 购物车 */
.cart {
    margin-top: 32px;
    position: relative;
}


.cart .iconfont {
    font-size: 24px;
}

.cart i {
    position: absolute;
    top: 1px;
    /* right 定位右对齐：如果文字多了，向左撑开，可能盖住其他的内容 */
    /* right: 1px; */
     /* left 定位左对齐：文字多了，向右撑开 */
    left: 16px;
    padding: 0 6px;
    background-color: #E26237;
    height: 15px;
    border-radius: 7.5px;
    color: #FFFEFE;
    font-size: 14px;
    line-height: 15px;
}

/* 底部 */
.footer {
    height: 580px;
    background-color: #F5F5F5;
}

/* 服务 */
.footer .service {
    padding: 60px 0;
    height: 178px;
    border-bottom: 1px solid #E8E8E8;
}

.service ul {
    display: flex;
    justify-content: space-evenly;
}

.service li {
    display: flex;
    width: 190px;
    height: 58px;
}

.service li h5 {
    width: 58px;
    height: 58px;
    background: url(../images/sprite.png);
    margin-right: 20px;
}

.service li:nth-child(2) h5 {
    background: url(../images/sprite.png);
    background-position: 0 -58px;
}

.service li:nth-child(3) h5 {
    background: url(../images/sprite.png);
    background-position: 0 -116px;
}

.service li:nth-child(4) h5 {
    background: url(../images/sprite.png);
    background-position: 0 -174px;
}

.service li p {
    font-size: 27px;
    line-height: 58px;
}

/* 帮助中心 */
.footer .help {
    display: flex;
    justify-content: space-between;
    padding-top: 60px;
    height: 300px;
}

/* left */
.help .left {
    display: flex;
}

.help .left dl {
    margin-right: 84px;
}

.help .left dl:last-child {
    margin-right: 0;
}

.help .left dt {
    margin-bottom: 30px;
    font-size: 18px;
}

.help .left dd {
    margin-bottom: 10px;
}

.help .left dd a {
    color: #969696;
}

.help .left .iconfont {
    color: #5EB69C;
}

.help .right ul {
    display: flex;
}

.help .right li:first-child {
    margin-right: 55px;
}

.help .right .pic {
    width: 120px;
    height: 120px;
    margin-bottom: 10px;
}

.help .right p {
    color: #969696;
    text-align: center;
}

/* 版权 */
.copyright {
    text-align: center;
}

.copyright p {
    margin-bottom: 10px;
    color: #A1A1A1;
}

.copyright p a {
    margin: 0 10px;
    color: #A1A1A1;
}
```

### index.css

```css
/* 首页内容的样式 */
/* banner */
.banner {
    height: 500px;
    background-color: #F5F5F5;
}

.banner .wrapper {
    height: 500px;
    background-color: pink;
    overflow: hidden;
    position: relative;
}

/* 图片 */
.banner .pic {
    display: flex;
    /* flex 布局，父级宽度不够，子级被挤小，不想挤小，增大父级尺寸 */
    width: 3720px;
}

/* 侧导航 */
.subnav {
    width: 250px;
    height: 500px;
    background-color: rgba(0, 0, 0, 0.42);
    position: absolute;
    left: 0;
    top: 0;
}

.subnav li {
    display: flex;
    justify-content: space-between;
    height: 50px;
    line-height: 50px;
    padding-left: 30px;
    padding-right: 12px;
    color: #fff;
    cursor: pointer;
}

/* a所有都是小字，分类是大字 */
.subnav li a {
    font-size: 14px;
    margin-right: 5px;
    color: #fff;
}

.subnav li .classify {
    font-size: 16px;
    margin-right: 14px;
}

.subnav li .iconfont {
    font-size: 14px;
}

.subnav li:hover {
    background-color: #00BE9A;
}

/* 圆点指示器 */
.banner ol {
    display: flex;
    position: absolute;
    bottom: 17px;
    right: 16px;
}

.banner ol li {
    width: 22px;
    height: 22px;
    margin-left: 8px;
    border-radius: 50%;
    cursor: pointer;
}

.banner ol li i {
    display: block;
    margin: 4px;
    width: 14px;
    height: 14px;
    background-color: rgba(255, 255, 255, 0.5);
    border-radius: 50%;
}

/* 选中 */
.banner ol .current {
    background-color: rgba(255, 255, 255, 0.5);
}

.banner ol .current i {
    background-color: #fff;
}

/* 新鲜好物 */
/* 标题 -- 公共样式 */
.title {
    display: flex;
    justify-content: space-between;
    height: 42px;
    margin-top: 40px;
    margin-bottom: 30px;
}

.title .left {
    display: flex;
}

.title .left h3 {
    margin-right: 35px;
    font-size: 30px;
}

.title .left p {
    align-self: flex-end;
    color: #A1A1A1;
}

.title .right .more {
    line-height: 42px;
    color: #A1A1A1;
}

.title .right .iconfont {
    margin-left: 10px;
}

/* 好物内容 -- 公共样式 */
.bd ul {
    display: flex;
    justify-content: space-between;
}

.bd ul li {
    width: 304px;
    height: 404px;
    background-color: #EEF9F4;
}

.bd li .pic {
    width: 304px;
    height: 304px;
}

.bd li .txt {
    text-align: center;
}

.bd li .txt h4 {
    margin-top: 18px;
    margin-bottom: 8px;
    font-size: 20px;
}

.goods .bd p {
    color: #AA2113;
    font-size: 18px;
}

.goods .bd p span {
    margin-left: 3px;
    font-size: 22px;
}

/* 人气推荐 */
.recommend .bd li {
    background-color: #fff;
}

.recommend .bd p {
    color: #A1A1A1;
}

/* 热门品牌 */
.brand {
    margin-top: 60px;
    height: 468px;
    background-color: #f5f5f5;
}

.brand .wrapper {
    overflow: hidden;
    height: 468px;
}

.brand .title {
    position: relative;
    margin-bottom: 40px;
}

.brand .button {
    display: flex;
    position: absolute;
    right: 0;
    bottom: -25px;
}

.brand .button a {
    width: 20px;
    height: 20px;
    margin-left: 12px;
    text-align: center;
    line-height: 20px;
    color: #fff;
}

.brand .button .prev {
    background-color: #ddd;
}

.brand .button .next {
    background-color: #00BE9A;
}

.brand .bd li {
    width: 244px;
    height: 306px;
}

/* 生鲜 */
.fresh .title {
    margin-top: 60px;
    margin-bottom: 20px;
}

.title .right {
    display: flex;
}

.title .right ul {
    display: flex;
    margin-top: 10px;
    margin-right: 58px;
}

.title .right ul a {
    display: block;
    margin-left: 6px;
    height: 20px;
    padding: 0 7px;
    line-height: 20px;
}

.title .right ul .active {
    background-color: #00BE9A;
    color: #fff;
}

/* 生鲜内容 */
.content {
    display: flex;
    justify-content: space-between;
}

.content .left {
    width: 248px;
    height: 610px;
}

.content .right {
    width: 968px;
    height: 610px;
}

.content .right ul {
    display: flex;
    flex-wrap: wrap;
}

.content .right li {
    position: relative;
    padding: 10px 21px 0;
    width: 242px;
    height: 305px;
    border: 2px solid #fff;
    overflow: hidden;
}

/* 产品内容 */
.content .right .pic {
    width: 200px;
    height: 180px;
}

.content .right .info {
    height: 60px;
    margin-top: 14px;
    margin-bottom: 5px;
    line-height: 19px;
}

.content .right .price {
    color: #AF2F22;
}

.content .right .price span {
    font-size: 22px;
    margin-left: 3px;
}

/* 产品底部绿色区域 */
.content li .cover {
    position: absolute;
    left: 0;
    bottom: -86px;
    width: 242px;
    height: 84px;
    background-color: #00BE9A;
    text-align: center;
    padding-top: 15px;
    color: #fff;
    transition: all 0.5s;
}

.content li .cover p:first-child {
    font-size: 18px;
}

.content li .cover p:nth-child(2) {
    margin: 3px auto 6px;
    width: 120px;
    height: 1px;
    background-color: rgba(255, 255, 255, 0.11);
}

.content li .cover p:nth-child(3) {
    font-size: 13px;
}

.content li .cover .iconfont {
    font-size: 13px;
}

/* 鼠标悬停到li，显示cover，改变位置 */
.content .right li:hover .cover {
    bottom: 0;
}

.content .right li:hover {
    border: 2px solid #00BE9A;
}

/* 最新专题 */
.topic {
    margin-bottom: 40px;
}

.topic .title {
    margin-top: 100px;
}

.topic-bd ul {
    display: flex;
    justify-content: space-between;
}

.topic-bd li {
    width: 405px;
    height: 355px;
}

.topic-bd .pic {
    position: relative;
    width: 405px;
    height: 288px;
}

.topic-bd .txt {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 15px;
    width: 405px;
    height: 67px;
    font-size: 14px;
    color: #666666;
}

.topic-bd .txt .left {
    display: flex;
}

.topic-bd .txt .left p {
    margin-right: 20px;
}

.topic-bd .txt .left p:first-child .iconfont {
    color: #AA2113;
}

/* 定位区域 */
.topic-bd .cover {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 15px;
    position: absolute;
    left: 0;
    bottom: 0;
    width: 405px;
    height: 90px;
    background-image: linear-gradient(180deg, rgba(137, 137, 137, 0.00) 0%, rgba(0, 0, 0, 0.90) 100%);
}

.topic-bd .cover .left {
    color: #fff;
}

.topic-bd .cover .left h4 {
    font-size: 20px;
    margin-bottom: 6px;
}

.topic-bd .cover .right {
    padding: 0 7px;
    height: 25px;
    background-color: #fff;
    color: #AA2113;
    font-size: 15px;
    line-height: 25px;
}

.topic-bd .cover .right span {
    font-size: 18px;
}
```

