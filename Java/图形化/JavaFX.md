---
title: JavaFx
---

---

# 大体结构：

节点->面板->场景->舞台

例子1：

```Java
import javafx.application.*;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.layout.StackPane;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class Main extends Application{

	@Override
	public void start(Stage primaryStage) throws Exception {
		Pane pane = new StackPane();			// 创建一个面板
		Text text = new Text("意难平");			// 创建一个文本节点
		pane.getChildren().add(text);			// 将节点放入面板中
		Scene scene = new Scene(pane,200,200);	// 创建一个场景	
		Stage stage = new Stage();				// 创建一个舞台
		stage.setTitle("后来的我们");	     		// 给舞台命名
		stage.setScene(scene); 					// 给舞台设置场景
		stage.show(); 							// 展示舞台
	}
	
}
```

结果：

<img src="../../img/Java/JavaFx/屏幕截图 2022-06-28 163928.jpg" style="zoom: 50%;" />

示例2：

```Java
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.layout.StackPane;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class test extends Application {

    @Override
    public void start(Stage primStage) {
    	Pane pane = new StackPane();			// 创建一个面板
		Text text = new Text("意难平");			// 创建一个文本节点
		pane.getChildren().add(text);			// 将节点放入面板中
		Scene scene = new Scene(pane,200,200);	// 创建一个场景	
		Stage stage = new Stage();				// 创建一个舞台
		stage.setTitle("后来的我们");	     		// 给舞台命名
		stage.setScene(scene); 					// 给舞台设置场景
		stage.show(); 							// 展示舞台
    	
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

结果和示例1的一致

---

# 舞台设置

1、舞台设置一般步骤

```Java
primaryStage.setTitle("Main Stage");		// 设置标题
primaryStage.setScene(scene);				// 设置场景
primaryStage.show();						// 展示
```

2、设置禁止改变窗口大小

```
stage.setResizable(false);
```

3、改窗口图标

```java
primaryStage.getIcons().add(new Image("file:D:\\java\\白生\\图标\\象棋.png"));
```

4、设置窗口无边框

```Java
primaryStage.initStyle(StageStyle.UNDECORATED);

StageStyle有几种类型：
1) DECORATED——白色背景，带有最小化/最大化/关闭等有操作系统平台装饰（ 默认设置）
2) UNDECORATED——白色背景，没有操作系统平台装饰
3) TRANSPARENT——透明背景，没有操作系统平台装饰
4) UTILITY——白色背景，只有关闭操作系统平台装饰
5) UNIFIED——有操作系统平台装饰，消除装饰和内容之间的边框，内容背景和边框背景一致
```

5、窗口关闭时同时终止所有进程和线程

```Java
primaryStage.setOnCloseRequest(e->{	// 窗口关闭时同时终止所有进程和线程
	System.exit(0);
});
```

6、获取电脑屏幕大小

```Java
// AWT类
Dimension screensize = Toolkit.getDefaultToolkit().getScreenSize();

// javafx
Rectangle2D screenRectangle = Screen.getPrimary().getBounds();
double width1 = screenRectangle.getWidth();
double height1 = screenRectangle.getHeight();		// 可能需要放在start函数中使用（需继承Application）
```



---

# 属性绑定

可以将一个目标对象和一个源对象绑定。如果源对象中的值改变了，目标对象也将自动改变。目标对象称为绑定对象或者螂定属性，源对象称为可绑定对象或者可观察对象。

例如可以通过属性绑定，让一个节点的位置不随面板的大小而改变，从而保证相对位置不变

例如：

```Java
import javafx.application.*;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.layout.StackPane;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;

public class Main extends Application{

	@Override
	public void start(Stage primaryStage) throws Exception {
		Pane pane = new StackPane();			// 创建一个面板
		
		Circle circle = new Circle(50);			// 创建一个圆，50为圆的半径
		circle.centerXProperty().bind(pane.widthProperty().divide(2));		// 将圆的x轴坐标设置为pane宽度的一半
		circle.centerYProperty().bind(pane.heightProperty().divide(2));		// 将圆的y轴坐标设置为pane高度的一半，保证相对位置不变
		
		pane.getChildren().add(circle);			// 将节点放入面板中
		Scene scene = new Scene(pane,500,500);	// 创建一个场景	
				
		Stage stage = new Stage();				// 创建一个舞台
		stage.setTitle("白生");	     		// 给舞台命名
		stage.setScene(scene); 					// 给舞台设置场景
		stage.show(); 							// 展示舞台
	}
	
}

