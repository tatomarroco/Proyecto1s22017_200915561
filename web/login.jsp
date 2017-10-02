<%-- 
    Document   : login
    Created on : 4/09/2017, 11:08:04 PM
    Author     : Estuardo
--%>

<%@page import="Controladores.conectServer" %>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<% 
        
    String mensaje="";
    if(session.getAttribute("sesionError")!=null){
        mensaje=String.valueOf(session.getAttribute("sesionError"));
    }
%>

<html lang="en">
<head>
  <title>Login</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="css/bootstrap.min.css">
  <script src="js/jquery.min.js"></script>
  <script src="js/bootstrap.min.js"></script>
  <!-- Custom styles for this template -->
        <link href="css/sb-admin.css" rel="stylesheet">
 
  
</head>
<body>    
<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
        <ul class="nav navbar-nav">
            <li class="active"><a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Login</a></li>
      </ul>
    </div>
    
  </div>
</nav>

    

  <div class="container">

      <div class="card card-login mx-auto mt-5">
        <div class="card-body">
            <form action="conectServer" method="post">
            <div class="form-group">
                <label for="exampleInputEmail1">Usuario</label>
              <input type="text" name="user" id="user" class="form-control" placeholder="Usuario"  required>
            </div>
            <div class="form-group">
              <label for="exampleInputPassword1">Contraseña</label>
              <input type="password" name="password" id="password" class="form-control" placeholder="Password" required>
            </div>
            <input  class="btn btn-primary btn-block" type="submit" name="login" value="LOGIN"/>
            <!--<a class="btn btn-primary btn-block" href="login.jsp">Login</a>-->
           
            <font color="red"><%=mensaje%></font>
            <%
                mensaje="";
                session.setAttribute("sesionError","");
            %>
          </form>
          <div class="text-center">
            <a class="d-block small mt-3" href="registrar.jsp">Registrar una Cuenta</a>
          </div>
        </div>
      </div>
    </div> 
    


</body>
</html>
