## vw适配方案

### vw和vh基本使用

vw和vh是相对单位，相对**视口尺寸**计算结果

* **vw**：viewport width（1vw = 1/100视口宽度 ）
* vh：viewport height ( 1vh = 1/100视口高度 )

示例：

```css
/* vw 和 vh 是相对视口宽高计算结果，可以直接实现移动端适配效果 */
/* .box {
width: 50vw;
height: 30vw;
background-color: pink;
} */

.box {
  width: 50vh;
  height: 30vh;
  background-color: green;
}
```

### vw布局

vw单位的尺寸 = px 单位数值 / ( 1/100 视口宽度 ) 

示例：

```less
.box {
    width: (68 / 3.75vw);
    height: (29 / 3.75vw);
    background-color: pink;
}

.box {
    width: (68 / 6.67vh);
    height: (29 / 6.67vh);
    background-color: green;
}

// px单位尺寸 / 1/100视口的宽度或高度
```

### vh问题

vh是1/100视口高度，全面屏视口高度尺寸大，如果混用可能会导致盒子变形 

----

## 综合案例—酷我音乐

### 缩放 img

```less
@vw: 3.75vw;

li {
  width: (345 / @vw);
  height: (108 / @vw);
  img {
    width: 100%;
    height: 100%;
    // cover完全覆盖
    // 缩放img，图片比例跟父级盒子比例不同，避免图片挤压变形
    object-fit: cover;
  }
}
```

