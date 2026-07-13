class Sede():
    def __init__(self, nombre, direccion, ciudad):
        self.id_sede      = None
        self.nombre       = nombre
        self.direccion    = direccion
        self.ciudad       = ciudad
    
    def __str__(self):
        return f"[{self.id_sede}] {self.nombre} {self.direccion} {self.ciudad}"