```

每个属性的获取方法实在每个属性后面加上**Property()**，每个属性都有**set**方法和**get**方法

---

# 节点的通用属性和方法

　　JavaFX的样式属性类似于用于在Web页面中指定HTML元素样式的层叠样式表(CSS)。因此，JavaFX的样式属性称为JavaFX CSS。JavaFX中，样式属性使用前缀 **-fx-** 进行定义

```java 
　　设定样式的语法是styleName:value。一个节点的多个样式属性可以一起设置，通过分号（；）进行分隔。比如，以下语句
　　circle.setStyle("-fx-stroke:black;-fx-fill:red;")
　　设置了一个圆的两个JavaFXCSS属性。该语句等价于下面两个语句：
　　circle.setStroke(Color.BLACK):
　　circle.setFil(Color.RED)
```

```Java
"-fx-background-image: url(" + "file:picture.jpg" + "); " 	// 背景图片
"-fx-background-position: center center; " 			// 图片位置
"-fx-background-repeat: stretch;" 					// 图片是否重复
"-fx-background-color:  transparent;" 				// 图片颜色		
"-fx-background-size: cover;");						// 图片大小（覆盖）
"-fx-stroke:black;"									// 边框填充色
"-fx-fill:red;"										// 内部填充色
```

　　rotate属性可以设定一个以度为单位的角度，让节点围绕它的中心旋转该角度。如果设置的角度是正的，表示旋转是顺时针；否则，逆时针。例如

```
button.setRotate(90);
```

rotate属性不止能旋转节点，也能旋转面板。

---

# 形状

## Text

Text类定义了一个节点，用于在一个起始点（x,y)处显示一个宇符串。一个字符串可以通过 **\n** 分隔从而显示在多行。

Text节点允许我们在场景图上显示文本。要创建Text节点，请使用javafx.scene.text.Text类。所有JavaFX场景节点都从javafx.scene.Node中扩展，并且它们继承了许多功能，例如缩放，翻译或旋转的功能。
Text节点的直接父对象是javafx.scene.shape.Shape类。可以在两个文本之间执行几何操作，如减法，相交或联合。还可以使用文本剪辑视口区域。

UML图：

| javafx.scene.text.Text;                      | 作用                                        |
| -------------------------------------------- | ------------------------------------------- |
| `-text: StringProperty`                      | 定义显示的文本                              |
| **-x**: DoubleProperty                       | 定义文本的x坐标（默认：0)                   |
| **-**y: DoubleProperty                       | 定义文本的y坐标（默认：0)                   |
| **-underline**: BooleanProperty              | 定义是否每行文本下面有下划线（默认：false） |
| **-strikethrough**: BooleanProperty          | 定义是否每行文本中间有删除线（默认：false   |
| **-font**: ObjectProperty<Font>              | 定义文本的字体                              |
| **+Text**()                                  | 创建一个空的Text                            |
| **+Text**(text:String)                       | 使用给定的文本创建一个Text                  |
| **+Text**(x: double, y:double, text: String) | 使用给定的x、少坐标以及文本创建一个Text     |
| **+setFill**(value: Paint)                   | 设置字体颜色                                |
| `+setWrappingWidth(value:double)`            | 设置换行宽度                                |

实例-1：

DropShadow 对象基于相对于Text节点的x，y偏移量定位。可以设置阴影的颜色。

以下代码显示如何使用DropShadow绘制文本。

```Java
import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.effect.DropShadow;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class Main extends Application {
  public static void main(String[] args) {
    Application.launch(args);
  }

  @Override
  public void start(Stage primaryStage) {
    primaryStage.setTitle("");
    Group root = new Group();
    Scene scene = new Scene(root, 300, 250, Color.WHITE);

    Group g = new Group();

    DropShadow ds = new DropShadow();
    ds.setOffsetY(3.0);
    ds.setColor(Color.color(0.4, 0.4, 0.4));

    Text t = new Text();
    t.setEffect(ds);
    t.setCache(true);
    t.setX(10.0);
    t.setY(70.0);
    t.setFill(Color.RED);
    t.setText("Nothing to lose...");
    t.setFont(Font.font(null, FontWeight.BOLD, 32));
    g.getChildren().add(t);

    

    root.getChildren().add(g);
    primaryStage.setScene(scene);
    primaryStage.show();
  }
}
```

结果：

<img src="../../img/Java/JavaFx/屏幕截图 2022-06-30 224937.jpg" style="zoom: 50%;" />

实例-2

使用`0.7f`作为`setFraction()`方法参数并调用此方法，本质上是指定所希望显示`70％`的反射。
以下代码显示如何在文本上使用反射效果。

```java 
import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.effect.Reflection;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class Main extends Application {
    public static void main(String[] args) {
        Application.launch(args);
    }
    
    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("");
        Group root = new Group();
        Scene scene = new Scene(root, 300, 250, Color.WHITE);
        
        Text t = new Text();
        t.setX(10.0);
        t.setY(50.0);
        t.setCache(true);
        t.setText("江月年年花相似...");
        t.setFill(Color.RED);
        t.setFont(Font.font(null, FontWeight.BOLD, 30));

        Reflection r = new Reflection();		// 反射类
        r.setFraction(0.7);						// 反射值范围 0~1

        t.setEffect(r);			// 设置反射效果
        
        root.getChildren().add(t); 
        primaryStage.setScene(scene);
        primaryStage.show();
    }
}
```

反射值范围从零(0％)到一(100％)。

我们还可以通过`setTopOffset()`方法设置不透明节点部分和反射部分之间的空间。顶部偏移默认为零。

<img src="../../img/Java/JavaFx/屏幕截图 2022-06-30 225732.jpg" style="zoom:50%;" />

实例-3

```Java
import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class Main extends Application {
    public static void main(String[] args) {
        Application.launch(args);
    }
    @Override
    public void start(Stage primaryStage) {
        Group root = new Group();
        Text text = new Text(100, 100, "爱意随风起\n风止意难平");
        text.setFont(Font.font("华文仿宋", 25));
        
        text.setWrappingWidth(100);		// 设置换行宽度
        
        root.getChildren().add(text);
        Scene scene = new Scene(root, 640, 480, Color.ALICEBLUE);
        primaryStage.setTitle("白生");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
}
```

结果：

<img src="../../img/Java/JavaFx/屏幕截图 2022-06-30 232040.jpg" style="zoom:50%;" />

## Line 类

创造线节点的方法：

```Java
// 方法一
// 构造函数 Line(strrtX, startY, endX, endY)
Line line = new Line(100, 10,   10,   110);

// 方法二
// 利用属性的set方法来指定起点和终点位置
Line line = new Line();
line.setStartX(100);
line.setStartY(100);
line.setEndX(400);
line.setEndY(400);

```

| 属性             | 数据类型/说明                                                |
| ---------------- | ------------------------------------------------------------ |
| fill             | `javafx.scene.paint.Paint` - 用于填充形状内的颜色。          |
| smooth           | Boolean - true - 表示打开反锯齿，false表示关闭反锯齿。       |
| strokeDashOffset | Double - 将距离设置为虚线模式。                              |
| strokeLineCap    | javafx.scene.shape.StrokeLineCap - 在线或路径的末尾设置帽样式。 有三种风格：1.StrokeLineCap.BUTT  2. StrokeLineCap.ROUND 3. StrokeLineCap.SQUARE |
| strokeLineJoin   | javafx.scene.shape.StrokeLineJoin - 当线相遇时设置装饰。 有三种类型：1. StrokeLineJoin.MITER 2. StrokeLineJoin.BEVEL  3. StrokeLineJoin.ROUND |
| strokeMiterLimit | Double - 设置斜角连接的限制以及斜角连接装饰StrokeLineJoin.MITER |
| stroke           | javafx.scene.paint.Paint - 设置形状的笔划线的颜色。          |
| strokeType       | javafx.scene.shape.StrokeType - 设置在Shape节点的边界周围绘制描边的位置。有三种类型： 1. StrokeType.CENTERED 2. StrokeType.INSIDE 3. StrokeType.OUTSIDE |
| strokeWidth      | Double - 设置线的宽度。                                      |

示例：

以下代码设置更多的线属性，包括笔触颜色，笔触宽度和线帽。之后，它还设置了线的破折号样式。

```Java
import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.paint.Color;
import javafx.scene.shape.Line;
import javafx.scene.shape.StrokeLineCap;
import javafx.stage.Stage;

public class Main extends Application {
  @Override
  public void start(Stage primaryStage) {
    primaryStage.setTitle("Drawing Lines");

    Group root = new Group();
    Scene scene = new Scene(root, 300, 150, Color.GRAY);

    Line redLine = new Line(10, 10, 200, 10);

    redLine.setStroke(Color.RED);
    redLine.setStrokeWidth(10);
    redLine.setStrokeLineCap(StrokeLineCap.BUTT);

    redLine.getStrokeDashArray().addAll(15d, 5d, 15d, 15d, 20d);
    redLine.setStrokeDashOffset(10);

    root.getChildren().add(redLine);

    primaryStage.setScene(scene);
    primaryStage.show();
  }
  public static void main(String[] args) {
    launch(args);
  }
}
```

结果

<img src="../../img/Java/JavaFx/屏幕截图 2022-06-29 204331.jpg" style="zoom:50%;" />

---

## Rectangle 类

在场景图上绘制矩形需要宽度，高度和左上角的（x，y）位置。

可以用有参的构造函数进行创建；也可以用先用无参的构造函数先创建一个Rectangle类，再将宽度、高度，左上角的x和y用set方法进行配置。

UML图：

| `javafx.scene.shape.Rectangle`                               | 作用                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `-X: DoubleProperty`                                         | 矩形左上角的x坐标（默认：0）                                 |
| `-y: DoubleProperty`                                         | 矩形左上角的y坐标（默认：0）                                 |
| `-width: DoubleProperty`                                     | 矩形的宽度（默认：0）                                        |
| `-height: DoubleProperty`                                    | 矩形的高度（默认：0）                                        |
| `-arcWidth: DoubleProperty`                                  | 矩形的`arcWidth`值（默认：0),`arcWidth`是圆角处圆弧的水平直径 |
| `-arcHeight: DoubleProperty`                                 | 矩形的`arcHeight`值（默认：0),`arcHeight`是圆角外圆弧的垂直直径 |
| `+Rectangle()`                                               | 创建一个空的Rectangle                                        |
| `　+Rectanlge(x:double,y:double,width:double,height:double)` | 使用给定的左上角点、宽度和高度创建一个Rectangle              |
| `+setFill(Paint value): void`                                | 设置颜色                                                     |



- `setArcHeight(double n1) 和 setArcWidth(double n2)`

​		是用来设置圆角矩形的，这两个方法必须一起使用，且n1=n2才有效。

示例：

```Java
Rectangle rect = new Rectangle(200, 200, 100, 100);
rect.setArcHeight(25);
rect.setArcWidth(25);
```

- `setStroke(Paint value)`

  设置矩形边框颜色

示例：

```Java
rect.setStroke(Color.GREEN);
```

---

## Circle 类

`Circle`类创建一个新的圆，其中指定的半径和中心位置以像素为单位。。一个圆由其参数`centerX`、`centerY`以及`radius`定义。

UML图：

| `javafx.scene.shape.Circle`                                  | 作用                                  |
| ------------------------------------------------------------ | ------------------------------------- |
| `-ctnterX:　DoubleProperty`                                  | 圆心的x坐标（默认为0）                |
| `-ctnterY:　DoubleProperty`                                  | 圆心的y坐标（默认为0）                |
| `-radius: DoubleProperty`                                    | 圆的半径（默认为0）                   |
| `+Circle()`                                                  | 创建一个空的Circle                    |
| `+Circle(x:double,y:double)`                                 | 使用给定的圆心创建一个Circle          |
| `+Circle(x:double,y:double,radius:double)`                   | 使用给定的圆心和半径创建一个Circle    |
| `+setStroke(Paint value)`                                    | 设置圆的边框的颜色，如Color.BLUE 蓝色 |
| `+setFille(Paint value)`                                     | 设置填充颜色，如Color.BLANK 黑色      |
| `+centerXProperty().bind(pane.widthProperty().divide(double))` | 圆的横坐标将随面板的大小的改变而改变  |
| `+centerYProperty().bind(pane.heightProperty().divide(double))` | 圆的纵坐标将随面板的大小的改变而改变  |

 实例-1

```Java
import javafx.application.*;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.layout.StackPane;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;

public class Main extends Application{

	@Override
	public void start(Stage primaryStage) throws Exception {
		Pane pane = new StackPane();			// 创建一个面板
		
		Circle circle = new Circle(50);			// 创建一个圆，50为圆的半径
		circle.centerXProperty().bind(pane.widthProperty().divide(2));		// 将圆的x轴坐标设置为pane宽度的一半
		circle.centerYProperty().bind(pane.heightProperty().divide(2));		// 将圆的y轴坐标设置为pane高度的一半，保证相对位置不变
		
		pane.getChildren().add(circle);			// 将节点放入面板中
		Scene scene = new Scene(pane,500,500);	// 创建一个场景	
				
		Stage stage = new Stage();				// 创建一个舞台
		stage.setTitle("白生");	     		// 给舞台命名
		stage.setScene(scene); 					// 给舞台设置场景
		stage.show(); 							// 展示舞台
	}
	
}
```



---

## Ellipse 类

　　一个捕圆由其参数`centerX`、`centerY`、`radiusX`以及`radiusY`定义。`Ellipse`类定义了一个椭圆。

UML图： 

| `javafx.scene.shape.Ellipse`                                | 作用                                |
| ----------------------------------------------------------- | ----------------------------------- |
| `-centerX: DoubleProperty`                                  | 椭圆中心的x坐标（默认为0）          |
| `-centerY: DoubleProperty`                                  | 椭圆中心的y坐标（默认为0）          |
| `-radlusX: DoubleProperty`                                  | 椭圆的水平半径（默认为0）           |
| `-radlusY: DoubleProperty`                                  | 椭圆的垂直半径（默认为0）           |
| `+Ellipse()`                                                | 创建一个空的Ellipse                 |
| `+Ellipse(x:double,y:double)`                               | 使用给定的中心创建一个Ellipse       |
| `+Ellipse(x:double,y:double,radiusX:double,radiusY:double)` | 使用给定的中心和半径创建一个Ellipse |

实例-1：

```Java
import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.effect.DropShadow;
import javafx.scene.paint.Color;
import javafx.scene.shape.Ellipse;
import javafx.stage.Stage;

public class test extends Application {

    @Override
    public void start(Stage primaryStage) {
    	primaryStage.setTitle("");
        Group root = new Group();
        Scene scene = new Scene(root, 300, 250, Color.WHITE);

        Group g = new Group();

        DropShadow ds = new DropShadow();
        ds.setOffsetY(3.0);
        ds.setColor(Color.color(0.4, 0.4, 0.4));

        Ellipse ellipse = new Ellipse();
        ellipse.setCenterX(50.0f);
        ellipse.setCenterY(50.0f);
        ellipse.setRadiusX(50.0f);
        ellipse.setRadiusY(25.0f);
        ellipse.setEffect(ds);
          
        g.getChildren().add(ellipse);

        root.getChildren().add(g);
        primaryStage.setScene(scene);
        primaryStage.show();
    	
    }

    public static void main(String[] args) {
        launch(args);
    }

}
```

结果：

<img src="../../img/Java/JavaFx/屏幕截图 2022-06-29 211549.jpg" style="zoom:50%;" />

实例-2：

```Java
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.layout.StackPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Ellipse;
import javafx.stage.Stage;

public class test extends Application {

    @Override
    public void start(Stage primaryStage) {
    	Pane pane = new StackPane();
    	
    	for(int i=0; i<16; i++) {
    		Ellipse ell = new Ellipse(150, 100, 100, 50);
        // 随机设置椭圆线的颜色
    		ell.setStroke(Color.color(Math.random(), Math.random(), Math.random()));		
    		ell.setRotate(i*180/16);
    		ell.setFill(Color.WHITE);		// 将椭圆内容填充为白色
    		pane.getChildren().add(ell);
    	}
    	
    	Scene scene = new Scene(pane, 640, 480);
    	Stage stage = new Stage();
    	stage.setTitle("白生");
    	stage.setScene(scene);
    	stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

结果：

<img src="../../img/Java/JavaFx/屏幕截图 2022-07-04 205411.jpg" style="zoom:50%;" />

---

## Arc 类

　　一段弧可以认为是椭圆的一部分，由参数`centerX`、`centerY`、`radiusX`、`radiusY`、`startAngle`、`length`以及一个弧的类型（`ArcType.0PEN`、`ArcType.CHORD`或者`ArcType.ROUND`)来确定。参数`startAngle`是起始角度，`length`是跨度（即弧所覆盖的角度）。角度使用度来作为单位，并且遵循通常的数学约定（即，0°是最东的方向，正的角度表示从最东。

UML图：

| `javafx.scene.shape.Arc`                                     | 作用                                                       |
| ------------------------------------------------------------ | ---------------------------------------------------------- |
| `-centerX: DoubleProperty`                                   | 椭圆中心的x坐标（默认为0）                                 |
| `-centerY: DoubleProperty`                                   | 椭圆中心的y坐标（默认为0）                                 |
| `-radlusX: DoubleProperty`                                   | 椭圆的水平半径（默认为0）                                  |
| `-radlusY: DoubleProperty`                                   | 椭圆的垂直半径（默认为0）                                  |
| `-startAngle: DoubleProperty`                                | 弧的起始角度，以度为单位                                   |
| `-length: DoubleProperty`                                    | 孤的角度范围，以度为单位                                   |
| `-type: ObjectProperty<ArcTyp>`                              | 弧的闭合类型（`ArcType.OPEN,ArcType.CHORD,ArcType.ROUND`） |
| `+Arc()`                                                     | 创建一条空的弧                                             |
| `+Arc(x:double,y:double, radlusX:double,radiusY:double, startAngle:double,length:double)` | 使用给定的参数创建一条弧                                   |

实例-1：

```Java
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.FlowPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Arc;
import javafx.scene.shape.ArcType;
import javafx.stage.Stage;

public class test extends Application {

    @Override
    public void start(Stage primaryStage) {
    	FlowPane pane = new FlowPane();
    	pane.setHgap(15);
    	pane.setVgap(15);
    	
    	Arc arc1 = new Arc(150, 100, 100, 100, 0, 90);
    	arc1.setFill(Color.WHITE);
    	arc1.setStroke(Color.BLACK);
    	Arc arc2 = new Arc(150, 100, 100, 100, 0, 90);
    	arc2.setType(ArcType.OPEN);
    	arc2.setFill(Color.WHITE);
    	arc2.setStroke(Color.BLACK);
    	Arc arc3 = new Arc(150, 100, 100, 100, 0, 90);
    	arc3.setType(ArcType.CHORD);
    	arc3.setFill(Color.WHITE);
    	arc3.setStroke(Color.BLACK);
    	Arc arc4 = new Arc(150, 100, 100, 100, 0, 90);
    	arc4.setType(ArcType.ROUND);
    	arc4.setFill(Color.WHITE);
    	arc4.setStroke(Color.BLACK);
    	pane.getChildren().addAll(arc1, arc2, arc3, arc4);
    	
    	Scene scene = new Scene(pane, 640, 480);
    	Stage stage = new Stage();
    	stage.setTitle("白生");
    	stage.setScene(scene);
    	stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

结果：

<img src="../../img/Java/JavaFx/屏幕截图 2022-07-04 212815.jpg" style="zoom:50%;" />

---

## Polygon 类 和 Polyline 类

　　`Polygon`类定义一个连接一个点序列的多边形，如图14-38a所示。`Polyline`类类似于`Polygon`类，不同之处是`Polyline`类不会自动闭合，如图所示：

<img src="../../img/Java/JavaFx/屏幕截图 2022-07-04 215028.jpg" style="zoom: 33%;" />

`Polygon` 类的UML图如下：

| `javafx.scene.shape.Polygon`           | 作用                                       |
| -------------------------------------- | ------------------------------------------ |
| `+Polygon()`                           | 创建一个空的Polygon                        |
| `+Polygon(double…points)`              | 根据给定的点集创建一个Polygon              |
| `+getPoints(): ObservableList<Double>` | 返回一个双精度值列表作为点集的x坐标和y坐标 |

实例-1：

```Java
import javafx.application.Application;
import javafx.collections.ObservableList;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Polygon;
import javafx.stage.Stage;

public class test extends Application {

    @Override
    public void start(Stage primaryStage) {
    	Pane pane = new Pane();
    	
    	// 方法一
    	Polygon ploy1 = new Polygon();
    	ploy1.getPoints().addAll(new Double[]{100.0,100.0, 200.0,200.0, 300.0,100.0});
    	ploy1.setFill(Color.WHITE);
    	ploy1.setStroke(Color.BLACK);
    	// 方法二
    	Polygon ploy2 = new Polygon();
    	ObservableList<Double> list = ploy2.getPoints();
		list.addAll(new Double[]{100.0,300.0, 200.0,200.0, 300.0,300.0});
		ploy2.setFill(Color.WHITE);
    	ploy2.setStroke(Color.RED);	
    	
    	pane.getChildren().addAll(ploy1, ploy2);
    	
    	Scene scene = new Scene(pane, 640, 480);
    	Stage stage = new Stage();
    	stage.setTitle("白生");
    	stage.setScene(scene);
    	stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

结果：

<img src="../../img/Java/JavaFx/屏幕截图 2022-07-04 221317.jpg" style="zoom:50%;" />

---

## 曲线

### 立方曲线

要创建三次曲线，请使用适当的构造函数。

设置三次曲线的主要参数是`startX`，`startY`，controlX1(控件点1X)，controlY1(控件点1Y)，controlX2(控件点2X)和controlY2(控件点2Y)，`endX`，`endY`。

`startX`，`startY`，`endX`和`endY`参数是曲线的起点和终点。`controlX1`，`controlY1`，`controlX2`和`controlY2`是控件点。

控制点(控制X1，控制Y1)影响线起点(startX，startY)和中间点之间的线段。控制点(controlX2，controlY2)影响线的中点与其终点(endX，endY)之间的线段。

控制点将曲线拉向自身的方向。

实例-1：

```Java
import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.shape.CubicCurve;
import javafx.stage.Stage;

public class Main extends Application {
  public static void main(String[] args) {
    launch(args);
  }

  @Override
  public void start(Stage stage) {
    stage.setTitle("白生");
    Scene scene = new Scene(new Group(), 450, 250);

    CubicCurve cubic = new CubicCurve();
    cubic.setStartX(0.0f);
    cubic.setStartY(50.0f);
    cubic.setControlX1(25.0f);
    cubic.setControlY1(0.0f);
    cubic.setControlX2(75.0f);
    cubic.setControlY2(100.0f);
    cubic.setEndX(100.0f);
    cubic.setEndY(50.0f);
 

    Group root = (Group) scene.getRoot();
    root.getChildren().add(cubic);
    stage.setScene(scene);
    stage.show();
  }
}
```

结果：

<img src="../../img/Java/JavaFx/屏幕截图 2022-07-04 223527.jpg" style="zoom:50%;" />

### QuadCurve

`javafx.scene.shape.QuadCurve `类与三次曲线类似。代替两个控制点，我们只有一个控制点为QuadCurve。

实例-1：

```Java
import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.shape.QuadCurve;
import javafx.stage.Stage;

public class Main extends Application {
  @Override
  public void start(Stage stage) {
    Group root = new Group();
    Scene scene = new Scene(root, 300, 150);
    stage.setScene(scene);
    stage.setTitle("白生");

    QuadCurve quad = new QuadCurve();
    quad.setStartX(0.0f);
    quad.setStartY(50.0f);
    quad.setEndX(50.0f);
    quad.setEndY(50.0f);
    quad.setControlX(25.0f);
    quad.setControlY(0.0f);
    
    root.getChildren().add(quad);

    scene.setRoot(root);
    stage.show();
  }

  public static void main(String[] args) {
    launch(args);
  }
}
```

结果：

<img src="../../img/Java/JavaFx/屏幕截图 2022-07-04 223830.jpg" style="zoom: 80%;" />

---

## 组合形状

例如：

```java
Circle circle = new Circle(320, 240, 4);
double[] points = new double[]{320-4,240 , 320-2,240+12.5,
                               320,240+25, 320+2,240+12.5 ,320+4,240};
Polyline pl = new Polyline(points);
pl.setFill(Color.BISQUE);
Shape shape = Path.union(circle, pl);
```



---

# 基本类

## Color 类（通用）

属性：

* red: double		// 该 Color 对象的红色值（0.0 1.0 之间）
* green: double		// 该 Color 对象的绿色值（0.0 1.0 之间）
* blue: double		// 该 Color 对象的蓝色值（0.0 丨.0之间）
* opacity: double	// 该Color 对象的透明度（0.0 1.0 之间）

方法：

1、`Color(r: double, g: double, b:double, opacity: double)`
		使用给定的红色、绿色、蓝色值以及透明度创建一个 Color 对象

2、`brighter(): Color`		

​		创建一比该 Color 对象更亮的 Color 对象

3、`darker(): Color`		

​		创建一比该 Color 对象更暗的 Color 对象

4、`color(r: double, g: double, b:double, ): Color`

​		使用给定的红色、绿色、 蓝色值创建一个不透明的 Color 对象

5、`co1or(r: double, g: double, b: double, opacity：double) :Color`
				使用给定的红色、绿色、蓝色值以及透明度创建一个 Color 对象

6、`rgb(r: int, g: int, b: int): Color`
				使用给定的红色、绿色、蓝色值创建一个 Color 对象，这些值的范围为 0 255

7、`rgb(r: int, g: int, b: int, opacity: double): Color`
				使用给定的范围为 0~255 的红色、 绿色、蓝色值，以及一个给定的透明度创建一个 Color 对象

8、`web(String colorString, [double opacity]): color`

​		使用RGB十六进制值作为CSS指定颜色值，从Web值创建颜色

如：`Color.web("#0000FF")` 表示蓝色



Color类中定义的许多标准颜色之一，如BEIGE、BLACK、BLUE、BROWN、CYAN、DARKGRAY,GOLD、GRAY、GREN、LIGHTGRAY、MAGENTA、NAVY、ORANGE、PINK、RED、SILVER、WHITE和YELLOW

示例：

```Java
circle.setFil(Color.RED);
```

**注意：**

　　Color对象是不可改变的。一旦一个Color对象创建，它的属性就不能改变

---

## 渐变颜色

---

## Font 类（通用）

属性：

* size: double		// 该字体的大小
* name: String		//  该字体的名字
* family: String	// 该字体属于的字体集

方法：

1、**Font**(size: double)		

​		使用给定字体大小创建一个 Font

2、**Font**(name: String, size:double)	

​		使用给定的字体完整名称和大小创建一个 Font

3、**font**(name: String, size:double)	

​		使用给定的字体名称和大小创建一个 Font

4、**font**(name: String, w:FontWeight, size: double)
				使用给定的字体名称、粗细和大小创建一个 Font

5、**font**(name: String, w: FontWeight, p: FontPosture, size: double)
				使用给定的字体名称、粗细、字形以及大小创建一个 Font

6、**getFamilies**()：List<Strinq>	

​		返回一个字体集名字的列表

7、**getFontNames**(): List<String>	

​		返回一个字体完整名称的列表，包括字体集和粗细

```
FontWeight.BOLD			加粗
FontPosture.ITALIC	斜体
```

示例：

```java 
// 使用字体（Times New Roman,加粗、斜体和大小为20)来显示一个标签
Label label = new Label("白生");
label.setFont(Font.font("Times New Roman",FontWeight.BOLD,FontPosture.ITALIC,20));
```

**注意：**

　　Font对象是不可改变的。一旦一个Font对象创建，它的属性就不能改变

---

## Image 类和 ImageView 类

　　javafx.scene.image.Image类表示一个图像，用于从一个特定的文件名或者一个URL载入一个图像

```java
Image img1 = new Image(”file:文件路径");
Image img2 = new Image("url:文件路径");
```

　　javax.scene.image.ImageView是一个用于显示图像的节点。ImageView可以从一个Image对象产生

```java
Image img = new Image(“file:文件路径”);
ImageView img_view = new ImageView(img);
```

　　另外，也可以直接从一个文件或者一个URL来创建一个ImageView,如下所示

```java
ImageView img_view1 = new ImageView("file:文件路径");
ImageView img_view2 = new ImageView("url:文件地址");
```

**Image** 类的 UML图

| javafx.scene.image.Image           | 作用                                      |
| ---------------------------------- | ----------------------------------------- |
| -error:  ReadOnlyBooleanProperty   | 显示图像是否正确载入                      |
| -height:  ReadOnlyDoubleProperty   | 图像的高度                                |
| -width:  ReadOnlyDoubleProperty    | 图像的宽度                                |
| -progress:  ReadOnlyDoubleProperty | 已经完成图像载入的大致百分比              |
| +Image(filenameOrURL: String)      | 创建一个内容来自一个文件或者 URL 的 Image |

**ImageView** 类的UML图

| javax.scene.image.ImageView       | 作用                                             |
| --------------------------------- | ------------------------------------------------ |
| -fitHeight:  DoubleProperty       | 图像改变大小从而适合的边界框的高度               |
| -fitWidth:  DoubleProperty        | 图像改变大小从而适合的边界框的宽度               |
| -x:  DoubleProperty               | ImageView 原点的x 坐标                           |
| -y:  DoubleProperty               | ImageView 原点的y 坐标                           |
| -image:  ObjectProperty<Image>    | 图像视图中显示的图像                             |
| +ImageView()                      | 创建一个 ImageView                               |
| +ImageView(image: Image)          | 使用给定的图像创建一个 ImageView                 |
| +ImageView(fi1enameOrURL: String) | 使用从给定文件和 URL载人的图像创建一个 ImageView |
| +setFitHeight(double)             | 设置图片高度                                     |
| +setFitWidth(double)              | 设置图片宽度                                     |

注意：

在一个程序中如果要展示图像，可以不用 **Image** 类，但必须要用 **ImageView** 类

综合示例：

```java
import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.FlowPane;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

public class test extends Application {

    @Override
    public void start(Stage stage) {
    	FlowPane pane = new FlowPane();			// 流面板
    	
    	pane.setPadding(new Insets(10,10,10,10));		// 设置节点与面板边缘的距离
    	pane.setHgap(20);			// 设置节点间的水平间隔
    	pane.setVgap(20);			// 设置节点间的垂直间隔
    	pane.setStyle("-fx-background-color:wheat");
    	
    	// 打开本地图片
    	Image image1 = new Image("file:D:\\java\\新\\javafx_16\\src\\javafx_16\\image\\夜晚 星空 ɽ 光 · 一个人背影 4k唯美壁纸3840x2160_彼岸图网.jpg");
    	ImageView imageview1 = new ImageView(image1);
    	imageview1.setFitHeight(100);
    	imageview1.setFitWidth(100);
    	
    	// 打开网络图片
    	ImageView imageview2 = new ImageView("url:https://t7.baidu.com/it/u=1956604245,3662848045&fm=193&f=GIF");
    	imageview2.setFitHeight(50);
    	imageview2.setFitWidth(50);
    	
    	pane.getChildren().addAll(imageview1,imageview2);
    	
    	Scene scene = new Scene(pane, 400, 400, Color.BLACK);
    	stage = new Stage();
    	stage.setTitle("你好");
    	stage.setScene(scene);
    	stage.show();
    	
    }

    public static void main(String[] args) {
        launch(args);
    }

}

```

结果：

<img src="../../img/Java/JavaFx/屏幕截图 2022-06-30 094958.jpg" style="zoom:50%;" />

---

# 布局面板

面板种类：

| 类         | 描述                                                         |
| :--------- | :----------------------------------------------------------- |
| Pane       | 布局面板的基类，它有getChildren()方法来返回面板中的节点列表  |
| StackPane  | 节点放置在面板中央.并且叠加在其他节点之上（中央面板）        |
| FlowPane   | 节点以水平方式一行一行放置，或者垂直方式一列一列放置（流面板） |
| GridPane   | 节点放置在一个二维网格的单元格中（网格面板）                 |
| BorderPane | 将节点放置在顶部、右边、底部、左边以及中间区域（边界面板）   |
| HBox       | 节点放在单行中（水平面板）                                   |
| VBox       | 节点放在单列中（垂直面板）                                   |

---

## Pane

1、创建面板

```java 
Pane pane = new Pane();
```

2、将节点添加到面板

```java
pane.getChildren(Node node);
```

3、将所有节点从面板中清除

```java
pane.getChildren().clear();
```

4、删除面板中特定的节点

```java
pane.getChildren().remove()
```

5、设置背景色（同样适用于按钮等）

```
Background background = new Background(new BackgroundFill(Color.ANTIQUEWHITE, null, null));
pane.setBackground(background);
```

6、设置背景图片

```Java
// 代码方式
Image img = new Image("file:D:\\精选壁纸\\备用 (3).jpg");
BackgroundSize size = new BackgroundSize(BackgroundSize.AUTO, 
							BackgroundSize.AUTO, false, false, true, true);
BackgroundImage bgImg = new BackgroundImage(img, BackgroundRepeat.NO_REPEAT, 
							BackgroundRepeat.NO_REPEAT, BackgroundPosition.DEFAULT, size);
Background bg = new Background(bgImg);
pane.setBackground(bg);

// CSS方式
pane.setStyle("-fx-background-image: url(" + "file:picture.jpg" + "); " +
                "-fx-background-position: center center; " +
                "-fx-background-repeat: stretch;" +
                "-fx-background-color:  transparent;" +
                "-fx-background-size: cover;");
```

```
BackgroundSize(width, height, 是否将宽度解释为百分比, 是否将高度解释为百分比, 图像大小是否应最大限度地适合该区域, 图像大小是否应“覆盖”该区域)
```

```
BackgroundImage(Image, x轴的背景重复, y轴的背景重复, BackgroundPosition, BackgroundSize)
```

7、退出程序

```
pane.setOnMousePressed(e -> {
	Platform.exit();
});
```

8、禁止改变窗口大小

```
stage.setResizable(false);		// 禁止改变窗口大小
```

9、改窗口图标

```Java
primaryStage.getIcons().add(new Image("file:D:\\java\\白生\\图标\\象棋.png"));
```



---

## FlowPane

　　FlowPane将节点按照加入的次序，从左到右水平或者从上到下垂直组织。当一行或者一列排满的时候，开始新的一行或者一列。可以使用以下两个常数中的一个来确定节点是水平还是垂直排列：Orientation.HORIZONTAL或者Orientation.VERTICAL。可以使用像素为单位指定节点之间的距离。

UML图：

| javafx.scene.layout.FlowPane                                 | 作用                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **-alignment**:  ObjectProperty<Pos>                         | 该面板内容的整体对齐方式（默认：Pos.LEFT)                    |
| **-orientation**: 0bjectProperty<0r1entatlon>                | 面板中的方向（默认：Orientation.HORIZONTAL	水平)； Orientation.VERTICAL 垂直 |
| **-hgap**:  DoubleProperty                                   | 节点之间的水平间隔（默认：0)                                 |
| **-vgap**:  DoubleProperty                                   | 节点之间的垂直间隔（默认：0)                                 |
| **+FlowPane**()                                              | 创建一个默认的 FlowPane                                      |
| **+FlowPane**(hgap: double, vgap:double)                     | 使用给定的水平和垂直间隔创建一个 FlowPane                    |
| **+FIowPane**(orientation:ObjectProperty<0r1entatlon>)       | 使用给定的方向创建一个 FlowPane                              |
| **+FlowPane**(orientatlon:ObjectProperty<Or1entation>,hgap: double, vgap: double) | 使用给定的方向、水平间隔以及垂直间隔创建一个 FlowPane        |
| **+setHgap**(double)                                         | 设置节点间的水平间隔                                         |
| **+setVgap**(double)                                         | 设置节点间的垂直间隔                                         |
| **+setPadding**(new Insets(double,double,double,double));    | 设置边框的大小，（顶部，右部，底部，左部）                   |

