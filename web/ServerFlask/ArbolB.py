import sys
import os
import os.path
from NodoB import NodoB
from Page import Page

#page = Page()
#nodob = NodoB()

########################################################################
class ArbolB():
    carpstring = ""
    
    #----------------------------------------------------------------------
    def __init__(self):
        self.Inicio = Page()
        self.Inicio2 = Page()
        self.NBinsert = NodoB()
        self.Enlace = Page()
        self.Pivote = False
        self.Bandera = False
        self.Bandera2 = False
        """"""
        
    #----------------------------------------------------------------------
    def getInicio(self):
        return self.Inicio
    
    #----------------------------------------------------------------------
    def getPivote(self):
        return self.Pivote    
    
    #----------------------------------------------------------------------
    def setPivote(self, piv):
        self.Pivote = piv
        """"""
        
    #----------------------------------------------------------------------
    def getBandera(self):
        return self.Bandera
    
    #----------------------------------------------------------------------
    def setBandera(self, bandera):
        self.Bandera = bandera
        """"""
    #----------------------------------------------------------------------
    def getBandera2(self):
        return self.Bandera2
            
    #----------------------------------------------------------------------
    def setBandera2(self, bandera2):
        self.Bandera2 = bandera2
        """"""        
            
        
    #----------------------------------------------------------------------
    def getEnlace(self):
        return self.Enlace
    
    #----------------------------------------------------------------------
    def setEnlace(self, enlace):
        self.Enlace = enlace
        """"""
    
    #----------------------------------------------------------------------
    def getInsert(self):
        return self.NBinsert
    
    #----------------------------------------------------------------------
    def setNBInsert(self,nbinsert):
        self.NBinsert = nbinsert
        """""" 
    
    #-------RAIZ EXISTE O NO---------------------------------------------------------------
    def RootExiste(self, root):
        if(root == None or root.Cuentas == 0):
            return True
        else:
            return False
        
    #----------------------------------------------------------------------
    def Existe(self, clave, root):
        valor = 0
        if(clave.getNombre() < root.Claves[0].getNombre()):
            self.Bandera2 = False
            valor = 0
        else:
            valor = root.Cuentas
            while(clave.getNombre() < root.Claves[valor - 1].getNombre() and valor > 1):
                valor -= 1
                
            if (clave.getNombre() < root.Claves[valor - 1].getNombre()):
                self.setBandera(True) 
            else:
                self.setBandera(False)

            if (clave.getNombre() == root.Claves[valor - 1].getNombre()):
                self.setBandera2(True)
            else:
                self.setBandera2(False)
                
        return valor
        
        
        
    #------CREA NODO A INSERTAR----------------------------------------------------------------
    def CrearNodo(self,usuario,nombre,root):
        Nuevo = NodoB(nombre)
        self.InsertarNodo(usuario, nombre, Nuevo, self.Inicio)
    
    #-------AGREGAR---------------------------------------------------------------
    def Add(self,usuario,nombre, clave, root):
        posicion = 0
        self.setPivote(False)
        
        if(self.RootExiste(root)):
            self.setPivote(True)
            self.setNBInsert(clave)
            self.Enlace = None
            self.crearCarpeta(usuario, nombre)
            print("Se inserto")
        else:
            posicion = self.Existe(clave, root)
            if(self.getBandera() == True):
                self.setPivote(False)
            else:
                self.Add(usuario, nombre, clave, root.Ramas[posicion])
                if(self.getPivote() == True):
                    if(root.getCuentas() < 4):
                        self.setPivote(False)
                        self.ClaveInsert(self.getInsert(), root, posicion)
                        self.crearCarpeta(usuario, nombre)
                        print("Se inserto")
                    else:
                        self.setPivote(True)
                        self.DivPage(self.getInsert(), root, posicion)
                        
                    
        
        
    #-----INSERTA NODO EN EL ARBOL-----------------------------------------------------------------
    def InsertarNodo(self, usuario, nombre, clave, root):
        self.Add(usuario, nombre, clave, root)
        if(self.getPivote() == True):
            self.Inicio = Page(Ramas=[None, None, None, None, None], Claves=[None, None, None, None],Cuentas=0)
            self.Inicio.setCuentas(1)
            self.Inicio.Claves[0] = self.getInsert()
            self.Inicio.Ramas[0] = root
            self.Inicio.Ramas[1] = self.getEnlace()
        """"""
        
    #-----INSERTA LA CLAVE EN LA PAGINA-----------------------------------------------------------------
    def ClaveInsert(self,clave,root, position):
        i = root.getCuentas()
        while(i != position):
            root.Claves[i] = root.Claves[i - 1]
            root.Ramas[i + 1] = root.Ramas[i]
            i -= 1
        root.Claves[position] = clave
        root.Ramas[position + 1] = self.getEnlace()
        valorCuenta = root.getCuentas() + 1
        root.Cuentas = valorCuenta
        #root.setCuentas(valorCuenta)
        print("Nodo Insertado...")
        """"""
        
    #------DIVIDE PAGINA----------------------------------------------------------------
    def DivPage(self, clave, root, position):
        posi = 0
        PosPiv = 0
        if(position <= 2):
            PosPiv = 2
        else:
            PosPiv = 3
        Medio = Page(Ramas=[None, None, None, None, None], Claves=[None, None, None, None],Cuentas=0)
        Posi = PosPiv + 1
        while(posi != 5):
            i = ((posi - PosPiv) - 1)
            j = posi - 1
            Medio.Claves[i] = root.Claves[j]
            Medio.Ramas[posi - PosPiv] = root.Ramas[posi]
            posi += 1
        Medio.setCuentas(4 - PosPiv)
        root.setCuentas(PosPiv)
        
        if(posi < 2):
            self.ClaveInsert(clave, root, position)
        else:
            self.ClaveInsert(clave, Medio, (position - PosPiv))
        
        self.setNBInsert(root.Claves[root.getCuentas() - 1])
        Medio.Ramas[0] = root.Ramas[root.getCuentas()]
        valor = root.getCuentas() - 1
        root.setCuentas(valor)
        self.setEnlace(Medio)        
        """"""
    
    #-------CREAR CARPETA FISICA---------------------------------------------------------------
    def crearCarpeta(self, usuario, nombre):
        if(os.path.exists(usuario+"/"+nombre)):
            print ""
        else:
            print "Carpeta no creada la Creare..."
            print "."
            print "."
            print "."
            os.makedirs(usuario+"/"+nombre)
            self.carpstring += "<div class=\"col-sm-3\"> \n <p>" + str(nombre) + "</p> \n  <img src=\"imgs/carpeta.png\" class=\"img-responsive\" style=\"width:100%\" alt=\"Image\"> \n </div> \n"
            print "Carpeta creada con exito"
            
    
    def retornarNodoArbolB(self, nombreCarpeta, root):	
        self.Inicio = root 
        clave = NodoB(nombre)
        return self.retornarNodo(clave, self.Inicio)
        
    #Buscar Nodo
    def retornarNodo(self, clave, root):
        valorEncontrado = None
        pos = 0
        vacio = self.RootExiste(root)

        if(vacio == True):
            print("No Existe")
        else:
            pos = self.Existe(clave, root)
            if(self.Bandera2 == True):
                valorEncontrado = root.Claves[pos - 1]				
            else:
                valorEncontrado = self.retornarNodo(clave, root.Ramas[pos])
        return valorEncontrado
    
    
    #----------------------------------------------------------------------
    def CrearCarpetaHTML(self):
        print self.carpstring
        return str(self.carpstring)
        """archivo = open('carpetas.html','w')
        archivo.write('<html>')
        archivo.write('<body> \n')
        archivo.close()
        self.NodoCarpeta()
        
        
        
        

    def NodoCarpeta(self):
        self.EscribirHTML(self.Inicio)
        archivo = open('carpetas.html','a')
        archivo.write('</body>')
        archivo.write('</html>')
        archivo.close()
    
    
    def EscribirHTML(self, root):
        nodo = root		
        archivo=open('carpetas.html','a')
        if(nodo == None):
            print("No hay nada que Graficar")
        else:
            if (nodo.Cuentas != 0):
                #self.carpstring = "<div class=\"col-sm-3\"> \n <p>" + str(nodo.Claves[0].Nombre) + "</p> \n  <img src=\"imgs/carpeta.png\" class=\"img-responsive\" style=\"width:100%\" alt=\"Image\"> \n </div> \n"
                archivo.writelines("<div class=\"col-sm-3\"> \n <p>" + str(nodo.Claves[0].Nombre) + "</p> \n  <img src=\"imgs/carpeta.png\" class=\"img-responsive\" style=\"width:100%\" alt=\"Image\"> \n </div> \n")
                k=1
                while k <= nodo.Cuentas:
                    if(nodo.Claves[k]!= None):
                        #self.carpstring += "<div class=\"col-sm-3\"> \n <p>" + str(nodo.Claves[k].Nombre) + "</p> \n  <img src=\"imgs/carpeta.png\" class=\"img-responsive\" style=\"width:100%\" alt=\"Image\"> \n </div> \n"
                        archivo.writelines("<div class=\"col-sm-3\"> \n <p>" + str(nodo.Claves[k].Nombre) + "</p> \n  <img src=\"imgs/carpeta.png\" class=\"img-responsive\" style=\"width:100%\" alt=\"Image\"> \n </div> \n")
                    k+=1
                j=0
                while j <= nodo.Cuentas:
                    self.EscribirHTML(nodo.Ramas[j])
                    j+=1"""
        
    
    
    def CrearArchivo(self):
        archivo=open('ArbolB.txt','w')
        archivo.write('digraph G{\n')
        archivo.write("node [shape = record];\n");
        archivo.write("rankdir = TD;\n");
        archivo.close()
        self.CrearArchivoNB()		    
    
    #Escribir el inicio del Archivo
    def CrearArchivoNB(self):
        self.Escribir(self.Inicio)
        archivo=open('ArbolB.txt','a')
        archivo.write('}')
        archivo.close()
    
    #Escribir Contenido del Archivo
    def Escribir(self, root):
        nodo = root		
        archivo=open('ArbolB.txt','a')
        if(nodo == None):
            print("No hay nada que Graficar")
        else:
            if (nodo.Cuentas != 0):
                archivo.writelines("activo_" + str(nodo.Claves[0].Nombre) + " [label= \"")
                k=1
                while k <= nodo.Cuentas:
                    archivo.writelines("<r" + str(k - 1) + ">" + " | " + "<cl" + str(k) + ">" + "Carpeta: " + str(nodo.Claves[k - 1].Nombre) + " &#92;" + " | ")
                    k+=1


                archivo.writelines("<r" + str(k - 1) + "> \"];\n")
                i=0
                while i <= nodo.Cuentas:
                    if (nodo.Ramas[i] != None):
                        if (nodo.Ramas[i].Cuentas != 0):
                            archivo.writelines("activo_" + str(nodo.Claves[0].Nombre) + ":r" + str(i) + " -> activo_" + str(nodo.Ramas[i].Claves[0].Nombre) + ";\n")							

                    i+=1

                j=0
                while j <= nodo.Cuentas:
                    self.Escribir(nodo.Ramas[j])
                    j+=1    