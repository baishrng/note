---
学习Flask Web开发实战--第五天
---

## 配置 Python Shell 上下文

```python
@app.shell_context_processor
def make_shell_context():
  return dict(db=db, Note=Note)
```

当你使用 flask shell 命令启动 Python Shell 时，所有使用 `app.shell_context_processor`装饰器注册的 shell 上下文处理函数都会被自动执行，这回将 db 和 Note 对象推送到 Python Shell 上下文里。

---

## 一对多关系

（1）单向关系

```python
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), unique=True)
    phone = db.Column(db.String(20))

    # 建立关系
    articles = db.relationship('Article')   # 另一侧的模型名称（单向关系）


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True)
    body = db.Column(db.Text)

    # 定义外键
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))   # 表名.主键字段名
```

也可以在 `Article` 类中建立联系而不在 `Author` 类中建立。即：

```python
author = db.relationship('Author')
```

（2）双向联系

```python
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), unique=True)
    phone = db.Column(db.String(20))

    # 建立关系
    articles = db.relationship('Article', back_populates='author')   # 另一侧的模型名称, 惯性另一侧的关系属性名


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True)
    body = db.Column(db.Text)

    # 定义外键
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))   # 表名.主键字段名
    
    # 定义关系
    author = db.relationship('Author', back_populates='articles')   # 另一侧的模型名称, 惯性另一侧的关系属性名
```

（3）使用 `backref` 建立双向关系

这种方式与（2）的方式达到的效果完全一致。

```python
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), unique=True)
    phone = db.Column(db.String(20))

    # 建立关系
    articles = db.relationship('Article', backref='author')   # 另一侧的模型名称, 惯性另一侧的关系属性名


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True)
    body = db.Column(db.Text)

    # 定义外键
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))   # 表名.主键字段名
```

---

## 一对一关系

```python
class Country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    
    # 建立联系
    capital = db.realationship('Capital', uselist=False)
    
class Capital(db.Model):
    __tablename__ = 'capital'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    
    # 定义外键
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    
    # 定义关系
    country = db.relationship('Country')
```

---

## 多对多关系

```python
association_table = db.Table('association',
                             db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
                             db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id'))
                             )


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), unique=True)
    grade = db.Column(db.String(20))
    teachers = db.relationship('Teacher',
                               secondary=association_table,
                               back_populates='students')  # 关系


class Teacher(db.Model):
    __tablename__= ‘teacher’
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), unique=True)
    office = db.Column(db.String(20))
    students = db.relationship('Student',
                               secondary=association_table,
                               back_populates='teachers')  # 关系
```

---

## 更新数据库表

使用 `Flask-Migrate`

1、安装 `Flask-Migrate`

```shell
pip install flask_migrate
```

2、实例化 `Flask-Migrate` 提供的 `Migrate` 类，进行初始化操作

```python
from flask import Flask
from flask_sqlalcheny import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

db = SQLAlcheny(app)
migrate = Migrate(app, db)	# 在db对象创建后调用
```

3、创建迁移环境

在命令行输入命令，迁移环境只需要创建一次，也就是说这个命令只使用一次。

```
flask db init
```

4、生成迁移脚本

输入命令

```
flask db migrate -m "备注信息"
```

5、更新数据库

输入命令

```
flask db upgrade
```

6、回滚迁移

使用命令

```
flask db downupgrade
```

会撤销最后一次迁移在数据库中的改动。

---

## 级联操作

级联行为通过关系函数 `relationship()`的 `cascade `参数设置。  

设置了 `cascade `参数的一侧将被视为父对象，相关的对象则被视为子对象。  

常用的配置组合如下所示 ：  

- `save-update、merge`（默认值）
- `save-update、merge、delete`
- `all`
- `all、delete`

```python
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.Text)
    comments = db.relationship('Comment', back_populates='post', cascade='all, delete-orphan')  # collection


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship('Post', back_populates='comments')  # scalar
```

---

## 事件监听

创建了 一个 Draft 模型类表示草稿 ， 其中包含 body字段和 edit_time字段，分别存储草稿正文和被修改的 次数，其 中 dedit_time字段 的 默认值为 0

```python
class Draft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    edit_time = db.Column(db.Integer, default=0)
```

通过注册事件监昕函数，我们可以实现在 body 列修改时，自动叠加表示被修改次数 的edit_ time 字段 。  

