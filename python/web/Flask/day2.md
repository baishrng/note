---
Flask--学习第二天
---

##  ORM模型与表的映射

ORM：对象关系映射

一个ORM模型与一张表对应

---

## ORM模型的CRUD操作

```python
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
app = Flask(__name__)

HOSTNAME = '127.0.0.1'
PORT = 3306
USERNAME = 'root'
PASSWORD = '123456'
DATABASE = 'ntru'
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

db = SQLAlchemy(app)

# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute(text("select 1"))
#         print(rs.fetchone())    # 输出 (1,)

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(200))
    user_IP = db.Column(db.String(20))
    is_online = db.Column(db.Integer)

# 若数据库中没有对应胡表，则创建表
with app.app_context():
    db.create_all()

# 增加
@app.route('/user/add')
def add_user():
    user = User(user_name='七三', user_IP='127.0.0.1', is_online=0)   # 创建ORM对象
    db.session.add(user)
    db.session.commit()
    return "用户创建成功"

# 查找
@app.route('/user/query')
def query_user():
    # 1.get查找，根据主键查找，只查一条数据
    # user = User.query.get(10002)
    # print(f'{user.user_id}, {user.user_name}, {user.user_IP}, {user.is_online}')

    # 2.filter_by
    users = User.query.filter_by(user_name='五月')
    for user in users:
        print(user.user_name)
    return "数据查找成功"

# 修改
@app.route('/user/update')
def update_user():
    user = User.query.filter_by(user_name='七三').first()
    user.user_IP = '192.168.31.52'
    db.session.commit()

    return "数据修改成功"

# 删除
@app.route('/user/delete_by_id')
def delete_by_id():
    user = User.query.get(10015)
    if user:
        db.session.delete(user)
        db.session.commit()

    return "数据删除成功"

@app.route('/user/delete_by_username')
def delete_by_username():
    users = User.query.filter_by(user_name='七三')
    print(users)
    for user in users:
        db.session.delete(user)
    db.session.commit()
    return "数据删除完成"
```

---

## ORM模型外键与表关系

```python
class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(200))
    user_IP = db.Column(db.String(20))
    is_online = db.Column(db.Integer)

class Article(db.Model):
    __tabelname__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)

    author_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    # 前半句等同于：Article.author = User.query.get(article.author_id)
    # backref:会自动给User模型添加一个articles的属性，用来获取文章列表
    author = db.relationship("User", backref='articles')

    # 上面的后半句可以改成
    # author = db.relationship("User", back_populates='articles')
    # 但是在User类中需要添加下面的语句
    # articles = db.relationship("Article", backref='articles')

# 若数据库中没有对应胡表，则创建表
with app.app_context():
    db.create_all()
```

```python
# 文章添加
@app.route('/article/add')
def add_article():
    article1 = Article(title="Flask学习", content="1234567890")
    article1.author = User.query.get(10014)

    article2 = Article(title="python web学习", content="acshjhudjnfgkjzh")
    article2.author = User.query.get(10013)

    db.session.add_all([article1, article2])
    db.session.commit()

    return "文章添加成功"

# 文章查找
@app.route('/article/query')
def query_article():
    user = User.query.get(10014)
    for article in user.articles:
        print(article.title)
    return "文章查找成功"
```

---

## flask-migrate迁移ORM模型

使用`db.create_all()`，当表中的字段增加或删除后，并不能同步更新到数据库中。

如想要达到想要的效果，需要安装另一个插件`flask-migrate`

安装`flask-migrate`

```shell
pip install flask-migrate
```

使用

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)

HOSTNAME = '127.0.0.1'
PORT = 3306
USERNAME = 'root'
PASSWORD = '123456'
DATABASE = 'ntru'
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

db = SQLAlchemy(app)

