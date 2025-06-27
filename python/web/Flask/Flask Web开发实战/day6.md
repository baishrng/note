---
学习Flask Web开发实战--第六天
---

## 设置缓存

安装 `flask_caching`

```
pip install flask_caching
```

设置 Cache

```python
from flask_caching import Cache
app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
```

为视图函数添加缓存

```python
@app.route('/bar')
@cache.cached(timeout=10 * 60)
def bar():
    time.sleep(1)
    return render_template('index.html')
```

```python
@app.route('/qux')
@cache.cached(query_string=True)
def qux():
    time.sleep(1)
    page = request.args.get('page', 1)
    return render_template('qux.html', page=page)
```

下面这个会将查询参数的散列值作为缓存的键

为普通函数添加缓存

```python
@cache.cached(key_prefix='add')
def add(a, b):
    time.sleep(2)
    return a + b
```

```python
# cache memorize (with argument)
@cache.memoize()
def add_pro(a, b):
    time.sleep(2)
    return a + b
```

下面这个会将函数参数一起作为 cache 键名

---

## 更新缓存

```python
@app.route('/baz')
@cache.cached(timeout=60 * 60)
def baz():
    time.sleep(1)
    return render_template('baz.html')
  
@app.route('/update/baz')
def update_baz():
    cache.delete('view/%s' % url_for('baz'))
    flash('Cached data for baz have been deleted.')
    return redirect(url_for('index'))
```

更新 `@cache.memoize()` 设置的缓存

```python
def del_pro_cache():
    cache.delete_memoized(add_pro)	# 传入对象名
```

清除所有缓存

```python
@app.route('/update/all')
def update_all():
    cache.clear()
    flash('All cached data deleted.')
    return redirect(url_for('index'))
```

