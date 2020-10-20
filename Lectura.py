def Lectura_De_Archivo(Ruta):
    Cadena = ""
    Estado_Tipo = "ninguno"
    Estado_Cadena = "ninguno"
    Estado_Comentario = False
    Estado_Error = False
    file = open(Ruta, "r")
    for line in file:
        for char in line:
            if char == " " or char == "\n":
                pass
            else:
                Cadena += char
            if Cadena == "//":
                Estado_Comentario = True
            if Estado_Comentario == True:
                if char == "\n":
                    Estado_Comentario = False
                    Cadena = ""
            elif Estado_Tipo == "ninguno":
                if Cadena.lower() == "lista" or Cadena.lower() == "matriz" or Cadena.lower() == "tabla":
                    if Cadena.lower() == "lista":
                        Estado_Tipo = "lista"
                    elif Cadena.lower() == "matriz":
                        Estado_Tipo = "matriz"
                    elif Cadena.lower() == "tabla":
                        Estado_Tipo = "tabla"
                    Cadena = ""
            elif Estado_Tipo == "lista":
                if char == "(" and Estado_Cadena == "ninguno":
                    Estado_Cadena = "apertura_especificaciones"
                    cadena = ""
            elif Estado_Tipo == "matriz":
                pass
            elif Estado_Tipo == "tabla":
                pass