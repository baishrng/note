---
title: Typora
---



| 命令                                  | 解释                             |
| ------------------------------------- | -------------------------------- |
| `Ctrl+Shift+I`                        | 插入图片（可以直接拖动图片放入） |
| `Ctrl+T`                              | 插入表格                         |
| `Ctrl+回车`                           | 表格下方插入行                   |
| `Ctrl+Shift+删除键`                   | 表格删除行                       |
| `三个“-”或者“+“ 加回车(用减号较方便)` | 分割线                           |
| 输入 “>[!tip]"                        | 插入提示框                       |
| 输入 “>[!note]"                       | 插入建议框                       |
| 输入 “>[!important]"                  | 插入重要框                       |
| 输入 “>[!warning]"                    | 插入警告框                       |
| 输入 “>[!caution]"                    | 插入注意框                       |



```
def getNS(D:list[list], S:list) -> list:
    NS = []
    for s in S:
        for i in range(len(D)):
            if D[s][i] != 0 and i not in NS:
                NS.append(i)
    return NS

def hungarian(D:list[list]) -> dict:
    Mx = [] # x 饱和点
    My = []  # y 饱和点
    edges = dict()

    # 获取初始匹配
    for i in range(len(D)):
        for j in range(len(D[i])):
            if D[i][j] != 0 and i not in Mx and j not in My:
                Mx.append(i)
                My.append(j)
                edges.update({i:j})

    while len(Mx) != len(D) and len(My) != len(D[0]):
        Vx = [i for i in range(len(D)) if i not in Mx]  # x 非饱和点
        T = list()
        S = [Vx[0]]
        NS = getNS(D, S)

        while NS != T:

            # 求 NS - T
            NS_T = []
            for i in NS:
                if i not in T:
                    NS_T.append(i)

            y = NS_T[0]

            # y 是饱和点
            if y in My:
                x = -1

                # 找到与 y 相连的 x
                for key, value in edges.items():
                    if value == y:
                        x = key
                        break

                S.append(x)     # 将 x 加入到 集合 S 中
                T.append(y)     # 将 y 加入到 集合 T 中
                NS = getNS(D, S)
                NS = sorted(NS)

            # y 不是饱和点
            else:
                mY = -1
                # 找出一条增广路
                for x in Mx:
                    if D[x][y] != 0:
                        mY = edges[x]
                        edges.update({x:y})
                        break
                for x in Vx:
                    if D[x][mY] != -1:
                        edges.update({x:mY})
                        Mx.append(x)
                        Vx.remove(x)
                        break
                break

        if NS == T:
            break
    return dict(sorted(edges.items(), key=lambda x : x[0])) # 对字典按键值从小到大排序

D = [
    [1,1,0,0,0],
    [0,1,0,1,0],
    [1,0,0,0,0],
    [0,0,1,0,1]
]

edges = hungarian(D)
for key, value in edges.items():
    print(key+1, value+1)
```



```

def getNS(D:list[list], S:list) -> list:
    NS = []
    for s in S:
        for i in range(len(D[s])):
            if D[s][i] not in NS:
                NS.append(D[s][i])
    return NS

def hungarian(D:list[list]) -> dict:
    Mx = [] # x 饱和点
    My = []  # y 饱和点
    edges = dict()

    # 获取初始匹配，首先将只有一条边的节点放入初始匹配中
    for i in range(len(D)):
        if len(D[i]) == 1 and D[i][0] not in My:
            Mx.append(i)
            My.append(D[i][0])
            edges.update({i: D[i][0]})
    for i in range(len(D)):
        for j in range(len(D[i])):
            if D[i][j] not in My:
                Mx.append(i)
                My.append(D[i][j])
                edges.update({i:D[i][j]})
                break

    while len(Mx) != len(D):
        Vx = [i for i in range(len(D)) if i not in Mx]  # x 非饱和点
        T = list()
        S = [Vx[0]]
        NS = getNS(D, S)

        while NS != T:

            # 求 NS - T
            NS_T = []
            for i in NS:
                if i not in T:
                    NS_T.append(i)

            y = NS_T[0]

            # y 是饱和点
            if y in My:
                x = -1

                # 找到与 y 相连的 x
                for key, value in edges.items():
                    if value == y:
                        x = key
                        break

                S.append(x)     # 将 x 加入到 集合 S 中
                T.append(y)     # 将 y 加入到 集合 T 中
                NS = getNS(D, S)
                NS = sorted(NS)

            # y 不是饱和点
            else:
                mY = -1
                # 找出一条增广路
                for x in Mx:
                    if y in D[x]:
                        mY = edges[x]
                        edges.update({x:y})
                        break
                for x in Vx:
                    if mY in D[x]:
                        edges.update({x:mY})
                        Mx.append(x)
                        Vx.remove(x)
                        break
                break

        if NS == T:
            break
    return dict(sorted(edges.items(), key=lambda x : x[0])) # 对字典按键值从小到大排序

D = [
    [0,3,4],
    [3,5],
    [0,2],
    [1],
    [2,4],
    [0,2]
]

edges = hungarian(D)
for key, value in edges.items():
    print(key, value)






```

