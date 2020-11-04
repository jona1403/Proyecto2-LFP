from Clases import Lista, NodoLista, RevisionForma, RevisionColor
from Clases import Matriz, NodoMatriz
from Clases import Tabla, filatabla
from ReporteTokens import Reportes
from ReporteErrores import ReporteErrores
import re
def Lectura_De_Archivo(Ruta):
    ListaDeTokens = []
    ListaDeErrores = []
    NoError = 0
    NoToken = 0
    ListaDeErrores.append(["No", "Línea", "Columna", "Descripción"])
    ListaDeTokens.append(["No", "Línea", "Columna", "Lexema", "Token"])
    ListaDeListas = []
    ListaDeMatrices = []
    ListaDeTablas = []
    DobleLista = False
    NombreLista = ""
    FormaLista = ""
    FilasMatriz = 0
    ColumnasMatriz = 0
    NombreMatriz = ""
    FormaMatriz = ""
    DobleMatriz = ""
    ListaDeNombresMatriz = []
    x_matriz = 0
    y_matriz = 0
    y = 0
    Encabezado = []
    ListaNodosMatriz = []
    ListaDeNodos = []
    CantidadNodos = 0
    NombreNodos = ""
    Cadena = ""
    ColumnasTabla = 0
    NombreTabla = ""
    ListaDeFilasTabla = []
    ListaDeNombresFila = []
    Estado_Tipo = "ninguno"
    Estado_Cadena = "ninguno"
    Estado_Comentario = False
    PatternFalse = r"[F|f][A|a][L|l][S|s][O|o]"
    PatternVerdadero = r"[V|v][E|e][R|r][D|d][A|a][D|d][E|e][R|r][O|o]"
    PatternLista = r"[L|l][I|i][S|s][T|t][A|a]"
    PatternMatriz = r"[M|m][A|a][T|t][R|r][I|i][Z|z]"
    PatternTabla = r"[T|t][A|a][B|b][L|l][A|a]"
    PatternNodo = r"[N|n][O|o][D|d][O|o]"
    PatternFila = r"[F|f][I|i][L|l][A|a]"
    PatternNodos = r"[N|n][O|o][D|d][O|o][S|s]"
    PatternDefecto = r"[D|d][E|e][F|f][E|e][C|c][T|t][O|o]"
    PatternNumeros = r"[0-9]*"
    PatternEncabezados = r"[E|e][N|n][C|c][A|a][B|b][E|e][Z|z][A|a][D|d][O|o][S|s]"
    Fila = 0
    Columna = 0
    file = open(Ruta, "r")
    for line in file:
        Fila += 1
        Columna = 0
        for char in line:
            Columna +=1
            if char == " " or char == "\n" or char == "," or ord(char) == 34 or ord(char) == 39 or char == "(" or char == ")" or char == ";":
                pass
            else:
                Cadena += char
            if Cadena == "//":
                Estado_Comentario = True
            if Estado_Comentario == True:
                if char == "\n":
                    Estado_Comentario = False
                    Cadena = ""
            elif Estado_Tipo == "ninguno" and ListaDeNodos == []:
                if Cadena.lower() == "lista" or Cadena.lower() == "matriz" or Cadena.lower() == "tabla":
                    if re.match(PatternLista, Cadena):
                        Estado_Tipo = "lista"
                    elif re.match(PatternMatriz, Cadena):
                        Estado_Tipo = "matriz"
                    elif re.match(PatternTabla, Cadena):
                        Estado_Tipo = "tabla"
                    NoToken += 1
                    ListaDeTokens.append([str(NoToken), str(Fila), str(Columna-len(Cadena)+1), Cadena, Cadena.lower()])
                    ListaDeTokens.append(["No", "Línea", "Columna", "Lexema", "Token"])
                    Cadena = ""
                else:
                    if char == " " or char == "\n":
                        NoError+=1
                        ListaDeErrores.append([str(NoError), str(Fila), str(Columna-len(Cadena)+1), Cadena])
                        print("Cadena inesperada")
                        Cadena = ""
            elif Estado_Tipo == "lista":
                if char == "(" and Estado_Cadena == "ninguno":
                    NoToken += 1
                    ListaDeTokens.append([str(NoToken), str(Fila), str(Columna), char, Cadena.lower()])
                    Estado_Cadena = "apertura_especificaciones"
                    Cadena = ""
                elif Estado_Cadena == "ninguno" and re.match(PatternDefecto, Cadena):
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, Cadena.lower()])
                    Cadena = ""
                    Estado_Cadena = "defecto_nodo"
                elif (char == "(" or char == " ") and Estado_Cadena == "ninguno":
                    NoError += 1
                    ListaDeErrores.append([str(NoError), str(Fila), str(Columna - len(Cadena) + 1), Cadena])
                elif (ord(char) == 34 or ord(char) == 39) and Estado_Cadena == "apertura_especificaciones":
                    Estado_Cadena = "nombre_lista"
                elif (ord(char) == 34 or ord(char) == 39) and Estado_Cadena == "nombre_lista":
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Cadena nombre lista"])
                    Estado_Cadena = "ninguno"
                    NombreLista = Cadena
                    Cadena = ""
                elif char == "," and Estado_Cadena == "ninguno" and NombreLista != "":
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), char, char])
                    Estado_Cadena = "forma_lista"
                elif char == "," and Estado_Cadena == "forma_lista" and NombreLista !="":
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, Cadena.lower()])
                    Estado_Cadena = "ninguno"
                    FormaLista = RevisionForma(Cadena)
                    if FormaLista == "nomatch":
                        NoError += 1
                        ListaDeErrores.append([str(NoError), str(Fila), str(Columna - len(Cadena) + 1), Cadena])
                    else:
                        pass
                    Cadena = ""
                elif Estado_Cadena == "ninguno" and FormaLista != "":
                    Estado_Cadena = "lista_doble"
                    if char == ",":
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna), char, char])
                elif char == ")" and Estado_Cadena == "lista_doble" and FormaLista != "":
                    Estado_Cadena = "cerradura_especificaciones"
                    if re.match(PatternFalse, Cadena):
                        DobleLista = False
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, Cadena.lower()])
                        Cadena = ""
                    elif re.match(PatternVerdadero, Cadena):
                        DobleLista = True
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, Cadena.lower()])
                        Cadena = ""
                elif Estado_Cadena == "cerradura_especificaciones":
                    if char == "{":
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna), char, char])
                        Estado_Cadena = "apertura_nodos"
                        Cadena = ""
                    else:
                        if char == " ":
                            pass
                        else:
                            if char != " " and char != "\n":
                                NoError += 1
                                ListaDeErrores.append([str(NoError), str(Fila), str(Columna - len(Cadena) + 1), char])
                elif Estado_Cadena == "apertura_nodos":
                    if char == "(":
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna), char, char])
                        if re.match(PatternNodos, Cadena):
                            NoToken += 1
                            ListaDeTokens.append(
                                [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, Cadena.lower()])
                            Estado_Cadena = "nodos"
                            Cadena = ""
                        elif re.match(PatternNodo, Cadena):
                            NoToken += 1
                            ListaDeTokens.append(
                                [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, Cadena.lower()])
                            Estado_Cadena = "nodo"
                            Cadena = ""
                        else:
                            NoError += 1
                            ListaDeErrores.append([str(NoError), str(Fila), str(Columna - len(Cadena) + 1), Cadena])
                    elif char == "}":
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna), char, char])
                        Estado_Tipo = "defecto_lista"
                        Estado_Cadena = "ninguno"
                        Cadena = ""
                    elif char == " " and Cadena != "":
                        if re.match(PatternNodo, Cadena) or re.match(PatternNodos, Cadena):
                            continue
                        else:
                            NoError += 1
                            ListaDeErrores.append([str(NoError), str(Fila), str(Columna - len(Cadena) + 1), Cadena])
                            Cadena = ""
                elif Estado_Cadena == "nodo" or Estado_Cadena == "nodos":
                    if Estado_Cadena == "nodo":
                        if (ord(char) == 34 or ord(char) == 39):
                            NoToken += 1
                            ListaDeTokens.append(
                                [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Nombre nodo"])
                            Estado_Cadena = "nombre_nodo"
                            Cadena = ""
                        elif Cadena == "#" and char == "#":
                            NoToken += 1
                            ListaDeTokens.append(
                                [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Nombre nodo defecto"])
                            NombreNodos = Cadena
                            Cadena = ""
                            Estado_Cadena = "color_nodo"
                    if Estado_Cadena == "nodos":
                        if (ord(char) == 34 or ord(char) == 39):
                            NoToken += 1
                            ListaDeTokens.append(
                                [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Cantidad de nodos"])
                            Estado_Cadena = "nombre_nodo"
                            CantidadNodos = int(Cadena)
                            Cadena = ""
                        elif char == "#":
                            numaux = ""
                            for i in Cadena:
                                if re.match(PatternNumeros, i) and i != "#":
                                    numaux+=i
                            NoToken += 1
                            ListaDeTokens.append(
                                [str(NoToken), str(Fila), str(Columna - len(numaux) + 1), numaux, "Cantidad de nodos"])
                            CantidadNodos = int(numaux)
                            NombreNodos = "#"
                            Cadena = ""
                            Estado_Cadena = "color_nodo"
                elif Estado_Cadena == "nombre_nodo":
                    if (ord(char) == 34 or ord(char) == 39):
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Nombre nodo"])
                        NombreNodos = Cadena
                        Estado_Cadena = "color_nodo"
                        Cadena = ""
                elif Estado_Cadena == "color_nodo" and char == ";":
                    if CantidadNodos == 0:
                        Estado_Cadena = "apertura_nodos"
                        if Cadena == "#":
                            ListaDeNodos.append(NodoLista(NombreNodos, Cadena))
                        else:
                            ListaDeNodos.append(NodoLista(NombreNodos, RevisionColor(Cadena)))
                        NombreNodos = ""
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Color nodo"])
                        CantidadNodos = 0
                        Cadena = ""
                    else:
                        Estado_Cadena = "apertura_nodos"
                        for i in range(1 , CantidadNodos+1):
                            if Cadena == "#":
                                ListaDeNodos.append(NodoLista(NombreNodos+str(i), Cadena))
                            else:
                                ListaDeNodos.append(NodoLista(NombreNodos+str(i), RevisionColor(Cadena)))
                        NombreNodos = ""
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Color nodo"])
                        CantidadNodos = 0
                        Cadena = ""
            if Estado_Tipo == "defecto_lista" and ListaDeNodos != []:
                if re.match(PatternDefecto, Cadena):
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Defecto"])
                    Estado_Cadena = "defecto_nodo"
                    Cadena = ""
                elif Estado_Cadena == "defecto_nodo" and NombreNodos == "":
                    if (ord(char) == 34 or ord(char) == 39):
                        Estado_Cadena = "nombre_nodo"
                        Cadena = ""
                elif Estado_Cadena == "nombre_nodo":
                    if (ord(char) == 34 or ord(char) == 39):
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Nombre defecto"])
                        NombreNodos = Cadena
                        Estado_Cadena = "color_nodo"
                        Cadena = ""
                elif Estado_Cadena == "color_nodo" and char == ";":
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Color defecto"])
                    NodoDefecto = NodoLista(NombreNodos, RevisionColor(Cadena))
                    Estado_Cadena = "ninguno"
                    Estado_Tipo = "ninguno"
                    NombreNodos = ""
                    CantidadNodos = 0
                    Cadena = ""
                    ListaDeListas.append(Lista(NombreLista, FormaLista, DobleLista, ListaDeNodos))
                    Reportes(ListaDeTokens)
                    ReporteErrores(ListaDeErrores)
                    return ListaDeListas, NodoDefecto, Encabezado
                    #GraficarListas(ListaDeListas, NodoDefecto)
            elif Estado_Tipo == "matriz":
                if char == "(" and Estado_Cadena == "ninguno":
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna), char, char])
                    Estado_Cadena = "apertura_especificaciones"
                    Cadena = ""
                elif Estado_Cadena == "ninguno" and re.match(PatternDefecto, Cadena):
                    Cadena = ""
                    Estado_Cadena = "defecto_nodo"
                elif (char == "(" or char == " ") and Estado_Cadena == "ninguno":
                    print("Se repite " + Cadena)
                elif char == "," and Estado_Cadena == "apertura_especificaciones":
                    Estado_Cadena = "columnas_matriz"
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Filas matriz"])
                    FilasMatriz = int(Cadena)
                    Cadena = ""
                elif char == "," and Estado_Cadena == "columnas_matriz":
                    Estado_Cadena = "apertura_especificaciones"
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Columnas matriz"])
                    ColumnasMatriz = int(Cadena)
                    Cadena = ""
                elif (ord(char) == 34 or ord(char) == 39) and Estado_Cadena == "apertura_especificaciones":
                    Estado_Cadena = "nombre_matriz"
                elif (ord(char) == 34 or ord(char) == 39) and Estado_Cadena == "nombre_matriz":
                    Estado_Cadena = "ninguno"
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Nombre matriz"])
                    NombreMatriz = Cadena
                    Cadena = ""
                elif char == "," and Estado_Cadena == "ninguno" and NombreMatriz != "":
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna), char, char])
                    Estado_Cadena = "forma_matriz"
                elif char == "," and Estado_Cadena == "forma_matriz" and NombreMatriz != "":
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Forma matriz"])
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna), char, char])
                    Estado_Cadena = "ninguno"
                    FormaMatriz = RevisionForma(Cadena)
                    if FormaMatriz == "nomatch":
                        NoError += 1
                        ListaDeErrores.append([str(NoError), str(Fila), str(Columna - len(Cadena) + 1), Cadena])
                    else:
                        pass
                    Cadena = ""
                elif Estado_Cadena == "ninguno" and FormaMatriz != "":
                    Estado_Cadena = "matriz_doble"
                elif char == ")" and Estado_Cadena == "matriz_doble" and FormaMatriz != "":
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna), char, char])
                    Estado_Cadena = "cerradura_especificaciones"
                    if re.match(PatternFalse, Cadena):
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Matriz doble"])
                        DobleMatriz = False
                        Cadena = ""
                    elif re.match(PatternVerdadero, Cadena):
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Matriz doble"])
                        DobleMatriz = True
                        Cadena = ""
                elif Estado_Cadena == "cerradura_especificaciones":
                    if char == "{":
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna), char, char])
                        Estado_Cadena = "apertura_nodos"
                        Cadena = ""
                    else:
                        if char == " ":
                            pass
                        else:
                            if char != " " and char != "\n":
                                NoError += 1
                                ListaDeErrores.append([str(NoError), str(Fila), str(Columna), char])
                elif Estado_Cadena == "apertura_nodos":
                    if char == "(":
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna), char, char])
                        if re.match(PatternFila, Cadena):
                            NoToken += 1
                            ListaDeTokens.append(
                                [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "fila"])
                            Estado_Cadena = "fila"
                            Cadena = ""
                        elif re.match(PatternNodo, Cadena):
                            NoToken += 1
                            ListaDeTokens.append(
                                [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, Cadena.lower()])
                            Estado_Cadena = "nodo"
                            Cadena = ""
                        else:
                            NoError += 1
                            ListaDeErrores.append([str(NoError), str(Fila), str(Columna - len(Cadena) + 1), Cadena])
                    elif char == "}":
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna), char, char])
                        Estado_Tipo = "defecto_matriz"
                        Estado_Cadena = "ninguno"
                        Cadena = ""
                    elif char == " " and Cadena != "":
                        if re.match(PatternNodo, Cadena) or re.match(PatternFila, Cadena):
                            continue
                        else:
                            NoError += 1
                            ListaDeErrores.append([str(NoError), str(Fila), str(Columna - len(Cadena) + 1), Cadena])
                            Cadena = ""
                elif Estado_Cadena == "nodo" or Estado_Cadena == "fila":
                    if Estado_Cadena == "nodo":
                        if char == ",":
                            NoToken += 1
                            ListaDeTokens.append(
                                [str(NoToken), str(Fila), str(Columna), char, char])
                            Estado_Cadena = "y_matriz"
                            NoToken += 1
                            ListaDeTokens.append(
                                [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "x_nodo"])
                            x_matriz = int(Cadena)
                            Cadena = ""
                    if Estado_Cadena == "fila":
                        if (ord(char) == 34 or ord(char) == 39):
                            Estado_Cadena = "nombre_nodo"
                            Cadena = ""
                elif Estado_Cadena == "y_matriz":
                    if char == ",":
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna), char, char])
                        Estado_Cadena = "nombre_nodo"
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "y_nodo"])
                        y_matriz = int(Cadena)
                        Cadena = ""
                elif Estado_Cadena == "nombre_nodo":
                    if char == "," or char == ")":
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna), char, char])
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Nombre nodo"])
                        ListaDeNombresMatriz.append(Cadena)
                        Cadena = ""
                        if char == ")":
                            Estado_Cadena = "color_nodo"
                elif Estado_Cadena == "color_nodo" and char == ";":
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna), char, char])
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Color nodo"])
                    if len(ListaDeNombresMatriz) == 1:
                        Estado_Cadena = "apertura_nodos"
                        if Cadena == "#":
                            ListaNodosMatriz.append(NodoMatriz(x_matriz, y_matriz, ListaDeNombresMatriz[0], Cadena))
                        else:
                            ListaNodosMatriz.append(NodoMatriz(x_matriz, y_matriz, ListaDeNombresMatriz[0], RevisionColor(Cadena)))
                        NombreNodos = ""
                        ListaDeNombresMatriz = []
                        Cadena = ""
                    else:
                        y+=1
                        x = 0
                        Estado_Cadena = "apertura_nodos"
                        for i in ListaDeNombresMatriz:
                            x += 1
                            if Cadena == "#":
                                ListaNodosMatriz.append(NodoMatriz(x, y, i, Cadena))
                            else:
                                ListaNodosMatriz.append(NodoMatriz(x, y, i, RevisionColor(Cadena)))
                        NombreNodos = ""
                        ListaDeNombresMatriz = []
                        Cadena = ""
            if Estado_Tipo == "defecto_matriz" and ListaNodosMatriz != []:
                if re.match(PatternDefecto, Cadena):
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Defecto Matriz"])
                    Estado_Cadena = "defecto_nodo"
                    Cadena = ""
                elif Estado_Cadena == "defecto_nodo" and NombreNodos == "":
                    if (ord(char) == 34 or ord(char) == 39):
                        Estado_Cadena = "nombre_nodo"
                        Cadena = ""
                elif Estado_Cadena == "nombre_nodo":
                    if (ord(char) == 34 or ord(char) == 39):
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Nombre nodo defecto"])
                        NombreNodos = Cadena
                        Estado_Cadena = "color_nodo"
                        Cadena = ""
                elif Estado_Cadena == "color_nodo" and char == ";":
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna), char, char])
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Color nodo defecto"])
                    NodoDefecto = NodoLista(NombreNodos, RevisionColor(Cadena))
                    Estado_Cadena = "ninguno"
                    Estado_Tipo = "ninguno"
                    NombreNodos = ""
                    CantidadNodos = 0
                    Cadena = ""
                    ListaDeMatrices.append(Matriz(FilasMatriz, ColumnasMatriz, NombreMatriz, FormaMatriz, DobleMatriz, ListaNodosMatriz))
                    Reportes(ListaDeTokens)
                    ReporteErrores(ListaDeErrores)
                    return ListaDeMatrices, NodoDefecto, Encabezado
                    #GraficaMatriz(ListaDeMatrices, NodoDefecto)
            elif Estado_Tipo == "tabla":
                if char == "(" and Estado_Cadena == "ninguno":
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna), char, char])
                    Estado_Cadena = "apertura_especificaciones"
                    Cadena = ""
                elif Estado_Cadena == "ninguno" and re.match(PatternDefecto, Cadena):
                    Cadena = ""
                    Estado_Cadena = "defecto_nodo"
                elif (char == "(" or char == " ") and Estado_Cadena == "ninguno":
                    print("Se repite " + Cadena)
                elif char == "," and Estado_Cadena == "apertura_especificaciones":
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Columnas_tabla"])
                    Estado_Cadena = "apertura_especificaciones"
                    ColumnasTabla = int(Cadena)
                    Cadena = ""
                elif (ord(char) == 34 or ord(char) == 39) and Estado_Cadena == "apertura_especificaciones":
                    Estado_Cadena = "nombre_tabla"
                elif (ord(char) == 34 or ord(char) == 39) and Estado_Cadena == "nombre_tabla":
                    Estado_Cadena = "ninguno"
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Nombre_tabla"])
                    NombreTabla = Cadena
                    Cadena = ""
                elif Estado_Cadena == "ninguno" and char == ")":
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna), char, char])
                    Estado_Cadena = "cerradura_especificaciones"
                    Cadena = ""
                elif Estado_Cadena == "cerradura_especificaciones":
                    if char == "{":
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna), char, char])
                        Estado_Cadena = "apertura_nodos"
                        Cadena = ""
                    else:
                        if char == " ":
                            pass
                        else:
                            if char != " " and char != "\n":
                                NoError += 1
                                ListaDeErrores.append([str(NoError), str(Fila), str(Columna - len(Cadena) + 1), Cadena])
                elif Estado_Cadena == "apertura_nodos":
                    if char == "(":
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna), char, char])
                        if re.match(PatternFila, Cadena):
                            NoToken += 1
                            ListaDeTokens.append(
                                [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, Cadena.lower()])
                            Estado_Cadena = "fila"
                            Cadena = ""
                        elif re.match(PatternEncabezados, Cadena):
                            NoToken += 1
                            ListaDeTokens.append(
                                [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, Cadena.lower()])
                            Estado_Cadena = "encabezados"
                            Cadena = ""
                        else:
                            NoError += 1
                            ListaDeErrores.append([str(NoError), str(Fila), str(Columna - len(Cadena) + 1), Cadena])
                    elif char == "}":
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna), char, char])
                        Estado_Tipo = "defecto_matriz"
                        Estado_Cadena = "ninguno"
                        Cadena = ""
                    elif char == " " and Cadena != "":
                        if re.match(PatternFila, Cadena):
                            continue
                        elif re.match(PatternEncabezados, Cadena):
                            continue
                        else:
                            NoError += 1
                            ListaDeErrores.append([str(NoError), str(Fila), str(Columna - len(Cadena) + 1), Cadena])
                            Cadena = ""
                elif Estado_Cadena == "encabezados":
                    if (ord(char) == 34 or ord(char) == 39):
                        Estado_Cadena = "nombre_nodo_encabezado"
                        Cadena = ""
                elif Estado_Cadena == "nombre_nodo_encabezado":
                    if char == "," or char == ")":
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna), char, char])
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Nombre_nodo"])
                        ListaDeNombresFila.append(Cadena)
                        Cadena = ""
                        if char == ")":
                            Estado_Cadena = "color_nodo_encabezado"
                elif Estado_Cadena == "color_nodo_encabezado" and char == ";":
                    Estado_Cadena = "apertura_nodos"
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna), char, char])
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Color nodo"])
                    if Cadena == "#":
                        Encabezado.append(filatabla(ListaDeNombresFila, Cadena))
                    else:
                        Encabezado.append(filatabla(ListaDeNombresFila, RevisionColor(Cadena)))
                    NombreNodos = ""
                    ListaDeNombresFila = []
                    Cadena = ""
                elif Estado_Cadena == "fila":
                    if (ord(char) == 34 or ord(char) == 39):
                        Estado_Cadena = "nombre_nodo"
                        Cadena = ""
                    elif char == "#":
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna), char, "nombre_nodo"])
                        ListaDeNombresFila.append(Cadena)
                        Cadena = ""
                elif Estado_Cadena == "nombre_nodo":
                    if char == "," or char == ")":
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna), char, char])
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Nombre nodo"])
                        ListaDeNombresFila.append(Cadena)
                        Cadena = ""
                        if char == ")":
                            Estado_Cadena = "color_nodo"
                elif Estado_Cadena == "color_nodo" and char == ";":
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna), char, char])
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "color_nodo"])
                    Estado_Cadena = "apertura_nodos"
                    if Cadena == "#":
                        ListaDeFilasTabla.append(filatabla(ListaDeNombresFila, Cadena))
                    else:
                        ListaDeFilasTabla.append(filatabla(ListaDeNombresFila, RevisionColor(Cadena)))
                    NombreNodos = ""
                    ListaDeNombresFila = []
                    Cadena = ""
            if Estado_Tipo == "defecto_matriz" and ListaDeFilasTabla != []:
                if re.match(PatternDefecto, Cadena):
                    Estado_Cadena = "defecto_nodo"
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Defecto_nodo"])
                    Cadena = ""
                elif Estado_Cadena == "defecto_nodo" and NombreNodos == "":
                    if (ord(char) == 34 or ord(char) == 39):
                        Estado_Cadena = "nombre_nodo"
                        Cadena = ""
                elif Estado_Cadena == "nombre_nodo":
                    if (ord(char) == 34 or ord(char) == 39):
                        NoToken += 1
                        ListaDeTokens.append(
                            [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Nombre nodo defecto"])
                        NombreNodos = Cadena
                        Estado_Cadena = "color_nodo"
                        Cadena = ""
                elif Estado_Cadena == "color_nodo" and char == ";":
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna), char, char])
                    NoToken += 1
                    ListaDeTokens.append(
                        [str(NoToken), str(Fila), str(Columna - len(Cadena) + 1), Cadena, "Color nodo defecto"])
                    NodoDefecto = NodoLista(NombreNodos, RevisionColor(Cadena))
                    Estado_Cadena = "ninguno"
                    Estado_Tipo = "ninguno"
                    NombreNodos = ""
                    CantidadNodos = 0
                    Cadena = ""
                    ListaDeTablas.append(Tabla(ColumnasTabla, NombreTabla, ListaDeFilasTabla))
                    Reportes(ListaDeTokens)
                    ReporteErrores(ListaDeErrores)
                    return ListaDeTablas, NodoDefecto, Encabezado
                    #GraficarTablas(ListaDeTablas, NodoDefecto, Encabezado)