class Lista:
    def __init__(self, nombre, forma, doble, listanodos):
        self.nombre = nombre
        self.forma = forma
        self.doble = doble
        self.listanodos = listanodos

class Matriz:
    def __init__(self, filas, colmnas, nombre, forma, matrizdoble, listanodos):
        self.filas = filas
        self.columnas = colmnas
        self.nombre = nombre
        self.forma = forma
        self.matrizdoble = matrizdoble

class Tabla:
    def __init__(self, columnas, nombre):
        self.columnas = columnas
        self.nombre = nombre

class NodoLista:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

class NodosLista:
    def __init__(self, cantidad, nombre, color):
        self.cantidad = cantidad
        self.nombre = nombre
        self.color = color

class FilaMatriz:
    def __init__(self, listanodos, color):
        self.listanodos = listanodos
        self.color = color

class NodoMatriz:
    def __init__(self, x, y, nombre, color):
        self.x = x
        self.y = y
        self.nombre = nombre
        self.color = color
