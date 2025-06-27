---
学习Flask Web开发实战--第四天
---

## 富文本编辑框

使用 `Flask-CKEditor`

---

## 单个表单多个提交按钮

被按下的提交按钮在`request.form`中的值为`True`，没有被按下的值为`False`。

```python
class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(1, 50)])
    body = TextAreaField('Body', validators=[DataRequired()])
    save = SubmitField('Save')
    publish = SubmitField('Publish')
```

```python
@app.route('/two-submits', methods=['GET', 'POST'])
def two_submits():
    form = NewPostForm()
    if form.validate_on_submit():
        if form.save.data:
            # save it...
            flash('You click the "Save" button.')
        elif form.publish.data:
            # publish it...
            flash('You click the "Publish" button.')
        return redirect(url_for('index'))
    return render_template('2submit.html', form=form)
```

---

## 单个页面多个表单

（1）单视图处理

为两个表单的提交字段设置不同的名称，利用的是被点击的提交按钮的值为`True`。

```python
class SigninForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    submit1 = SubmitField('Sign in')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(1, 254)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    submit2 = SubmitField('Register')
```

```python
@app.route('/multi-form', methods=['GET', 'POST'])
def multi_form():
    signin_form = SigninForm()
    register_form = RegisterForm()

    if signin_form.submit1.data and signin_form.validate():
        username = signin_form.username.data
        flash('%s, you just submit the Signin Form.' % username)
        return redirect(url_for('index'))

    if register_form.submit2.data and register_form.validate():
        username = register_form.username.data
        flash('%s, you just submit the Register Form.' % username)
        return redirect(url_for('index'))

    return render_template('2form.html', signin_form=signin_form, register_form=register_form)
```

（2）多视图处理

将渲染页面页 处理请求的视图函数分离：

```python
@app.route('/multi-form-multi-view')
def multi_form_multi_view():
    signin_form = SigninForm2()
    register_form = RegisterForm2()
    return render_template('2form2view.html', signin_form=signin_form, register_form=register_form)
```

```python
@app.route('/handle-signin', methods=['POST'])
def handle_signin():
    signin_form = SigninForm2()
    register_form = RegisterForm2()

    if signin_form.validate_on_submit():
        username = signin_form.username.data
        flash('%s, you just submit the Signin Form.' % username)
        return redirect(url_for('index'))

    return render_template('2form2view.html', signin_form=signin_form, register_form=register_form)


@app.route('/handle-register', methods=['POST'])
def handle_register():
    signin_form = SigninForm2()
    register_form = RegisterForm2()

    if register_form.validate_on_submit():
        username = register_form.username.data
        flash('%s, you just submit the Register Form.' % username)
        return redirect(url_for('index'))
    return render_template('2form2view.html', signin_form=signin_form, register_form=register_form)
```

然后HTML页面中的`<form>`中的`action`属性值要只想各自的视图函数

```jinja2
<form method="post" action="{{ url_for('handle_signin') }}">

<form method="post" action="{{ url_for('handle_register') }}">
```

---

## 使用Flask-SQLAlchemy管理数据库

初始化操作

``` python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)
```

---

## 配置数据库URI

默认使用的是内存型 sqlite 数据库

```python
import os

...
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(app.root_path, 'data.db'))
```

----

## 定义数据库模型

```python
class Note(db.Model):
  __tablename__ = 'note'
  id = db.Column(db.Integer, primary_key=True)
  body = db.Column(db.Text)
```

---

## CRUD

（1）Create

```PYTHON
note1 = Note(body="hello world")
    note2 = Note(body="baishng")
    note3 = Note(body="I will be there.")
    db.session.add(note1)
    db.session.add_all([note2, note3])
    db.session.commit()
```

（2）Read

```python
note = Note.query.filter_by(body='baishng').first()
```

（3）Update

```python
note = Note.query.get(2)
note.body = "春风若有怜花意，可否许我再少年"
db.session.commit()
```

（4）Delete

```python
note = Note.query.get(2)
db.session.delete(note)
db.session.commit()
```

----

