class usuario():
    def __init__(self, nombres, apellidos, nombre_usuario ,correo , contraseña, rol, estado):
        self.id_usuario       = None
        self.nombres          = nombres
        self.apellidos        = apellidos
        self.nombre_usuario   = nombre_usuario
        self.correo           = correo
        self.contraseña       = contraseña
        self.rol              = rol
        self.estado           = estado
        self.fecha_creacion   = None
        self.ultimo_acceso    = None
        
    def __str__(self):
            return f"[{self.nombres}] {self.apellidos} {self.__nombre_usuario} {self.correo} {self.__contraseña} {self.rol} {self.estado} {self.fecha_creacion} {self.ultimo_acceso}"