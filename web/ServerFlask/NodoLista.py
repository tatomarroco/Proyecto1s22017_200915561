from NRaiz import NRaiz


########################################################################
class NodoLista():

    #----------------------------------------------------------------------
    def __init__(self, usuario, password):
        self.Usuario = usuario
        self.Password = password
        self.PublicKey = None
        self.PrivateKey = None
        self.Sig = None
        self.Ant = None
        self.Raiz = NRaiz()
        
        
    def getUsuario(self):
        return self.Usuario
    
    def setUsuario(self, usuario):
        self.Usuario = usuario
    
    #----------------------------------------------------------------------
    def getPassword(self):
        return self.Password
    
    #----------------------------------------------------------------------
    def setPassword(self, password):
        self.Password = password
        
    #----------------------------------------------------------------------
    def getNRaiz(self):
        return self.Raiz
    
    #----------------------------------------------------------------------
    def getPublicKey(self):
        return self.PublicKey
    
    #----------------------------------------------------------------------
    def setPublicKey(self, public):
        self.PublicKey = public
        
    #----------------------------------------------------------------------
    def getPrivateKey(self):
        return self.PrivateKey
    
    #----------------------------------------------------------------------
    def setPrivateKey(self, private):
        self.PrivateKey = private