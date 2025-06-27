---
title: html5学习笔记
---



## 第一个程序



```html
<!DOCTYPE html>
<html>
<head>
<title>前端工程师</title>	 <!-- 网页的标题 -->
</head>
<body>
<p>
这是我的第一个html
</p>
</body>
</html>
```

***

## 基本框架



```html
<!DOCTYPE html>
<html>

<head>			<!-- 头部 -->
<title>xxx</title>
</head>

<body>			<!-- 内部 -->
</body>

</html>
```

***

## **常用标签**

#### 标题

标题（Heading）是通过 <h1> - <h6> 等标签进行定义的。

```html
<h1>一级标题</h1>
<h2>二级标题</h2>
<h3>三级标题</h3>
<h4>四级标题</h4>
<h5>五级标题</h5>
<h6>六级标题</h6>
```

如：

<h1>一级标题</h1>
<h2>二级标题</h2>
<h3>三级标题</h3>
<h4>四级标题</h4>
<h5>五级标题</h5>
<h6>六级标题</h6>

#### 水平线

```html
<hr>		
```

<hr>


#### 段落

**非格式化段落**

```html
<p>非格式化段落</p>
```

如：

<p>
    我肩上是风
    风上是闪耀的群星
</p>

格式化段落

```html
<pre>格式化段落</pre>
```

<pre>
	我肩上是风
    风上是闪耀的群星
</pre>
---

#### 换行

```html
<br />
```

#### 缩写

```html
<abbr title="一步一想">赠尔铃铛</abbr>  
```

实例：

<abbr title="一步一想">赠尔铃铛</abbr> 

---

#### 注释

```html
<!-- 这是html5的注释 -->
```



---

## 列表

#### 有序列表	

```html
<ol>
	<li>1</li></a>
	<li>2</li></a>
	<li>3</li></a>
	<li>4</li></a>
	<li>5</li></a>
</ol>
```

例如：

<ol>
	<li>临</li></a>
	<li>兵</li></a>
	<li>斗</li></a>
	<li>者</li></a>
	<li>皆</li></a>
</ol>

#### 无序列表

```HTML
 <ul>
            <li>三寸人间</li>
            <li>万古神帝</li>
            <li>武炼巅峰</;>
            <li>伏天氏</li>
            <li>圣墟</li>
</ul>
```

例如：

<ul>
	<li>临</li></a>
	<li>兵</li></a>
	<li>斗</li></a>
	<li>者</li></a>
	<li>皆</li></a>
</ul>

#### 自定义列表

自定义列表也可以叫注释说明

```html
<dl>                                <!--一个dt可以包含多个dd-->
            <dt>xx专业</dt>                <!--说明的对象-->
            <dd>xx1班</dd>                 <!--说明对象的注释-->
            <dd>xx2班</dd>
            <dd>xx3班</dd>
            <dd>xx4班</dd>
            <dd>xx5班</dd>
</dl>
```

例如：

<dl>                            
            <dt>xx专业：</dt>               
            <dd>xx1班</dd>             
            <dd>xx2班</dd>
            <dd>xx3班</dd>
            <dd>xx4班</dd>
            <dd>xx5班</dd>
</dl>

## 字体



| <b>      | 定义粗体文本。 |
| -------- | -------------- |
| <em>     | 定义着重文字。 |
| <i>      | 定义斜体字。   |
| <big>    | 定义大号字。   |
| <small>  | 定义小号字。   |
| <strong> | 定义加重语气。 |
| <sub>    | 定义下标字     |
| <sup>    | 定义上标字。   |
| <ins>    | 定义插入字。   |
| <del>    | 定义删除字。   |

实例：

<b> 定义粗体文本</b>

<em> 定义着重文字。</em>
 <i>       定义斜体字。   </i>
<big>     定义大号字。   </big>
 <small>   定义小号字。   </small>
 <strong>  定义加重语气。 </strong>
 <sub>     定义下标字     </sub>
 <sup>     定义上标字。   </sup>
 <ins>     定义插入字。   </ins>
 <del>     定义删除字。  </del>	

---

## 链接

**target**="**_blank**" 表示在新的页面打开

**align**:对齐方式（**center**,**left**,**right**）

#### 文字链接

```html
<a  href="链接" target="_blank" align="center">链接文字</a>
```

如：<a href="https://book.qidian.com/info/1010327039" target="_blank" align="center">三寸人间</a>

#### 图片链接

