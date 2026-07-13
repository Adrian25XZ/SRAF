class AjusteActivo():
    def __init__(self, tipo_ajuste, observacion, valor_anterior, valor_nuevo):
        self.id_ajuste      = None
        self.tipo_ajuste    = tipo_ajuste 
        self.observacion    = observacion
        self.valor_anterior = valor_anterior
        self.valor_nuevo    = valor_nuevo
        self.fecha          = None
    
    def __str__(self):
        return f"[{self.id_ajuste}] {self.tipo_ajuste} {self.observacion} {self.valor_anterior} {self.valor_nuevo} {self.fecha}"