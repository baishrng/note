---
Flask--学习第四天
---

## 【实战】首页问答列表渲染完成

首先是前端部分内容的编写

index.html

```python
{% extends "base.html" %}
{% block head %}
    <link rel="stylesheet" href="{{ url_for("static",filename="css/index.css") }}">
{% endblock %}
{% block title %}
    三月-首页
{% endblock %}
{% block body %}
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul class=flashes>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
    <div class="row" style="margin-top: 20px;">
        <div class="col"></div>
        <div class="col-10">
            <ul class="question-ul">
                {% for question in questions %}
                    <li>
                        <div class="side-question">
                            <img class="side-question-avatar" src="{{ url_for("static",filename="images/avatar.jpg") }}"
                                 alt="">
                        </div>
                        <div class="question-main">
                            <div class="question-title"><a
                                    href="">{{ question.title }}</a>
                            </div>
                            <div class="question-content">{{ question.content }}</div>
                            <div class="question-detail">
                                <span class="question-author">{{ question.author.username }}</span>
                                <span class="question-time">{{ question.create_time }}</span>
                            </div>
                        </div>
                    </li>
                {% endfor %}
            </ul>
        </div>
        <div class="col"></div>
    </div>
{% endblock %}
```

然后是编写`blueprints/qa.py`中的`index()`函数

```python
@bp.route('/')
@bp.route('/index')
def index():
    # todo: 数据过多时需要使用分页技术
    questions = QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()    # 倒序排序
    return render_template("index.html", questions=questions)
```

---

## 【实战】问答列表页渲染

实现功能：点击问题的标题跳转到详情页面

首先编写`detail.html`页面

detail.html

```html
{% extends "base.html" %}
{% block head %}
    <link rel="stylesheet" href="{{ url_for("static",filename="css/detail.css") }}">
{% endblock %}
{% block title %}
    {{ question.title }}
{% endblock %}


{% block body %}
    <div class="row" style="margin-top: 20px;">
        <div class="col"></div>
        <div class="col-10" style="background-color: #fff;padding: 20px;">
            <h3 class="page-title">{{ question.title }}</h3>
            <p class="question-info">
                <span>作者：{{ question.author.username }}</span>
                <span>时间：{{ question.create_time }}</span>
            </p>
            <hr>
            <p class="question-content">{{ question.content }}</p>
            <hr>
            <h4 class="comment-group-title">评论（{{ question.answers |length }}）：</h4>
            <form action="#" method="post">
                <div class="form-group">
                    <input type="text" placeholder="请填写评论" name="content" class="form-control">
                    <input type="hidden" name="question_id" value="{{ question.id }}">
                </div>
                <div class="form-group" style="text-align: right;">
                    <button class="btn btn-primary">评论</button>
                </div>
            </form>
            <ul class="comment-group">
                {% for answer in question.answers %}
                    <li>
                        <div class="user-info">
                            <img class="avatar" src="{{ url_for("static",filename="images/avatar.jpg") }}" alt="">
                            <span class="username">{{ answer.author.username }}</span>
                            <span class="create-time">{{ answer.create_time }}</span>
                        </div>
                        <p class="comment-content">{{ answer.content }}</p>
                    </li>

                {% endfor %}
            </ul>
        </div>
        <div class="col"></div>
    </div>
{% endblock %}
```

然后是在`blueprints/qa.py`中编写`qa_detail()`函数

```python
@bp.route('qa/detail/<qa_id>')
def qa_detail(qa_id: int):
    question =  QuestionModel.query.get(qa_id)
    return render_template("detail.html", question=question)
```

然后是改写`index.html`页面，将详情页面的链接首页上

```html
<div class="question-title"><a
                                    href="{{ url_for("qa.qa_detail", qa_id=question.id) }}">{{ question.title }}</a>
                            </div>
```

---

## 【实战】答案模型创建

在`models.py`中创建答案模型

```python
class AnswerModel(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    
    # 外键
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    
    # 关系
    question = db.relationship(QuestionModel, backref=db.backref("answers", order_by=create_time.desc()))
    # 在这个demo中，下面这个字段没有应用场景，所以可以不写
    # author = db.relationship(UserModel, backref="answers")
```

在命令行中同步模型到数据库

```
flask db migarate

flask db upgrade
```

---

## 【实战】发布答案功能实现

在`blueprints/frms.py`创建表单校验数据

```python
from wtforms.validators import Email, Length, EqualTo, InputRequired

class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[Length(min=3, message="内容长度不足！")])
    question_id = wtforms.IntegerField(validators=[InputRequired(message="必须要传入问题id")])
```

在`blueprints/qa.py`中编写`publish_answer()`函数

```python
# @bp.route('/answer/publish', methods=['POST'])
@bp.post('/answer/publish')		# 这句直接等同于上面那句
@login_required
def publish_answer():
    form = AnswerForm(request.form)
    if form.validate():
        content = form.content.data
        question_id = form.question_id.data
        answer = AnswerModel(question_id=question_id, content=content, author=g.user)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for("qa.qa_detail", question_id=question_id))
    else:
        print(form.errors)
        # 这里使用request.form.get("question_id")获取question_id是因为如果form验证不通过，则可能没有question_id这个值
        return redirect(url_for("qa.qa_detail", question_id=request.form.get("question_id")))
```

修改`detail.html`页面

```
{% extends "base.html" %}
{% block head %}
    <link rel="stylesheet" href="{{ url_for("static",filename="css/detail.css") }}">
{% endblock %}
{% block title %}
    {{ question.title }}
{% endblock %}


{% block body %}
    <div class="row" style="margin-top: 20px;">
        <div class="col"></div>
        <div class="col-10" style="background-color: #fff;padding: 20px;">
            <h3 class="page-title">{{ question.title }}</h3>
            <p class="question-info">
                <span>作者：{{ question.author.username }}</span>
                <span>时间：{{ question.create_time }}</span>
            </p>
            <hr>
            <p class="question-content">{{ question.content }}</p>
            <hr>
            <h4 class="comment-group-title">评论（{{ question.answers |length }}）：</h4>
            <form action="{{ url_for("qa.publish_answer") }}" method="post">
                <div class="form-group">
                    <input type="text" placeholder="请填写评论" name="content" class="form-control">
                    <!-- 下面这个输入是不会显示在页面上的，但是会传给后端 -->
                    <input type="hidden" name="question_id" value="{{ question.id }}">
                </div>
                <div class="form-group" style="text-align: right;">
                    <button class="btn btn-primary">评论</button>
                </div>
            </form>
            <ul class="comment-group">
                {% for answer in question.answers %}
                    <li>
                        <div class="user-info">
                            <img class="avatar" src="{{ url_for("static",filename="images/avatar.jpg") }}" alt="">
                            <span class="username">{{ answer.author.username }}</span>
                            <span class="create-time">{{ answer.create_time }}</span>
                        </div>
                        <p class="comment-content">{{ answer.content }}</p>
                    </li>

                {% endfor %}
            </ul>
        </div>
        <div class="col"></div>
    </div>
{% endblock %}
```