```python
@db.event.listens_for(Draft.body, 'set')
def increment_edit_time(target, value, oldvalue, initiator):
    if target.edit_time is not None:
        target.edit_time += 1
```

`listern_for()` 装饰器主要接收两个参数， `target `表示监听的对象 ， 这个对象可 以是模型类 、 类实例或类属性等 。`identifier`参数表示被监昕事件的标识符， 比如 ，用于监听属性的事件标识符有 set、append、remove、init_scalar、init_collection等

也可以通过如下方式注册事件监听函数：

```python
@db.event.listens_for(Draft.body, 'set', named=True)
def increment_edit_time(**kwargs):
    if kwargs['target'].edit_time is not None:
        kwargs['target'].edit_time += 1
```

----

## 使用 `Flask-Mail` 发送电子邮件

安装 `Flask-Mail`

```
pip install flask_mail
```

实例化 `Flask-Mail` 提供的 `Mail` 类井传入程序实例以完成初始化  

```python
from flask_mail import Mail
app = Flask(__name__)

mail = Mail(app)
```

实例化 `Mail `类时，`Flask-Mail`会获取配置以创建一个用于发信的对象，所以确保在实例化 `Mail `类之前加载配置。

```python
app = Flask(__name__)

app.config.update(
    SECRET_KEY=os.getenv('SECRET_KEY', 'secret string'),
    MAIL_SERVER=os.getenv('MAIL_SERVER'),
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
    MAIL_DEFAULT_SENDER=('Grey Li', os.getenv('MAIL_USERNAME'))
)

mail = Mail(app)
```

  构建邮件数据

```python
from flask_mail import Message
from app import mail

message = Message(subject="hello world!", recipients=[邮箱1, 邮箱2], body="这是正文内容")
```

发送邮件

```python
mail.send(message)
```

完整代码

```python
from flask_mail import Mail
from flask_mail import Message

app = Flask(__name__)

app.config.update(
    SECRET_KEY=os.getenv('SECRET_KEY', 'secret string'),
    MAIL_SERVER=os.getenv('MAIL_SERVER'),
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
    MAIL_DEFAULT_SENDER=('Grey Li', os.getenv('MAIL_USERNAME'))
)

mail = Mail(app)

message = Message(subject="hello world!", recipients=[邮箱1, 邮箱2], body="这是正文内容")
mail.send(message)
```

可以将发送邮件功能包装成一个通用函数：

```python
def send_smtp_mail(subject, to, body):
    message = Message(subject, recipients=[to], body=body)
    mail.send(message)
```

----

## 使用 Jinja2 模板组织邮件正文

纯文本邮件模板

```
Hello {{ name }},

Thank you for subscribing Flask Weekly!
Enjoy the reading :)

Visit this link to unsubscribe: {{ url_for('unsubscribe', _external=True) }}
```

HTML 邮件模板

```python
<div style="width: 580px; padding: 20px;">
    <h3>Hello {{ name }},</h3>
    <p>Thank you for subscribing Flask Weekly!</p>
    <p>Enjoy the reading :)</p>
    <small style="color: #868e96;">
        Click here to <a href="{{ url_for('unsubscribe', _external=True) }}">unsubscribe</a>.
    </small>
</div>

```

发信函数

```python
def send_subscribe_mail(subject, to, **kwargs):
    message = Message(subject, recipients=[to], sender='Flask Weekly <%s>' % os.getenv('MAIL_USERNAME'))
    message.body = render_template('emails/subscribe.txt', **kwargs)
    message.html = render_template('emails/subscribe.html', **kwargs)
    mail.send(message)
```

---

## 异步发送邮件

```python
from threading import Thread

def _send_async_mail(app, message):
    with app.app_context():
        mail.send(message)


def send_async_mail(subject, to, body):
    # app = current_app._get_current_object()  # if use factory (i.e. create_app()), get app like this
    message = Message(subject, recipients=[to], body=body)
    thr = Thread(target=_send_async_mail, args=[app, message])
    thr.start()
    return thr
```

因为 `Flask-Mail `的 `send()`方法内部的调用逻辑中使用了 `current_app` 变量，而这个变量只在激活的程序上下文中才存在，这里在后台线程调用发信函数，但是后台线程并没有程序上下文存在 。 为了正常实现发信功能，我们传入程序实例 `app `作为参数，并调用 `app.app_context()`手动激活程序上下文 。  