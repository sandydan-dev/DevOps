<%@ page import="java.time.LocalDateTime" %>
<%
    String user = "Sandeep";
    LocalDateTime now = LocalDateTime.now();
%>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Welcome Page</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f5f7fa;
            margin: 0;
            padding: 0;
        }

        .header {
            background: #4a90e2;
            padding: 20px;
            text-align: center;
            color: white;
            font-size: 28px;
            font-weight: bold;
            text-shadow: 1px 1px 3px #00000033;
        }

        .container {
            margin: 50px auto;
            width: 70%;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        .info {
            font-size: 18px;
            color: #333;
            line-height: 1.6;
        }

        .footer {
            margin-top: 40px;
            text-align: center;
            color: #777;
            font-size: 14px;
        }
    </style>
</head>

<body>

    <div class="header">🌐 Welcome to My JSP Application</div>

    <div class="container">
        <p class="info">
            Hello <b><%= user %></b>, welcome to your JSP home page!  
        </p>

        <p class="info">
            Current server time:  
            <b><%= now %></b>
        </p>

        <hr>

        <p class="info">
            This page is generated using a mix of HTML + JSP.<br>
            You can modify this file at:  
            <b>webapps/YourAppName/index.jsp</b>
        </p>
    </div>

    <div class="footer">
        © 2025 JSP Demo | Powered by Apache Tomcat
    </div>

</body>
</html>
