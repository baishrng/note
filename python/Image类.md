---
title: PIL中的Image类
---

### 1、引用：

```python
from PIL import Image
```

### 2、读取一张图片

```python
im = Image.open('照片路径')			# 打开照片
```

### 3、显示图片

```python
im.show()			# 显示照片
```

### 4、图片信息

```python
print(im.size)			# 照片的大小
print(im.mode)			# 照片的模式
print(im.format)		# 照片的格式，如jpg,png等
```

---

**模式**：

1、模式“1”：

如果图像模式为1，那么它就是二值图，非黑即白，每个像素用8个bit表示，那么可表示的范围为[0~255]，0表示黑，255表示白。

2、模式“L”

该模式表示图像是灰度图像，同样每个像素用8位表示，0表示最黑，255表示最白，介于之间的数字可表示不同的灰度。

3、模式“RGB”和“RGBA”

三通道彩色图像一般都是该模式，每个像素用24个bit来表示，R、G、B三个分量都各占8位；而“RGBA”模式多了一个Alpha通道，一共需要32bit。不作过多介绍。

---

### 5、模式转换

```python
im = im.convert('L')			# 转为灰度模式
```

### 6、保存图片

```python
im.save("zzz.png","png")
```

### 7、创建新图片

```python

Image.new(mode,size)
Image.new(mode,size,color)

# 例子
newIm = Image.new('RGB',(640,480),(252,230,202))
newIm = Image.new('RGBA',(640,480),(252,230,202,30))		# 透明度30表示0.3
newIm = Image.new('RGBA',(640,480),'wheat')
newIm = Image.new('1', (100, 100), 255)        #255表示白色，1表示黑色
newIm = Image.new('L', (100, 100), 128)

---
new方法可以创建图片对象，new参数说明：
第一个参数：指定模式：
L：灰度模式,每个像素的颜色使用 0-255 的整数表示。
1：表示单色模式
RGBA：三元色加透明度的表示方式，每个像素的颜色使用类似 (12,34,23,1) 的 tuple 表示。
第二个参数：指定图片大小
第三个参数：指定背景色
---
```

### 8、改变图片大小（压缩）

```python
im1 = im1.resize((640,480))
```

### 9、图片合成

```python
Image.blend(img1,img2,alpha) # 这里alpha表示img1和img2的比例参数，如果为1 													  # 的话则合成后的图片jimg1

# 例子：
from PIL import Image

im1 = Image.open('1 (1).jpg')
im2 = Image.open('1 (2).jpg')
im1 = im1.convert('RGBA')					# 最好将模式变为一致
im2 = im2.convert('RGBA')

im1 = im1.resize((640,480))				# 将图片大小改为一致
im2 = im2.resize((640,480))

im3 = Image.blend(im1,im2,0.3)
im3.show()
```

### 10、点操作

```python
im.point(function) #,这个function接受一个参数，且对图片中的每一个点执行这个函数

# 例如：
im3 = im3.point(lambda i:i*1.5)		# 对每个点进行50%的加强
im3 = im3.point(lambda p: p > 120 and 199)		# 对每个可能的像素值调用一次该函数，并将结果表应用于图像的所有波段。
```

### 11、图片裁剪

```python
box = (100,100,500,500)			# 设置要裁剪的区域
im2 = im1.crop(box)				  #  此时，im2是一个新的图像对象。

---
crop() : 从图像中提取出某个矩形大小的图像。它接收一个四元素的元组作为参数，各元素为（left, upper, right, lower），坐标系统的原点（0, 0）是左上角。
---
```

### 12、图像黏贴（合并）

```python
im.paste(region,box)			# 粘贴box大小的region到原先的图片对象中。

# 例如：
box = (100,100,500,500)
im2 = im1.crop(box)
im1.paste(im2,box)			# 将裁剪出的图像粘贴回原图像
im1.show()
```

### 13、通道分离

```python
lists = im.split()			#分割成四个通道，返回一个Image对象列表
# 或者
r,g,b,k = im1.split()		# k为透明度的哪个通道
```

### 14、通道合并

```python
im2 = Image.merge('RGB',(r,b,g))		# (r,g,b)的顺序可以打乱，以得到不同的图片
```

### 15、图片旋转

```python
im1 = im1.transpose(Image.Transpose.ROTATE_90)		# 逆时针旋转90度
im1 = im1.transpose(Image.Transpose.ROTATE_180)		# 逆时针旋转180度
im1 = im1.transpose(Image.Transpose.ROTATE_270)		# 逆时针旋转270度
im1 = im1.rotate(45)			# 逆时针旋转45度
im1 = im1.transpose(Image.Transpose.FLIP_TOP_BOTTOM)			# 上下交换
im1 = im1.transpose(Image.Transpose.FLIP_LEFT_RIGHT)			# 左右交换
```

### 16、取出某个图像中某个像素点的RGB值：

```python
im1.getpixel((100,100))				# 返回一个rgb元组
```

### 17、更改某个图像中某个像素点的RGB值：

```python
im1.putpixel((200,200),(255,0,0))
```

