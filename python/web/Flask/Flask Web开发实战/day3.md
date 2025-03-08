---
学习Flask Web开发实战--第三天
---

## 验证表单数据

WTForms验证表单字段的方式是在实例化表单类时传入表单数据，然后对表单实例调用`validate()`方法。

因为表单基本上都是POST方法提交，如果单纯使用WTForms，我们在实例化表单类时需要首先把`request.form`传入表单类，而使用Flask-WTF时，表单类继承的FlaskForm基类默认会哦那个`request.form`获取表单数据，所以不需要手动传入。

例如：

当 `LoginForm`类继承的是`FlaskForm`时：（这种方法是有可取之处的）

```python
from flask_wtf import FlaskForm
from flask import request, reder_template, redircet, url_for

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')
    
@app.route('/form', methods=['GET', 'POST'])
def just_form():
	if request.method == 'GET':
    render_template("login.html")
  else:
		form = LoginForm()
    if form.validate():
      username = form.username.data
      password = form.password.data
      return redirect(url_for('index'))
    else:
      print(form.errors)
			return redirect(url_for('index'))
```

当 `LoginForm`类继承的是`Form`时：

```python
from wtforms import Form
from flask import request, reder_template, redircet, url_for

class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')
    
@app.route('/form', methods=['GET', 'POST'])
def just_form():
	if request.method == 'GET':
    render_template("login.html")
  else:
		form = LoginForm(request.form)
    if form.validate():
      username = form.username.data
      password = form.password.data
      return redirect(url_for('index'))
    else:
      print(form.errors)
      return redirect(url_for('index'))
```

当验证表单数据成功后，必须要进行重定向操作，不能返回一个渲染的界面。

----

## 自定义验证器

1、行内验证器

针对铁定字段的验证器

```python
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import ValidationError

class FortyTwoForm(FlaskForm):
    answer = IntegerField('The number')
    submit = SubmitField('Submit')
    
    def validate_answer(self, field):
        if field.data != 42:
            raise ValidationError
```

2、全局验证器

当不需要传入参数定义验证器，则如下所示例：

```python
from wtforms.validators import ValidationError, Length
from wtforms import IntegerField, SubmitField
from flask_wtf import FlaskForm

def is_42(form, field):
    if field.data != 42:
        raise ValidationError
    
class FortyTwoForm(FlaskForm):
    answer = IntegerField(validators=[is_42])
    submit = SubmitField('Submit')
```

当需要传入参数时，则如下所示：

```python
from wtforms.validators import ValidationError, Length
from wtforms import IntegerField, SubmitField
from flask_wtf import FlaskForm

def is_42(message=None):
    if message is None:
        message = "Must be 42."
    
    def _is_42(form, field):
        if field.data != 42:
            raise ValidationError
        
    return _is_42
    
class FortyTwoForm(FlaskForm):
    answer = IntegerField(validators=[is_42])
    submit = SubmitField('Submit')
```

---

## 创建上传表单

创建文件上传表单

```python
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    photo = FileField("上传头像", validators=[FileRequired, FileAllowed(['jpg', 'jpeg', 'png'])])
```

限制文件上传大小：

```python
app.config[MAX_CONTENT_LENGTH] = 3 *1024 * 1024	// 	将最大长度限制为3M
```

限制文件上传大小

---

## 处理上传文件

```python
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.photo.data
        filename = random_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        flash('Upload success.')
        session['filenames'] = [filename]
        return redirect(url_for('show_images'))
    return render_template('upload.html', form=form)
```

```PYTHON
app.config['UPLOAD_PATH'] = os.path.join(app.rppt_path, 'uploads')
```

---

