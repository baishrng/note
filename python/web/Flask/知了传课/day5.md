---
Flask--学习第五天
---

## 【实战】搜索功能实现

定义一个视图函数

blueprints/qa.py

```python
@bp.route('/search')
def search():
    key = request.args.get("key")
    questions = QuestionModel.query.filter(QuestionModel.title.contains(key)).all()
    return render_template("index.html", questions=questions)   # 重新渲染首页
```

修改`base.html`页面

```html
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
                    <a class="nav-link" href="{{ url_for("qa.publish_qa") }}">发布问答</a>
                </li>
                <li class="nav-item ml-2">
                    <form class="form-inline my-2 my-lg-0" method="GET" action="{{ url_for('qa.search') }}">
                        <input class="form-control mr-sm-2" type="search" placeholder="关键字" aria-label="Search"
                               name="key">
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

