#
#3.- Configurar contenedores
#
#eliminar barra y de titulo - opacidad
self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
self.setWindowOpacity(1)
#Cerrar ventana
self.boton_salir.clicked.connect(lambda: self.close())
# mover ventana
self.frame_superior.mouseMoveEvent = self.mover_ventana
#menu lateral
self.boton_menu.clicked.connect(self.mover_menu)
#Fijar ancho columnas
self.tabla_productos.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)