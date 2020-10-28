from Clases import Lista, NodoLista, NodosLista
from GraficarLista import GraficarListas
import re
def Lectura_De_Archivo(Ruta):
    ListaDeListas = []
    DobleLista = False
    NombreLista = ""
    FormaLista = ""
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
    PatternNodos = r"[N|n][O|o][D|d][O|o][S|s]"
    PatternDefecto = r"[D|d][E|e][F|f][E|e][C|c][T|t][O|o]"
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
                    FormaLista = Cadena
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
                        Estado_Tipo = "defecto"
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
                    if Estado_Cadena == "nodos":
                        if (ord(char) == 34 or ord(char) == 39):
                            Estado_Cadena = "nombre_nodo"
                            CantidadNodos = int(Cadena)
                            Cadena = ""
                elif Estado_Cadena == "nombre_nodo":
                    if (ord(char) == 34 or ord(char) == 39):
                        NombreNodos = Cadena
                        Estado_Cadena = "color_nodo"
                        Cadena = ""
                elif Estado_Cadena == "color_nodo" and char == ";":
                    if CantidadNodos == 0:
                        Estado_Cadena = "apertura_nodos"
                        ListaDeNodos.append(NodoLista(NombreNodos, Cadena))
                        NombreNodos = ""
                        CantidadNodos = 0
                        Cadena = ""
                    else:
                        Estado_Cadena = "apertura_nodos"
                        for i in range(1 , CantidadNodos+1):
                            ListaDeNodos.append(NodoLista(NombreNodos+str(i), Cadena))
                        NombreNodos = ""
                        CantidadNodos = 0
                        Cadena = ""
            if Estado_Tipo == "defecto" and ListaDeNodos != []:

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
                    ListaDeNodos.append(NodoLista(NombreNodos, Cadena))
                    Estado_Cadena = "ninguno"
                    NombreNodos = ""
                    CantidadNodos = 0
                    Cadena = ""
                    ListaDeListas.append(Lista(NombreLista, FormaLista, DobleLista, ListaDeNodos))
                    GraficarListas(ListaDeListas)
            elif Estado_Tipo == "matriz":
                pass
            elif Estado_Tipo == "tabla":
                pass