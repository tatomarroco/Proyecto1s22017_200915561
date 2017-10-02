from NodoB import NodoB

nodoB = NodoB()

########################################################################
class Page():
    """"""

    #----------------------------------------------------------------------
    def __init__(self, Ramas=[None,None,None,None,None],Claves=[None,None,None,None],Cuentas=0):
        self.Ramas = Ramas
        self.Claves = Claves
        self.Cuentas = Cuentas        
        """Constructor"""
        
    #----------------------------------------------------------------------
    def getRamas(self):
        return self.Ramas

    #----------------------------------------------------------------------
    def setRamas(self, ramas):
        self.Ramas = ramas
        """"""
        
    #----------------------------------------------------------------------
    def getClaves(self):
        return self.Claves
    
    #----------------------------------------------------------------------
    def setClaves(self, claves):
        self.Claves = claves
        """"""
        
    #----------------------------------------------------------------------
    def getCuentas(self):
        return self.Cuentas

    #----------------------------------------------------------------------
    def setCuentas(self, cuentas):
        self.Cuentas = cuentas
        """"""
        
        
        
        
        
    
    