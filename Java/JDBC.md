---
title: Java--JD
---

使用Java开发任何数据库应用程序都需要4个主要接口:`Driver、Connection、Statement和ResultSet。`

## 一般接口

使用Java开发任何数据库应用程序都需要4个主要接口:Driver、Connection、Statement和ResultSet。

<img src="../img/Java/JDBC/屏幕截图 2022-11-19 202653.jpg" style="zoom:50%;" />

JDBC应用程序使用`Driver`接口加载一个合适的驱动程序,使用Connection接口连接到数据库,使用Statement接口创建和执行SQL语句,如果语句返回结果,那么使用ResultSet接口处理结果。注意,有一些语句不返回结果，例如,SQL 数据定义语句和 SQL 数据修改语句。

---

## 一般步骤

访问数据库的典型 Java程序主要采用下列步骤:

- 1）加载驱动程序

在连接到数据库之前，必须使用下面的语句，加载一个合适的驱动程序。

```
Class.forName( "JDBCDriverClass ");
```

驱动程序是一个实现接口java. sql. Driver的具体类。如果程序访问一些不同的数据库，必须加载它们各自的驱动程序。

| 数据库 | 驱动程序类                       | 来源                            |
| ------ | -------------------------------- | ------------------------------- |
| Access | sun . jdbc. odbc. JdbcOdbcDriver | 已在JDK中                       |
| MySQL  | com. mysql.jdbc. Driver          | mysql-connector-java-5.1.26.jar |
| Oracle | oracle.jdbc.driver. 0racleDriver | ojdbc6.jar                      |

- 2）建立连接

为了连接到一个数据库,需要使用`DriverManager`类中的静态方法getConnection(databaseURL)，如下所示:

```
Connection connection = DriverManager.getConnection("databaseURL");
```

其中databaseURL是数据库在Internet上的唯一标识符。

| 数据库 | URL模式                                         |
| ------ | ----------------------------------------------- |
| Access | `jdbc:odbc:dataSource`                          |
| MySQL  | `jdbc:mysql://hostname/dbname`                  |
| Oracle | `jdbc:oracle:thin:@hostname: port#:oracleDBSID` |

MySQL数据库的databaseURL 指定定位数据库的主机名和数据库名。例如，下面的语句以用户名scott和密码tiger，为本地MySQL 数据库javabook创建一个Connection对象:

```
Connection connection = DriverManager.getConnection
	("jdbc :mysql://locathost/javabook","scott","tiger")
```

