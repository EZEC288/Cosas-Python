from datetime import datetime

class Usuario:
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contraseña = contraseña
        self.fecha_registro = fecha_registro
        self.avatar = avatar
        self.estado = estado
        self.online = online

def login(self):
    pass

def registrar(self):
    pass

class Publico(Usuario):
    def __init__(self, id, nombre, apellido, telefono, username, email, contraseña):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña)
        self.es_publico = True

    def Comentar(self):
        pass

    class Colaborador(Usuario):
      def __init__(self, id, nombre, apellido, telefono, username, email, contraseña):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña)
        self.es_colaborador = True

    def comentar(self):
        pass

    def publicar(self):
        pass

    class Articulo(Usuario):
        def __init__(self, id, id_usuario, titulo, resumen, contenido):
            self.id = id
            self.id_usuario = id_usuario
            self.titulo = titulo
            self.resumen = resumen
            self.contenido = contenido
            self.fecha_publicacion = datetime.now()
            self.imagen = None
            self.estado = "publicado"

class Comentario(Usuario):
     def __init__(self, id, id_articulo, id_usuario, contenido):
        self.id = id
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = datetime.now()
        self.estado = "Activo"

def menu_principal():
    opcion = input("Seleccione una opción:\n1. Registrar usuario\n2. Iniciar sesión\nOpción: ")

    def registrar_usuario():
        pass

    def iniciar_sesion():
        pass


    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        iniciar_sesion()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        menu_principal    


        



