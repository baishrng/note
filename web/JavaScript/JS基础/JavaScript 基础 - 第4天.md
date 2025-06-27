## 声明和调用

函数可以把具有相同或相似逻辑的代码“包裹”起来，通过函数调用执行这些被“包裹”的代码逻辑，这么做的优势是有利于精简代码方便复用。

### 声明（定义）

声明（定义）一个完整函数包括**关键字**、**函数名**、**形式参数**、**函数体**、**返回值**5个部分

![function-1750846855657](assets/function-1750846855657.jpg)

**函数体**是函数的构成部分，它负责将相同或相似代码“包裹”起来，直到函数调用时函数体内的代码才会被执行。函数的功能代码都要写在函数体当中。

例如：

```JS
function sayHi() {
	document.write('hai~~')
}
```

### 调用

声明（定义）的函数必须调用才会真正被执行，使用 `()` 调用函数。

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>JavaScript 基础 - 声明和调用</title>
</head>
<body>
  <script>
    // 声明（定义）了最简单的函数，既没有形式参数，也没有返回值
    function sayHi() {
      console.log('嗨~')
    }
    // 函数调用，这些函数体内的代码逻辑会被执行
    // 函数名()
        
    sayHi()
    // 可以重复被调用，多少次都可以
    sayHi()
  </script>
</body>
</html>
```

> 注：函数名的命名规则与变量是一致的，并且尽量保证函数名的语义。前缀应该为动词。

| 动词 | 含义                   |
| ---- | ---------------------- |
| can  | 判断是否可执行某个动作 |
| has  | 判断是否含义某个值     |
| is   | 判断是否为某个值       |
| get  | 获取某个值             |
| set  | 设置某个值             |
| load | 加载某些数据           |

例如：

```JS
function getName() {}
function addSquares() {}
```

**示例：**

需求：

1. 封装一个函数，计算两个数的和

2. 封装一个函数，计算1-100之间所有数的和

```JS
function add(a, b) {
  return a + b
}

function add1To100() {
  let sum = 0
  for (let i = 1; i <= 100; i++) {
    sum += i
  }
  return sum
}

console.log(add(2, 3))
console.log(add1To100())
```

---

##  函数传参

通过向函数传递参数，可以让函数更加灵活多变，参数可以理解成是一个变量。

声明（定义）一个功能为打招呼的函数

- 传入数据列表
- 声明这个函数需要传入几个数据
- 多个数据用逗号隔开

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>JavaScript 基础 - 函数参数</title>
</head>
<body>

  <script>
    // 声明（定义）一个功能为打招呼的函数
    // function sayHi() {
    //   console.log('嗨~')
    // }
    // 调用函数
    // sayHi()
	

    // 这个函数似乎没有什么价值，除非能够向不同的人打招呼
    // 这就需要借助参数来实现了
    function sayHi(name) {
      // 参数 name 可以被理解成是一个变量
      console.log(name)
      console.log('嗨~' + name)
    }

    // 调用 sayHi 函数，括号中多了 '小明'
    // 这时相当于为参数 name 赋值了
    sayHi('小明')// 结果为 小明

    // 再次调用 sayHi 函数，括号中多了 '小红'
    // 这时相当于为参数 name 赋值了
    sayHi('小红') // 结果为 小红
  </script>
</body>
</html>
```

总结：

1. 声明（定义）函数时的形参没有数量限制，当有多个形参时使用 `,` 分隔
2. 调用函数传递的实参要与形参的顺序一致

### 形参和实参

形参：声明函数时写在函数名右边小括号里的叫形参（形式上的参数）

实参：调用函数时写在函数名右边小括号里的叫实参（实际上的参数）

形参可以理解为是在这个函数内声明的变量（比如 num1 = 10）实参可以理解为是给这个变量赋值

开发中尽量保持形参和实参个数一致

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>JavaScript 基础 - 函数参数</title>
</head>
<body>
  <script>
    // 声明（定义）一个计算任意两数字和的函数
    // 形参 x 和 y 分别表示任意两个数字，它们是两个变量
    function count(x, y) {
      console.log(x + y);
    }
    // 调用函数，传入两个具体的数字做为实参
    // 此时 10 赋值给了形参 x
    // 此时 5  赋值给了形参 y
    count(10, 5); // 结果为 15
  </script>
</body>
</html>
```

### 参数默认值

如果不给形参设置默认值，则默认为undefined

```JS
function getSum(x = 0, y = 0) {
    document.write(x + y)
}
getSum() // 结果是0，而不是 N
getSum(1, 2) // 结果是 3
```

> 说明：这个默认值只会在缺少实参参数传递时 才会被执行，所以有参数会优先执行传递过来的实参, 否则默认为  undefined

**示例：**

需求：学生的分数是一个数组,计算每个学生的总分

```JS
function getScore(arr = []) {
  let sum = 0
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i]
  }
  return sum
}
console.log(getScore([100, 99, 98, 78]))
```

---

## 函数返回值

函数的本质是封装（包裹），函数体内的逻辑执行完毕后，函数外部如何获得函数内部的执行结果呢？要想获得函数内部逻辑的执行结果，需要通过 `return` 这个关键字，将内部执行结果传递到函数外部，这个被传递到外部的结果就是返回值。

```JS
// 定义求和函数
function count(a, b) {
  let s = a + b
  // s 即为 a + b 的结果
  // 通过 return 将 s 传递到外部
  return s
}

