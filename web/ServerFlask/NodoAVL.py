########################################################################
class NodoAVL():

    #----------------------------------------------------------------------
    def __init__(self, idname, nombre, extension, contenido):
        self.idName = idname
        self.Nombre = nombre
        self.ext = extension
        self.Contenido = contenido
        self.Raiz = None
        self.Izq = None
        self.Der = None
        self.FE = 0
    
    #----------------------------------------------------------------------
    def getIdName(self):
        return self.idName
    
    #----------------------------------------------------------------------
    def setIdName(self, idname):
        self.idName = idname
        
    #----------------------------------------------------------------------
    def getNombre(self):
        return self.Nombre
    
    #----------------------------------------------------------------------
    def setNombre(self, nombre):
        self.Nombre = nombre
    
    #----------------------------------------------------------------------
    def getExtension(self):
        return self.ext
    
    #----------------------------------------------------------------------
    def setExtension(self, extension):
        self.ext = extension
    
    #----------------------------------------------------------------------
    def getContent(self):
        return self.Contenido
    
    #----------------------------------------------------------------------
    def setContent(self, contenido):
        self.Contenido = contenido
    
    #----RAIZ------------------------------------------------------------------
    def getRoot(self):
        return self.Raiz
    
    #----RAIZ------------------------------------------------------------------
    def setRoot(self, raiz):
        self.Raiz = raiz
    
    #----IZQUIERDA------------------------------------------------------------------
    def getLeft(self):
        return self.Izq
    
    #----IZQUIERDA------------------------------------------------------------------
    def setLeft(self, izquierda):
        self.Izq = izquierda
    
    #----DERECHA------------------------------------------------------------------
    def getDerecha(self):
        return self.Der
    
    #----DERECHA------------------------------------------------------------------
    def setRight(self, derecha):
        self.Der = derecha
    
    #----FACTOR EQUILIBRIO------------------------------------------------------------------
    def getFactorEquilibrio(self):
        return self.FE
    
    #----FACTOR EQUILIBRIO------------------------------------------------------------------
    def setFactorEquilibrio(self,fe):
        self.FE = fe