示例：

```Java
import javafx.application.*;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.RadioButton;
import javafx.scene.control.TextField;
import javafx.scene.layout.FlowPane;
import javafx.stage.Stage;

public class Main extends Application{

	@Override
	public void start(Stage primaryStage){
		FlowPane root = new FlowPane();

        root.setHgap(10);
        root.setVgap(20);
        root.setPadding(new Insets(15,15,15,15));

        // Button 1
        Button button1= new Button("Button1");
        root.getChildren().add(button1);


        // Button 2
        Button button2 = new Button("Button2");
        button2.setPrefSize(100, 100);
        root.getChildren().add(button2);

        // TextField
        TextField textField = new TextField("Text Field");
        textField.setPrefWidth(110);


        root.getChildren().add(textField);

        // CheckBox
        CheckBox checkBox = new CheckBox("Check Box");

        root.getChildren().add(checkBox);

        // RadioButton
        RadioButton radioButton = new RadioButton("Radio Button");
        root.getChildren().add(radioButton);

        Scene scene = new Scene(root, 550, 250);

        primaryStage.setTitle("FlowPane Layout Demo");
        primaryStage.setScene(scene);
        primaryStage.show();


	}
	
	public static void main(String[] args) {
    launch(args);
	}
	
}

```

结果：

<img src="../../img/Java/JavaFx/屏幕截图 2022-06-30 160142.jpg" style="zoom:67%;" />

