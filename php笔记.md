---
title: php学习笔记
---



## 代码框架

```php
<?php
    内容1;
	内容2;
?>
```

---

## 基础

### 注释

```php
// 这是单行注释

/* 这是多行注释 */

/*
*文档注释
*/

# 风格注释（相当于单行注释）
```

---

### 变量

所有的变量均是以$开头的，如定义一个字符串变量 $str = '人间';

```php
$b = 16;		// 十进制数
$c = 016;		// 八进制数
$d = 0x16;		// 十六进制数
```

科学计数法：如

```PHP
3.14E2
859.34E-4
```

赋值

```php
//直接赋值
$a = 31;

// 引用赋值
$b = &$a;		// 相当于C语言中的指针
```

变量的作用域

```PHP
// 局部变量

// 全局变量
在用户自定义的函数中无法使用，若想使用，则在定义全局变量时要使用关键字global生申明
    
// 静态变量
用sattic关键字申明
```



---

### **数据类型**

**boolean**（布尔型）,**string**（字符串），**integer**（整形），**float**（浮点型），**array**（数组），**object**（对象），**resource**（资源），**null**（空值）

---

### 强制类型转换

​	如字符串转化为整形

```php
$a = '3.14159r4r'
$b = (integer)$a		// $b = 3.14159
```

注意：字符串转化为整形截取到非数字位

可以用**settype()**函数来完成

```php
settype(变量, string type);
// 例如
$a = 'God is a girl';
settype($a, 'integer');
```



---

### 单引号与双引号

单引号中的包含的变量按普通字符输出，双引号中所包含的变量回背自动替换为实际数值。

如：

```PHP
<?php
    $a = '落日归山海';
    echo '$a';      // 用单引号输出
    echo "<p>";     // 输出段落标志
    echo "$a";      // 用双引号输出
?>
```

结果：

```
$a

落日归山海
```

---

### 转义字符

**\\n**（换行），**\\r**（回车），**\\t**（水平制表符，tab键），**\\\\**（反斜杠），**\\'**（单引号），**\\"**（双引号）

**\\[0-7]{1,3}**（正则表达式，匹配一个用八进制符号表示的字符，如\\467）

**\\x[0-9A-Fa-f]{1,2}**（正则表达式，匹配一个用八进制符号表示的字符，如\\x9f）

---

### 常量

用define()函数定义常量

```php
define(常量名, 常量的值, 是否区分大小写);
// 默认大小敏感，true表示大小写不敏感
// 如：
define('Meg', '常量');
```

defined()函数用来判断常量是否被定义

```php
defined('meg');		// 若被定义，返回true
```

---

### 预定义常量

| 常量名      | 功能                                 |
| :---------- | ------------------------------------ |
| \__FILE__   | PHP程序文件名                        |
| \__LINE__   | PHP程序行数                          |
| PHP_VERSION | PHP版本                              |
| PHP_OS      | 执行PHP解析器的操作系统名，如windows |

注意：\_\__LINE__中的'\_\_'是两条下划线

---

### 可变变量

可变变量是一种特殊的变量，它允许动态的改变一个变量的名称。

```PHP
$a = "b";
$b = '万封信写不完牵挂';
echo $a;		// 输出 b
echo $$a;		// 输出 万封信写不完牵挂
```

---

### 运算符

**+**（加法）	**-**（减法）	*****（乘法）	**/**（除法）	**%**（取余）

```PHP
// 负数取余结果依旧为负数
$a = -12;
echo $a%10;		// 结果为-2
```

. 用来连接两个字符串

```PHP
$a = '落日归山海';
$b = $a.','.'山河藏真意';
echo $b;

结果：
落日归山海,山河藏真意
```

赋值运算符：**=**		**+=**		**-=**		**\*=**		**/=**		**.=**		**%=**

递增或递减：**++**		**--**		（注意 **++$i** 和 **$i++** 的区别）

位运算：**&**（按位与）	**|**（按位或）	**^**（按位异或）	**~**（按位取反）

​				**<<**（向左移位）	**>>**（向右移位）

逻辑运算符：**&&或and**（逻辑与）	**||或or**（逻辑或）

​						**xor**（逻辑异或）	**！**（逻辑非）

​						**注意**：优先级：**||**   >  **and**	>	**or**

