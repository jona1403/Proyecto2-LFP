import re
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

def RevisionForma(FormaIngresada):
    PatternCirculo = r"[C|c][I|i][R|r][C|c][U|u][L|l][O|o]"
    PatternRectangulo = r"[R|r][E|e][C|c][T|t][A|a][N|n][G|g][U|u][L|l][O|o]"
    PatternTriangulo = r"[T|t][R|r][I|i][A|a][N|n][G|g][U|u][L|l][O|o]"
    PatternPunto = r"[P|p][U|u][N|n][T|t][O|o]"
    PatternHexagono = r"[H|h][E|e][X|x][A|a][G|g][O|o][N|n][O|o]"
    PatternDiamante = r"[D|d][I|i][A|a][M|m][A|a][N|n][T|t][E|e]"
    if re.match(PatternCirculo, FormaIngresada):
        return "circle"
    elif re.match(PatternRectangulo, FormaIngresada):
        return "rect"
    elif re.match(PatternTriangulo, FormaIngresada):
        return "triangle"
    elif re.match(PatternPunto, FormaIngresada):
        return "point"
    elif re.match(PatternHexagono, FormaIngresada):
        return "hexagon"
    elif re.match(PatternDiamante, FormaIngresada):
        return "diamond"
    else:
        return "nomatch"

def RevisionColor(ColorIngresado):
    PatternAzul = r"[A|a][Z|z][U|u][L|l]"
    PatternAzul2 = r"[A|a][Z|z][U|u][L|l][2]"
    PatternAzul3 = r"[A|a][Z|z][U|u][L|l][3]"
    PatternRojo = r"[R|r][O|o][J|j][O|o]"
    PatternRojo2 = r"[R|r][O|o][J|j][O|o][2]"
    PatternRojo3 = r"[R|r][O|o][J|j][O|o][3]"
    PatternAmarillo = r"[A|a][M|m][A|a][R|r][I|i][L|l][L|l][O|o]"
    PatternAmarillo2 = r"[A|a][M|m][A|a][R|r][I|i][L|l][L|l][O|o][2]"
    PatternAmarillo3 = r"[A|a][M|m][A|a][R|r][I|i][L|l][L|l][O|o][3]"
    PatternAnaranjado = r"[A|a][N|n][A|a][R|r][A|a][N|n][J|j][A|a][D|d][O|o]"
    PatternAnaranjado2 = r"[A|a][N|n][A|a][R|r][A|a][N|n][J|j][A|a][D|d][O|o][2]"
    PatternAnaranjado3 = r"[A|a][N|n][A|a][R|r][A|a][N|n][J|j][A|a][D|d][O|o][3]"
    PatternCafe = r"[C|c][A|a][F|f][E|e]"
    PatternCafe2 = r"[C|c][A|a][F|f][E|e][2]"
    PatternCafe3 = r"[C|c][A|a][F|f][E|e][3]"
    PatternGris = r"[G|g][R|r][I|i][S|s]"
    PatternGris2 = r"[G|g][R|r][I|i][S|s][2]"
    PatternGris3 = r"[G|g][R|r][I|i][S|s][3]"
    PatternMorado = r"[M|m][O|o][R|r][A|a][D|d][O|o]"
    PatternMorado2 = r"[M|m][O|o][R|r][A|a][D|d][O|o][2]"
    PatternMorado3 = r"[M|m][O|o][R|r][A|a][D|d][O|o][3]"
    PatternVerde = r"[V|v][E|e][R|r][D|d][E|e]"
    PatternVerde2 = r"[V|v][E|e][R|r][D|d][E|e][2]"
    PatternVerde3 = r"[V|v][E|e][R|r][D|d][E|e][3]"
    PatternBlanco = r"[B|b][L|l][A|a][N|n][C|c][O|o]"

    if re.match(PatternAzul3, ColorIngresado):
        return "#0000cc"
    elif re.match(PatternAzul2, ColorIngresado):
        return "#0000ff"
    elif re.match(PatternAzul, ColorIngresado):
        return "#4040ff"
    elif re.match(PatternRojo3, ColorIngresado):
        return "#cc0000"
    elif re.match(PatternRojo2, ColorIngresado):
        return "#ff0000"
    elif re.match(PatternRojo, ColorIngresado):
        return "#ff4040"
    elif re.match(PatternAmarillo3, ColorIngresado):
        return "#ffdf00"
    elif re.match(PatternAmarillo2, ColorIngresado):
        return "#ffff00"
    elif re.match(PatternAmarillo, ColorIngresado):
        return "#fcf75e"
    elif re.match(PatternAnaranjado3, ColorIngresado):
        return "#cc5200"
    elif re.match(PatternAnaranjado2, ColorIngresado):
        return "#ff6600"
    elif re.match(PatternAnaranjado, ColorIngresado):
        return "#ff8c40"
    elif re.match(PatternCafe3, ColorIngresado):
        return "#663300"
    elif re.match(PatternCafe2, ColorIngresado):
        return "#804000"
    elif re.match(PatternCafe, ColorIngresado):
        return "#a05000"
    elif re.match(PatternGris3, ColorIngresado):
        return "#7c7c7c"
    elif re.match(PatternGris2, ColorIngresado):
        return "#9b9b9b"
    elif re.match(PatternGris, ColorIngresado):
        return "#c2c2c2"
    elif re.match(PatternMorado3, ColorIngresado):
        return "#572364"
    elif re.match(PatternMorado2, ColorIngresado):
        return "#8e6995"
    elif re.match(PatternMorado, ColorIngresado):
        return "#e2d8e4"
    elif re.match(PatternVerde3, ColorIngresado):
        return "#244623"
    elif re.match(PatternVerde2, ColorIngresado):
        return "#008000"
    elif re.match(PatternVerde, ColorIngresado):
        return "#b5c4b3"
    elif re.match(PatternBlanco, ColorIngresado):
        return "#FFFFFF"
    else:
        return "nomatch"