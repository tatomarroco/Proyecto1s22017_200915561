<%-- 
    Document   : drive
    Created on : 6/09/2017, 08:54:37 PM
    Author     : Estuardo
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import="Controladores.conectServer" %>
<%@page import="Controladores.crearCarpeta" %>
<!DOCTYPE html>


<% 
    crearCarpeta cp = new crearCarpeta();
    
    String usuario="";
    if(session.getAttribute("sesionusuario")!=null){
        usuario=String.valueOf(session.getAttribute("sesionusuario"));
    }
    
    String carpetas = "";
    carpetas = cp.getCarpetasString();
%>

<html lang="en">
<head>
  <title>USAC DRIVE</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!--<link rel="stylesheet" href="css/d.css">-->
  <link rel="stylesheet" href="css/bootstrap.min.css">
  <script src="js/jquery.min.js"></script>
  <script src="js/bootstrap.min.js"></script>
  
  <style>
    /* Remove the navbar's default margin-bottom and rounded borders */ 
    .navbar {
      margin-bottom: 0;
      border-radius: 0;
    }
    
    .dialogoejemplo{text-align:right;border:1px solid #888;-moz-border-radius:6px;-webkit-border-radius:6px;-khtml-border-radius:6px;border-radius:6px;-moz-box-shadow:1px 1px 20px rgba(0,0,0,0.4);-webkit-box-shadow:1px 1px 20px rgba(0,0,0,0.4);box-shadow:0 0 20px rgba(0,0,0,0.4)}
    
    /* Add a gray background color and some padding to the footer */
    footer {
      background-color: #f2f2f2;
      padding: 25px;
    }
  </style>
</head>
<body style="background-color: #f2f2f2">

<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <div class="navbar-text"><font color="white" size="3">&nbsp;&nbsp&nbsp;&nbsp USAC Drive</font></div>
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav">
        <li><a href="#">Acerca De</a></li>
      </ul>
       
        <!--Barra Buscador-->
        <form class="navbar-form navbar-nav" role="search" style="float: top">
            &nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp
            <div class="input-group" > 
                <input type="text" class="form-control" style="width: 450px" placeholder="Buscar en el Drive">
                <span class="input-group-btn">
                    <button class="btn btn-default" type="button">
                        <span class="glyphicon glyphicon-search"></span>
                    </button>
                </span>
            </div>
        </form>
        <!--++++++++++++++++-->
        
        
            
      
      <!--ELEMENTOS DE SESION-->   
      <ul class="nav navbar-nav navbar-right">
          <li>
              <div class="navbar-text">
                  <span style="color:chartreuse" class="glyphicon glyphicon-user"></span>
                  <font color="white" size="3"> <%=usuario%>'s Drive</font>
              </div>
          </li>  
        <li>
            <a href="#"><span class="glyphicon glyphicon-log-out"></span> Cerrar Sesión</a>
        </li>
      </ul>
      <!--++++++++++++++++++++++++++++++++++++++++++-->  
        
    </div>
  </div>
</nav>

        

  
      
              <footer class="container-fluid" style="-webkit-box-shadow: inset 0px 6px 7px -1px rgba(0,0,0,0.34);
-moz-box-shadow: inset 0px 6px 7px -1px rgba(0,0,0,0.34);
box-shadow: inset 0px 6px 7px -1px rgba(0,0,0,0.34);">
               
        
                <div class="btn-group col-sm-3">
                    <input style="-webkit-box-shadow: 4px 5px 7px -1px rgba(0,0,0,0.34);
                  -moz-box-shadow: 4px 5px 7px -1px rgba(0,0,0,0.34);
                  box-shadow: 4px 5px 7px -1px rgba(0,0,0,0.34);" class="btn btn-primary btn-sm" type="button" data-toggle="dropdown" name="uploadFile" value="Nuevo"/>
                    
                    <ul class="dropdown-menu" role="menu">
                        <li>
                            <form action="crearCarpeta" method="post">
                                <input type="hidden" id="nombre" name="nombre" value="nulo">
                                <input type="submit" onclick="myFunction()" class="btn btn-info" value=" Carpeta ">
                            </form>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <form action="" method="post">
                                <input type="file" name="Archivo" id="fileElem" style="display:none" onchange="handleFiles(this.files)">
                                <input type="submit" onclick="doClick()" class="btn btn-info" value="Subir Archivo">
                            </form>
                        </li>
                    </ul>
                </div>
                <!--DIRECCION++++++++++++++++++++++++++-->  
                <div class="col-sm-9">
                    <p class="text-left text-warning"><span class="glyphicon glyphicon-triangle-right"></span>/</p>
                </div>
                <!--+++++++++++++++++++++++++++++++++++-->
             
          
     
  </footer>
       
<div class="container-fluid">
    <div style="height: 555px" class="row content">
        
        
    
    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#barralat" style="background-color:#31b0d5" >
        <span style="color:chartreuse" class="icon-bar"></span>
        <span style="color:chartreuse" class="icon-bar"></span>
      </button>
   
        
    <div class="col-sm-3 sidenav sidenav-toggled" style="background-color: #f2f2f2; height: 1025px;float: left;-webkit-box-shadow: inset 0px 6px 7px -1px rgba(0,0,0,0.34);
-moz-box-shadow: inset 0px 6px 7px -1px rgba(0,0,0,0.34);
box-shadow: inset 0px 6px 7px -1px rgba(0,0,0,0.34);" id="barralat">
      
        <br>  
      <ul class="nav nav-pills nav-stacked">
        <li class="active"><a href="drive.jsp">Mi Unidad</a></li>
        <li><a href="#section2">Compartidos Conmigo</a></li>
      </ul><br>
      
      <br><br>
    
      </div>
           
       
<!--DIVISION PARA CARPETAS-->        
<div class="container-fluid col-md-9 text-center" style="float: right;background-color: white;-webkit-box-shadow: inset 0px 6px 7px -1px rgba(0,0,0,0.34);
-moz-box-shadow: inset 0px 6px 7px -1px rgba(0,0,0,0.34);
box-shadow: inset 0px 6px 7px -1px rgba(0,0,0,0.34);" >  
    <div class="row nav navbar-inverse" style="width: 103.10%">
        <h5 style="color: white; text-align: left">&nbsp;&nbsp&nbsp;&nbsp Carpetas</h5>
    </div>
    
  <div class="row" style="overflow: auto; height:480px">
      <%=carpetas%>
      
     
      <!--<div class="col-sm-3">
      <p>Some text..</p>
      <img src="imgs/carpeta.png" class="img-responsive" style="width:100%" alt="Image">
    </div>
    <div class="col-sm-3"> 
      <p>Some text..</p>
      <img src="imgs/img.png" class="img-responsive" style="width:100%" alt="Image">
    </div>
    <div class="col-sm-3"> 
      <p>Some text..</p>
      <img src="imgs/video.png" class="img-responsive" style="width:100%" alt="Image">
    </div>
    <div class="col-sm-3">
      <p>Some text..</p>
      <img src="imgs/audio.png" class="img-responsive" style="width:100%" alt="Image">
    </div>
      <div class="col-sm-3">
      <p>Some text..</p>
      <img src="imgs/carpeta.png" class="img-responsive" style="width:100%" alt="Image">
    </div>
    <div class="col-sm-3"> 
      <p>Some text..</p>
      <img src="imgs/img.png" class="img-responsive" style="width:100%" alt="Image">
    </div>
    <div class="col-sm-3"> 
      <p>Some text..</p>
      <img src="imgs/video.png" class="img-responsive" style="width:100%" alt="Image">
    </div>
    <div class="col-sm-3">
      <p>Some text..</p>
      <img src="imgs/audio.png" class="img-responsive" style="width:100%" alt="Image">
    </div>
      <div class="col-sm-3"> 
      <p>Some text..</p>
      <img src="imgs/video.png" class="img-responsive" style="width:100%" alt="Image">
    </div>
    <div class="col-sm-3">
      <p>Some text..</p>
      <img src="imgs/audio.png" class="img-responsive" style="width:100%" alt="Image">
    </div>
      <div class="col-sm-3"> 
      <p>Some text..</p>
      <img src="imgs/img.png" class="img-responsive" style="width:100%" alt="Image">
    </div>
    <div class="col-sm-3"> 
      <p>Some text..</p>
      <img src="imgs/video.png" class="img-responsive" style="width:100%" alt="Image">
    </div>
    <div class="col-sm-3">
      <p>Some text..</p>
      <img src="imgs/audio.png" class="img-responsive" style="width:100%" alt="Image">
    </div>
      <div class="col-sm-3"> 
      <p>Some text..</p>
      <img src="imgs/video.png" class="img-responsive" style="width:100%" alt="Image">
    </div>
    <div class="col-sm-3">
      <p>Some text..</p>
      <img src="imgs/audio.png" class="img-responsive" style="width:100%" alt="Image">
    </div>-->
  </div>
</div><br>

<!--DIVISION PARA ARVHIVOS-->
<div class="container-fluid col-md-9 text-center" style="float: right;background-color: white">
  
  <div class="row nav navbar-inverse" style="width: 103.10%">
        <h5 style="color: white; text-align: left">&nbsp;&nbsp&nbsp;&nbsp Archivos</h5>
  </div>  
    
  <div class="row" style="overflow: auto; height:480px">
    <div class="col-sm-3">
      <p>Some text..</p>
      <img src="imgs/apk.png" class="img-responsive" style="width:100%" alt="Image">
    </div>
    <div class="col-sm-3"> 
      <p>Some text..</p>
      <img src="imgs/archivo.png" class="img-responsive" style="width:100%" alt="Image">
    </div>
    <div class="col-sm-3"> 
      <p>Some text..</p>
      <img src="imgs/pdf.png" class="img-responsive" style="width:100%" alt="Image">
    </div>
    <div class="col-sm-3">
      <p>Some text..</p>
      <img src="imgs/texto.png" class="img-responsive" style="width:100%" alt="Image">
    </div>
  </div>
</div>
</div>

 </div>
              <script type="text/javascript" src="js/c.js"></script>
              <script type="text/javascript">olTag()</script>    <script>
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

      ga('create', 'UA-420622-2', 'auto');
      ga('send', 'pageview');
    </script>
    
    <script>
        function myFunction(){

            var name = prompt("Nueva Carpeta","Escribe el Nombre de Carpeta...");
            
            if (name!=null){
                document.getElementById("nombre").value = name;
            }else{
                document.getElementById("nombre").value = "nulo";
            }
            
        }
    </script>
    
    <script>
        function doClick() {
            var el = document.getElementById("fileElem");
            if (el) {
              el.click();
            }
        }
    </script>
    
    
</body>



</html>
