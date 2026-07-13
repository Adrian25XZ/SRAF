class Area():
    def __init__(self, nombre, descripcion):
        self.id_area      = None
        self.nombre       = nombre
        self.descripcion  = descripcion
    
    def __str__(self):
        return f"[{self.id_sede}] {self.nombre} {self.descripcion}"