比较运算符：**<**	**>**	**<=**	**>=**	**==**	**!=**

​						**===**（恒等）	**!==**（非恒等）

​						**注意**：恒等指的是数值和类型均相等

条件运算符：**?:**（也叫三目运算符）

```php
$a = 100;
echo ($a == 50)?"true":"false";
```

错误控制运算符：**@**

---

## 函数

### 定义和调用

```PHP
// 定义
function fun_name($str1, $str2, ..., $strn){
    fun_body
}

// 调用
fun_name($str1, $str2, ..., $strn)
```

如：

```php
function fun($num){			// 定义
    $num = $num * $num;
    echo $num;
}

fun(10);				// 调用
```



---

## 系统函数

| 函数名             | 功能                                              |
| ------------------ | ------------------------------------------------- |
| is_null()          | 判断变量是否为null（boolean）                     |
| unset()            | 销毁指定的变量                                    |
| is_bool()          | 检查变量是否是布尔类型（boolean）                 |
| is_string          | 检查变量是否是字符串类型（boolean）               |
| is_float/is_double | 检查变量是否是浮点数类型（boolean）               |
| is_integer/is_int  | 检查变量是否是整型（boolean）                     |
| is_array           | 检查变量是否是数组类型（boolean）                 |
| is_object          | 检查变量是否是对象类型（boolean）                 |
| is_numeric         | 检查变量是否为数字或有数字组成的字符串（boolean） |



## json文件

```php

$json_string = json_encode($_POST);         // 把PHP数组转成JSON字符串
    file_put_contents($filepath, $json_string);     // 写入文件
    $json_string = file_get_contents($filepath);    // 从文件中读取数据到PHP变量  
    $data = json_decode($json_string, true);        //把JSON字符串转成PHP数组  
    var_dump($data);            // 显示出来看看 
```

---

## PDO

### 查找

```php
$sqlstr = "select * from tb_user where ID = '$ID'";        // 查询语句
    $result = $pdo->prepare($sqlstr);       // 准备查询语句
    $result->execute();             // 执行查询语句
    $result_arr = $result->fetch(PDO::FETCH_ASSOC);     // 返回结果
```

### 修改

```PHP
$sqlstr = "update tb_user set QQ = '$QQ' where ID = '$user_ID'";
    $result = $pdo->prepare($sqlstr);
    $result = $pdo->exec($sqlstr);
```

---

### **注意**

在进行类型转换的过程中应该注意以下内容：转换成boolean
型时，null、0和未赋值的变量或数组会被转换为false，其他的为
真；转换成整型时，布尔型的false转换为0，true转换为1，浮点型的小数部分被舍去，字符型如果以数字开头就截取到非数字位，否则输出0。

当字符串转换为整型或浮点型时，如果字符串是以数字开头
的，就会先把数字部分转换为整型，再舍去后面的字符串；如果
数字中含有小数点，则会取到小数点前一位。

如果“+”号的两边有字符类型，则自动转换为整型；

在逻辑运算符中，逻辑与和逻辑或这两个运算符有4种运算符号（&&、and、
||和or），其中属于同一个逻辑结构的两个运算符号（例如&&和and）之间却有
着不同的优先级。

break语句不仅可以跳出当前的循环，还可以指定跳出几重循环。break语句不仅可以跳出当前的循环，还可以指定跳出几重循环。

在进行SQL查询之前，所有字符串都必须加单引号，以避免可能的注入漏洞和SQL错误。

---

#### 字符串

trim()函数去除字符串左右两边的空格和特殊字符、ltrim()函数去除字符串左边的空格和特殊字符、rtrim()函数去除字符串中右边的空格和特殊字符。

自动转义、还原字符串数据可以应用PHP提供的addslashes()

 stripslashes()函数用来将使用addslashes()函数转义后的字
符串str返回原样

addcslashes()函数，实现转义字符串中的字符，即在指定的字符charlist前加上反
斜线。

获取字符串的长度使用的是strlen()函数

说明：汉字占两个字符，数字、英文、小数点、下划线和空格占一
个字符。

PHP对字符串截取可以采用PHP的预定义函数substr()实现

按字节进行字符串比较的方法有两种，分别是strcmp()和strcasecmp()
函数，通过这两个函数即可实现对字符串进行按字节的比较。这两种函数的区
别是strcmp()函数区分字符的大小写，而strcasecmp()函数不区分字符的大
小写。

