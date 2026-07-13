class BajaActivo():
    def __init__(self, fecha_baja, motivo, descripcion):
        self.id_baja      = None
        self.fecha_baja   = fecha_baja
        self.motivo       = motivo
        self.descripcion  = descripcion
        
    def __str__(self):
            return f"[{self.id_baja}] {self.fecha_baja} {self.motivo} {self.__descripcion}"