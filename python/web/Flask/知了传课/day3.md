---
Flask--学习第三天
---

## 发送邮箱验证码功能实现（2）

创建邮箱验证码模型

models.py

```python
from exts import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    emial = db.Column(db.String(100), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)    # 这里需要的是一个函数，而不是函数的值

class EmialCaptchaModel(db.Model):
    __tablename__ = 'emial_captcha'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    captcha = db.Column(db.String(10), nullable=False)
```

将模型同步数据库，在命令行输入以下命令

```
flask db migrate

flask db upgrade
```

编写处理逻辑

blueprints/auth.py

```python
from flask import Blueprint, render_template, request, jsonify
from exts import mail, db
from flask_mail import Message
import string
import random
from models import EmialCaptchaModel

# /auth
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login')
def login():
    return "欢迎进行登录界面"

@bp.route('/register')
def register():
    return render_template('register.html')

@bp.route('/mail/test')
def mail_test():
    message = Message(subject="邮箱测试", recipients=['3155729148@qq.com', 'baishng@163.com'], body="这是一条测试邮件")
    mail.send(message)
    return "邮件发送成功"

# 用get方式传参
@bp.route('/captcha/email')
def get_email_captcha():
    email = request.args.get('email')
    source = string.digits*4
    captcha = random.sample(source, 4)  # 4位随机验证码
    captcha = "".join(captcha)  # 将数组转换成字符串
    print(email, captcha)

    # 发送邮件
    message = Message(subject="注册验证码", recipients=[email], body=f"您的验证码是：{captcha}, 请不要轻易泄露！")
    mail.send(message)

    # 存储验证码，这里使用的是数据库存储（改进可以用memcache/redis）
    email_captcha = EmialCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    # RESTful API, 统一格式
    # {code: 200/400/500, message: "", data: {}}
    return jsonify({"code":200, "message":"", "data":None})
```

返回数据的格式需要一致，这里返回的是json格式，所以需要导入`jsonify`

```python
from flask import jsonify
```

----

## 发送邮箱验证码功能实现（3）

主要是前端部分的内容，主要是写注册功能的`js`文件。

register.js

```javascript
// 整个网页都加载完毕后执行
$(function(){
    // 通过id获取按键元素
    $("#captcha-btn").click(function(event){
       // 阻止默认的事件
       event.preventDefault();

       var email = $("input[name='email']").val();
       $.ajax({
           url: "/auth/captcha/email?email=" + email,
           method: "GET",
           success: function(result){
               var code = result['code'];
               if(code == 200){
                   alert("邮箱验证码发送成功！");
               } else{
                   alert(result["message"]);
               }
           },
           fail: function(error){
               console.log(error);
           },
       })
    });
});
```

---

## 发送邮箱验证码功能实现（4）

实现 点击“获取验证码”按钮后，该按钮上编程一个倒计时。主要也是前端的内容。

register.js

```javaScript
function bindEmailCaptchaClick(){
    // 通过id获取按键元素
    $("#captcha-btn").click(function(event){
        // $this: 表示当前按钮的jquery对象
        var $this = $(this)

       // 阻止默认的事件
       event.preventDefault();

       var email = $("input[name='email']").val();
       $.ajax({
           url: "/auth/captcha/email?email=" + email,
           method: "GET",
           success: function(result){
               var code = result['code'];
               if(code == 200){
                   var countdown = 60; // 倒计时 60 秒
                   // 开始倒计时之前，就取消按钮的点击事件
                   $this.off("click");
                   var timer = setInterval(function(){
                       $this.text(countdown);
                       countdown -= 1;
                       // 倒计时结束的时候执行
                       if( countdown <= 0 ){
                           // 清除定时器
                           clearInterval(timer);
                           // 将按钮的文字重新修改回来
                           $this.text("获取验证码");
                           // 重新绑定点击事件
                           bindEmailCaptchaClick();
                       }
                   }, 1000)  // 每 1000毫秒(也就是每1秒)执行前面指定的函数
                   alert("邮箱验证码发送成功！");
               } else{
                   alert(result["message"]);
               }
           },
           fail: function(error){
               console.log(error);
           },
       })
    });
}


// 整个网页都加载完毕后执行
$(function(){
    bindEmailCaptchaClick();
});
```

---

## 实战：后端注册表单验证器实现

首先需要验证表单数据，需要安装`flask-wtf`，这是`wtforms`的`flask`版本

安装`flask-wtf`，会自动安装`wtforms`

```python
pip install flask-wtf
```

新建py文件，blueprints/forms.py