Oracle数据库的databaseURL 指定主机名（hostname)、数据库监听输入连接请求的端口号( port#)，以及定位数据库的数据库名（oracleDBSID)。

- 3）创建语句

一旦创建了Connection 对象，就可以创建执行SQL语句的语句，如下所示:

```
Statement statement = connection.createStatement();
```

- 4）执行语句

可以使用方法executeUpdate(String sql)来执行SQL DDL(数据定义语言)或更新语句，可以使用executeQuery(String sq1)来执行SQL查询语句。查询结果在ResultSet中返回。例如，下面的代码执行SQL语句create table Temp(col1 char(5) ,co12 char(5)):

```
statement.executeUpdate("create table Temp (col1 char(5),co12 char(5))");
```

下面的代码执行SQL查询select firstName,mi, lastName from Student wherelastName ='Smith' :

```
// Select the columns from the Student table
ResultSet resu1tSet = statement. executeQuery("select firstName,mi, 7astName from Student where lastName" + "='Smith'");
```

- 5）处理ResultSet

结果集ResultSet 维护一个表,该表的当前行可以获得。当前行的初始位置是null。可以使用next方法移动到下一行，可以使用各种getter方法从当前行获取值。例如，下面给出的代码显示前面SQL查询的所有结果。

```
// Iterate through the result and print the student names
whil1e (resu1tSet.next())
	System. out.println(resultSet.getString(1) +" "+resu1tSet.getString(2) +" " +resu1tSet.getString(3));
```

方法 getString(1)、 getString(2)和getString(3)分别获取firstName列、mi列和1astName列的值。还可使用getString("firstName")、 getString("mi")和getString("lastName")来获取同样的三列值。第一次执行next()方法时，将当前行设置为结果集中的第一行，接着再调用next()方法，将当前行设为第二行，然后是第三行，以此类推,直到最后一行。

例1：

```Java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;


public class test {
 
    public static void main(String[] args)  {
    	try {
    		// 加载驱动
    		Class.forName("com.mysql.cj.jdbc.Driver");
    		System.out.println("成功");
    		
    		// 连接数据库
			Connection connection = DriverManager.getConnection("jdbc:mysql://localhost/db_student", "用户名", "密码");
			System.out.println("连接成功");
			
			// 创建语句
			Statement statement = connection.createStatement();
			
			// 执行语句、返回结果
			String sqlStr = "select title from tb_articles";
			ResultSet resultSet = statement.executeQuery(sqlStr);
			System.out.println("输出结果:");
			
			while( resultSet.next() ) {
				System.out.println(resultSet.getString(1));
			}
			
			// 断开数据库
			connection.close();
			System.out.println("断开连接");
			
		} catch (SQLException | ClassNotFoundException e) {
			e.printStackTrace();
		}
    }
}
```

结果：

```
成功
连接成功
输出结果:
hello
爱情
悲哀
灯塔
黑暗深林
记录
落日
青铜时代
三体
生存
失去
维德
文明
无知
宇宙法则
责任
断开连接
```

---

## PreparedStatement

`PreparedStatement` 可以创建参数化的 SQL语句。

Statement接口用于执行不含参数的静态SQL语句。PreparedStatement接口继承自Statement接口，用于执行含有或不含参数的预编译的SQL语句。由于SQL语句是预编译的,所以重复执行它们时效率较高。

PreparedStatement对象是用Connection接口中的preparedStatement方法创建的。例如，下面的代码为SQL语句insert创建一个 PreparedStatement对象:

```java 
PreparedStatement preparedStatement = connection.prepareStatement
	( "insert into Student (firstName,mi, 1astName)" +
		"values (?,?,?)");
```

这条insert语句有三个问号用作参数的占位符，它们表示表Student中一条记录的firstName、mi和lastName的值。

作为Statement接口的子接口，PreparedStatement接口继承了Statement接口中定义的所有方法。它还提供在PreparedStatement对象中设置参数的方法。这些方法用来在执行语句或过程之前设置参数的值。一般的，设置的方法有如下的名字和签名:

```
setX(int parameterIndex，x value);
```

其中X是参数的类型，parameterIndex是语句中参数的下标。下标从1开始。例如，方法setString(int parameterIndex，String value)把一个String类型的值设置给指定参数。

下面的语句将参数"Jack"、"A"、"Ryan”传递给preparedStatement对象中firstName ,mi和 1astName的占位符:

```java
preparedStatement.setString(1，"Jack"）;
preparedStatement.setString(2，"A");
preparedStatement.setString(3，"Ryan");
```

例2：对例1的修改

```Java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Scanner;


public class test {
 
    public static void main(String[] args)  {
    	try {
    		// 加载驱动
    		Class.forName("com.mysql.cj.jdbc.Driver");
    		System.out.println("驱动加载成功");
    		
    		// 连接数据库
			Connection connection = DriverManager.getConnection("jdbc:mysql://localhost/db_student", "用户名", "密码");
			System.out.println("连接成功");
			System.out.println("------------------------------------------------------");
			
			// 创建语句
//			Statement statement = connection.createStatement();
			
			Scanner in = new Scanner(System.in);
			System.out.print("输入要查找的人:");
			String checkStr = in.next();
			in.close();
			
			// 执行语句、返回结果
			String sqlStr = "select title from tb_articles where ID = ?";
			PreparedStatement preparedStatement = connection.prepareStatement(sqlStr);
			preparedStatement.setString(1, checkStr);
			ResultSet resultSet = preparedStatement.executeQuery();
			System.out.println("输出结果:");
			
			while( resultSet.next() ) {
				System.out.println(resultSet.getString(1));
			}
			
			// 断开数据库
			connection.close();
			System.out.println("------------------------------------------------------");
			System.out.println("断开连接");
			
		} catch (SQLException | ClassNotFoundException e) {
			e.printStackTrace();
		}
    }
}
```

结果：

```
驱动加载成功
连接成功
------------------------------------------------------
输入要查找的人:白生
输出结果:
hello
------------------------------------------------------
断开连接
```

---

## CallableStatement

CallableStatement可以执行SQL存储过程。

CallableStatement接口是为执行SOL存储过程而设计的。这个进程可能会有IN、OUT 或 IN OUT 参数。当调用过程时，参数IN接收传递给过程的值。在进程结束后，参数oUT返回一个值，但是当调用过程时，它不包含任何值。当过程被调用时，IN OUT 参数包含传递给过程的值，在它完成之后返回一个值。

。。。。。。（用的时候再学）

---

## 获取元数据

要点提示：可以使用DatabaseMetaData接口来获取数据库的元数据，例如数据库URL、用户名、JDBC驱动程序名称等。ResultSetMetaData接口可以用于获取到结果集合的元数据，例如表的列数和列名等。

JDBC提供DatabaseMetaData接口，可用来获取数据库范围的信息，还提供Result-SetMetaData接口,用于获取特定的ResultSet的信息。

---

### 数据库元数据

Connection接口用于建立与数据库的连接。SQL 语句的执行和结果的返回是在一个连接上下文中进行的。连接还提供对数据库元数据信息的访问，该信息描述了数据库的能力，支持的SQL语法、存储过程，等等。要得到数据库的一个DatabaseMetaData 实例，可以使用Connection对象的getMetaData方法，如下所示:

```
DatabaseMetaData dbMetaData = connection.getMetaData();
```

| DatabaseMetaData  | 作用                                    |
| ----------------- | --------------------------------------- |
| `getURL()`        | 返回一个String类对象，代表数据库的URL。 |
| `getUserName()`   | 返回连接当前数据库管理系统的用户名。    |
| `getDriverName()` | 返回驱动驱动程序的名称。                |

例：

```Java
import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.SQLException;


public class test {
 
    public static void main(String[] args)  {
    	try {
    		// 加载驱动
    		Class.forName("com.mysql.cj.jdbc.Driver");
    		System.out.println("驱动加载成功");
    		
    		// 连接数据库
			Connection connection = DriverManager.getConnection("jdbc:mysql://localhost/db_student", "用户名", "密码");
			System.out.println("连接成功");
			System.out.println("------------------------------------------------------");
			
			DatabaseMetaData dbMetaData = connection.getMetaData();
			System.out.println("DB URL: "+dbMetaData.getURL());
			System.out.println("DB username: "+dbMetaData.getUserName());
			System.out.println("DB product name: "+dbMetaData.getDatabaseProductName());
			System.out.println("DB product version: "+dbMetaData.getDatabaseProductVersion());
			System.out.println("DB product name: "+dbMetaData.getDatabaseProductName());
			System.out.println("JDBC driver name: "+dbMetaData.getDriverName());
			System.out.println("JDBC driver version: "+dbMetaData.getDriverVersion());
			System.out.println("JDBC driver major version: "+dbMetaData.getDriverMajorVersion());
			System.out.println("JDBC driver minor version: "+dbMetaData.getDriverMinorVersion());
			System.out.println("Max number of connections: "+dbMetaData.getMaxConnections());
			System.out.println("MaxTableNameLength: "+dbMetaData.getMaxTableNameLength());
			System.out.println("MaxColumnsInTable: "+dbMetaData.getMaxColumnsInTable());
			
			// 断开数据库
			connection.close();
			System.out.println("------------------------------------------------------");
			System.out.println("断开连接");
			
		} catch (SQLException | ClassNotFoundException e) {
			e.printStackTrace();
		}
    }
}
```

结果：

```
驱动加载成功
连接成功
------------------------------------------------------
DB URL: jdbc:mysql://localhost/db_student
DB username: root@localhost
DB product name: MySQL
DB product version: 5.7.26
DB product name: MySQL
JDBC driver name: MySQL Connector/J
JDBC driver version: mysql-connector-j-8.0.31 (Revision: 0c86fc148d567b62266c2302bdad0f1e7a7e4eba)
JDBC driver major version: 8
JDBC driver minor version: 0
Max number of connections: 0
MaxTableNameLength: 64
MaxColumnsInTable: 512
------------------------------------------------------
断开连接
```

---

### 获取数据库表

使用getTables方法通过数据库元数据可以确定数据库中的表格。

例：获取数据库中的表名

```Java
import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;


public class test {
 
    public static void main(String[] args)  {
    	try {
    		// 加载驱动
    		Class.forName("com.mysql.cj.jdbc.Driver");
    		System.out.println("驱动加载成功");
    		
    		// 连接数据库
			Connection connection = DriverManager.getConnection("jdbc:mysql://localhost/db_student", "root", "123456");
			System.out.println("连接成功");
			System.out.println("------------------------------------------------------");
			
			DatabaseMetaData dbMetaData = connection.getMetaData();
			
			ResultSet rsTable = dbMetaData.getTables(null, null, null, new String[]{"TABLE"});
			System.out.println("table name:");
			while( rsTable.next() ) {
				System.out.print(rsTable.getString("TABLE_NAME") + " ");
			}
			System.out.println();
			
			// 断开数据库
			connection.close();
			System.out.println("------------------------------------------------------");
			System.out.println("断开连接");
			
		} catch (SQLException | ClassNotFoundException e) {
			e.printStackTrace();
		}
    }
}
```

结果：

```
驱动加载成功
连接成功
------------------------------------------------------
table name:
tb_leaveword tb_user tb_articles tb_user sys_config 
------------------------------------------------------
断开连接
```

---

### 结果集元数据

ResultSetMetaData接口描述属于结果集的信息。ResultSetMetaData对象能够用于在结果集ResultSet中找出关于列的类型和属性的信息。要得到ResultSetMetaData的一个实例，可在结果集上使用getMetaData方法，如下所示:

```
ResultSetMetaData rsMetaData = resu1tSet.getMetaData();
```

使用getColumnCount()方法可以在结果中求得列的数目，使用getColumnName(int)方法可以求得列名。

例：获取表的列名和表的内容

```java 
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;



public class test {
 
    public static void main(String[] args)  {
    	try {
    		// 加载驱动
    		Class.forName("com.mysql.cj.jdbc.Driver");
    		System.out.println("驱动加载成功");
    		
    		// 连接数据库
			Connection connection = DriverManager.getConnection("jdbc:mysql://localhost/db_student", "root", "123456");
			System.out.println("连接成功");
			System.out.println("------------------------------------------------------");
			
			// 创建语句
			Statement statement = connection.createStatement();
			
			ResultSet resultSet = statement.executeQuery("select * from tb_articles");
			ResultSetMetaData rsMetaData = resultSet.getMetaData();
			
			// 输出列名
			for(int i=1; i<=rsMetaData.getColumnCount(); i++) {
				System.out.printf("%-12s\t", rsMetaData.getColumnName(i));
			}
			System.out.println();
			
			// 输出内容
			while( resultSet.next() ) {
				for(int i=1; i<=rsMetaData.getColumnCount(); i++) {
					System.out.printf("%-12s\t", resultSet.getObject(i));	// 也可以用 getString(i)
				}
				System.out.println();
			}
            
            resultSet.close();
			
			// 断开数据库
			connection.close();
			System.out.println("------------------------------------------------------");
			System.out.println("断开连接");
			
		} catch (SQLException | ClassNotFoundException e) {
			e.printStackTrace();
		}
    }
}
```