测试用例：

```
findAPath函数
D = [
    [0,3,4],
    [3,5],
    [0,2],
    [1],
    [2,4],
    [0,2]
]

Mx = [0,1,2,3,4]
My = [0,1,2,3,4]
edges = {0:0, 1:3, 2:2, 3:1, 4: 4}
结果：[(5, 1), (1, 3), (3, 0), (0, 0), (5, 0)]
```

```
hungarian函数
D = [
    [1,2],
    [0,1,3,4],
    [1,2],
    [1,2],
    [3,4]
]
结果：
0 1
1 0
2 2
4 3

D = [
    [0,3,4],
    [3,5],
    [0,2],
    [1],
    [2,4],
    [0,2]
]
结果：
0 3
1 5
2 2
3 1
4 4
5 0

D = [
    [0,1],
    [0,2],
    [1,3],
    [1,2]
]
结果：
0 0
1 2
2 3
3 1
```

```
from typing import List, Optional


def getNS(D:list[list], S:list) -> List[int]:
    NS = []
    for s in S:
        for i in range(len(D[s])):
            if D[s][i] not in NS:
                NS.append(D[s][i])
    return NS

def hungarian(D:list[list]) -> dict:
    Mx = [] # x 饱和点
    My = []  # y 饱和点
    edges = dict()
    xNum = len(D)

    # 获取初始匹配，首先将只有一条边的节点放入初始匹配中
    for i in range(xNum):
        for j in range(len(D[i])):
            if D[i][j] not in My:
                Mx.append(i)
                My.append(D[i][j])
                edges.update({i:D[i][j]})
                break

    while len(Mx) != xNum:
        Vx = [i for i in range(len(D)) if i not in Mx]  # x 非饱和点
        T = list()
        S = [Vx[0]]
        NS = getNS(D, S)

        while NS != T:

            # 求 NS - T
            NS_T = []
            for i in NS:
                if i not in T:
                    NS_T.append(i)

            y = NS_T[0]

            # y 是饱和点
            if y in My:
                x = -1

                # 找到与 y 相连的 x
                for key, value in edges.items():
                    if value == y:
                        x = key
                        break

                S.append(x)     # 将 x 加入到 集合 S 中
                T.append(y)     # 将 y 加入到 集合 T 中
                NS = getNS(D, S)
                NS = sorted(NS)

            # y 不是饱和点
            else:
                # 找出一条增广路
                path = find_a_path(D, Mx, My, edges, y)
                for i in range(1, len(path), 2):
                    edges.pop(path[i][0])
                    Mx.remove(path[i][0])
                for i in range(0, len(path), 2):
                    edges.update({path[i][1]: path[i][0]})
                    Mx.append(path[i][1])
                break

        if NS == T:
            break
    return dict(sorted(edges.items(), key=lambda x : x[0])) # 对字典按键值从小到大排序

if __name__ == '__main__':
    D = [
        [0,3,4],
        [3,5],
        [0,2],
        [1],
        [2,4],
        [0,2]
    ]

    edges = hungarian(D)
    for key, value in edges.items():
       print(key, value)
```

