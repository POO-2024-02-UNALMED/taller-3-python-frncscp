class TV:
    numTV = 0

    def __init__(self, marca, estado):
        TV.numTV += 1
        self.__marca = marca
        self.estado = estado
        self.canal = 1
        self.__precio = 500
        self.volumen = 1
        self.__control = None

    def getMarca(self):
        return self.__marca
    
    def setMarca(self, marca):
        self.__marca = marca

    def getCanal(self):
        return self.canal
    
    def setCanal(self, canal):
        if self.estado and canal >= 1 and canal <= 120:
            self.canal = canal

    def getPrecio(self):
        return self.__precio
    
    def setPrecio(self, precio):
        self.__precio = precio

    def getVolumen(self):
        return self.volumen
    
    def setVolumen(self, volumen):
        if self.estado and volumen >= 0 and volumen <= 7:
            self.volumen = volumen

    def getControl(self):
        return self.__control
    
    def setControl(self, control):
        self.__control = control

    def getNumTv():
        return TV.numTV
    
    def setNumTV(numTV):
        TV.numTV = numTV

    def turnOff(self):
        self.estado = False

    def turnOn(self):
        self.estado = True

    def getEstado(self):
        return self.estado
    
    def canalUp(self):
        if self.canal < 120 and self.canal > 0 and self.estado:
            self.canal += 1

    def canalDown(self):
        if self.canal > 1 and self.canal <= 120 and self.estado:
            self.canal -= 1

    def volumenUp(self):
        if self.volumen >= 0 and self.volumen < 7 and self.estado:
            self.volumen += 1
    
    def volumenDown(self):
        if self.volumen > 0 and self.volumen <= 7 and self.estado:
            self.volumen -= 1

        