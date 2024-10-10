from datetime import datetime
import paises

class Autor(paises):
    def __init__(self, id_autor, nombre_autor, pseudonimo_autor, codigo_pais, fecha_nacimiento, fecha_defuncion, biografia_autor, foto_autor):
        super().__init__(codigo_pais)
        self.id_autor = id_autor
        self.nombre_autor = nombre_autor
        self.pseudonimo_autor = pseudonimo_autor
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_defuncion = fecha_defuncion
        self.biografia_autor = biografia_autor
        self.foto_autor = foto_autor

        def fechas(fecha):
            fecha_datetime = datetime.strptime(fecha, '%d/%m/%Y')
            fecha_string = fecha_datetime.strftime('%Y/%m/%d')
            return fecha_string