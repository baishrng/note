---
学习Flask Web开发实战--第一天
---

## 自定义 flask 命令

```python
@app.cli.command()
def echo_info():
    click.echo("flask 命令行测试")
```

然后在命令行中运行

```
flask echo_info
```

----

## flask routes

使用 `flask routes` 命令可以查看程序中定义的所有路由。

----

## 定义方法列表

```PYTHON
@app.route('/index', methods=['GET', 'POST'])
```

---

## URL变量转换器

url中含有变量，`<int:para>`叫做转换器，表示接受int型参数，但是我觉得可以不用转换器，直接使用`<para>`，因为在下面的视图函数的参数中规定了para参数为`int`型。

```python
@app.route('/render/<int:para>')
def render(para: int):
    print(para)
    return render_template("index.html")
```

---

## 请求钩子

有五种请求钩子：`before_first_request`,`before_request`,`after_request`,`tear_down`,`after_this_request`

```python
@app.before_request
def do_something():
	pass
```

---

## 重定向

```python
from flask import redirect, url_for
@app.route('/redirect')
def my_redirect():
    return redirect(url_for('hello_world'))
```

----

## 视图函数返回 json 格式的数据

```python
from flask import jsonify, Flask
@app.route('/json')
def my_json():
    data = {
        'name' : 'xin',
        'age' : 13
    }
    return jsonify(data)
```

---

## 自定义相应状态码

```python
from flask import jsonify
@app.route('/json')
def my_json():
    data = {
        'name' : 'xin',
        'age' : 13
    }
    return jsonify(data), 404
```

---

## 设置cookie

```python
@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)
    return response
```

---

## 设置session

1、设置程序密钥

方法一：

```python
app.secret_key = 'secret key'
```

方法二：（更安全）

设置成环境变量

```
SECRET_KEY = secret key
```

然后通过 os 模块设置

```
import os
app.secret_key = os.getenv('SECRET_KEY', 'abcdefhskns')
```

2、模拟用户登录

```python
from flask import Flask, session, url_for, redirect

@app.route('/login')
def login():
    session['logged_in'] = True
    return redirect(url_for('hello'))
```

----

## 上下文

程序上下文：`current_app`、`g`

请求上下文：`request`、`session`

手动激活程序上下文：

```python
# 方法一
with app.app_context() as app:
  pass
```

```python
# 方法二
app_ctx = app.app_context()
app_ctx.push()

pass

app_ctx.pop()
```

手动激活请求上下文

```python
# 方法一
with app.test_request_context('/hello'):
  pass
```

```python
# 方法二
request_ctx = app.test_request_context('/hello')
request_cts.push()

pass

request_cts.pop()
```

---

## 重定向回上一个页面

**1、获取上一个页面的URL**

两种方法：

（1）HTTP refer

通过 `request.referrer`，但是这个在很多情况下会为空值

```python
from flask import Flask, request, url_for

@app.route('/foo')
def foo():
  return '<h1>Foo page</h1><a href=%s>Do something and redirect</a>' % url_for('do_something')

@app.route('/bar')
def bar():
  return '<h1>Bar page</h1><a href=%s>Do something and redirect</a>' % url_for('do_something')

@qpp.route('/do_something')
def do_something():
  pass
	return redirect(request.referrer or url_for('hello'))
```

（2）查询参数

```python
from flask import Flask, request, url_for

@app.route('/foo')
def foo():
  return '<h1>Foo page</h1><a href=%s>Do something and redirect</a>' % url_for('do_something', next=request.full_path)

@app.route('/bar')
def bar():
  return '<h1>Bar page</h1><a href=%s>Do something and redirect</a>' % url_for('do_something', next=request.full_path)

@qpp.route('/do_something')
def do_something():
  pass
	return redirect(request.args.get('next', url_for('hello')))
```

（3）两种方法搭配一起使用

```python
from flask import Flask, request, url_for

@app.route('/foo')
def foo():
  return '<h1>Foo page</h1><a href=%s>Do something and redirect</a>' % url_for('do_something', next=request.full_path)

@app.route('/bar')
def bar():
  return '<h1>Bar page</h1><a href=%s>Do something and redirect</a>' % url_for('do_something', next=request.full_path)

# 这是一个通用的方法
def redirect_back(default='hello', **kwargs):
  for target in request.args.get('next'), request.referrer:
    if target:
      return redirect(target)
  return redirect(url_for(default), **kwargs)

@qpp.route('/do_something')
def do_something():
  pass
	return redirect_back()
```

**2、对URL进行安全验证**

验证重定向的URL是否是程序内部URL

```python
from urlparse import urlparse, urljoin

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc
```

修改`redirect_back()`函数

```python
def redirect_back(default='hello', **kwargs):
  for target in request.args.get('next'), request.referrer:
    if is_safe_url(target):
      return redirect(target)
  return redirect(url_for(default), **kwargs)
```

---