```python
import wtforms
from wtforms.validators import Email, Length, EqualTo
from models import UserModel, EmialCaptchaModel
from exts import db

# Form: 主要就是用来验证前端提交的数据是否符合要求
class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误！")])
    captcha = wtforms.StringField(validators=[Length(min=4, max=4, message="验证码格式错误！")])
    username = wtforms.StringField(validators=[Length(min=3, max=20, message="用户名格式错误！")])
    password = wtforms.StringField(validators=[Length(min=3, max=20, message="密码格式错误！")])
    password_confirm = wtforms.StringField(validators=[EqualTo(fieldname="password", message="密码不一致")])

    # 自定义验证
    # 1.邮箱是否已经被注册
    def validate_email(self, filed):
        email = filed.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="该邮箱已经被注册！")

    # 2.验证码是否正确
    def validate_captcha(self, filed):
        captcha = filed.data
        email = self.email.data
        captcha_model = EmialCaptchaModel.query.filter_by(email=email, captcha=captcha).first()
        if not captcha_model:
            raise wtforms.ValidationError(message="邮箱或验证码错误！")
        # todo: 可以在数据库中删掉captcha_model, 或可以在模型中新增一个字段表示已经使用过了,
        #  然后数据库定期清理, 或可以使用多线程/异步的方式执行删除
        # else:
        #     db.session.delete(captcha_model)
        #     db.sessiom.commit()
```

在 Python 中，`# todo:` 是一种**特殊注释格式**，用于标记代码中待完成的任务或需要后续处理的部分。它的核心作用是 **提醒开发者此处有未完善的功能、待修复的问题或需优化的代码**。

---

## 后端注册功能完成

`wtforms`的邮箱验证功能需要用到另一个库`email_validator`，所以需要安装这个库

```
pip install email_validator
```

重写`blueprints/auth.py`中的`register()`函数

```python
from flask import Blueprint, render_template, request, jsonify, redirect
from exts import mail, db
from flask_mail import Message
import string
import random
from models import EmialCaptchaModel, UserModel
from .forms import RegisterForm
from werkzeug.security import generate_password_hash

# /auth
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login')
def login():
    return "欢迎进行登录界面"

# GET: 从服务器上获取数据
# POST: 将客户端的数据提交给服务器
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # 验证用户提交的邮箱和验证码是否正确
        # 表单验证: flask-wtf: wtforms
        form = RegisterForm(request.form)
        if form.validate(): # 会自动执行 RegisterForm中的验证方法，包括自定义的方法
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect("login")   # 注册成功，将页面重定向到登录界面
        else:
            print(form.errors)
            return redirect('register')

@bp.route('/mail/test')
def mail_test():
    message = Message(subject="邮箱测试", recipients=['3155729148@qq.com', 'baishng@163.com'], body="这是一条测试邮件")
    mail.send(message)
    return "邮件发送成功"

# 用get方式传参,如果没有指定methods参数，默认就是GET请求
@bp.route('/captcha/email', methods=["GET"])
def get_email_captcha():
    email = request.args.get('email')
    source = string.digits*4
    captcha = random.sample(source, 4)  # 4位随机验证码
    captcha = "".join(captcha)  # 将数组转换成字符串
    print(email, captcha)

    # 发送邮件
    message = Message(subject="注册验证码", recipients=[email], body=f"您的验证码是：{captcha}, 请不要轻易泄露！")
    mail.send(message)

    # todo: 存储验证码，这里使用的是数据库存储（改进可以用memcache/redis）
    email_captcha = EmialCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    # RESTful API, 统一格式
    # {code: 200/400/500, message: "", data: {}}
    return jsonify({"code":200, "message":"", "data":None})

```

测试中发现密码长度不够，所以将user表中的password字段的长度从100增加到200

----

## 【实战】登录页面模板渲染完成

修改`blueprints/auth.py`中的`login()`函数

```python
@bp.route('/login')
def login():
    return render_template("login.html")
```

----

## 【实战】登录功能后端实现

重写`blueprints/auth.py`中的`login()`函数

```python
from flask import Blueprint, render_template, request, jsonify, redirect, session
from exts import mail, db
from flask_mail import Message
import string
import random
from models import EmialCaptchaModel, UserModel
from .forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱在数据库中不存在")
                return redirect('login')
            if check_password_hash(user.password, password):
                # cookie:
                # cookie中不适合存储太多的数据，只适合存储少量的数据
                # cookie一般用来存放登录授权的东西
                # flask中的session，是经过加密后存储在cookie中的
                session['user_id'] = user.id
                return redirect("/")    # 跳转到首页
            else:
                print("密码错误！")
                return redirect('login')
        else:
            return redirect('login')

```

这里需要在`config.py`中设置`SECRET_KEY`，这个变量用于对`session`中的值进行加`salt`操作。

config.py

```python
......

SECRET_KEY = "baishngshdbfd"
```

---

## 【实战】两个钩子函数

钩子函数：在执行其他之前先执行本函数。

app.py

```python
from flask import Flask, session, g
import config
from exts import db, mail
from models import UserModel
from blueprints.auth import bp as auth_bp
from blueprints.qa import bp as qa_bp
from flask_migrate import Migrate

# 钩子函数：在执行其他之前先执行本函数
# before_request/before_first_request/after_request
@app.before_request
def my_before_request():
    user_id = session.get("user_id", None)
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g, "user", user)    # g 是一个全局变量
    else:
        setattr(g, "user", None)
    
# 上下文处理器，所有的模板都可以访问这里面的内容（相当于模板中的全局变量）       
@app.context_processor
def my_context_processor():
    return {"user": g.user}
```