int strcmp ( string str1, string str2)
参数str1和参数str2指定要比较的两个字符串。如果相等则返回0；如果参数
str1大于参数str2则返回值大于0；如果参数str1小于参数str2则返回值小于
0。

在PHP中，按照自然排序法进行字符串的比较是通过strnatcmp()函
数来实现的。自然排序法比较的是字符串中的数字部分，将字符串中的
数字按照大小进行排序。本函数区分字母大小写

strncmp()函数用来比较字符串中的前n个字符。该函数区分字母大小写。

使用strstr()函数查找指定的关键字
    获取一个指定字符串在另一个字符串中首次出现的位置到后者末尾的
子字符串。如果执行成功，则返回剩余字符串（存在相匹配的字符）；
如果没有找到相匹配的字符，则返回false。本函数区分字母的大小写。

注意：strchr()函数与其正好相反，该函数是从字符串后序的位置开始
检索子串（子字符串）的。

使用substr_count()函数检索子串出现的次数

str_ireplace()函数
    使用新的子字符串（子串）替换原始字符串中被指定要替换的字符串。本函数区分大小写。本函数不区分大小写。

substr_replace()函数
    对指定字符串中的部分字符串进行替换。本函数区分大小写。

number_format()函数用来将数字字符串格式化。number_format()函数可以有一个、两个或是4个参数，但不能是3个参数。

  字符串的分割是通过explode()函数实现的。explode()函数按照指定的规则
对一个字符串进行分割，返回值为数组。

implode()函数可以将数组的内容组合成一个新字符串。

---

#### 数组

使用foreach结构遍历数组

使用list()函数遍历数组，list()函数仅能用于数字索引的数组，且数字索引从0开始。

使用count()函数对数组中的元素个数进行统计。

array_search()函数，在数组中搜索给定的值，找到后返回键名，否则返回false

array_pop()函数获取并返回数组的最后一个单元，并将数组的长度减
1，如果数组为空（或者不是数组）将返回null。

array_push()函数将数组当成一个栈，将传入的变量压入该数组的末
尾，该数组的长度将增加入栈变量的数目，返回数组新的单元总数。

array_unique()函数，将值作为字符串排序，然后对每个值只保留第一个键名，忽略所有后面的键名，即删除数组中重复的元素。

---

#### 表单

Select 下拉选框传递的是value，不是后面的“选项1”等

Cookie的值被保存在客户端。

Session在服务器端保存用户的信息（cookie在浏览器中）

使用$_SESSION[]传参的方法获取的变量值，保存之后任何页面都可以使用。但这种方法很耗费系统资源，建议读者慎重使用。

复选框能够进行项目的多项选择。浏览者填写表单时，有时需要选择多个项目，例如，在线听歌中需要同时选取多个歌曲等，就会用到复选框。复选框一般都是多个同时存在，为了便于传值，name的名字可以是一个数组形式，格式为：
<input type="checkbox" name="chkbox[]" value="chkbox1">

文件域的作用是实现文件或图片的上传。文件域有一个特有的属性accept，用于指定上传的文件类型，如果需要限制上传文件的类型，则可以通过设置该属性完成。

urlencode()函数实现将字符串str进行URL编码

urldencode()函数可将URL编码后的str查询字符串进行解码。

#### JavaScript

变量名不能包含空格或加号、减号等符号。

在JavaScript中，一般使用变量前需要先声明变量，但有时变量可
以不必先声明，在使用时根据变量的实际作用来确定其所属的数据类
型。所有的JavaScript变量都由关键字var声明。

document.write()

在JS文件中，只能包含JavaScript脚本代码，不能包含<script>标记和HTML代码。

在引用JS文件的<script>与</script>标记之间不应存在其他的JavaScript代码，即使存在，浏览器也会忽略此脚本代码，而只执行JS文件中的JavaScript脚本代码。

#### 时间函数

mktime()函数根据给出的参数返回UNIX时间戳。

PHP通过time()函数获取当前的UNIX时间戳，返回值为从UNIX纪元（格林威治时间1970年1月1日00:00:00）到当前时间的秒数。

