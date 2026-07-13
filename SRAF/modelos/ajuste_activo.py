class AjusteActivo():
    def __init__(self, tipo_ajuste, observacion, valor_anterior, valor_nuevo):
        self.__id_ajuste      = None
        self.__tipo_ajuste    = tipo_ajuste 
        self.__observacion    = observacion
        self.__valor_anterior = valor_anterior
        self.__valor_nuevo    = valor_nuevo
        self.__fecha          = None
    
    def __str__(self):
        return f"[{self.id_ajuste}] {self.tipo_ajuste} {self.observacion} {self.valor_anterior} {self.valor_nuevo} {self.fecha}"