import tipo_categoria_libro

class categoria_libro(tipo_categoria_libro):
    def __init__(self, id_categoria_libro, id_tipo_categoria, categoria_libro, descripcion):
        super().__init__(id_tipo_categoria)
        self.id_categoria_libro = id_categoria_libro
        self.categoria_libro = categoria_libro
        self.descripcion = descripcion