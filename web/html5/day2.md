## 换行与水平线

```html
换行: <br> (单标签)

水平线: <hr> （单标签）
```

```html
<p>这是第一行<br>这是第二行</p>
<hr>
```

---

## 文本格式化

```html
<strong>加粗</strong>
<em>倾斜</em>
<ins>下划线</ins>
<del>删除线</del>

<br>

<b>加粗</b>
<i>倾斜</i>
<u>下划线</u>
<s>删除线</s>
```

---

## 图像

```html
<img src="imgs/钢铁侠.jpg" alt="图片无法正常实现的替换文本" title="鼠标放在图片上的提示文本" width="" height="">
```

----

## 超链接

```html
<a href="https://baidu.com">跳转到百度</a>

<!--新窗口跳转页面-->
<a href="https://baidu.com" target="_blank">跳转到百度</a>

<!-- 如果不知道跳转地址，href里写# -->
<a href="#">空链接</a>
```

| 属性                                                         | 值                                                           | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| [charset](https://www.w3cschool.cn/htmltags/att-a-charset.html) | *char_encoding*                                              | HTML5 不支持。规定目标 URL 的字符编码。                      |
| [coords](https://www.w3cschool.cn/htmltags/att-a-coords.html) | *coordinates*                                                | HTML5 不支持。规定链接的坐标。                               |
| [download](https://www.w3cschool.cn/htmltags/att-a-download.html) | *filename*                                                   | 指定下载链接                                                 |
| [href](https://www.w3cschool.cn/htmltags/att-a-href.html)    | *URL*                                                        | 规定链接的目标 URL。                                         |
| [hreflang](https://www.w3cschool.cn/htmltags/att-a-hreflang.html) | *language_code*                                              | 规定目标 URL 的基准语言。仅在 href 属性存在时使用。          |
| [media](https://www.w3cschool.cn/htmltags/att-a-media.html)  | *media_query*                                                | 规定目标 URL 的媒介类型。默认值：all。仅在 href 属性存在时使用。 |
| [name](https://www.w3cschool.cn/htmltags/att-a-name.html)    | *section_name*                                               | HTML5 不支持。规定锚的名称。                                 |
| [rel](https://www.w3cschool.cn/htmltags/att-a-rel.html)      | alternate author bookmark help license next nofollow noreferrer prefetch prev search tag | 规定当前文档与目标 URL 之间的关系。仅在 href 属性存在时使用。 |
| [rev](https://www.w3cschool.cn/htmltags/att-a-rev.html)      | *text*                                                       | HTML5 不支持。规定目标 URL 与当前文档之间的关系。            |
| [shape](https://www.w3cschool.cn/htmltags/att-a-shape.html)  | default rect circle poly                                     | HTML5 不支持。规定链接的形状。                               |
| [target](https://www.w3cschool.cn/htmltags/att-a-target.html) | _blank _parent _self _top *framename*                        | 规定在何处打开目标 URL。仅在 href 属性存在时使用。           |
| [type](https://www.w3cschool.cn/htmltags/att-a-type.html)    | *MIME_type*                                                  | 规定目标 URL 的 MIME 类型。仅在 href 属性存在时使用。 注：MIME = Multipurpose Internet Mail Extensions。 |

---

## 音频签

在 html5 中如果属性名和属性值完全一样，可以简写为一个单词

```html
<audio src="audio/h1.mp3" controls loop></audio>
```

| 属性                                                         | 值                 | 描述                                                        |
| :----------------------------------------------------------- | :----------------- | :---------------------------------------------------------- |
| [autoplay](https://www.w3cschool.cn/htmltags/att-audio-autoplay.html) | autoplay           | 如果出现该属性，则音频在就绪后马上播放。                    |
| [controls](https://www.w3cschool.cn/htmltags/att-audio-controls.html) | controls           | 如果出现该属性，则向用户显示音频控件（比如播放/暂停按钮）。 |
| [loop](https://www.w3cschool.cn/htmltags/att-audio-loop.html) | loop               | 如果出现该属性，则每当音频结束时重新开始播放。              |
| [muted](https://www.w3cschool.cn/htmltags/att-audio-muted.html) | muted              | 如果出现该属性，则音频输出为静音。                          |
| [preload](https://www.w3cschool.cn/htmltags/att-audio-preload.html) | auto metadata none | 规定当网页加载时，音频是否默认被加载以及如何被加载。        |
| [src](https://www.w3cschool.cn/htmltags/att-audio-src.html)  | *URL*              | 规定音频文件的 URL。                                        |

浏览器会禁用自动播放。

----

## 视频

```html
<video src="media/＂你在思念谁。- 做个好梦-治愈版《虫儿飞》吉他弹唱.mp4" controls height="100%" width="100%"></video>

<!--静音自动播放-->
<video src="media/＂你在思念谁。- 做个好梦-治愈版《虫儿飞》吉他弹唱.mp4" controls height="100%" width="100%" autoplay muted></video>
```

|                             属性                             |         值         |                             描述                             |
| :----------------------------------------------------------: | :----------------: | :----------------------------------------------------------: |
| [autoplay](https://www.w3cschool.cn/htmltags/att-video-autoplay.html) |      autoplay      | 如果出现该属性，则视频在就绪后马上播放。（浏览器只支持静音自动播放） |
| [controls](https://www.w3cschool.cn/htmltags/att-video-controls.html) |      controls      |       如果出现该属性，则向用户显示控件，比如播放按钮。       |
| [height](https://www.w3cschool.cn/htmltags/att-video-height.html) |      *pixels*      |                    设置视频播放器的高度。                    |
| [loop](https://www.w3cschool.cn/htmltags/att-video-loop.html) |        loop        |     如果出现该属性，则当媒介文件完成播放后再次开始播放。     |
| [muted](https://www.w3cschool.cn/htmltags/att-video-muted.html) |       muted        |            如果出现该属性，视频的音频输出为静音。            |
| [poster](https://www.w3cschool.cn/htmltags/att-video-poster.html) |       *URL*        |     规定视频正在下载时显示的图像，直到用户点击播放按钮。     |
| [preload](https://www.w3cschool.cn/htmltags/att-video-preload.html) | auto metadata none | 如果出现该属性，则视频在页面加载时进行加载，并预备播放。如果使用 "autoplay"，则忽略该属性。 |
| [src](https://www.w3cschool.cn/htmltags/att-video-src.html)  |       *URL*        |                     要播放的视频的 URL。                     |
| [width](https://www.w3cschool.cn/htmltags/att-video-width.html) |      *pixels*      |                    设置视频播放器的宽度。                    |

----

## 综合案例——个人简介

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <h1>钢铁侠</h1>
    <hr>
    <p>托尼·史塔克（Tony Stark），即钢铁侠（Iron Man），是美国漫威漫画旗下的超级英雄，初次登场于《悬疑故事》第39期（1963年3月），由斯坦·李、赖瑞·理柏、唐·赫克和杰克·科比联合创造。</p>

    <p> 全名安东尼·爱德华·“托尼”·史塔克（Anthony Edward 'Tony' Stark），出生于1970年5月29日，是斯塔克工业（STARK
        INDUSTRIES）的CEO，因一场阴谋绑架中，胸部遭弹片穿入，生命危在旦夕，为了挽救自己的性命，在同被绑架的物理学家何·银森（Ho Yinsen）的协助下托尼制造方舟反应炉（Arc
        Reactor）从而逃过一劫，利用方舟反应炉作为能量运转的来源，暗中制造了一套装甲（Mark1）杀出重围后逃脱，后参与创立<a
            href="https://baike.baidu.com/item/%E5%A4%8D%E4%BB%87%E8%80%85%E8%81%94%E7%9B%9F/391050?fromModule=lemma_inlink">复仇者联盟</a>。
    </p>
    <img src="./imgs/钢铁侠.jpg" alt="钢铁侠的照片" width="10%" height="10%" title="钢铁侠">

    <h2>角色背景</h2>
    <p>钢铁侠是由美国漫威漫画公司的数位作者联合创作的，包括编辑兼编剧斯坦·李、编辑赖瑞·理柏、负责绘制早期钢铁侠故事的画家唐·赫克，以及设计第一套钢铁侠装甲并绘制首次亮相的封面底稿的<a
            href="https://baike.baidu.com/item/%E6%9D%B0%E5%85%8B%C2%B7%E7%A7%91%E6%AF%94/6476526?fromModule=lemma_inlink">杰克·科比</a>。
    </p>

    <h3>角色形象</h3>
    <p><strong>身份背景：</strong>托尼·史塔克是斯塔克工业的董事长，从父亲霍华德·斯塔克那里接手了庞大的家业——史塔克工业，是一个拥有着亿万家产的实业家、军火制造商，以他独特的生活方式与其聪明才智及天才发明家闻名。
    </p>
    <p><strong>性格特点：</strong>很多人在媒体上见到的托尼只是一个以自我为中心的花花公子，托尼几乎总是骄傲地战斗。但是即使他表现得像个自大狂，他却总是尽他最大努力去保护队友。由于他与父亲的关系十分紧张，他对权威人士也表现得十分不敬。在绑架事件之前，托尼是一个以自我为中心的，不照顾他人感受的人。而在这些年里托尼已经成熟起来，成为团队中的一员也不再那么傲慢。他甚至开始敞开心扉，并与小辣椒展开了一段真正的关系。
    </p>
</body>

</html>
```

---

## 列表

列表分类：无序列表、有序列表、定义列表

### 无序列表

```html
<ul>
    <li>第一项</li>
    <li>第二项</li>
    <li>第三项</li>
    <li>第四章：天下无敌</li>
    <li>第五章：天上来敌</li>
</ul>
```

ul 标签里面只能包裹 li 标签

li 标签里面可以包裹任何内容

### 有序列表

```html
<ol>
    <li>第一项</li>
    <li>第二项</li>
    <li>第三项</li>
</ol>
```

ol 标签里面只能包裹 li 标签

li 标签里面可以包裹任何内容

### 定义列表

dl 使定义列表，dt 使定义列表的标题，dd 使定义列表的描述 / 详情。

```html
<dl>
    <dt>列表标题</dt>
    <dd>第一项</dd>
    <dd>第二项</dd>
    <dd>第三项</dd>
</dl>
```

dl 标签里面只能包裹 dt 和 dd 标签

dt 和 dd 标签里面可以包裹任何内容

----

## 表格

`<table>` 标签定义 HTML 表格


一个 HTML 表格包括` <table>` 元素，一个或多个 `<tr>`、`<th>` 以及 `<td>` 元素。

`<tr>` 元素定义表格行，`<th>` 元素定义表头，`<td>` 元素定义表格单元。

更复杂的 HTML 表格也可能包括 `<caption>`、`<col>`、`<colgroup>`、`<thead>`、`<tfoot>` 以及 `<tbody>` 元素。

提示：在网页中，表格默认没有边框线，使用 `border ` 属性可以为表格添加边框线。

```html
<table border="1px" >
    <tr>
        <th>姓名</th>
        <th>语文</th>
        <th>数学</th>
        <th>总分</th>
    </tr>
    <tr>
        <td>张三</td>
        <td>99</td>
        <td>100</td>
        <td>199</td>
    </tr>
    <tr>
        <td>里斯</td>
        <td>98</td>
        <td>100</td>
        <td>198</td>
    </tr>
</table>
```

### 表格结构标签

| 标签名 | 含义     | 特殊说明     |
| ------ | -------- | ------------ |
| thead  | 表格头部 | 表格头部内容 |
| tbody  | 表格主体 | 主要内容区域 |
| tfoot  | 表格底部 | 汇总信息区域 |

```html
<table border="1px">
    <thead>
        <tr>
            <th>姓名</th>
            <th>语文</th>
            <th>数学</th>
            <th>总分</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>张三</td>
            <td>99</td>
            <td>100</td>
            <td>199</td>
        </tr>
        <tr>
            <td>里斯</td>
            <td>98</td>
            <td>100</td>
            <td>198</td>
        </tr>
    </tbody>
    <tfoot>
        <td>总结</td>
        <td>全是第一</td>
        <td>全是第一</td>
        <td>全是第一</td>
    </tfoot>
</table>
```

### 合并单元格

如果表格中有结构标签，则合并只能在每个结构标签里进行。

（1）跨行合并

跨行合并，保留最上单元格，添加属性 rowspan

```html
<table border="1px">
    <thead>
        <tr>
            <th>姓名</th>
            <th>语文</th>
            <th>数学</th>
            <th>总分</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>张三</td>
            <td>99</td>
            <td rowspan="2">100</td>
            <td>199</td>
        </tr>
        <tr>
            <td>里斯</td>
            <td>98</td>
            <!-- <td>100</td> -->
            <td>198</td>
        </tr>
    </tbody>
    <tfoot>
        <td>总结</td>
        <td >全是第一</td>
        <td>全是第一</td>
        <td>全是第一</td>
    </tfoot>
</table>
```

<table border="1px">
    <thead>
        <tr>
            <th>姓名</th>
            <th>语文</th>
            <th>数学</th>
            <th>总分</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>张三</td>
            <td>99</td>
            <td rowspan="2">100</td>
            <td>199</td>
        </tr>
        <tr>
            <td>里斯</td>
            <td>98</td>
            <!-- <td>100</td> -->
            <td>198</td>
        </tr>
    </tbody>
    <tfoot>
        <td>总结</td>
        <td >全是第一</td>
        <td>全是第一</td>
        <td>全是第一</td>
    </tfoot>
</table>

（2）跨列合并

跨列合并，保留最左单元格，添加属性 colspan

```html
<table border="1px">
    <thead>
        <tr>
            <th>姓名</th>
            <th>语文</th>
            <th>数学</th>
            <th>总分</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>张三</td>
            <td>99</td>
            <td>100</td>
            <td>199</td>
        </tr>
        <tr>
            <td>里斯</td>
            <td>98</td>
            <td>100</td>
            <td>198</td>
        </tr>
    </tbody>
    <tfoot>
        <td>总结</td>
        <td colspan="3">全是第一</td>
    </tfoot>
</table>
```

<table border="1px">
    <thead>
        <tr>
            <th>姓名</th>
            <th>语文</th>
            <th>数学</th>
            <th>总分</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>张三</td>
            <td>99</td>
            <td>100</td>
            <td>199</td>
        </tr>
        <tr>
            <td>里斯</td>
            <td>98</td>
            <td>100</td>
            <td>198</td>
        </tr>
    </tbody>
    <tfoot>
        <td>总结</td>
        <td colspan="3">全是第一</td>
    </tfoot>
</table>

---

## 表单

### input 标签

```html
<input type="text" name="" id="">
```

| type值         | 描述                                                         |
| :------------- | :----------------------------------------------------------- |
| button         | 定义可点击的按钮（通常与 JavaScript 一起使用来启动脚本）。   |
| checkbox       | 定义复选框。                                                 |
| color          | 定义拾色器。                                                 |
| date           | 定义 date 控件（包括年、月、日，不包括时间）。               |
| datetime       | 定义 date 和 time 控件（包括年、月、日、时、分、秒、几分之一秒，基于 UTC 时区）。 |
| datetime-local | 定义 date 和 time 控件（包括年、月、日、时、分、秒、几分之一秒，不带时区）。 |
| email          | 定义用于 e-mail 地址的字段。                                 |
| file           | 定义文件选择字段和 "浏览..." 按钮，供文件上传。              |
| hidden         | 定义隐藏输入字段。                                           |
| image          | 定义图像作为提交按钮。                                       |
| month          | 定义 month 和 year 控件（不带时区）。                        |
| number         | 定义用于输入数字的字段。                                     |
| password       | 定义密码字段（字段中的字符会被遮蔽）。                       |
| radio          | 定义单选按钮。                                               |
| range          | 定义用于精确值不重要的输入数字的控件（比如 slider 控件）。   |
| reset          | 定义重置按钮（重置所有的表单值为默认值）。                   |
| search         | 定义用于输入搜索字符串的文本字段。                           |
| submit         | 定义提交按钮。                                               |
| tel            | 定义用于输入电话号码的字段。                                 |
| text           | 默认。定义一个单行的文本字段（默认宽度为 20 个字符）。       |
| time           | 定义用于输入时间的控件（不带时区）。                         |
| url            | 定义用于输入 URL 的字段。                                    |
| week           | 定义 week 和 year 控件（不带时区）。                         |

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    文本框：<input type="text">
    <br>
    密码框：<input type="password">
    <br>
    单选框：<input type="radio">
    <br>
    多选框：<input type="checkbox">
    <br>
    上传文件：<input type="file">
</body>
</html>
```

### input 标签占位文本

`placeholder` 属性

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    文本框：<input type="text" placeholder="提示信息">
    <br>
    密码框：<input type="password" placeholder="输入密码">
    <br>
    单选框：<input type="radio">
    <br>
    多选框：<input type="checkbox">
    <br>
    上传文件：<input type="file">
</body>
</html>
```

### 单选框 radio

| 属性名  | 作用     | 特殊说明                               |
| ------- | -------- | -------------------------------------- |
| name    | 控件名称 | 控件分组，同组只能选中一个（单选功能） |
| checked | 默认选中 | 属性名和属性值相同，简写为一个单词     |

```html
<body>
    性别：
    <input type="radio" name="gender" checked>男
    <input type="radio" name="gender" >女
</body>
```

### 上传文件 file

```html
<body>
    上传单个文件：
    <input type="file">
    <br>
    上传多个文件：
    <input type="file" multiple>
</body>
```

### 多选框 ckeckbox

默认选中：`checked`

```html
<body>
    多选框：
    <input type="checkbox">学习
    <input type="checkbox">敲代码
    <input type="checkbox" checked>睡觉
</body>
```

-----

## 下拉菜单

`selected` ：默认选中

```html
<body>
    城市：
    <select name="" id="">
        <option value="">北京</option>
        <option value="">成都</option>
        <option value="" selected>重庆</option>
        <option value="">杭州</option>
    </select>
</body>
```

----

## 文本域

作用：多行输入文本的表单控件。

标签：textarea，双标签。

```html
<textarea name="" id="" placeholder="请输入文本"></textarea>
```

注意点： （1）实际开发中，使用 CSS 设置 文本域的尺寸 （2） 实际开发中，一般禁用右下角的拖拽功能

----

## Label 标签

作用：网页中，某个标签的说明文本

经验：用 label 标签绑定文字和表单控件的关系，增大表单控件的点击范围。

| 属性                                                         | 值         | 描述                                  |
| :----------------------------------------------------------- | :--------- | :------------------------------------ |
| [for](https://www.w3cschool.cn/htmltags/att-label-for.html)  | element_id | 规定 label 与哪个表单元素绑定。       |
| [form](https://www.w3cschool.cn/htmltags/att-label-form.html) | form_id    | 规定 label 字段所属的一个或多个表单。 |

**增大点击范围：**

```html
写法一：
	label 标签只包裹内容，不包裹表单控件
	设置 label 标签的 for 属性值 和表单控件的 id 属性值相同
	
	<body>
    性别：
    <input type="radio" name="gender" id="gender-man"> <label for="gender-man">男</label>
    <input type="radio" name="gender" id="gender-woman"><label for="gender-woman">女</label>
  </body>

写法二：
	使用 label 标签包裹文字和表单控件，不需要属性
	<body>
    性别：
    <label><input type="radio" name="gender" id="gender-man">男</label>
    <label><input type="radio" name="gender" id="gender-woman">女</label>
  </body>
```

提示：支持 label 标签增大点击范围的表单控件：文本框、密码框、上传文件、单选框、多选框、下拉菜单、文本域等等。

----

## 按钮 button

```html
<button type="">按钮</button> 
```

| 属性                                                         | 值                                                           | 描述                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| [autofocus](https://www.w3cschool.cn/htmltags/att-button-autofocus.html) | autofocus                                                    | 规定当页面加载时按钮应当自动地获得焦点。                     |
| [disabled](https://www.w3cschool.cn/htmltags/att-button-disabled.html) | disabled                                                     | 规定应该禁用该按钮。                                         |
| [form](https://www.w3cschool.cn/htmltags/att-button-form.html) | form_id                                                      | 规定按钮属于一个或多个表单。                                 |
| [formaction](https://www.w3cschool.cn/htmltags/att-button-formaction.html) | URL                                                          | 规定当提交表单时向何处发送表单数据。覆盖 form 元素的 action 属性。该属性与 type="submit" 配合使用。 |
| [formenctype](https://www.w3cschool.cn/htmltags/att-button-formenctype.html) | application/x-www-form-urlencoded multipart/form-data text/plain | 规定在向服务器发送表单数据之前如何对其进行编码。覆盖 form 元素的 enctype 属性。该属性与 type="submit" 配合使用。 |
| [formmethod](https://www.w3cschool.cn/htmltags/att-button-formmethod.html) | get post                                                     | 规定用于发送表单数据的 HTTP 方法。覆盖 form 元素的 method 属性。该属性与 type="submit" 配合使用。 |
| [formnovalidate](https://www.w3cschool.cn/htmltags/att-button-formnovalidate.html) | formnovalidate                                               | 如果使用该属性，则提交表单时不进行验证。覆盖 form 元素的 novalidate 属性。该属性与 type="submit" 配合使用。 |
| [formtarget](https://www.w3cschool.cn/htmltags/att-button-formtarget.html) | _blank _self _parent _top framename                          | 规定在何处打开 action URL。覆盖 form 元素的 target 属性。该属性与 type="submit" 配合使用。 |
| [name](https://www.w3cschool.cn/htmltags/att-button-name.html) | name                                                         | 规定按钮的名称。                                             |
| [type](https://www.w3cschool.cn/htmltags/att-button-type.html) | button reset submit                                          | 规定按钮的类型。                                             |
| [value](https://www.w3cschool.cn/htmltags/att-button-value.html) | text                                                         | 规定按钮的初始值。可由脚本进行修改。                         |

| type 属性值 | 说明                                             |
| ----------- | ------------------------------------------------ |
| submit      | 提交按钮，点击后可以提交数据到后台（默认功能）   |
| reset       | 重置按钮，点击后将表单控件恢复默认值             |
| button      | 普通按钮，默认没有功能，一般配合 JavaScript 使用 |

```html
<body>
    <form action="">
        用户名：<input type="text"> <br>
        密码：<input type="password"> <br>
        <button type="reset">重置</button>
        <button type="submit">提交</button>
        <button type="button">普通按钮</button>
    </form>
</body>
```

----

## 无语义的布局标签

作用：布局网页（划分网页区域，摆放内容）

`div`：独占一行

`span`：不换行

```html
<body>
    <!-- div: 大盒子-->
    <div>这是 div 标签</div>
    <div>这是 div 标签</div>

    <!-- span: 小盒子 -->
    <span>这是 span 标签</span>
    <span>这是 span 标签</span>
</body>

```

---

## 有语义的布局标签

| 标签名  | 语义       |
| ------- | ---------- |
| header  | 网页头部   |
| nav     | 网页导航   |
| footer  | 网页底部   |
| aside   | 网页侧边栏 |
| section | 网页区块   |
| article | 网页文章   |

----

## 字符实体

| 显示结果 | 描述   | 实体名称 |
| -------- | ------ | -------- |
|          | 空格   | `&nbsp;` |
| <        | 小于号 | `&lt;`   |
| >        | 大于号 | `&gt;`   |

其他字符实体：https://www.w3cschool.cn/htmltags/html-symbols.html

```html
<p>春风若有怜花意&nbsp;可否许我再&lt;少年&gt;</p>
```

----

## 综合案例——新闻列表

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <ul>
        <li>
            <img src="./imgs/钢铁侠.jpg" alt="" width="10%" height="10%">
            <p><strong>该项目计划总投资65亿元，分两期建设，一期项目投资</strong></p>
        </li>
        <li>
            <img src="./imgs/钢铁侠.jpg" alt="" width="10%" height="10%">
            <p><strong>著名的有机太阳能中心，长期以来专注</strong></p>
        </li>
        <li>
            <img src="./imgs/钢铁侠.jpg" alt="" width="10%" height="10%">
            <p><strong>位于意大利，是一</strong></p>
        </li>
    </ul>
</body>

</html>
```

----

## 综合案例——注册信息

