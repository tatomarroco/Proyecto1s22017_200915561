<%-- 
    Document   : registrar
    Created on : 6/09/2017, 11:42:32 AM
    Author     : Estuardo
--%>
<!-- Aqui importan el/los Servlet para la/s funcion/es que va a tener la pagina-->
<%@page import="Controladores.crearUsuario"%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>

<%    
    String mensaje="";
%>

<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Registrar</title>
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
            <li class="active"><a>&nbsp;&nbsp;&nbsp;Registrar</a></li>
      </ul>
    </div>
    
  </div>
</nav>
        
        
        <div class="container">

      <div class="card card-register mx-auto mt-1">
        <div class="card-body">
          <form action="crearUsuario" method="post">
            <div class="form-group">
              <label for="exampleInputEmail1">Usuario</label>
              <input type="text" name="user" id="user" class="form-control" placeholder="Usuario"  required>
            </div>
            <div class="form-group">
              <div class="form-row">
                <div class="col-md-6">
                  <label for="exampleInputPassword1">Contraseña</label>
                  <input type="password" name="password" id="password" class="form-control" placeholder="Contraseña" required>
                </div>
                <div class="col-md-6">
                  <label for="exampleConfirmPassword">Confirmar Contraseña</label>
                  <input type="password" name="cpassword" id="cpassword" class="form-control" placeholder="Confirmar Contraseña" required>
                </div>
              </div>
            </div>
            <br /><br /><br /><br /><br />  
            <input  class="btn btn-primary btn-block" type="submit" name="register" value="REGISTRAR"/>
            
            <!--asigno a la variable mensaje creada arriba un error en dado caso lo haya -->
            <%
                mensaje = crearUsuario.getError();
            %>
            <!--muestro el mensaje (o la variable)-->
            <font color="red"><%=mensaje%></font>
            
            
            
          </form>
        </div>
      </div>
    </div>
        
        
    </body>
</html>
