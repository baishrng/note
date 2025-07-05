## 事件流

**事件流**指的是事件完整执行过程中的流动路径

![event](assets/event.png)

如上图所示，任意事件被触发时总会经历两个阶段：【捕获阶段】和【冒泡阶段】。

简言之，捕获阶段是【从父到子】的传导过程，冒泡阶段是【从子向父】的传导过程。

**实际工作都是使用事件冒泡为主**

### 事件捕获

事件捕获：从DOM的根元素开始去执行对应的事件 (从外到里)

事件捕获需要写对应代码才能看到效果

代码：

```JS
DOM.addEventListener(事件类型, 事件处理函数, 是否使用捕获机制)
```

说明：

- addEventListener第三个参数传入 **`true`** 代表是捕获阶段触发（很少使用）
- 若传入false代表冒泡阶段触发，默认就是false
- 若是用 L0 事件监听，则只有冒泡阶段，没有捕获

### 事件冒泡

事件冒泡：当一个元素的事件被触发时，同样的事件将会在该元素的所有祖先元素中依次被触发。这一过程被称为事件冒 泡

简单理解：当一个元素触发事件后，会依次向上调用所有父级元素的 **同名事件**

事件冒泡是默认存在的

L2事件监听第三个参数是 false，或者默认都是冒泡

例如：

```JS
const father = document.querySelector('.father')
const son = document.querySelector('.son')
document.addEventListener('click', function () {
    alert('我是爷爷')
})
father.addEventListener('click', function () {
    alert('我是爸爸')
})
son.addEventListener('click', function () {
    alert('我是儿子')
})
```

### 阻止冒泡

**问题：**因为默认就有冒泡模式的存在，所以容易导致事件影响到父级元素

**需求：**若想把事件就限制在当前元素内，就需要阻止事件冒泡

**前提：**阻止事件冒泡需要拿到事件对象

**语法：**

```JS
事件对象.stopPropagation()
```

> 注意：此方法可以阻断事件流动传播，不光在冒泡阶段有效，捕获阶段也有效

例如：

```JS
const father = document.querySelector('.father')
const son = document.querySelector('.son')
document.addEventListener('click', function () {
    alert('我是爷爷')
})
fa.addEventListener('click', function () {
    alert('我是爸爸')
})
son.addEventListener('click', function (e) {
  	alert('我是儿子')
    // 阻止冒泡
    e.stopPropagation()
})
```

**我们某些情况下需要**阻止默认行为的发生，比如 阻止 链接的跳转，表单域跳转

**语法：**

```JS
e.preventDefault()
```

例如：

```Js
<form action="http://www.baidu.com">
    <input type="submit" value="提交">
</form>
<script>
const form = document.querySelector('form')
form.addEventListener('click', function (e) {
    // 阻止表单默认提交行为
    e.preventDefault()
})
```

### 解绑事件

- on事件方式，直接使用null覆盖偶就可以实现事件的解绑

**语法：**

```JS
// 绑定事件
btn.onclick = function () {
    alert('点击了')
}
// 解绑事件
btn.onclick = null
```

- addEventListener方式，必须使用：

`removeEventListener(事件类型, 事件处理函数,  [获取捕获或者冒泡阶段])`

```JS
function fn() {
    alert('点击了')
}
// 绑定事件
btn.addEventListener('click', fn)
// 解绑事件
btn.removeEventListener('click', fn)
```

> **注意：匿名函数无法被解绑**

### 鼠标经过事件的区别

鼠标经过事件：

`mouseover `和 `mouseout `会有冒泡效果

`mouseenter  `和 `mouseleave   `没有冒泡效果 (推荐)

### 两种注册事件的区别

1. **传统on注册（L0）**

- 同一个对象,后面注册的事件会覆盖前面注册(同一个事件)
- 直接使用null覆盖偶就可以实现事件的解绑
- 都是冒泡阶段执行的

2. **事件监听注册（L2）**

- 语法: addEventListener(事件类型, 事件处理函数, 是否使用捕获)
- 后面注册的事件不会覆盖前面注册的事件(同一个事件)
- 可以通过第三个参数去确定是在冒泡或者捕获阶段执行
- 必须使用removeEventListener(事件类型, 事件处理函数, 获取捕获或者冒泡阶段)
- 匿名函数无法被解绑





















