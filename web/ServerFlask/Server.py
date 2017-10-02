from flask import Flask, Response, request
from ListaDoble import ListaDoble
from ArbolB import ArbolB
from Page import Page 

app = Flask("Server")

ListaUsuarios = ListaDoble()
Carpetas = ArbolB()

########################################################################
class Server():

        @app.route('/crearUsuario',methods=['POST'])
        def insertarUsuario():
                user = str(request.form['user'])
                contra = str(request.form['password'])
                ListaUsuarios.Add(user,contra)
                print "true"
                return "true"
        
        #METODO Para consultar la Lista Doble
        @app.route('/verify',methods=['POST'])
        def consulta():
                user = str(request.form['user'])
                contra = str(request.form['password'])                
                resultado = ListaUsuarios.consultar(user, contra)
                print resultado
                return str(resultado)
        
        #METODO Para Crear Carpeta
        @app.route('/crearCarpeta',methods=['POST'])
        def insertarCapeta():
                usuario = str(request.form['user'])
                nombre = str(request.form['nombre'])
                if(nombre == "nulo"):
                        return "No inserta nada"
                else:
                        LaRaiz = ListaUsuarios.ObtenerCarpetaRaiz(usuario)
                        LaRaiz.CrearNodo(usuario, nombre, Page(Ramas=[None,None, None,None,None], Claves=[None,None,None,None],Cuentas=0))
                        LaRaiz.CrearArchivo()
                        elestring =  LaRaiz.CrearCarpetaHTML()
                return str(elestring)
                                        
        
        #CORRE EL SERVIDOR EN
        if __name__ == "__main__":
                app.run(debug=True, host='0.0.0.0')                