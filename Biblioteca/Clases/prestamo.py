import detalle_libro
import usuarios

class prestamo(detalle_libro, usuarios):
    def __init__(self, id_prestamo, id_detalle_libro, id_usuario, fecha_prestamo, fecha_devolucion, fecha_devuelto, cantidad_solicitada):
        super().__init__(id_detalle_libro)
        super().__init__(id_usuario)
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.fecha_devuelto = fecha_devuelto
        self.cantidad_solicitada = cantidad_solicitada

    
