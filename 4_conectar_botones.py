#4.- Conectar botones

#Botones para cambiar de página
self.boton_agregar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_agregar))
self.boton_buscar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_buscar))
self.boton_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
self.boton_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_eliminar))
self.boton_consultar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_consultar))

#Botones para guardar, buscar, actualizar, eliminar y salir
#Botones para guardar, buscar, actualizar, eliminar y salir
self.boton_guardar_producto.clicked.connect(self.guardar_producto)
self.boton_buscar_producto_actualizar.clicked.connect(self.buscar_producto)
self.boton_buscar_producto_eliminar.clicked.connect(self.buscar_producto)
self.boton_actualizar_producto.clicked.connect(self.actualizar_producto)
self.boton_eliminar_producto.clicked.connect(self.eliminar_producto)
self.boton_limpiar_formulario.clicked.connect(self.eliminar_producto)
