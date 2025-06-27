---
title: tkinter库的使用
---

引入tkinter库

```python
import tkinter as tk
```

创建窗口：

```python
window = tk.Tk()
```

设置窗口信息

```python
window.title('白生')				# 设置标题
window.geometry('1000x800')		  # 窗口大小，长x宽
window.update()					 # 更新窗口信息，如长、宽等，可用对象.winfo_height()函数得到
canvas = tk.Canvas(window, height=window.winfo_height(), width=window.winfo_width())  # 创建画布
window.resizable(width=False, height=True)  # 禁止窗口调整大小
```

Label标签

```python
# 方法一：
main_label = tk.Label(window, text='DES算法的OFB演示', font=('#f0f0f0', 25))
main_label.pack()

# 方法二：
tk.Label(window, text='明文:', width=5, height=2, anchor='e', font=('#0f0f0f', 13)).place(relx=0, y=730)
```

