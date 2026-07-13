class Categoria_Activo():
    def __init__(self,nombre ,descripcion ):
        self.id_categoria     = None
        self.nombre           = nombre
        self.descripcion      = descripcion
        
    def __str__(self):
            return f"[{self.id_sede}] {self.nombre} {self.descripcion}"