---

## 【实战】登录和非登录状态切换

首先在前端的`base.html`进行修改

base.html

第 42 - 56 行

```python
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="{{ url_for("static",filename="bootstrap/bootstrap.4.6.min.css") }}">
    <link rel="stylesheet" href="{{ url_for('static',filename='css/init.css') }}">
    {% block head %}

    {% endblock %}
    <title>{% block title %}

    {% endblock %}</title>
</head>

<body>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
        <a class="navbar-brand" href="#">知了问答</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="/">首页 <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="">发布问答</a>
                </li>
                <li class="nav-item ml-2">
                    <form class="form-inline my-2 my-lg-0" method="GET" action="">
                        <input class="form-control mr-sm-2" type="search" placeholder="关键字" aria-label="Search"
                               name="q">
                        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">搜索</button>
                    </form>
                </li>
            </ul>
            <ul class="navbar-nav">
                {% if user %}
                    <li class="nav-item">
                        <span class="nav-link">{{ user.username }}</span>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for("auth.logout") }}">退出登录</a>
                    </li>
                {% else %}
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for("auth.login") }}">登录</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for("auth.register") }}">注册</a>
                    </li>
                {% endif %}


            </ul>
        </div>
    </div>
</nav>

<div class="container">
    {% block body %}
    {% endblock %}
</div>

</body>

</html>
```

然后在`blueprints/auth.py`中增加一个视图函数用以退出登录

```python
@bp.route('logout')
def logout():
    session.clear()
    return redirect('/')    # 重定向到 首页
```

----

## 【实战】发布问答页面渲染

首先是对`public_question.html`进行编写

public_question.html

```python
{% extends "base.html" %}

{% block title %}
	发布问答
{% endblock %}

{% block head %}

{% endblock %}

{% block body %}
    <div class="row" style="margin-top: 20px;">
        <div class="col"></div>
        <div class="col-10">
            <h1 style="text-align: center;">发布问答</h1>
            <form action="#" method="post">
                <div class="form-group">
                    <input type="text" name="title" class="form-control" placeholder="请输入标题">
                </div>
                <div class="form-group">
                    <textarea name="content" class="form-control" rows="10" placeholder="请输入内容"></textarea>
                </div>
                <div class="form-group" style="text-align: right;">
                    <button class="btn btn-primary">发布</button>
                </div>
            </form>
        </div>
        <div class="col"></div>
    </div>
{% endblock %}
```

然后在`blueprits/qa.py`中新增`publish_qa()`函数

blueprints/qa.py

```python
from flask import Blueprint, request, render_template, g

bp = Blueprint('qa', __name__, url_prefix='/')

@bp.route('/')
def index():
    return "这是首页"

@bp.route('/qa/publish', methods=['GET', 'POST'])
def publish_qa():
    # todo: 这里还应该判断是否已经登录
    if request.method == 'GET':
        return render_template('public_question.html')
```

----

## 【实战】发布问答后端功能实现

首先创建问题的模型

models.py

```python
class QuestionModel(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

    # 外键
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship(UserModel, backref="questions")
```

然后同步到数据库

```
flask db migrate

flask db upgrade
```

然后在`blueprints/forms.py`中写检查表单数据的类

blueprints/forms.py

```python
class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=3, max=100, message="标题长度错误！")])
    context = wtforms.StringField(validators=[Length(min=3, message="内容长度不足！")])
```

然后在`blueprints/qa.py`中写发布问答的逻辑

blueprints/qa.py

```python
from flask import Blueprint, request, render_template, g, url_for, redirect
from .forms import QuestionForm
from models import QuestionModel
from exts import db

bp = Blueprint('qa', __name__, url_prefix='/')

@bp.route('/')
def index():
    return "这是首页"

@bp.route('/qa/publish', methods=['GET', 'POST'])
def publish_qa():
    # todo: 这里还应该判断是否已经登录
    if request.method == 'GET':
        return render_template('public_question.html')
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect(url_for("qa.detail"))
        else:
            print(form.errors)
            return redirect(url_for("qa.publish_qa"))

@bp.route('qa/detail')
def detail():
    return "这是详情页面"
```

----

## 【实战】登录装饰器的实现

实现在用户没有登录的情况下无法访问发布问答页面。

装饰器本身来讲就是函数。

新建py文件，decorators.py

```python
from functools import wraps
from flask import g, redirect, url_for

def login_required(func):
    # 保留func的信息
    @wraps(func)
    # 位置参数都在*args中，关键字参数都在**kwargs中
    def inner(*args, **kwargs):
        if g.user:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("auth.login"))
    return inner
```

修改`blueprints/qa.py`中的`publish_qa()`函数

blueprints/qa.py

```python
from decorators import login_required

@bp.route('/qa/publish', methods=['GET', 'POST'])
@login_required
def publish_qa():
    if request.method == 'GET':
        return render_template('public_question.html')
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect(url_for("qa.detail"))
        else:
            print(form.errors)
            return redirect(url_for("qa.publish_qa"))
```

