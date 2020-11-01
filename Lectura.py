from Clases import Lista, NodoLista, RevisionForma, RevisionColor
from Clases import Matriz, NodoMatriz, FilaMatriz
from GraficarLista import GraficarListas
from GraficarMatriz import GraficaMatriz
import re
def Lectura_De_Archivo(Ruta):
    ListaDeListas = []
    ListaDeMatrices = []
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
    ListaNodosMatriz = []
    ListaDeNodos = []
    CantidadNodos = 0
    NombreNodos = ""
    Cadena = ""
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
                    Cadena = ""
                else:
                    if char == " " or char == "\n":
                        print("Cadena inesperada")
                        Cadena = ""
            elif Estado_Tipo == "lista":
                if char == "(" and Estado_Cadena == "ninguno":
                    Estado_Cadena = "apertura_especificaciones"
                    Cadena = ""
                elif Estado_Cadena == "ninguno" and re.match(PatternDefecto, Cadena):
                    Cadena = ""
                    Estado_Cadena = "defecto_nodo"
                elif (char == "(" or char == " ") and Estado_Cadena == "ninguno":
                    print("Se repite "+Cadena)
                elif (ord(char) == 34 or ord(char) == 39) and Estado_Cadena == "apertura_especificaciones":
                    Estado_Cadena = "nombre_lista"
                elif (ord(char) == 34 or ord(char) == 39) and Estado_Cadena == "nombre_lista":
                    Estado_Cadena = "ninguno"
                    NombreLista = Cadena
                    Cadena = ""
                elif char == "," and Estado_Cadena == "ninguno" and NombreLista != "":
                    Estado_Cadena = "forma_lista"
                elif char == "," and Estado_Cadena == "forma_lista" and NombreLista !="":
                    Estado_Cadena = "ninguno"
                    FormaLista = RevisionForma(Cadena)
                    if FormaLista == "nomatch":
                        print("La forma ingresada por el usuario no es valida")
                    else:
                        pass
                    Cadena = ""
                elif Estado_Cadena == "ninguno" and FormaLista != "":
                    Estado_Cadena = "lista_doble"
                elif char == ")" and Estado_Cadena == "lista_doble" and FormaLista != "":
                    Estado_Cadena = "cerradura_especificaciones"
                    if re.match(PatternFalse, Cadena):
                        DobleLista = False
                        Cadena = ""
                    elif re.match(PatternVerdadero, Cadena):
                        DobleLista = True
                        Cadena = ""
                elif Estado_Cadena == "cerradura_especificaciones":
                    if char == "{":
                        Estado_Cadena = "apertura_nodos"
                        Cadena = ""
                    else:
                        if char == " ":
                            pass
                        else:
                            if char != " " and char != "\n":
                                print("Se esperaba {: "+char)
                elif Estado_Cadena == "apertura_nodos":
                    if char == "(":
                        if re.match(PatternNodos, Cadena):
                            Estado_Cadena = "nodos"
                            Cadena = ""
                        elif re.match(PatternNodo, Cadena):
                            Estado_Cadena = "nodo"
                            Cadena = ""
                        else:
                            print("Error: "+Cadena)
                    elif char == "}":
                        Estado_Tipo = "defecto_lista"
                        Estado_Cadena = "ninguno"
                        Cadena = ""
                    elif char == " " and Cadena != "":
                        if re.match(PatternNodo, Cadena) or re.match(PatternNodos, Cadena):
                            continue
                        else:
                            print("Error: "+Cadena)
                            Cadena = ""
                elif Estado_Cadena == "nodo" or Estado_Cadena == "nodos":
                    if Estado_Cadena == "nodo":
                        if (ord(char) == 34 or ord(char) == 39):
                            Estado_Cadena = "nombre_nodo"
                            Cadena = ""
                        elif Cadena == "#" and char == "#":
                            NombreNodos = Cadena
                            Cadena = ""
                            Estado_Cadena = "color_nodo"
                    if Estado_Cadena == "nodos":
                        if (ord(char) == 34 or ord(char) == 39):
                            Estado_Cadena = "nombre_nodo"
                            CantidadNodos = int(Cadena)
                            Cadena = ""
                        elif char == "#":
                            numaux = ""
                            for i in Cadena:
                                if re.match(PatternNumeros, i) and i != "#":
                                    numaux+=i
                            CantidadNodos = int(numaux)
                            NombreNodos = "#"
                            Cadena = ""
                            Estado_Cadena = "color_nodo"
                elif Estado_Cadena == "nombre_nodo":
                    if (ord(char) == 34 or ord(char) == 39):
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
                        CantidadNodos = 0
                        Cadena = ""
            if Estado_Tipo == "defecto_lista" and ListaDeNodos != []:
                if re.match(PatternDefecto, Cadena):
                    Estado_Cadena = "defecto_nodo"
                    Cadena = ""
                elif Estado_Cadena == "defecto_nodo" and NombreNodos == "":
                    if (ord(char) == 34 or ord(char) == 39):
                        Estado_Cadena = "nombre_nodo"
                        Cadena = ""
                elif Estado_Cadena == "nombre_nodo":
                    if (ord(char) == 34 or ord(char) == 39):
                        NombreNodos = Cadena
                        Estado_Cadena = "color_nodo"
                        Cadena = ""
                elif Estado_Cadena == "color_nodo" and char == ";":
                    NodoDefecto = NodoLista(NombreNodos, RevisionColor(Cadena))
                    Estado_Cadena = "ninguno"
                    Estado_Tipo = "ninguno"
                    NombreNodos = ""
                    CantidadNodos = 0
                    Cadena = ""
                    ListaDeListas.append(Lista(NombreLista, FormaLista, DobleLista, ListaDeNodos))
                    GraficarListas(ListaDeListas, NodoDefecto)
            elif Estado_Tipo == "matriz":
                if char == "(" and Estado_Cadena == "ninguno":
                    Estado_Cadena = "apertura_especificaciones"
                    Cadena = ""
                elif Estado_Cadena == "ninguno" and re.match(PatternDefecto, Cadena):
                    Cadena = ""
                    Estado_Cadena = "defecto_nodo"
                elif (char == "(" or char == " ") and Estado_Cadena == "ninguno":
                    print("Se repite " + Cadena)
                elif char == "," and Estado_Cadena == "apertura_especificaciones":
                    Estado_Cadena = "columnas_matriz"
                    FilasMatriz = int(Cadena)
                    Cadena = ""
                elif char == "," and Estado_Cadena == "columnas_matriz":
                    Estado_Cadena = "apertura_especificaciones"
                    ColumnasMatriz = int(Cadena)
                    Cadena = ""
                elif (ord(char) == 34 or ord(char) == 39) and Estado_Cadena == "apertura_especificaciones":
                    Estado_Cadena = "nombre_matriz"
                elif (ord(char) == 34 or ord(char) == 39) and Estado_Cadena == "nombre_matriz":
                    Estado_Cadena = "ninguno"
                    NombreMatriz = Cadena
                    Cadena = ""
                elif char == "," and Estado_Cadena == "ninguno" and NombreMatriz != "":
                    Estado_Cadena = "forma_matriz"
                elif char == "," and Estado_Cadena == "forma_matriz" and NombreMatriz != "":
                    Estado_Cadena = "ninguno"
                    FormaMatriz = RevisionForma(Cadena)
                    if FormaMatriz == "nomatch":
                        print("La forma ingresada por el usuario no es valida")
                    else:
                        pass
                    Cadena = ""
                elif Estado_Cadena == "ninguno" and FormaMatriz != "":
                    Estado_Cadena = "matriz_doble"
                elif char == ")" and Estado_Cadena == "matriz_doble" and FormaMatriz != "":
                    Estado_Cadena = "cerradura_especificaciones"
                    if re.match(PatternFalse, Cadena):
                        DobleMatriz = False
                        Cadena = ""
                    elif re.match(PatternVerdadero, Cadena):
                        DobleMatriz = True
                        Cadena = ""
                elif Estado_Cadena == "cerradura_especificaciones":
                    if char == "{":
                        Estado_Cadena = "apertura_nodos"
                        Cadena = ""
                    else:
                        if char == " ":
                            pass
                        else:
                            if char != " " and char != "\n":
                                print("Se esperaba {: " + char)
                elif Estado_Cadena == "apertura_nodos":
                    if char == "(":
                        if re.match(PatternFila, Cadena):
                            Estado_Cadena = "fila"
                            Cadena = ""
                        elif re.match(PatternNodo, Cadena):
                            Estado_Cadena = "nodo"
                            Cadena = ""
                        else:
                            print("Error: "+Cadena)
                    elif char == "}":
                        Estado_Tipo = "defecto_matriz"
                        Estado_Cadena = "ninguno"
                        Cadena = ""
                    elif char == " " and Cadena != "":
                        if re.match(PatternNodo, Cadena) or re.match(PatternFila, Cadena):
                            continue
                        else:
                            print("Error: "+Cadena)
                            Cadena = ""
                elif Estado_Cadena == "nodo" or Estado_Cadena == "fila":
                    if Estado_Cadena == "nodo":
                        if char == ",":
                            Estado_Cadena = "y_matriz"
                            x_matriz = int(Cadena)
                            Cadena = ""
                    if Estado_Cadena == "fila":
                        if (ord(char) == 34 or ord(char) == 39):
                            Estado_Cadena = "nombre_nodo"
                            Cadena = ""
                elif Estado_Cadena == "y_matriz":
                    if char == ",":
                        Estado_Cadena = "nombre_nodo"
                        y_matriz = int(Cadena)
                        Cadena = ""
                elif Estado_Cadena == "nombre_nodo":
                    if char == "," or char == ")":
                        ListaDeNombresMatriz.append(Cadena)
                        Cadena = ""
                        if char == ")":
                            Estado_Cadena = "color_nodo"
                elif Estado_Cadena == "color_nodo" and char == ";":
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
                    Estado_Cadena = "defecto_nodo"
                    Cadena = ""
                elif Estado_Cadena == "defecto_nodo" and NombreNodos == "":
                    if (ord(char) == 34 or ord(char) == 39):
                        Estado_Cadena = "nombre_nodo"
                        Cadena = ""
                elif Estado_Cadena == "nombre_nodo":
                    if (ord(char) == 34 or ord(char) == 39):
                        NombreNodos = Cadena
                        Estado_Cadena = "color_nodo"
                        Cadena = ""
                elif Estado_Cadena == "color_nodo" and char == ";":
                    NodoDefecto = NodoLista(NombreNodos, RevisionColor(Cadena))
                    Estado_Cadena = "ninguno"
                    Estado_Tipo = "ninguno"
                    NombreNodos = ""
                    CantidadNodos = 0
                    Cadena = ""
                    ListaDeMatrices.append(Matriz(FilasMatriz, ColumnasMatriz, NombreMatriz, FormaMatriz, DobleMatriz, ListaNodosMatriz))
                    ListaDeListas.append(Lista(NombreLista, FormaLista, DobleLista, ListaDeNodos))
                    GraficaMatriz(ListaDeMatrices, NodoDefecto)
            elif Estado_Tipo == "tabla":
                pass