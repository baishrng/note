---
学习Flask Web开发实战--第二天
---

## 对参数进行HTML转义

```python
from markupsafe import escape
@app.route('/xss')
def xss():
    args = request.args.get('para')
    return "<h1>h1llo, %s</h1>" % escape(args)
```

访问页面 `http://127.0.0.1:5000/xss?para=<script>alert("hello")</script>`

---

## Jinja2里常见的三种定界符

（1）语句

比如 if 判断、for 循环等；

```
{% ... %}
```

（2）表达式

比如字符串、变量、函数调用等；

```
{{ ... }}
```

（3）注释

```
{# ... #}
```

---

## 渲染模板

`render_template()`函数

视图函数

```python
from flask import render_template

user = {
    'username': 'Grey Li',
    'bio': 'A boy who loves movies and music.',
}

movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]

@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movies=movies)
```

`watchlist.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{{ user.username }}'s Watchlist</title>
</head>
<body>
<a href="{{ url_for('index') }}">&larr; Return</a>
<h2>{{ user.username }}</h2>
{% if user.bio %}
    <i>{{ user.bio }}</i>
{% else %}
    <i>This user has not provided a bio.</i>
{% endif %}
{# Below is the movie list (this is comment) #}
<h5>{{ user.username }}'s Watchlist ({{ movies|length }}):</h5>
<ul>
    {% for movie in movies %}
    <li>{{ movie.name }} - {{ movie.year }}</li>
    {% endfor %}
</ul>
</body>
</html>

```

----

## 模板上下文

（1）内置上下文变量

`config`、`request`、`session`、`g`，全部模板都可以使用

（2）自定义上下文

```python
@app.context_processor
def inject_foo():
    foo = "I'm your love!"
    return dict(foo=foo)
```

上面的代码相当于向所有的的模板中都传入了一个名为 `foo` 的变量，可以直接使用。

---

## 自定义模板全局函数

```python
@app.template_global()
def bar():
    return "i am man!"
```

---

## 过滤器

获取变量 `name` 的长度

```html
{{ name|length }}
```

将一段文字全部大写：

```
{% filter upper %}
	This text becomes uppercase
{% endfilter %}
```

（1）内置过滤器

......

过滤器可以重叠使用

```
{{ name|title|length }}
```

（2）自定义过滤器

使用 `app.template_filter` 装饰器

```python
# 自定义过滤器
@app.template_filter()
def author(name):
    return name + "baishng"
```

在使用时与其他过滤器的用法相同

```jinja2
{{ user.name|author }}
```

或者使用`app.add_template_filter()`方法注册自定义过滤器，例如

```python
@app.add_template_filter(函数名, [name=过滤器名])
```



---

## 测试器

（1）内置测试器

例如：使用 `number` 测试器来判断一个变量或表达式是否是数字

```jinja2
{% if age is number %}
	{{ age * 365 }}
{% else %}
	无效的数字
{% endif %}
```

（2）自定义测试器

```python
@app.template_test()
def baz(n):
  if n == 'baz':
    return True
  return False
```

或者使用 `app.add_template_test()` 函数注册自定义测试器，例如：

```python
@app.add_template_test(函数名, [name=测试器别名])
```

---

## 局部模板

局部模板的命名通常以一个下划线开始。

使用 `include` 标签来插入一个局部模板，这会把局部模板的全部内容插入到在使用 `include` 标签的位置。

例如：

```jinja2
{% include "_banner.html" %}
```

----

## 宏

就像python中的函数一样.

`macros.html`

```jinja2
{% macro qux(amount=1) %}
    {% if amount == 1 -%}
        I am qux.
    {%- elif amount > 1 -%}
        We are quxs.
    {%- endif %}
{% endmacro %}

{% macro static_file(type, filename_or_url, local=True) %}
    {% if local -%}
        {% set filename_or_url = url_for('static', filename=filename_or_url) %}
    {%- endif %}
    {% if type == 'css' -%}
        <link rel="stylesheet" href="{{ filename_or_url }}" type="text/css">
    {%- elif type == 'js' -%}
        <script type="text/javascript" src="{{ filename_or_url }}"></script>
    {%- elif type == 'icon' -%}
        <link rel="icon" href="{{ filename_or_url }}">
    {%- endif %}
{% endmacro %}
```

宏的使用也像 python 中的模块一样需要导入，例如：