在PHP中通过date()函数获取当前的日期和时间。date()函数的语法如下：
	date(string format,int timestamp)
	date()函数将返回参数timestamp按照指定格式而产生的字符串。

getdate()函数获取日期指定部分的相关信息。getdate()函数的语法如下：
	array getdate(int timestamp)
	getdate()函数返回数组形式的日期和时间信息，如果没有时间
戳，则以当前时间为准。

。PHP中内置了日期检查函数，就是checkdate()函数。checkdate()函数的语法如下：
	bool checkdate(int month,int day,int year)

setlocale()函数可以改变PHP默认的本地化环境。

strftime()函数根据本地化环境设置来格式化输出日期和时间。
	语法格式如下：
	string strftime(string format, int timestamp)
	该函数返回用给定的字符串对参数timestamp进行格式化后输出的字符串。如果没有给出时间戳则用本地时间。该函数依靠系统的底层实现，其行为不可控！最好不要使用！

PHP中应用strtotime()函数可将任何英文文本的日期和时间解析为UNIX时间戳，其值相对于now参数给出的时间，如果没有提供此参数则用系统当前时间。
	语法：
	int strtotime ( string time [, int now] )
	该函数有两个参数。如果参数time的格式是绝对时间，则now参数不起作用；如果参数time的格式是相对时间，那么其对应的时间就是参数now来提供的，如果没有提供参数now，对应的时间就为当前时间。如果解析失败返回false。

microtime()函数，该函数返回当前UNIX时间戳和微秒数。返回格式为msec sec的字符串，其中sec是当前的UNIX时间戳，msec为微秒数。
	语法格式如下：
	string microtime(void)

#### Cookie

文本文件的命令格式如下：
用户名@网站地址[数字].txt

现代的浏览器的cookie已经不是文本文件了。

在PHP中通过setcookie()函数创建Cookie。

如果Cookie不设定时间，就表示它的生命周期为浏览器会话的期间，只要关闭IE浏览器，Cookie就会自动消失。这种Cookie被称为会话Cookie，一般不保存在硬盘上，而是保存在内存中。
    如果设置了过期时间，那么浏览器会把Cookie保存到硬盘中，再次打开IE浏览器时会依然有效，直到它的有效期超时。

#### Session

在计算机专业术语中，Session是指一个终端用户与交互系统进行通信的时间间隔，通常指从注册进入系统到注销退出系统所经过的时间。因此，Session实际上是一个特定的时间概念。

启动PHP会话的方式有两种：一种是使用session_start()函数，另一种是使用session_register()函数为会话登录一个变量来隐含地启动会话。

如果整个会话已经结束，首先应该注销所有的会话变量，然后使用session_destroy()函数清除结束当前的会话，并清空会话中的所有资
源，彻底销毁Session，

客户端没有禁止Cookie
（1）使用session_set_cookie_params()设置Session的失效时间，此函数是Session结合Cookie设置失效时间
（2）使用setcookie()函数可对Session设置失效时间

使用PHP函数session_save_path()存储Session临时文件，可缓解因临时文件的存储导致服务器效率降低和站点打开缓慢的问题。 

Session缓存的完成使用的是session_cache_limiter()函数。同时Session缓存并不是指在服务器端而是客户端缓存，在服务器中没有显示。

缓存时间的设置，使用的是session_cache_expire()函数，其语法如下：
int session_cache_expire ( [int new_cache_expire])
  参数cache_expire是Session缓存的时间数字，单位是分钟。

数据库存储所使用PHP中的session_set_save_handler()函数 。语法格式如下：
bool session_set_save_handler ( string open, string close, string read, string write, string destroy, string gc)

#### 文件

访问一个文件需要3步：打开文件、读写文件和关闭文件。

 在PHP中使用fopen()函数打开文件，fopen()函数的语法如下：
resource fopen ( string filename, string mode [, bool use_include_path]);

对文件的操作结束后应该关闭这个文件，否则可能引起错误。在PHP中使用
fclose()函数关闭文件，该函数的语法如下：
bool fclose ( resource handle ) ;
    该函数将参数handle指向的文件关闭，如果成功，返回true，否则返回
false。其中的文件指针必须是有效的，并且是通过fopen()函数成功打开的文
件。

 readfile()函数用于读入一个文件并将其写入到输出缓冲，如果出现错误则
