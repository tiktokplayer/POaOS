import paises
import re

class Editorial():
    def __init__(self, id_editorial, nombre_editorial, fecha_fundacion, codigo_pais, telefono_pais, correo_contacto):
        super().__init__(codigo_pais)
        self.id_editorial = id_editorial
        self.nombre_editorial = nombre_editorial
        self.fecha_fundacion = fecha_fundacion
        self.telefono_pais = telefono_pais
        self.correo_contacto = correo_contacto

    def validar_correo(self):
        read_correo = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        return bool(re.fullmatch(read_correo, self.correo_usuario))
