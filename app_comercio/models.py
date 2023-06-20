from django.db import models

class Usuario:
    def __init__(self, nombre, correo):
        self.Nombre = nombre
        self.Favoritos = []
        self.Correo = correo

    def agregarFavoritos(self, favorito):
        pass

    def realizarComentario(self, comentario):
        pass





class Administrador:
    def __init__(self, nombre, correo):
        self.Nombre = nombre
        self.Favoritos = []
        self.Correo = correo

    def agregarFavoritos(self, favorito):
        pass

    def realizarComentario(self, comentario):
        pass

    def editarPagina(self):
        pass

    def borrarComentario(self, comentario):
        pass

    def crearDemostracion(self, demostracion):
        pass

    def borrarDemostracion(self, demostracion):
        pass



class Demostracion:
    def __init__(self, titulo, explicacion):
        self.Titulo = titulo
        self.Explicacion = explicacion
        self.Comentarios = []

    def realizarComentario(self, comentario):
        self.Comentarios.append(comentario)



class Comentario:
    def __init__(self, texto, usuario, id_comentario):
        self.Texto = texto
        self.Usuario = usuario
        self.IDcoment = id_comentario


class Cliente(models.Model):
    rut = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=120)
    direccion = models.TextField()
    celular = models.IntegerField()
    email = models.EmailField()
    compraMouse = models.ManyToManyField(Mouse, blank=True)
    compraComputador = models.ManyToManyField(Computador, blank=True)
    compraMonitor = models.ManyToManyField(Monitor, blank=True)

    def __str__(self):
        return str(self.rut) + " - " + self.nombre
