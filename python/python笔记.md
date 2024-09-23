## py文件转exe文件



打开命令提示符，下载pyinstaller工具

```python
pip install pyinstaller
```

在命令提示符中找到要转换文件的位置，输入以下命令

```python
pyinstaller -F 文件名.py
```

转换后的文件在该目录下的 dist 文件夹下，Build和  _pycache_ 文件夹可以删除

暴力打包

```python
pyinstaller.exe -D .\main.py --collect-all paddleocr --collect-all pyclipper --collect-all imghdr --collect-all skimage --collect-all imgaug --collect-all scipy.io --collect-all lmdb -i ./resources/程序图标2.png
```