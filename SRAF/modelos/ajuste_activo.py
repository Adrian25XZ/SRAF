class AjusteActivo():
    def __init__(self, fecha, tipo_ajuste, valor_anterior, valor_nuevo, observacion, id_activo, id_usuario):
        self.id_ajuste      = None
        self.fecha          = fecha
        self.tipo_ajuste    = tipo_ajuste 
        self.valor_anterior = valor_anterior
        self.valor_nuevo    = valor_nuevo
        self.observacion    = observacion
        self.id_activo      = id_activo
        self.id_usuario     = id_usuario
    
    def __str__(self):
        return f"[{self.id_ajuste}] {self.fecha} {self.tipo_ajuste} {self.valor_anterior} {self.valor_nuevo} {self.observacion} {self.id_activo} {self.id_usuario}"
    
    def to_dict(self):
        return{
            "id_ajuste":        self.id_ajuste,
            "fecha":            self.fecha,
            "tipo_ajuste":      self.tipo_ajuste,
            "valor_anterio":    self.valor_anterior,
            "valor_nuevo":      self.valor_nuevo,
            "observacion":      self.observacion,
            "id_activo":        self.id_activo,
            "id_usuario":       self.id_usuario
        }