```jinja2
{% from 'macros.html' import qux %}
```

---

## 模板继承

1、编写基模板

`base.html`

```html
<!DOCTYPE html>
<html>
<head>
    {% block head %}
        <meta charset="utf-8">
        <title>{% block title %}Template - HelloFlask{% endblock %}</title>
        <link rel="icon" type="image/x-icon" href="{{ url_for('static', filename='favicon.ico') }}">
        {% block styles %}
            <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css' ) }}">
        {% endblock %}
    {% endblock %}
</head>
<body>
<nav>
    <ul><li><a href="{{ url_for('index') }}">Home</a></li></ul>
</nav>

<main>
    {% for message in get_flashed_messages() %}
        <div class="alert">{{ message }}</div>
    {% endfor %}
    {% block content %}{% endblock %}
</main>
<footer>
    {% block footer %}
        <small> &copy; 2018 <a href="http://greyli.com" title="Written by Grey Li">Grey Li</a> /
            <a href="https://github.com/greyli/helloflask" title="Fork me on GitHub">GitHub</a> /
            <a href="http://helloflask.com" title="A HelloFlask project">HelloFlask</a>
        </small>
    {% endblock %}
</footer>
{% block scripts %}{% endblock %}
</body>
</html>
```

2、编写子模版

`index.html`

```jinja2
{% extends 'base.html' %}
{% from 'macros.html' import qux %}		# 这是一个宏

{% block content %}
{% set name='baz' %}
<h1>Template</h1>
<ul>
    <li><a href="{{ url_for('watchlist') }}">Watchlist</a></li>
    <li>Filter: {{ foo|musical }}</li>
    <li>Global: {{ bar() }}</li>
    <li>Test: {% if name is baz %}I am baz.{% endif %}</li>
    <li>Macro: {{ qux(amount=1) }}</li>
    <li><a href="{{ url_for('watchlist_with_static') }}">Watchlist with image and styles.</a></li>
    <li><a href="{{ url_for('just_flash') }}">Flash something</a></li>
</ul>
{% endblock %}
```

子模块中的 block 一般都是对父模块中的 block 中的内容进行覆盖，但是也可以对其进行追加内容操作，例如：

```jinja2
{% block style %}
{{ super() }}
<style>
	.foo {
		color: red;
	}
</style>
{% endblock %}
```

----

## 加载静态文件

静态文件的根目录在与主脚本同级的 `static` 目录下。

例如：

```jinja2
<img src="{{ urk_for('static', 'avatar.jpg') }}">
```

```jinja2
<script src="{{ url_for('static', 'js/register.js') }}"></script>
```

---

## 消息闪现

闪现的消息存储在 `session` 中，所以需要设置 `secret_key`，刷新页面后，消息会消失。

```python
from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'anhygdf'	

@app.route('just_flash')
def just_flash():
    flash("你好，我是一个消息闪现")
    return redirect(url_for('index'))
```

index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>这是一个flask测试</title>
</head>
<body>

{% for message in get_flashed_messages() %}
    <div class="alert">{{ message }}</div>
{% endfor %}

<p>这是一个测试</p>
</body>
</html>

<script src="{{ url_for('static',filename='alert.js') }}"></script>
```

----

## 自定义错误页面

注册错误处理函数

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
  return render_template('errors/404.html'), 404
```

errors/404.html

```jinja2
{% extends 'base.html' %}

{% block title %}404 - Page Not Found{% endblock %}

{% block content %}
<h1>Page Not Found</h1>
<p>You are lost...</p>
{% endblock %}
```

## 定义WTForms表单类

```python
from wtformsfrom wtforms import Form, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=128)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')
```

字段属性名称必须与HTML中对应的表单的 `<inut>` 元素的 `name` 属性的值一致。

字段属性的名称将作为对应的HTML`<input>`元素的`name`属性及`id`属性值。

字段属性名称大小写敏感，不能以下划线或`validate`开头。

`FlaskForm `类继承 `Form` 类，下面使用继承 `FlaskForm`  类的 `LoginForm` 表单

```python
from flask_wtf import FlaskForm
from wtformsfrom wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=128)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')
```

配置建 `WTF_CSRF_ENABLES` 用来设置是否开启 CSRF 保护，默认为 True。`FlaskForm` 会自动在实例化表单类时添加一个包含 CSRF 令牌值的隐藏字段，字段名为 `csrf_token` .

---

