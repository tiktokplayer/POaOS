import libro
import editorial

class detalle_libro(libro, editorial):
        def __init__(self, id_detalle_libro, id_isbn, fecha_edicion, id_editorial, numero_paginas, id_categoria_libro, cantidad_ejemplares, ejemplares_disponibles):
                super().__init__(id_isbn)
                super().__init__(id_editorial)
                self.id_detalle_libro = id_detalle_libro
                self.fecha_edicion = fecha_edicion
                self.numero_paginas = numero_paginas
                self.id_categoria_libro = id_categoria_libro
                self.cantidad_ejemplares = cantidad_ejemplares
                self,ejemplares_disponibles = ejemplares_disponibles

        def actualizar_disponibilidad(self, origen, cantidad):
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                return

            if origen == "retirar":
                if  self.ejemplares_disponibles >= cantidad:
                    self.ejemplares_disponibles -= cantidad
                    print(f"Se han retirado {cantidad} ejemplares. Ejemplares disponibles ahora: {self.ejemplares_disponibles}")
                else:
                    print(f"No hay suficientes ejemplares disponibles para realizar el préstamo. Ejemplares disponibles: {self.ejemplares_disponibles}")