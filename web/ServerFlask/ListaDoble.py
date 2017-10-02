from NodoLista import NodoLista
########################################################################
class ListaDoble():
    longitud = 0

    #----------------------------------------------------------------------
    def __init__(self):
        self.Primero = None
        self.Ultimo  = None
        
    #----------------------------------------------------------------------
    def Add(self, usuario, password):
        Nuevo = NodoLista(usuario, password)
        aux = self.Primero
        if (self.Primero == None):
            self.Primero = Nuevo
            self.Ultimo = Nuevo
            Nuevo.getNRaiz().crearCarpetaRaiz(usuario)
        else:
            while(aux != None):
                if(aux.Sig == None):
                    self.Ultimo.Sig = Nuevo
                    Nuevo.Ant = self.Ultimo
                    self.Ultimo = Nuevo
                    Nuevo.getNRaiz().crearCarpetaRaiz(usuario)
                    break
                aux = aux.Sig
        self.longitud += 1  
        
    #----------------------------------------------------------------------
    def recorrer(self):
        aux = self.Primero
        ant = None
        if (self.Primero == None):
            return "Lista Vacia"
        else:
            while (aux != None):
                    ant = aux
                    aux = aux.Sig
            print "True"
            return "True"    
        
    def consultar(self, usuario,password):
        aux = self.Primero
        if (self.Primero == None):
            print "Lista Vacia"
            return "Lista Vacia" 
        else:
            while (aux != None):
                user = aux.getUsuario()
                contra = aux.getPassword()
                if (user == str(usuario)) and (contra == str(password)):
                    print "True"
                    return "true"
                    break
                aux = aux.Sig
                
    def ObtenerCarpetaRaiz(self, usuario):
        aux = self.Primero
        if (self.Primero == None):
            print "Lista Vacia"
            return "Lista Vacia" 
        else:
            while (aux != None):
                user = aux.getUsuario()
                if (user == str(usuario)):
                    Raiz = aux.getNRaiz().getArbolBRaiz()
                    print "True"
                    return Raiz
                    break
                aux = aux.Sig    