---

## GridPane

　　GridPane（网络面板）将节点布局在一个网格（矩阵）中。节点放在一个指定的列和行索引中。

UML图：

| javafx.scene.layout.GridPane                             | 作用                                       |
| :------------------------------------------------------- | ------------------------------------------ |
| **-alignment**: ObjectProperty<Pos>-gridLinesVisible     | 该面板中内容的整体对齐（默认：Pos.LEFT)    |
| **-gridLinesVisible**: BooleanProperty                   | 网格线是否可见？（默认：false)             |
| **-hgap**: DoubleProperty                                | 节点间的水平间隔（默认：0）                |
| **-vgap**: DoubleProperty                                | 节点间的垂直间隔（默认：0                  |
| **+GridPane**()                                          | 创建一个GridPane                           |
| **+add**(child:Node,columnlndex:Int,rowlndex:int):void   | 添加一个节点到给定的列和行                 |
| **+addColumn**(columnlndex:1ntpchildren:Node...):void    | 添加多个节点到给定的列                     |
| **+addRow**(rowIndex:int,cMldreir.Node...)：void         | 添加多个节点到给定的行                     |
| **+getColumnIndex**(child: Node): int                    | 对于绝定的节点，返回列序号                 |
| **+setColumnIndex**(child: Node, columnIndex: int): void | 将一个节点设置到新的列，该方法重新定位节点 |
| **+getRowIndex**(child: Node): int                       | 对于给定的节点，返回行序号                 |
| **+setRowIndex**(child: Node, columnIndex: int): void    | 将一个节点设置到新的行，该方法重新定位节点 |
| **+setHalignment**(child: Node, value: Hpos): void       | 为单元格中的子节点设置水平对齐             |
| **+setValignment**(child: Node, value: Vpos): void       | 为单元格中的子节点设置垂直对齐             |