返回false。函数语法如下：
int readfile(string filename)
      使用readfile()函数，不需要打开/关闭文件，不需要echo/print等输出语
句，直接写出文件路径即可。

file()函数也可以读取整个文件的内容，只是file()函数将文件内容按行存
放到数组中，包括换行符在内。如果失败则返回false。函数语法如下：
array file(string filename)

file_get_contents()函数
      该函数将文件内容（filename）读入一个字符串。如果有offset和maxlen参数，将在
参数offset所指定的位置开始读取长度为maxlen的内容。如果败，返回false。

读取一行数据：fgets()和fgetss()

读取一个字符：fgetc()

读取任意长度的字串：fread()

在PHP中使用fwrite()和
file_put_contents()函数向文件中写入数据。fwrite()函数也称为
fputs()，它们的用法相同。

PHP使用opendir()函数来打开目录

关闭目录使用closedir()函数

在PHP中浏览目录中的文件使用的是scandir()函数。注意一个点和两个点

rewind()函数，该函数将文件handle的指针设为文件流的开头

fseek()函数实现文件指针的定位

feof()函数判断文件指针是否在文件尾

ftell()函数返回当前指针的位置

在PHP中锁定文件的函数为flock()

PHP中使用move_uploaded_file()函数上传文件。该函数的语法如下：
bool move_uploaded_file ( string filename, string destination )

#### 类

PHP所支持的是单继承，也就是说，一个子类有且只有一个父类

类定义不能分割在不同的PHP段中

类的方法已经添加，接下来就使用方法，但使用方法不像使用函数那么简单。首先要对类进行实例化，实例化是通过关键字new来声明一个对象。然后使用如下格式来调用要使用的方法：
	“对象名 -> 成员方法”

对象名 -> 成员变量

定义常量使用关键字const

常量的输出和变量的输出是不一样的。常量不需要实例化对象，直接由“类名+常量名”调用即可。常量输出的格式为：
类名::常量名

构造方法的格式如下：
void __construct([mixed args [,…]])

void __destruct ( void )

子类继承父类的所有成员变量和方法，包括构造函数，当子类被创建时，PHP会先在子类中查找构造方法。如果子类有自己的构造方法，PHP会先调用子类中的方法。当子类中没有时，PHP则去调用父类中的构造方法，这就是继承。

不是所有的变量（方法）都要通过创建对象来调用。可以通过给变量（方法）加上static关键字来直接调用。调用静态成员的格式为：
	关键字::静态成员

接口类通过interface关键字来声明，并且类中只能包含未实现的方法和一些成员变量

子类是通过implements关键字来实现接口的，如果要实现多个接口，那么每个接口之间应使用逗号“,”连接。

在PHP 5中如果需要将对象复制，也就是克隆一个对象。需要使用关键字clone来实现。克隆对象的格式为：
$object1 = new ClassName();
$object2 = clone $object1;

有时除了单纯地克隆对象外，还需要克隆出来的对象可以拥有自己的属性和行为。这时就可以使用__clone()方法来实现。__clone()方法的作用是：在克隆对象的过程中，调用__clone()方法，可以使克隆出来的对象保持自己的一些行为及属性。

通过克隆对象，相信读者已经理解表达式$Object2 = $Object1和$Object2 = clone $Object1所表示的不同含义。但在实际开发中，还需判断两个对象之间的关系是克隆还是引用，这时可以使用比较运算符“==”和“===”。两个等号“==”是比较两个对象的内容，3个等号“===”是比较对象的引用地址。

\__set()和__get()方法

\__call()方法

\__sleep()和__wakeup()方法

\__toString()方法

\__autoload()方法

#### 操作数据库

要操作MySQL数据库，首先必须与MySQL服务器建立连接。连接MySQL服务器的语句如下：
	mysql_connect('hostname','username','password');
	该函数的返回值用于表示这个数据库连接。如果连接成功，则函数返回一个资源，为以后执行SQL指令做准备。

在连接到MySQL数据库服务器之后，接下来使用mysql_select_db()函数选择数据库。
	语法：
	mysql_select_db ( string数据库名[,resource link_identifier] ) 
	或
	mysql_query("use数据库名"[,resource link_identifier]);
	如果没有指定连接标识符，则使用上一个打开的连接。如果没有打开的连接，本函数将无参数调用mysql_connect()函数来尝试打开一个并使