```html
<img src="图片链接（网络地址或本地地址）" alt="图片加载不出时显示的文字" title="鼠标放在图片上时显示的文字"/>
```



如：

```html
<img src="img/20331s.jpg" alt="　举头三尺无神明，掌心三寸是人间." title="万古神帝"/>
```

<img src="img/20331s.jpg" alt="　举头三尺无神明，掌心三寸是人间." title="万古神帝"/>

#### 视频链接

```html
<video src="视频地址" controls="controls" width="宽度数字" height="高度数字"></video> 
```

**controls** 属性供添加播放、暂停和音量控件

**width**,**height**添加视频画布的长宽，这两个属性可以不用添加

```html
<video width="320" height="240" controls="controls">
            <source src="视频/movie.ogv" type="video/ogg">
            <source src="视频/movie.mp4" type="video/mp4">
              Your browser does not support the video tag.
 </video>
```

上面的例子使用一个 Ogg 文件，适用于Firefox、Opera 以及 Chrome 浏览器。要确保适用于 Safari 浏览器，视频文件必须是 MPEG4 类型。

video 元素允许多个 source 元素。source 元素可以链接不同的视频文件。浏览器将使用第一个可识别的格式：

实例：

```html
<video width="320" height="240" controls="controls">
            <source src="视频/movie.ogv" type="video/ogg">
            <source src="视频/movie.mp4" type="video/mp4">
              Your browser does not support the video tag.
 </video>
```



<video width="320" height="240" controls="controls">
            <source src="视频/movie.ogv" type="video/ogg">
            <source src="视频/movie.mp4" type="video/mp4">
              Your browser does not support the video tag.
 </video>
#### 音频链接

```html
<audio src="音频链接" controls="controls" >
       Your browser does not support the audio tag.
    <!-- 视频无法加载时显示的文字 -->
</audio>
```

上面的例子使用一个 Ogg 文件，适用于Firefox、Opera 以及 Chrome 浏览器。

​      要确保适用于 Safari 浏览器，音频文件必须是 MP3 或 Wav 类型。

​      audio 元素允许多个 source 元素。source 元素可以链接不同的音频文件。浏览器将使用第一个可识别的格式：

实例：

<audio controls="controls">
    <source src="音频/song.ogv" type="audio/ogg">
    <source src="音频/song.mp4" type="audio/MPEG4">
    Your browser does not support the audio tag.
</audio>
#### 锚点链接

```html
<pre id="id名">
内容
<pre><a href="#id名">回到顶部</a></pre>
</pre>
```

实例：

<pre id="first">
内容
<pre id="lastest"><a href="#first">回到顶部</a></pre>
</pre>
---

## 表格

```html
<table align="" border="" cellpadding="" cellspacing="" width="" height="" bgcolor="" bordercolor="" background="" style="">
<tr> <th>文字</th>  <td>文字</td>  </tr>      
<tr> <th>文字</th>  <th>文字</th>  </tr>
<tr> <td>文字</td>  <td>文字</td>  </tr>
<tr> <td>文字</td>  <td>文字</td>  </tr>
<tr> <td>文字</td>  <td>文字</td>  </tr> 
</table>
```

| <table>    | 定义表格                 |
| ---------- | ------------------------ |
| <caption>  | 定义表格标题             |
| <th>       | 定义表格的表头，文字居中 |
| <tr>       | 定义表格的行。           |
| <td>       | 定义表格单元。           |
| <thead>    | 定义表格的页眉。         |
| <tbody>    | 定义表格的主体。         |
| <tfoot>    | 定义表格的页脚。         |
| <col>      | 定义用于表格列的属性。   |
| <colgroup> | 定义表格列的组。         |

```html
<table>表示一个表格，<tr>表示一行，<td>表示一行中的一个小格，<th>同样表示一行中的一个小格，但是加粗居中的
colspan="n" 表示合并n列，向右合并，写在<th>或<td>中
rowspan="n" 表示合并n行，向下合并，写在<th>或<td>中
```

**bgcolor**设置背景颜色,	**background**设置背景图片

**align**表示对齐方式，**center**,**right**,**left**

 **border**表示边框，**cellpadding**表示表格中文字距离边框的距离，**cellspacing**表示边框与边框间的距离

**width**表示宽度，**height**表示高度，这两个元素在图片里也可以应用

**backgroung-repeat**设置背景图片是否重复，默认重复 

**background-size**设置背景图片的大小

**style**设置内联样式

实例：

