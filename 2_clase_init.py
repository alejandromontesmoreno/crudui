#2.- Cargar archivo .ui
class Load_ui_productos(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Cargar archivo .ui
        uic.loadUi("ui/ui_productos.ui", self)
        self.show()