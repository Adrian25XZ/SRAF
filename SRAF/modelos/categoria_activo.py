class Categoria_Activo():
    def __init__(self,nombre ,descripcion ):
        self.id_categoria     = None
        self.nombre           = nombre
        self.descripcion      = descripcion
        
    def __str__(self):
            return f"[{self.id_sede}] {self.nombre} {self.descripcion}"
        
    def to_dict(self):
        
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion
            
        }
    @classmethod
    def from_dict(cls, datos):
        
        categoria = cls(
            datos["nombre"],
            datos["descripcion"]   
        )
        
        categoria.id = datos["id"]
        
        return categoria