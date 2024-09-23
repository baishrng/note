向量点积

```
torch.dot(x, y)
```

矩阵-向量积  

```python
torc.mx(A, x)
# 注意， A的列维数（沿轴1的长度）必须与x的维数（其长度,及行数）相同。
```

矩阵乘法  

```
torch.mm(A, B)
```

计算向量的L2范数（元素平方和的平方根）

```
u = torch.tensor([3.0, -4.0])
torch.norm(u)
```

```
tensor(5.)
```

计算L1范数，它表示为向量元素的绝对值之和：  

```
torch.abs(A).sum()
```

计算矩阵的Frobenius范数。  

```
torch.norm(torch.ones((4, 9)))
```

```
torch.matmul(X, w)			# 张量乘法
```

```
torch.rand()  #是 PyTorch 中用于生成指定形状的随机数张量的函数。它生成的张量中的元素是从区间 [0, 1) 中均匀分布的随机数。
```

```
torch.randn 	#是 PyTorch 中用于生成指定形状的随机数张量的函数，其中随机数是从标准正态分布（均值为 0，标准差为 1）中抽样得到的。
```

```
torch.save() 函数的作用是将PyTorch中的对象（如张量、模型的状态字典等）序列化并保存到磁盘上。

x = torch.tensor([1, 2, 3, 4])
torch.save(x, 'tensor.pt')
```

```
torch.load() 函数是PyTorch中用于加载之前保存的对象的函数。它的主要作用是从磁盘中读取之前使用              	       torch.save() 函数保存的二进制文件，并将其反序列化为Python对象或PyTorch特定的数据结构 

loaded_x = torch.load('tensor.pt')
print(loaded_x)  # 打印出 tensor([1, 2, 3, 4])
```

```python
torch.stack 是PyTorch中一个函数，用于沿着新的维度堆叠张量序列。具体来说，torch.stack 可以接受一个张量序列作为输入，并将它们堆叠成一个新的张量。新张量的维度比原来的张量序列多一维。

stacked = torch.stack([x, y])
print(stacked)
tensor([[1, 2, 3],
        [4, 5, 6]])
```

```python
torch.bmm()  # 批量矩阵乘法

input = torch.randn(batch_size, n, m)  # 形状为 (3, 4, 5)
mat2 = torch.randn(batch_size, m, p)   # 形状为 (3, 5, 6)

# 计算批次化矩阵乘积
result = torch.bmm(input, mat2)  # 结果的形状为 (3, 4, 6)
```

```python
torch.repeat_interleave()  # 是 PyTorch 中的一个函数，用于按指定的方式重复张量中的元素。
```