```html
<table align="center" border="1" cellpadding="10" cellspacing="10" width="500" height="700" bgcolor="yellow" bordercolor="yellow" background="img//QQ图片20201010213210.jpg" style="background-repeat:no-repeat;background-size:100% 100%">
    <!--bgcolor设置背景颜色,background设置背景图片-->
    <!--align表示对齐方式，center,right,left-->
     <!--border表示边框，cellpadding表示表格中文字距离边框的距离，cellspacing表示边框与边框间的距离-->
	<!--width表示宽度，height表示高度，这两个元素在图片里也可以应用-->
	<!-- backgroung-repeat设置背景图片是否重复，默认重复 -->
	<!-- background-size设置背景图片的大小 -->
	<tr> <th>嘟嘟嘟</th>  <td colspan="3"></td>  </tr>    <!--colspan="n" 表示合并n列-->
	<tr>  <th>姓名</th>  <th>性别</th>   <th>年龄</th>   <th>滴滴滴滴</th>     </tr>
	<tr> <td>张三</td>    <td >男</td>    <td>19</td>  <td rowspan="3"></td>  </tr>   <!--rowspan="n" 表示合并n行-->
	<tr> <td>李四</td>    <td>男</td>    <td >19</td>              </tr>
	<tr> <td>王二麻子 </td>  <td>男</td>    <td>19</td>              </tr>   
	<!--<table>表示一个表格，<tr>表示一行，<td>表示一行中的一个小格，<th>同样表示一行中的一个小格，但是加粗居中的-->
	</table>
```

<table align="center" border="1" cellpadding="10" cellspacing="10" width="500" height="700" bgcolor="yellow" bordercolor="yellow" background="img//QQ图片20201010213210.jpg" style="background-repeat:no-repeat;background-size:100% 100%">
    <!--bgcolor设置背景颜色,background设置背景图片-->
    <!--align表示对齐方式，center,right,left-->
     <!--border表示边框，cellpadding表示表格中文字距离边框的距离，cellspacing表示边框与边框间的距离-->
	<!--width表示宽度，height表示高度，这两个元素在图片里也可以应用-->
	<!-- backgroung-repeat设置背景图片是否重复，默认重复 -->
	<!-- background-size设置背景图片的大小 -->
	<tr> <th>嘟嘟嘟</th>  <td colspan="3"></td>  </tr>    <!--colspan="n" 表示合并n列-->
	<tr>  <th>姓名</th>  <th>性别</th>   <th>年龄</th>   <th>滴滴滴滴</th>     </tr>
	<tr> <td>张三</td>    <td >男</td>    <td>19</td>  <td rowspan="3"></td>  </tr>   <!--rowspan="n" 表示合并n行-->
	<tr> <td>李四</td>    <td>男</td>    <td >19</td>              </tr>
	<tr> <td>王二麻子 </td>  <td>男</td>    <td>19</td>              </tr>   
	<!--<table>表示一个表格，<tr>表示一行，<td>表示一行中的一个小格，<th>同样表示一行中的一个小格，但是加粗居中的-->
	</table>
---


## 表单

表格是表单的基础

```html
 <form name="" align="" action="post" >
     <table>
         <tr>
             <th></th>
             <td><input type="" placeholder="" name="" value="" id=""/></td>
         </tr>
         <tr>
             <td>
                 <input type="" name="" value="">
             </td>
         </tr>
         
     </table>
</form>
```

#### **input**元素

**input**表示输入框

```html
<input type="" name="" value="">
```

**type**表示类型	 有**text**（文本），**password**（密码，有标记但无内容），**radio**（单选），**checkbox**（多选），**month**（年月日），**number**（数字），**file**（文件），**submit**（提交按钮），**reset**（重置按钮）

**特有属性**	：**placeholder**（显示提醒信息），**name**（显示输入框的功能），**value**（显示值），**id**（标记），**min**（最小值），**max**（最大值）

#### **textarea**元素

**textarea**表示输入文本

```html
<textarea rows="" cols="" placeholder=""></textarea>
```

**rows**（行数），**cols**（列数）

#### **select**元素

**select**表示下拉列表

```HTML
<select>
	<option value=" ">中国</option>
	<option value="China">俄罗斯</option>
	<option value="America">美国</option>
	<option value="Engilad">英国</option>
</select>   
```

**option**（选项）

#### **label**元素