示例：

```Java
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.scene.text.Text;
import javafx.stage.Stage;



public class Main extends Application{

	@Override
	public void start(Stage primaryStage){
	primaryStage.setTitle("登录");
    GridPane grid = new GridPane();			// 网格面板
    grid.setAlignment(Pos.CENTER);			// 水平居中对齐
    grid.setHgap(10);						// 节点间的水平距离
    grid.setVgap(10);						// 节点间的垂直距离
    grid.setPadding(new Insets(25, 25, 25, 25));

    Text scenetitle = new Text("Welcome");
    scenetitle.setFont(Font.font("Tahoma", FontWeight.NORMAL, 20));			// 设置字体样式
    grid.add(scenetitle, 0, 0, 2, 1);		// 添加节点到面板中
    // 2表示行合并单元格数，1表示列何明单元格数
    Label userName = new Label("User Name:");		// 标签
    grid.add(userName, 0, 1);

    TextField userTextField = new TextField();		// 文本域
    grid.add(userTextField, 1, 1);

    Label pw = new Label("Password:");
    grid.add(pw, 0, 2);

    PasswordField pwBox = new PasswordField();		// 密码域
    grid.add(pwBox, 1, 2);

    Button btn = new Button("Sign in");		// 按钮
    HBox hbBtn = new HBox(10);						// 水平面板
    hbBtn.setAlignment(Pos.BOTTOM_RIGHT);
    hbBtn.getChildren().add(btn);					// 将按钮放在水平面板中
    grid.add(hbBtn, 1, 4);								// 将水平面板置于网格面板中

    final Text actiontarget = new Text();
    grid.add(actiontarget, 1, 6);

    btn.setOnAction(new EventHandler<ActionEvent>() {		// 事件处理

      @Override
      public void handle(ActionEvent e) {
        actiontarget.setFill(Color.FIREBRICK);
        actiontarget.setText("Sign in button pressed");
      }
    });

    Scene scene = new Scene(grid, 300, 275);
    primaryStage.setScene(scene);
    primaryStage.show();
	}
	
	public static void main(String[] args) {
		launch(args);
	}
	
}

```