// 调用函数，如果一个函数有返回值
// 那么可将这个返回值赋值给外部的任意变量
let total = count(5, 12)
```

总结：

1. 在函数体中使用`return `关键字能将内部的执行结果交给函数外部使用
2. 函数内部只能出现1 次 return，并且 `return `下一行代码不会再被执行，所以**`return `后面的数据不要换行写**
3. `return`会立即结束当前函数
4. 函数可以没有`return`，这种情况默认返回值为 `undefined`

**示例：**

需求：求任意数组中的最大值并返回这个最大值

```JS
function getArrMax(arr = []) {
  let max = arr[0]
  let min = arr[0]
  for (let i = 1; i < arr.length; i++) {
    if (max < arr[i]) {
      max = arr[i]
    }
    if (min > arr[i]) {
      min = arr[i]
    }
  }
  return [max, min]
}

let newArr = getArrMax([4, 9, 7, 6, 3, 6, 0, 5, 7])
console.log(newArr)
```

---

## 函数细节补充

- 两个相同的函数后面的会覆盖前面的函数

- 在Javascript中 实参的个数和形参的个数可以不一致
  - 如果形参过多 会自动填上undefined (了解即可)
  - 如果实参过多 那么多余的实参会被忽略 (函数内部有一个`arguments`,里面装着所有的实参)
- 函数一旦碰到return就不会在往下执行了  函数的结束用return

---

## 作用域

通常来说，一段程序代码中所用到的名字并不总是有效和可用的，而限定这个名字的可用性的代码范围就是这个名字的作用域。

作用域的使用提高了程序逻辑的局部性，增强了程序的可靠性，减少了名字冲突。

### 全局作用域

作用于所有代码执行的环境(整个 script 标签内部)或者一个独立的 js 文件

处于全局作用域内的变量，称为全局变量

即：函数外面 `let`的变量

### 局部作用域

作用于函数内的代码环境，就是局部作用域。 因为跟函数有关系，所以也称为函数作用域。

处于局部作用域内的变量称为局部变量

即：函数内部`let`的变量

>如果函数内部，变量没有声明，直接赋值，也当**全局变量**看，但是强烈不推荐
>
>但是有一种情况，函数内部的形参可以看做是局部变量。

---

## 匿名函数

函数可以分为具名函数和匿名函数

**匿名函数**：没有名字的函数，无法直接使用。

### 函数表达式

将匿名函数赋值给一个变量，并且通过变量名称进行调用 我们将这个称为**函数表达式**

~~~javascript
// 声明
let fn = function() { 
   console.log('函数表达式')
}
// 调用
fn()
~~~

其中函数的形参和实参使用跟具名函数一致。

> 必须先声明，后调用

### 立即执行函数

场景介绍: 避免全局变量之间的污染

~~~javascript
// 1. 第一种写法
(function(){ xxx  })();

// 2. 第二种写法
(function(){xxxx}());
~~~

后面那个`()`相当于调用函数

>无需调用，立即执行，其实本质已经调用了
>
>多个立即执行函数之间用分号隔开
>
>也可以添加函数名（可选）

---

## 综合案例-转换时间

需求： 用户输入秒数，可以自动转换为时分秒

```JS
function getTime(second) {
  let oldSecond = second;

  // 转换
  second = oldSecond % 60
  let minute = parseInt(oldSecond / 60) % 60
  let hour = parseInt(oldSecond / 3600) % 60

  // 补0
  if (second < 10) {
    second = '0' + second
  }
  if (minute < 10) {
    minute = '0' + minute
  }
  hour = hour < 10 ? '0' + hour : hour

  document.write(`${oldSecond}秒转换为${hour}小时${minute}分钟${second}秒`)
}
let second = +prompt('请输入秒数:')
getTime(second)
```

---

## 逻辑中断

### 逻辑运算符里的短路

短路：只存在于 && 和 || 中，当满足一定条件会让右边代码不执行

| 符号 | 短路条件          |
| ---- | ----------------- |
| &&   | 左边为false就短路 |
| \|\| | 左边为true就短路  |

原因：通过左边能得到整个式子的结果，因此没必要再判断右边

运算结果：无论 && 还是 || ，运算结果都是最后被执行的表达式值，一般用在变量赋值

### 转换为Boolean型

1. **显示转换**

`Boolean(内容)`

**记忆： ‘’、0、undefined、null、false、NaN 转换为布尔值后都是false, 其余则为 true**

`&&`为真，输出最后一个真值

`||`为真，输出第一个真值

例如：

```JS
console.log(false && 20) // false
console.log(5 < 3 && 20) // false
console.log(undefined && 20) // undefined
console.log(null && 20) // null
console.log(0 && 20) // 0
console.log(10 && 20) // 20
```

```JS
console.log(false || 20) // 20
console.log(5 < 3 || 20) // 20
console.log(undefined || 20) // 20
console.log(null || 20) // 20
console.log(0 || 20) // 20
console.log(10 || 20) // 10
```

2. **隐式转换**

- 有字符串的加法 “” + 1 ，结果是 “1”
- 减法 - （像大多数数学运算一样）只能用于数字，它会使空字符串 "" 转换为 0
- null 经过数字转换之后会变为 0
- undefined 经过数字转换之后会变为 NaN

例如：

```JS
console.log('' - 1)		// -1
console.log('pink老师' - 1)		// NaN
console.log(null + 1)		// 1
console.log(undefined + 1)		// NaN
console.log(NaN + 1)		// NaN
```





























