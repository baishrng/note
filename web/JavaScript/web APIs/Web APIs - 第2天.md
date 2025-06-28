## 事件监听（绑定）

- 什么是事件？

事件是在编程时系统内发生的**动作**或者发生的事情

比如用户在网页上**单击**一个按钮

- **语法：**

```JS
元素对象.addEventListener('事件类型', 要执行的函数)
```

- **事件监听三要素：**

**事件源：**  那个dom元素被事件触发了，要获取dom元素 

**事件类型：** 用什么方式触发，比如鼠标单击 click、鼠标经过 mouseover 等

**事件调用的函数：** 要做什么事

- 例如

```JS
<button class="btn">按钮</button>
<script>
    const btn = document.querySelector('.btn')
    // 修改元素样式
    btn.addEventListener('click', function () {
        alert('点击了~')
    })
</script>
```

> 注意：
>
> 1. 事件类型要**加引号**
> 2. 函数是点击之后再去执行，每 次点击都会执行一次

- **事件监听版本**

DOM L0：事件源.on事件 = function() { }

DOM L2：事件源.addEventListener(事件， 事件处理函数)

区别：on方式会被覆盖，`addEventListener`方式可绑定多次，拥有事件更多特性，推荐使用

- **示例1：**点击关闭顶部广告

需求：点击关闭之后，顶部关闭

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .box {
            position: relative;
            width: 1000px;
            height: 200px;
            background-color: pink;
            margin: 100px auto;
            text-align: center;
            font-size: 50px;
            line-height: 200px;
            font-weight: 700;
        }

        .box1 {
            position: absolute;
            right: 20px;
            top: 10px;
            width: 20px;
            height: 20px;
            background-color: skyblue;
            text-align: center;
            line-height: 20px;
            font-size: 16px;
            cursor: pointer;
        }
    </style>
</head>

<body>
    <div class="box">
        我是广告
        <div class="box1">X</div>
    </div>
    <script>
        const x = document.querySelector('.box1')
        x.addEventListener('click', function () {
            document.querySelector('.box').style.display = 'none'
        })
    </script>
</body>

</html>
```

- **示例2：**随机点名案例

业务分析：

点击开始按钮随机抽取数组的一个数据，放到页面中

点击结束按钮删除数组当前抽取的一个数据

当抽取到最后一个数据的时候，两个按钮同时禁用（写点开始里面，只剩最后一个数据不用抽了 ）

核心：利用定时器快速展示，停止定时器结束展示

```JS
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
        }

        h2 {
            text-align: center;
        }

        .box {
            width: 600px;
            margin: 50px auto;
            display: flex;
            font-size: 25px;
            line-height: 40px;
        }

        .qs {

            width: 450px;
            height: 40px;
            color: red;

        }

        .btns {
            text-align: center;
        }

        .btns button {
            width: 120px;
            height: 35px;
            margin: 0 50px;
        }
    </style>
</head>

<body>
    <h2>随机点名</h2>
    <div class="box">
        <span>名字是：</span>
        <div class="qs">这里显示姓名</div>
    </div>
    <div class="btns">
        <button class="start">开始</button>
        <button class="end">结束</button>
    </div>

    <script>
        // 数据数组
        const arr = ['马超', '黄忠', '赵云', '关羽', '张飞']
        let random
        let timer
        const start = document.querySelector('.btns .start')
        start.addEventListener('click', function () {
            timer = setInterval(function () {
                random = Math.floor(Math.random() * arr.length)
                const qs = document.querySelector('.box .qs')
                qs.innerText = arr[random]
            }, 200)
        })

        const end = document.querySelector('.btns .end')
        end.addEventListener('click', function () {
            clearInterval(timer)
            arr.splice(random, 1)
            if (arr.length === 1) {
                start.disabled = true
                this.disabled = true
            }
            console.log(arr)
        })
    </script>
</body>

