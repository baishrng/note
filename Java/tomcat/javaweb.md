---
title:javaweb
---

第一个例子：

```Java
import jakarta.servlet.*;

import java.io.IOException;
import java.io.PrintWriter;

public class firstServlet implements Servlet {
    @Override
    public void init(ServletConfig servletConfig) throws ServletException {

    }

    @Override
    public ServletConfig getServletConfig() {
        return null;
    }

    @Override
    public void service(ServletRequest servletRequest, ServletResponse servletResponse) throws ServletException, IOException {
        PrintWriter out = servletResponse.getWriter();
        out.print("This is my first java web Servlet!");
    }

    @Override
    public String getServletInfo() {
        return null;
    }

    @Override
    public void destroy() {

    }
}
```

一般来说程序不是直接实现Servlet接口，而是