用。每个其后的mysql_query()函数调用都会作用于活动数据库。

要对数据库中的表进行操作，通常使用mysql_query()函数执行SQL语句。
	语法：
	mysql_query ( string query [, resource link_identifier] ) 
	mysql_query()函数是查询指令的专用函数，所有的SQL语句都通过它执行，并返回结果集。 
	如果SQL语句是查询指令select，成功则返回查询后的结果集，失败则返回false；如果SQL语句是insert、delete、update等操作指令，成功则返回true，失败则返回false。

要对数据库中的表进行操作，通常使用mysql_query()函数执行SQL语句。
	语法：
	mysql_query ( string query [, resource link_identifier] ) 
	mysql_query()函数是查询指令的专用函数，所有的SQL语句都通过它执行，并返回结果集。 
	如果SQL语句是查询指令select，成功则返回查询后的结果集，失败则返回false；如果SQL语句是insert、delete、update等操作指令，成功则返回true，失败则返回false。

使用mysql_fetch_object()函数同样可以获取查询结果集中的数
据。下面通过同一个实例的不同方法来了解这两个函数在使用上的区别。首先来了解一下mysql_fetch_object()函数。
	语法格式如下：
	object  mysql_fetch_object ( resource result )
	mysql_fetch_object()函数和mysql_fetch_array()函数类似，只有一点区别，即返回的是一个对象而不是数组，该函数只能通过字段名来访问数组。使用下面的格式获取结果集中行的元素。
	$row->col_name                 //col_name为列名，$row代表结果集
	例如，如果从某数据表中检索id和name值，可以用$row->id和$row-> name访问行中的元素值。

mysql_fetch_row()函数逐行获取结果集中的每条记录。首先来了解mysql_fetch_row()函数。
	语法格式如下：
	array mysql_fetch_row ( resource result )
	mysql_fetch_row()函数从和指定的结果标识关联的结果集中获取一行数据并作为数组返回，将此行赋予变量$row，每个结果的列存储在一个数组的单元中，偏移量从0开始，即以$row[0]的形式访问第一个元素
（只有一个元素时也是如此），依次调用mysql_fetch_row()函数将返回结果集中的下一行，直到没有更多行则返回false。（使用循环）

使用mysql_close()函数关闭与MySQL服务器的连接	

#### PDO

PDO构造函数的语法如下：

__construct(string$dsn[,string$username[,string$password[,array$driver_options]]])

构造函数的参数说明如下：
dsn：数据源名，包括主机名端口号和数据库名称。
username：连接数据库的用户名。
password：连接数据库的密码。
driver_options：连接数据库的其他选项。
通过PDO连接MySQL数据库的代码如下：

```PHP
<?php 
	header("Content-Type:text/html;charset=utf-8");		       //设置页面的编码格式
	$dbms='mysql';								       //数据库类型
	$dbName='db_database19';					       //使用的数据库名称
	$user='root';								//使用的数据库用户名
	$pwd='111';								//使用的数据库密码
	$host='localhost';							//使用的主机名称
	$dsn="$dbms:host=$host;dbname=$dbName";			
	try {										//捕获异常
		$pdo=new PDO($dsn,$user,$pwd);			//实例化对象
		echo "PDO连接MySQL成功";
	} catch (Exception $e) {
		echo $e->getMessage()."<br>";
	}
?>	

```

exec()方法返回执行后受影响的行数，通常用于INSERT、DELETE和UPDATE语句中。

query()方法通过用于返回执行查询后的结果集。

预处理语句包括prepare()和execute()两个方法。首先，通过prepare()方法做查询的准备工作，然后，通过execute()方法执行查询。

fetch()方法获取结果集中的下一行，

通过fecth()方法获取结果集中下一行的数据，进而应用while语句完成数据库中数据的循环输出。

fetchAll()方法获取结果集中的所有行。其返回值是一个包含结果集中所有数据的二维数组。

fetchColumn()方法获取结果集中下一行指定列的值。

开启事务——beginTransaction()方法

提交事务——commit()方法

事务回滚——rollback()方法

“begin……end”表示存储过程中的语句块，它的作用类似与PHP语言中的“{……}”。

在PDO 中通过CALL语句调用存储过程