</html>
```

---

## 事件类型

将众多的事件类型分类可分为：鼠标事件、键盘事件、表单事件、焦点事件等。

### 鼠标事件

- `click `  鼠标点击
- `mouseenter` 鼠标经过
- `mouseleave`  鼠标离开

**示例：**轮播图点击切换

需求：当点击左右的按钮，可以切换轮播图

分析：

右侧按钮点击，变量++，如果大于等于8，则复原0

左侧按钮点击，变量--，如果小于0，则复原最后一张

鼠标经过暂停定时器

鼠标离开开启定时器

```JS
前面的代码见前面的轮播图示例
<script>
  // 1. 初始数据
  const sliderData = [
    { url: './images/slider01.jpg', title: '对人类来说会不会太超前了？', color: 'rgb(100, 67, 68)' },
    { url: './images/slider02.jpg', title: '开启剑与雪的黑暗传说！', color: 'rgb(43, 35, 26)' },
    { url: './images/slider03.jpg', title: '真正的jo厨出现了！', color: 'rgb(36, 31, 33)' },
    { url: './images/slider04.jpg', title: '李玉刚：让世界通过B站看到东方大国文化', color: 'rgb(139, 98, 66)' },
    { url: './images/slider05.jpg', title: '快来分享你的寒假日常吧~', color: 'rgb(67, 90, 92)' },
    { url: './images/slider06.jpg', title: '哔哩哔哩小年YEAH', color: 'rgb(166, 131, 143)' },
    { url: './images/slider07.jpg', title: '一站式解决你的电脑配置问题！！！', color: 'rgb(53, 29, 25)' },
    { url: './images/slider08.jpg', title: '谁不想和小猫咪贴贴呢！', color: 'rgb(99, 72, 114)' },
  ]

  // 函数：切换图片
  function changeImg(i = 0) {
    document.querySelector('.slider-indicator .active').classList.remove('active')
    const img = document.querySelector('.slider-wrapper img')
    const p = document.querySelector('.slider-footer p')
    const footer = document.querySelector('.slider-footer')
    img.src = sliderData[i].url
    p.innerText = sliderData[i].title
    footer.style.backgroundColor = sliderData[i].color
    document.querySelector(`.slider-indicator li:nth-child(${i + 1})`).classList.add('active')
  }

  let i = 0   // 当前展示的图片序号

  // 鼠标经过暂停定时器
  const slider = document.querySelector('.slider')
  slider.addEventListener('mouseenter', function () {
    clearInterval(timerId)
  })

  // 鼠标离开开启定时器
  slider.addEventListener('mouseleave', function () {
    clearInterval(timerId)
    timerId = setInterval(function () {
      i = (i + 1) % sliderData.length
      changeImg(i)
    }, 1000)
  })

  // 右侧按钮添加事件
  const prev = document.querySelector('.toggle .prev')
  prev.addEventListener('click', function () {
    i = (i - 1 + sliderData.length) % sliderData.length
    changeImg(i)
  })

  // 左侧按钮添加事件
  const next = document.querySelector('.toggle .next')
  next.addEventListener('click', function () {
    i = (i + 1) % sliderData.length
    changeImg(i)
  })

  // 轮播效果
  let timerId = setInterval(function () {
    next.click()    // 调用 next 的点击事件
  }, 1000)
</script>
```

### 键盘事件

- `keydown`   键盘按下触发

- `keyup`   键盘抬起触发

### 焦点事件

主要是与表单的输入有关

- `focus`  获得焦点

- `blur` 失去焦点

**示例：**小米搜索框案例

需求：当表单得到焦点，显示下拉菜单，失去焦点隐藏下来菜单

分析：

开始下拉菜单要进行隐藏

表单获得焦点 focus，则显示下拉菜单，并且文本框变色（添加类）

表单失去焦点，反向操作

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        ul {

            list-style: none;
        }

        .mi {
            position: relative;
            width: 223px;
            margin: 100px auto;
        }

        .mi input {
            width: 223px;
            height: 48px;
            padding: 0 10px;
            font-size: 14px;
            line-height: 48px;
            border: 1px solid #e0e0e0;
            outline: none;
        }

        .mi .search {
            border: 1px solid #ff6700;
        }

        .result-list {
            display: none;
            position: absolute;
            left: 0;
            top: 48px;
            width: 223px;
            border: 1px solid #ff6700;
            border-top: 0;
            background: #fff;
        }

        .result-list a {
            display: block;
            padding: 6px 15px;
            font-size: 12px;
            color: #424242;
            text-decoration: none;
        }

        .result-list a:hover {
            background-color: #eee;
        }
    </style>

</head>

<body>
    <div class="mi">
        <input type="search" placeholder="小米笔记本">
        <ul class="result-list">
            <li><a href="#">全部商品</a></li>
            <li><a href="#">小米11</a></li>
            <li><a href="#">小米10S</a></li>
            <li><a href="#">小米笔记本</a></li>
            <li><a href="#">小米手机</a></li>
            <li><a href="#">黑鲨4</a></li>
            <li><a href="#">空调</a></li>
        </ul>
    </div>
    <script>
        const input = document.querySelector('[type=search]')
        input.addEventListener('focus', function () {
            const list = document.querySelector('.result-list')
            list.style.display = 'block'
            input.classList.add('search')
        })
        input.addEventListener('blur', function () {
            const list = document.querySelector('.result-list')
            list.style.display = 'none'
            input.classList.remove('search')
        })
    </script>
</body>

</html>
```

![image-20250628210155267](assets/image-20250628210155267.png)

### 文本框输入事件

- `input` 用户输入事件



















