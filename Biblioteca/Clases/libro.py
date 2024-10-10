import autor

class Libro(autor):
    def __init__(self, id_isbn, titulo, id_autor):
        super().__init__(id_autor) #superclase utilizando metodos de herencia
        self.id_isbn = id_isbn
        self.titulo = titulo

    def validacion_isbn(self):
        if(1010 <= len(self.isbn) <= 13 and self.isbn.isdigit()):
            return True
        else:
            return False