**label** 元素不会向用户呈现任何特殊效果。不过，它为鼠标用户改进了可用性。如果您在 label 元素内点击文本，就会触发此控件。就是说，当用户选择该标签时，浏览器就会自动将焦点转到和标签相关的表单控件上。

<label> 标签的 for 属性应当与相关元素的 **id** 属性相同。

```HTML
<input type="radio" name="sex" value="man" id="man" /><label for="man">男</label>
```

实例：

```html
 <form name="form1" align="left" action="post" >
            <table align="left">
            <tr>
                <td>用户名：</td> 
                <td><input type="text" placeholder="请输入用户名"/> </td>
            <tr>
            <tr>
                <td> 密码：</td>
                <td> <input type="password" placeholder="请输入密码"/></td>
             </tr>
             <tr>
                 <td>性别：</td>
                 <td><input type="radio" name="sex" value="man" id="man"/><label for="man">男</label>
                   <input type="radio" name="sex" value="woman" id="woman"/><label for="woman">女</label>
                </td>
             </tr>
             <tr>
                <td>国家：</td>
                <td>
                <select>
                    <option value=" "> </option>
                    <option value="China">中国
                    </option>
                    <option value="America">美国</option>
                    <option value="Engilad">英国</option>
                </select>   
                </td>
            </tr>
            <tr>
                <td>城市:</td>
                <td>
                </td>
            </tr>
            <tr>
                <td class="red font">爱好：</td>
                <td>
                <input type="checkbox" name="interest" value="read">阅读
                <input type="checkbox" name="interest" value="exercise">运动
                <input type="checkbox" name="interest" value="cook">烹饪
                </td>
                <tr>
                    <td> </td>
                    <td>
                <input type="checkbox" name="interest" value="music">音乐
                <input type="checkbox" name="interest" value="dance">跳舞
                <input type="checkbox" name="interest" value="travel">旅游
                </td>
                </tr>
            </tr>
            <tr>
                <td>出生年月</td>
                <td>
                    <input type=month name="month" >
                    <!--  <input type="date" name="shengri">   -->
                </td>
            </tr>
            <tr>
                <td>身高(cm)</td>
                <td>
                    <input type="number" name="year" min="1" max="300" placeholder="身高">
                </td>
            </tr>
            <tr>
                <td>体重(kg)</td>
                <td>
                    <input type="number" min="1" max="300" placeholder="体重">
                </td>
            </tr>
            <tr>
                <td>年龄</td>
                <td>
                    <input type="number" min="1" max="120" placeholde="年龄">
                </td>
            </tr>
            <tr>
                <td>个人简介</td>
                <td>
                    <textarea rows="5" cols="15" placeholder="请加以描述"></textarea>
                </td>
            </tr>
            <tr>
                <td>个人照片</td>
                <td>
                    <input type="file" name="photo" >
                </td>
            </tr>
            <tr>
                <td>
                    <input type="submit" value="提交">
                </td>
                <td>
                    <input type="reset" value="重置">
                </td>
            </tr>
            </table>
        </form>
```

 <form name="form1" align="left" action="post" >
     <table align="left">
            <tr>
                <td>用户名：</td> 
                <td><input type="text" placeholder="请输入用户名"/> </td>
            <tr>
            <tr>
                <td> 密码：</td>
                <td> <input type="password" placeholder="请输入密码"/></td>
             </tr>
             <tr>
                 <td>性别：</td>
                 <td><input type="radio" name="sex" value="man" id="man"/><label for="man">男</label>
                   <input type="radio" name="sex" value="woman" id="woman"/><label for="woman">女</label>
                </td>
             </tr>
             <tr>
                <td>国家：</td>
                <td>
                <select>
                    <option value=" "> </option>
                    <option value="China">中国
                    </option>
                    <option value="America">美国</option>
                    <option value="Engilad">英国</option>
                </select>   
                </td>
            </tr>
            <tr>
                <td>城市:</td>
                <td>
                </td>
            </tr>
            <tr>
                <td class="red font">爱好：</td>
                <td>
                <input type="checkbox" name="interest" value="read">阅读
                <input type="checkbox" name="interest" value="exercise">运动
                <input type="checkbox" name="interest" value="cook">烹饪
                </td>
                <tr>
                    <td> </td>
                    <td>
                <input type="checkbox" name="interest" value="music">音乐
                <input type="checkbox" name="interest" value="dance">跳舞
                <input type="checkbox" name="interest" value="travel">旅游
                </td>
                </tr>
            </tr>
            <tr>
                <td>出生年月</td>
                <td>
                    <input type=month name="month" >
                    <!--  <input type="date" name="shengri">   -->
                </td>
            </tr>
            <tr>
                <td>身高(cm)</td>
                <td>
                    <input type="number" name="year" min="1" max="300" placeholder="身高">
                </td>
            </tr>
            <tr>
                <td>体重(kg)</td>
                <td>
                    <input type="number" min="1" max="300" placeholder="体重">
                </td>
            </tr>
            <tr>
                <td>年龄</td>
                <td>
                    <input type="number" min="1" max="120" placeholde="年龄">
                </td>
            </tr>
            <tr>
                <td>个人简介</td>
                <td>
                    <textarea rows="5" cols="15" placeholder="请加以描述"></textarea>
                </td>
            </tr>
            <tr>
                <td>个人照片</td>
                <td>
                    <input type="file" name="photo" >
                </td>
            </tr>
            <tr>
                <td>
                    <input type="submit" value="提交">
                </td>
                <td>
                    <input type="reset" value="重置">
                </td>
            </tr>
            </table>
