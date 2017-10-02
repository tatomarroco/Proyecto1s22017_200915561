from NodoAVL import NodoAVL 
########################################################################
class AVL():

    #----------------------------------------------------------------------
    def __init__(self):
        self.raiz = None
        self.Altura = -1
        self.Balance = 0
    
    #----------------------------------------------------------------------
    def Insertar(self, idname,nombre,extensio,contenido):
        nuevo = NodoAVL(idname, nombre, extension, contenido)
        
        if self.raiz == None:
            self.raiz = nuevo
            self.raiz.Izq = AVL()
            self.raiz.Der = AVL()
        elif idname < self.raiz.idName:
            self.raiz.Izq = nuevo
        elif idname > self.raiz.idName:
            self.raiz.Der
        """"""
        