结果：
<img src="../../img/Java/JavaFx/屏幕截图 2022-06-30 164645.jpg" style="zoom:67%;" />

---

## BorderPane

　　**BorderPane**可以将节点放置在五个区域：顶部、底部、左边、右边以及中间，分别使用setTop(node)、setBottom(node)、setLeft(node)、setRight(node)和setCenter(node)方法。

每个区域只能有一个节点。BorderPane的顶部和底部区域允许可调整大小的节点占用所有可用宽度。左边界区域和右边界区域占据顶部和底部边界之间的可用垂直空间。
默认情况下，所有边界区域尊重子节点的首选宽度和高度。放置在顶部，底部，左侧，右侧和中心区域中的节点的默认对齐方式如下：

顶部: Pos.TOP_LEFT底部: Pos.BOTTOM_LEFT左侧: Pos.TOP_LEFT右侧: Pos.TOP_RIGHT中心: Pos.CENTER

UML图：

| `javafx.scene.layout.BorderPane`         | `作用`                           |
| ---------------------------------------- | -------------------------------- |
| `-top: ObjectProperty<Node>`             | 放置在顶部区域的节点（默认：nul) |
| **-right**: ObjectProperty<Node>         | 放置在右边区域的节点（默认：nul) |
| **-bottom**: ObjectProperty<Node>        | 放置在底部区域的节点（默认：nul) |
| **-left**: ObjectProperty<Node>          | 放置在左边区域的节点（默认：nul) |
| **-center**: ObjectProperty<Node>        | 放置在中间区域的节点（默认：nul) |
| **+BorderPane**()                        | 创建一个BorderPane               |
| **+setAlignment**(child: Node, pos: Pos) | 设置BorderPane中的节点对齐       |