</form>


​     





















#### 表单居中

```html
margin:0 auto
```

前提是必须要线设置好表单的**height**和**width**

---

## 块元素

**div**表示块元素

```html
<div></div>
```

**width**（宽，单位可以是像素（px）或百分比），**height**（高），**background-color**（背景色），**padding**（）内边距，**border**（边框粗细），**margin**（边框位置）

例如：

通过style设置内联样式

```html
<div class="div">
                <div style="width:100px;height:100px;padding:20px;float: left;background-color: grey;">我是第一个</div>
                <div style="width:100px;height:100px;padding:20px;float: left;background-color: red">我是第二个</div>
                <div style="width:100px;height:100px;padding:20px;float: left;background-color: white">我是第三个</div>
</div>
```



<div class="div">
                <div style="width:100px;height:100px;padding:20px;float: left;background-color: grey;">我是第一个</div>
                <div style="width:100px;height:100px;padding:20px;float: left;background-color: red">我是第二个</div>
                <div style="width:100px;height:100px;padding:20px;float: left;background-color: white">我是第三个</div>
</div>




# css

## 应用方法

#### 内部 CSS

内部样式是在 head 部分的 <style> 元素中进行定义。

如：

```HTML
<!DOCTYPE html>
<html>
<head>
<style>
body {
  background-color: linen;
}

h1 {
  color: maroon;
  margin-left: 40px;
} 
</style>
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```

---

#### 外部 CSS

通过使用外部样式表，您只需修改一个文件即可改变整个网站的外观！

每张 HTML 页面必须在 head 部分的 <link> 元素内包含对外部样式表文件的引用。

```html
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```

外部样式表可以在任何文本编辑器中编写，并且必须以 .css 扩展名保存。

外部 .css 文件不应包含任何 HTML 标签。

"mystyle.css" 是这样的：

```css
body {
  background-color: lightblue;
}

h1 {
  color: navy;
  margin-left: 20px;
}
```

**注意：**请勿在属性值和单位之间添加空格（例如 **margin-left: 20 px;**）。正确的写法是：**margin-left: 20px;**

---

#### 行内 CSS

行内样式（也称内联样式）可用于为单个元素应用唯一的样式。

如需使用行内样式，请将 style 属性添加到相关元素。style 属性可包含任何 CSS 属性。

```html
<!DOCTYPE html>
<html>
<head></head>
<body>

<h1 style="color:blue;text-align:center;">This is a heading</h1>
<p style="color:red;">This is a paragraph.</p>

</body>
</html>
```



---

## 元素选择器

元素选择器根据元素名称来选择 HTML 元素

```css
p{
            color: #b12d2d;/*字体颜色*/
            text-indent: 2em;/*1em就是一个字符，首行缩进*/
            line-height: 30px;/*设置行间距：=字体的高度加上上下边距的高度*/
            text-align: left;/*设置字体位置*/
         }
```

---

## id 选择器

id 选择器使用 HTML 元素的 id 属性来选择特定元素。

元素的 id 在页面中是唯一的，因此 id 选择器用于选择一个唯一的元素！

要选择具有特定 id 的元素，请写一个井号（＃），后跟该元素的 id。

```css
/* 这条 CSS 规则将应用于 id="para1" 的 HTML 元素： */
#para1 {
  text-align: center;
  color: red;
}
```

**注意：**id 名称不能以数字开头。

---

