---
title: tomcat的配置
---

- Tomcat服务器要想运行，需要先有jre，所以要先安装JDK，配置java运行环境。
  - JAVA_HOME=C:\Program Files\Java\jdk-17.0.1
  - PATH=%JAVA_HOME%\bin
  - 目前JAVA_HOME没有配置，思考一个问题，这样行不行呢？目前只运行java程序是没问题的。真的没问题吗？
- Tomcat服务器的安装：
  - 绿色版本的安装很简单，直接zip包解压即可。解压就是安装。
  - 我有一个好习惯，在C盘的根目录下新建一个dev目录，java开发所有相关的工具都安装到dev目录下，这样比较方便管理。（你随意）
  - 启动Tomcat
    - bin目录下有一个文件：startup.bat,通过它可以启动Tomcat服务器。
      - xxx.bat文件是个什么文件？bat文件是windows操作系统专用的，bat文件是批处理文件，这种文件中可以编写大量的windows的dos命令，然后执行bat文件就相当于批量的执行dos命令。
      - startup.sh，这个文件在windows当中无法执行，在Linux环境当中可以使用。在Linux环境下能够执行的是shell命令，大量的shell命令编写在shell文件当中，然后执行这个shell文件可以批量的执行shell命令。
      - tomcat服务器提供了bat和sh文件，说明了这个tomcat服务器的通用性。
      - 分析startup.bat文件得出，执行这个命令，实际上最后是执行：catalina.bat文件。
      - catalina.bat文件中有这样一行配置：MAINCLASS=org.apache.catalina.startup.Bootstrap （这个类就是main方法所在的类。）
      - tomcat服务器就是Java语言写的，既然是java语言写的，那么启动Tomcat服务器就是执行main方法。
    - 我们尝试打开dos命令窗口，在dos命令窗口中输入startup.bat来启动tomcat服务器。
    - 启动Tomcat服务器只配置path对应的bin目录是不行的。有两个环境变量需要配置：
      - JAVA_HOME=JDK的根
      - CATALINA_HOME=Tomcat服务器的根
- 关于Tomcat服务器的目录
  - bin ： 这个目录是Tomcat服务器的命令文件存放的目录，比如：启动Tomcat，关闭Tomcat等。
  - conf： 这个目录是Tomcat服务器的配置文件存放目录。（server.xml文件中可以配置端口号，默认Tomcat端口是8080）
  - lib ：这个目录是Tomcat服务器的核心程序目录，因为Tomcat服务器是Java语言编写的，这里的jar包里面都是class文件。
  - logs: Tomcat服务器的日志目录，Tomcat服务器启动等信息都会在这个目录下生成日志文件。
  - temp：Tomcat服务器的临时目录。存储临时文件。
  - webapps：这个目录当中就是用来存放大量的webapp（web application：web应用）
  - work：这个目录是用来存放JSP文件翻译之后的java文件以及编译之后的class文件。
- 配置Tomcat服务器需要哪些环境变量？
  - JAVA_HOME=JDK的根
  - CATALINA_HOME=Tomcat服务器的根
  - PATH=%JAVA_HOME%\bin;%CATALINA_HOME%\bin
- 启动Tomcat： startup
- 关闭Tomcat：stop （shutdown.bat文件重命名为stop.bat，为什么？原因是shutdown命令和windows中的关机命令冲突。所以修改一下。）
- 怎么测试Tomcat服务器有没有启动成功呢？
  - 打开浏览器，在浏览器的地址栏上输入URL即可：
    - http://ip地址:端口号
    - ip地址是什么？端口号我知道，是8080
    - 本机的IP地址是：127.0.0.1，或者是localhost，都行。

## 第一个例子：

```Java 
package com.bjpowernode.servlet;

import jakarta.servlet.Servlet;
import jakarta.servlet.ServletException;
import jakarta.servlet.ServletRequest;
import jakarta.servlet.ServletResponse;
import jakarta.servlet.ServletConfig;
import java.io.IOException;
import java.io.PrintWriter;


public class HelloServlet implements Servlet{

	// 5个方法
	public void init(ServletConfig config) throws ServletException{
	
	}

	public void service(ServletRequest request,ServletResponse response)
		throws ServletException , IOException{

		// 向控制台打印输出
		System.out.println("My First Servlet, Hello Servlet");

		// 设置响应的内容类型是普通文本或html代码
		// 需要在获取流对象之前设置，有效。
		response.setContentType("text/html");

		// 怎么将一个信息直接输出到浏览器上？
		// 需要使用ServletResponse接口：response
		// response表示响应：从服务器向浏览器发送数据叫做响应。
		PrintWriter out = response.getWriter();
		
		// 设置响应的内容类型时不要在获取流之后设置。
		//response.setContentType("text/html");

		out.print("Hello Servlet, You are my first servlet!");

		// 浏览器是能够识别html代码的，那我们是不是应该输出一段HTML代码呢？
		out.print("<h1>hello servlet，你好Servlet</h1>");

		// 这是一个输出流，负责输出字符串到浏览器
		// 这个输出流不需要我们刷新，也不需要我们关闭，这些都由Tomcat来维护。
		/*
		out.flush();
		out.close();
		*/
	}

	public void destroy(){
	
	}

	public String getServletInfo(){
		return "";
	}

	public ServletConfig getServletConfig(){
		return null;
	}
}
```