示例：

```Java
import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;


public class Main extends Application{

	@Override
	public void start(Stage primaryStage){
		primaryStage.setTitle("BorderPane Test");
	    BorderPane bp = new BorderPane();
	    bp.setPadding(new Insets(10, 20, 10, 20));

	    Button btnTop = new Button("Top");
	    bp.setTop(btnTop);

	    Button btnLeft = new Button("Left");
	    bp.setLeft(btnLeft);

	    Button btnCenter = new Button("Center");
	    bp.setCenter(btnCenter);

	    Button btnRight = new Button("Right");
	    bp.setRight(btnRight);

	    Button btnBottom = new Button("Bottom");
	    bp.setBottom(btnBottom);

	    Scene scene = new Scene(bp, 300, 200);
	    primaryStage.setScene(scene);
	    primaryStage.show();
    }
	
	public static void main(String[] args) {
		launch(args);
	}
	
}
```

结果：

<img src="../../img/Java/JavaFx/屏幕截图 2022-06-30 171016.jpg" style="zoom:67%;" />

---

## HBox

HBox布局类将JavaFX子节点放在水平行中。 新的子节点附加到右侧的末尾。默认情况下，HBox布局尊重子节点的首选宽度和高度。当父节点不可调整大小时，例如Group节点，HBox的行高度设置为子节点的最大首选高度。
默认情况下，每个子节点与左上(Pos.TOP_LEFT)位置对齐。
我们可以通过编程方式改变HBox的布局约束，例如边框，填充，边距，间距和对齐。
当处理不可缩放的子节点(如Shape节点)时，父节点会考虑Shape的矩形边界(ParentInBounds)的宽度和高度。
当处理诸如TextField控件之类可调整大小的节点时，父节点计算TextField水平增长的可用空间。
要在HBox中水平增长UI控件，请使用静态HBox.setHgrow()方法。

