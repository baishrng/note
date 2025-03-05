---
Flask--学习第一天
---

## 注册路由

 注册路由

```python
from flask import Flask, request

@app.route('/')
def index():
    return '<h1>Hello World</h1>'
  
@app.route('/zh')
def zh():
    return '<p>ch</p>'
```

---

 注册多路路由

```python
@app.route('/')
@app.route('/hello')
@app.route('/hi')
def index():
    return '<h1>Hello World</h1>'
```

---

注册带参数的路由

```python
@app.route('/greet/<int:number>')     # 带参路由(int型参数)
def greet(number):
    return '<h1>hello %d</h1>' % number
    
@app.route('/greee/<name>')     # 带参路由(str型参数)
def greet(name):
    return '<h1>hello %s</h1>' % name
```

---

带默认参数的路由

```python
@app.route('/greet', defaults={'name':'padder'})    # 默认参数路由
@app.route('/greet/<int:name>')     # 带参路由(int型参数)
def greet(name):
    return '<h1>hello %s</h1>' % name
```

---

## 获取参数

```python
from flask import Flask, request, render_template

@app.route('/para')
def para():
    para = request.args.get('para', default=123, type=int)
    return f'你传入的参数为{para}'
```

---

## 渲染

普通渲染

```python
@app.route('/render')
def render():
    return render_template('index.html')
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>这是一个flask测试</title>
</head>
<body>
<p>这是一个测试</p>
</body>
</html>
```

---

带参数的渲染

1、普通传参

```python
@app.route('/html_para/<html_para>')
@app.route('/html_para', defaults={'html_para': 'test'})
def html_para(html_para):
    return render_template('html_para.html', html_para=html_para)
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>这是一个测试2</title>
</head>
<body>
<p>html页面传入的参数：{{ html_para }}</p>
</body>
</html>
```

2、对象传参

```python
class User:
  def __init__(self, name, emial):
    self.name = name
    self.emial = emial

@app.route('/test_html_dict_para')
def test_html_dict_para():
    user = User('张三', 'emial@qq.com')
    return render_template('test_html_dict_para.html', user=user)
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>test_html_dict_para</title>
</head>
<body>
<div>{{ user.name }} / {{ user.emial }} - {{ user.emial}}</div>
</body>
</html>
```

3、字典传参

```python
@app.route('/test_html_dict_para')
def test_html_dict_para():
    user = {'name':'张三',
            'emial':'123@qq.com'}
    # user = User('张三', 'emial@qq.com')
    return render_template('test_html_dict_para.html', user=user)
```

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>test_html_dict_para</title>
</head>
<body>
<div>{{ user.name }} / {{ user.emial }} - {{ user.emial}}</div>
</body>
</html>

---

## 过滤器

过滤器的使用

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>test_html_dict_para</title>
</head>
<body>
<!-- 过滤器：使用管道符（|）表示，该语句表示电子邮件的长度  -->
<div>{{ user.name }} / {{ user.emial }} - {{ user.emial|length }}</div>
</body>
</html>
```

自定义过滤器

```python
# 自定义过滤器
def fun(text):
    return '过滤器'
app.add_template_filter(fun, 'fun')
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>test_html_dict_para</title>
</head>
<body>
<!-- 过滤器：使用管道符（|）表示，该语句表示电子邮件的长度  -->
<div>{{ user.name }} / {{ user.emial }} - {{ user.emial|length }}</div>
</body>
</html>
```

---

## Jinja2--控制语句

if - else

```python
@app.route('/controll')
def controll_statement():
    age = request.args.get('age', default=17, type=int)
    return render_template('controll_statement.html', age=age)
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Jinja2控制语句</title>
</head>
<body>
{%  if age > 18 %}
    <div>已满18岁</div>
{% elif age<18 %}
    <div>未满18岁</div>
{%  else %}
    <div>刚好18岁</div>
{% endif %}
</body>
</html>
```

for循环

```python
@app.route('/controll')
def controll_statement():
    age = request.args.get('age', default=17, type=int)
    books = [{
        'name':'三国演义',
        'author':'罗贯中'
    },{
        'name':'西游记',
        'author':'吴承恩'
    },{
        'name':'红楼梦',
        'author':'曹雪芹'
    },{
        'name':'水浒传',
        'author':'施耐庵'
    }]
    return render_template('controll_statement.html', age=age, books=books)
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Jinja2控制语句</title>
</head>
<body>
{%  if age > 18 %}
    <div>已满18岁</div>
{% elif age<18 %}
    <div>未满18岁</div>
{%  else %}
    <div>刚好18岁</div>
{% endif %}

{% for book in books %}
    <div>{{ book.name }} : {{ book.author }}</div>
{% endfor %}
</body>
</html>
```

> 注意：没有 `break` 语句

---

## Jinja2 -- 模板继承

```python
@app.route('/child1')
def child1():
    return render_template('child1.html')
```

base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
<ui>
    <li><a href="">首页</a></li>
    <li><a href="">新闻</a></li>
</ui>
{% block body %}
{% endblock %}
<footer>这是底部的标签</footer>
</body>
</html>
```

child1.html

```html
{% extends "base.html" %}

{% block title %}
	这是child1的标题
{% endblock %}

{% block body %}
	<div>我是child1的body</div>
{% endblock %}
```

---

## JInja2 --加载静态文件

```python
@app.route('/static')
def static_demo():
    return render_template('static.html')
```

static.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>这是测试静态文件的页面</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css')}}">
    <script src="{{ url_for('static', filename="js/my.js") }}"></script>
</head>
<body>
<img src="{{ url_for('static', filename='images/test.jpg') }}" alt="这是测试图片">
</body>
</html>
```

style.css

```css
body{
    background-color: pink;
}
```

my.js

```java
alert('我是my.js中执行的')
```

---

## 连接数据库

安装`pymysql`

```shell
pip install pymysql
```

安装`flask-sqlalchemy`

```shell
pip install flask-sqlalchemy
```

配置数据库信息

```python
HOSTNAME = '127.0.0.1'
PORT = 3306
USERNAME = 'xxxx'
PASSWORD = 'xxxx'
DATABASE = 'bai'
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

db = SQLAlchemy(app)
```

测试数据库是否连接成功

```python
with app.app_context():
    with db.engine.connect() as conn:
        rs = conn.execute(text("select 1"))
        print(rs.fetchone())    # 输出 (1,)
```

