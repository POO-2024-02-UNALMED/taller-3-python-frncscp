class Control:

    def __init__(self):
        self.tv = None

    def getTv(self):
        return self.tv
    
    def setTv(self, tv):
        self.tv = tv

    def enlazar(self, tv):
        self.tv = tv
        self.tv.setControl(self)

    def turnOn(self):
        self.tv.estado = True

    def turnOff(self):
        self.tv.estado = False

    def canalUp(self):
        if self.tv.canal < 120 and self.tv.canal > 0 and self.tv.estado:
            self.tv.canal += 1

    def canalDown(self):
        if self.tv.canal > 1 and self.tv.canal <= 120 and self.tv.estado:
            self.tv.canal -= 1
    
    def volumenUp(self):
        if self.tv.volumen >= 0 and self.tv.volumen < 7 and self.tv.estado:
            self.tv.volumen += 1

    def volumenDown(self):
        if self.tv.volumen > 0 and self.tv.volumen <= 7 and self.tv.estado:
            self.tv.volumen -= 1

    def setVolumen(self, volumen):
        if self.tv.estado and volumen >= 0 and volumen <= 7:
            self.tv.volumen = volumen

    def setCanal(self, canal):
        if self.tv.estado and canal > 0 and canal <= 120:
            self.tv.canal = canal