UML图：

| javafx.scene.layout.HBox                         | 作用                                                         |
| ------------------------------------------------ | ------------------------------------------------------------ |
| **-alignment**: ObjectProperty<Pos>              | 方框中子节点的整体对齐方式（默认：Pos.T0P_LEFT）（左上对齐） |
| **-fillHeight**: BooleanProperty                 | 可改变大小的子节点是否自适应方框的髙度？（默认：true)        |
| **-spacing**: DoubleProperty                     | 两个节点的水平间隔（畎认：0)                                 |
| **+HBox**()                                      | 创建一个畎认的HBox                                           |
| **+HBox**(spacing:double)                        | 使用节点间指定的水平间隔创建一个HBox                         |
| **+setMargin**(node: Node, value: Insets): void  | 为面板中的节点设置外边距                                     |
| **+Hbox.setHgrow**(child: Node, value: Priority) | 对可调整大小的控件在HBox中水平增长，如HBox.setHgrow(myTextField, Priority.ALWAYS); |

示例一：

```java
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Priority;
import javafx.scene.paint.Color;
import javafx.stage.Stage;


public class Main extends Application{

	@Override
	public void start(Stage primaryStage){
		TextField myTextField = new TextField();
	    HBox hbox = new HBox();
	    hbox.getChildren().add(myTextField);
    
	    HBox.setHgrow(myTextField, Priority.ALWAYS);		// 可注释

	    Scene scene = new Scene(hbox, 320, 112, Color.rgb(0, 0, 0, 0));
	    primaryStage.setScene(scene);
	    primaryStage.show();
    }
	
	public static void main(String[] args) {
		launch(args);
	}
}
```

结果：

<img src="../../img/Java/JavaFx/屏幕截图 2022-06-30 213345.jpg" style="zoom:67%;" />

当把“可注释”语句注释掉后的结果：

<img src="../../img/Java/JavaFx/屏幕截图 2022-06-30 213622.jpg" style="zoom:67%;" />

示例二：

```java 
import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.layout.HBox;
import javafx.scene.shape.Rectangle;
import javafx.stage.Stage;



public class Main extends Application{

	@Override
	public void start(Stage primaryStage){
		Group root = new Group();
        Scene scene = new Scene(root, 300, 250);
        HBox hbox = new HBox(5);		// 节点间的水平间隔为5 
        hbox.setPadding(new Insets(1));	// 节点到面板左部的距离为1
        Rectangle r1 = new Rectangle(10, 10);	// （宽，高）
        Rectangle r2 = new Rectangle(20, 100);
        Rectangle r3 = new Rectangle(50, 20);
        Rectangle r4 = new Rectangle(20, 50);

        HBox.setMargin(r1, new Insets(2, 2, 2, 2));

        hbox.getChildren().addAll(r1, r2, r3, r4);
        root.getChildren().add(hbox);

        primaryStage.setScene(scene);
        primaryStage.show();
    }
	
	public static void main(String[] args) {
		launch(args);
	}
}
```

结果：

<img src="../../img/Java/JavaFx/屏幕截图 2022-06-30 214318.jpg" style="zoom:67%;" />

---

## VBox

VBox布局将子节点堆叠在垂直列中。新添加的子节点被放置在上一个子节点的下面。默认情况下，VBox尊重子节点的首选宽度和高度。
当父节点不可调整大小时，例如Group节点，最大垂直列的宽度基于具有最大优选宽度的节点。默认情况下，每个子节点与左上(Pos.TOP_LEFT)位置对齐。

UML图：

| javafx.scene.layout.HBox                         | 作用                                                         |
| ------------------------------------------------ | ------------------------------------------------------------ |
| **-alignment**: ObjectProperty<Pos>              | 方框中子节点的整体对齐方式（默认：Pos.T0P_LEFT）（左上对齐） |
| **-fillWidth**: BooleanProperty                  | 可改变大小的子节点是否自适应方框的宽度？（默认：true)        |
| **-spacing**: DoubleProperty                     | 两个节点的水平间隔（畎认：0)                                 |
| **+VBox**()                                      | 创建一个畎认的HBox                                           |
| **+VBox**(spacing:double)                        | 使用节点间指定的垂直间隔创建一个HBox                         |
| **+setMargin**(node: Node, value: Insets): void  | 为面板中的节点设置外边距                                     |
| **+Hbox.setWgrow**(child: Node, value: Priority) | 对可调整大小的控件在HBox中垂直增长，如HBox.setHgrow(myTextField, Priority.ALWAYS); |

可通过将HBox中的示例改变一下即可得到本面板的示例

---

## ScrollPane

可以将任何节点放置在ScrollPane中。如果控件太大以致于不能在显示区域内完整显示，ScrollPane提供了垂直和水平方向的自动滚动支持。

实例：

```Java
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TextArea;
import javafx.stage.Stage;

public class Main extends Application {
  public static void main(String[] args) {
    Application.launch(args);
  }

  @Override
  public void start(Stage primaryStage) {
	  TextArea textarea = new TextArea();		// 多行文本
	  textarea.setPrefColumnCount(20);			// 20列
	  textarea.setPrefRowCount(5);				// 5行
	  textarea.setWrapText(true);				// 允许文本折到下一行
	  
	  /* 方法一 */
//	  ScrollPane pane = new ScrollPane(textarea);
	  /* 方法二 */
	  ScrollPane pane = new ScrollPane();
	  pane.setContent(textarea);
	  
	  Scene scene = new Scene(pane, 200, 200);
	  primaryStage.setTitle("白生");
	  primaryStage.setScene(scene);
	  primaryStage.show();
  }
}
```

结果：

<img src="../../img/Java/JavaFx/屏幕截图 2022-07-07 095939.jpg" style="zoom:50%;" />