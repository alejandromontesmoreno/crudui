#7.- Mover menú
def mover_menu(self):
    if True:			
        width = self.frame_lateral.width()
        widthb = self.boton_menu.width()
        normal = 0
        if width==0:
            extender = 200
            self.boton_menu.setText("Menú")
        else:
            extender = normal
            self.boton_menu.setText("")
            
        self.animacion = QPropertyAnimation(self.frame_lateral, b'minimumWidth')
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacion.start()
        
        self.animacionb = QPropertyAnimation(self.boton_menu, b'minimumWidth')
    
        self.animacionb.setStartValue(width)
        self.animacionb.setEndValue(extender)
        self.animacionb.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacionb.start()