## 类选择器

类选择器选择有特定 class 属性的 HTML 元素。

如需选择拥有特定 class 的元素，请写一个句点（.）字符，后面跟类名。

```css
/* 在此例中，所有带有 class="center" 的 HTML 元素将为红色且居中对齐： */
.center {
  text-align: center;
  color: red;
}
```

```html
<!-- 引用 -->
<p class="center large">这个段落引用两个类。</p>
```

---

## 通配符选择器

通用选择器（*）选择页面上的所有的 HTML 元素。

```css
*{
                color: green;
                font-family: 微软雅黑
            }   
```

---

## 分组选择器

分组选择器选取所有具有相同样式定义的 HTML 元素。

```css
h1, h2, p {
  text-align: center;
  color: red;
}
```

---

## 后代选择器

1. 后代选择器，元素1和元素2一定要用空格隔开，且元素1一定是父级，元素2不一定是子级，也有可能是孙级   

```css
ul li {
			color: green;              
		}
```

2. 后代选择器可以多级嵌套,**ul**是**li**的父级，**li**是**a**的父级，两个元素之间必修用空格隔开    

```css
ul li a {
			color: red;                
		}
```

3. 后代选择器也可以这样用        

```css
.nav li {                        
			color: white;
		}
```

4. 后代选择器，意思是后代中的所有a元素均改为黄色，不管这个a是子级还是孙级   

```css
.nav li a {                      
			color: yellow;
		}
```

---

## 子元素选择器

​	选的必须是str的亲儿子 

​	子元素选择器选择的只是子级的a

```css
.str>a {
			color: green;                
		} 
```

---

## 并级选择器

​	几个元素之间用逗号隔开    

```css
p,div,a {                            
			font-family: 黑体;
			font-weight: 700;
			font-size: 27px;
		}
```

---

## 伪类选择器

​	未访问的链接

```css
a:link {
			color:black;
			text-decoration: none;             	/*  去除链接的下划线  */
		}
```

​	访问过的链接，点击访问过的链接

```css
a:visited {
			color:pink;
			font-size: 6px;
		}
```

​	选择鼠标经过的链接

```css
a:hover{
			color:red;
		}
```

​	选择是我们鼠标正在按下还没有弹起的那个链接

```css
a:active{
			color:green;
			font-size:33px;
		}
```

注意：伪类选择器这四个的顺序不能颠倒 ，即LVHA的顺序

---

## css元素

位于 \<style\> 元素内的 CSS 注释，以 /* 开始，以 */ 结束：

```css
/* 这是一条单行注释 */
p {
  color: red;
}
```



| 元素                | 功能                                                         |
| ------------------- | ------------------------------------------------------------ |
| **color**           | 文字颜色，如 red，                                           |
| **text-decoration** | 设置下划线，none无下划线，underline下划线                    |
| width               | 宽度，以像素（px）或百分比为单位                             |
| height              | 高度，以像素（px）或百分比为单位                             |
| text-align          | 文本位置，center,right,left                                  |
| text-indent         | 1em就是一个字符，文本首行缩进                                |
| line-height         | 设置行间距：=字体的高度加上上下边距的高度                    |
| font-size           | 文字大小，像素（px）为单位                                   |
| font-family         | 文字样式，如微软雅黑                                         |
| font-weight         | 文字粗细，如 font-weight: 400                                |
| border-radius       | 创建圆角，多用于\<div>标签                                   |
| float               | 属性用于定位和格式化内容，  left - 元素浮动到其容器的左侧 right - 元素浮动在其容器的右侧 none - 元素不会浮动（将显示在文本中刚出现的位置）。默认值。 inherit - 元素继承其父级的 float 值 |
| border              | 边框粗细                                                     |
| border-color        | 边框颜色                                                     |
| margin              | 设置\<div>的位置，0 auto：居中                               |
| padding             | 设置内边距                                                   |
| background          | 设置背景图片                                                 |
| background-color    | 背景颜色                                                     |
| backgroung-repeat   | 设置背景图片是否重复，默认重复，no-repeat：不重复            |
| background-size     | 设置背景图片的大小，以像素（px）或百分比为单位               |
| cellpadding         | 表示表格中文字距离边框的距离                                 |
| cellspacing         | 表示边框与边框间的距离                                       |
|                     |                                                              |
|                     |                                                              |
|                     |                                                              |
|                     |                                                              |
|                     |                                                              |
|                     |                                                              |
|                     |                                                              |