migrate = Migrate(app=app, db=db)
```

在虚拟环境的命令行中输入命令：（只要执行一次）

```shell
flask db init
```

然后运行命令（识别ORM模型的改变，生成迁移脚本）

```
flask db migrate
```

然后运行命令（运行迁移脚本，同步到数据库中）

```
flask db upgrade
```

以后需要更新同步数据库只运行后面两个命令即可

---

## 完整代码

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)

HOSTNAME = '127.0.0.1'
PORT = 3306
USERNAME = 'root'
PASSWORD = '123456'
DATABASE = 'ntru'
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

db = SQLAlchemy(app)

migrate = Migrate(app=app, db=db)
# migrate.init_app(app=app, db=db)

# 模型映射成表的三步
# 1.flask db init, 只要执行一次

# with app.app_context():
#     with db.engine.connect() as conn:
#         rs = conn.execute(text("select 1"))
#         print(rs.fetchone())    # 输出 (1,)

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(200))
    emial = db.Column(db.String(20))
    user_IP = db.Column(db.String(20))
    is_online = db.Column(db.Integer)

class Article(db.Model):
    __tabelname__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)

    author_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    # 前半句等同于：Article.author = User.query.get(article.author_id)
    # backref:会自动给User模型添加一个articles的属性，用来获取文章列表
    author = db.relationship("User", backref='articles')

    # 上面的后半句可以改成
    # author = db.relationship("User", back_populates='articles')
    # 但是在User类中需要添加下面的语句
    # articles = db.relationship("Article", backref='articles')

# 若数据库中没有对应胡表，则创建表
# with app.app_context():
#     db.create_all()


# 增加
@app.route('/user/add')
def add_user():
    user = User(user_name='七三', user_IP='127.0.0.1', is_online=0)   # 创建ORM对象
    db.session.add(user)
    db.session.commit()
    return "用户创建成功"

# 查找
@app.route('/user/query')
def query_user():
    # 1.get查找，根据主键查找，只查一条数据
    # user = User.query.get(10002)
    # print(f'{user.user_id}, {user.user_name}, {user.user_IP}, {user.is_online}')

    # 2.filter_by
    users = User.query.filter_by(user_name='五月')
    for user in users:
        print(user.user_name)
    return "数据查找成功"

# 修改
@app.route('/user/update')
def update_user():
    user = User.query.filter_by(user_name='七三').first()
    user.user_IP = '192.168.31.52'
    db.session.commit()

    return "数据修改成功"

# 删除
@app.route('/user/delete_by_id')
def delete_by_id():
    user = User.query.get(10015)
    if user:
        db.session.delete(user)
        db.session.commit()

    return "数据删除成功"

@app.route('/user/delete_by_username')
def delete_by_username():
    users = User.query.filter_by(user_name='七三')
    print(users)
    for user in users:
        db.session.delete(user)
    db.session.commit()
    return "数据删除完成"

# 文章添加
@app.route('/article/add')
def add_article():
    article1 = Article(title="Flask学习", content="1234567890")
    article1.author = User.query.get(10014)

    article2 = Article(title="python web学习", content="acshjhudjnfgkjzh")
    article2.author = User.query.get(10013)

    db.session.add_all([article1, article2])
    db.session.commit()

    return "文章添加成功"

# 文章查找
@app.route('/article/query')
def query_article():
    user = User.query.get(10014)
    for article in user.articles:
        print(article.title)
    return "文章查找成功"

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 实战：问答平台项目结构搭建

app.py

```python
from flask import Flask
import config
from exts import db
from models import UserModel
from blueprints.auth import bp as auth_bp
from blueprints.qa import bp as qa_bp

app = Flask(__name__)
app.config.from_object(config)  # 绑定配置文件

db.init_app(app)    # db 绑定 app

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(qa_bp, url_prefix='/')

if __name__ == '__main__':
    app.run()
```

exts.py

```python
"""为了解决循环引用的问题"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

```

config.py

```

```

models.py

```python
from exts import db

class UserModel(db.Model):
    pass
```

blueprints\auth.py

```python
from flask import Blueprint

# /auth
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login')
def login():
    return "欢迎进行登录界面"
```

blueprint/qa.py

```python
from flask import Blueprint

bp = Blueprint('qa', __name__, url_prefix='/')

@bp.route('/')
def index():
    return "这是首页"
```

## 实战：User模型创建

首先配置数据库信息

config.py

```python
# 数据库配置信息
HOSTNAME = '127.0.0.1'
PORT = 3306
DATABASE = 'xin'
USERNAME = 'xxxx'
PASSWORD = 'xxxx'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
```

User模型创建

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

```

迁移ORM模型

app.py

```python
from flask import Flask
import config
from exts import db
from models import UserModel
from blueprints.auth import bp as auth_bp
from blueprints.qa import bp as qa_bp
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(config)  # 绑定配置文件

db.init_app(app)    # db 绑定 app
migrate = Migrate(app, db)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(qa_bp, url_prefix='/')

if __name__ == '__main__':
    app.run()
```

一次在命令行输入以下命令：

```shell
flask db init
```

```
flask db migrate
```

```
flask db upgrade
```

---

## 实战：注册页面模板渲染

这里主要是前端部分，将静态的html页面改写成Jinja2模板，然后在auth.py中渲染出来

blueprints/auth.py

```python
from flask import Blueprint, render_template

# /auth
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login')
def login():
    return "欢迎进行登录界面"

@bp.route('/register')
def register():
    return render_template('register.html')
```

---

## 实战：Flask发送邮件功能实现

安装Flask_Mail

```
pip install flask-mail
```

邮箱配置

config.py

```python
# 数据库配置信息
HOSTNAME = '127.0.0.1'
PORT = 3306
DATABASE = 'xin'
USERNAME = 'xxxx'
PASSWORD = 'xxxx'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "xxx.qq.com"
MAIL_PASSWORD = "xxxxx"	# 授权码
MAIL_DEFAULT_SENDER = "xxx.qq.com"	# 邮箱发送者，与上面的一样
```

exts.py

```python
"""为了解决循环引用的问题"""

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()
```

app.py

```python
from flask import Flask
import config
from exts import db, mail
from models import UserModel
from blueprints.auth import bp as auth_bp
from blueprints.qa import bp as qa_bp
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(config)  # 绑定配置文件

db.init_app(app)    # db 绑定 app
mail.init_app(app)  # mail 绑定 app
migrate = Migrate(app, db)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(qa_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
```

测试发送邮件

blueprints/auth.py

```python
from flask import Blueprint, render_template
from exts import mail
from flask_mail import Message

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
    message = Message(subject="邮箱测试", recipients=['123456@qq.com', '123456@163.com'], body="这是一条测试邮件")
    mail.send(message)
    return "邮件发送成功"
```

---

## 实战：发送邮箱验证码功能实现（1）

blueprints/auth.py

```python
from flask import Blueprint, render_template, request
from exts import mail
from flask_mail import Message
import string
import random

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
    # 存储验证码，这里使用的是数据库存储（改进可以用memcache/redis）


    # 发送邮件
    message = Message(subject="注册验证码", recipients=[email], body=f"您的验证码是：{captcha}, 请不要轻易泄露！")
    mail.send(message)
    return 'success'
```

