# 6.- mover ventana
def mousePressEvent(self, event):
    self.clickPosition = event.globalPos()
def mover_ventana(self, event):
    if self.isMaximized() == False:			
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    if event.globalPos().y() <=20:
        self.showMaximized()
    else:
        self.showNormal()
            