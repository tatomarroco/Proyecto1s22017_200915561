import os
from ArbolB import ArbolB
from AVL import AVL 
########################################################################
class NRaiz():

    #----------------------------------------------------------------------
    def __init__(self):
        self.arbolB = ArbolB()
        self.avl = AVL()
        
    def getArbolBRaiz(self):
        return self.arbolB
    
    def setArbolBRaiz(self, arbolBEnR):
        self.arbolB = arbolBEnR

    #----------------------------------------------------------------------
    def getAVLRaiz(self):
        return self.avl

    #----------------------------------------------------------------------
    def setAVLRaiz(self, avlEnR):
        self.avl = avlEnR    
    
    def crearCarpetaRaiz(self, usuario):
        os.mkdir(usuario)