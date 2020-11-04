def ReporteErrores(lista):
    cadena = ""
    f = open('ReporteErrores.html', "w")
    f.write("<!DOCTYPE html>\n<html>\n<head>\n")
    f.write("<meta charset='utf-8'>\n")
    f.write("</head>\n")
    f.write("<body>\n")
    f.write("<table border = '1'>\n")
    for filas in lista:
        cadena += "<TR>"
        for i in filas:
            cadena += "<TD>"+i+"</TD>"
        cadena += "</TR>"
        pass
    f.write(cadena)
    f.write("</body>")
    f.write("</html>")
    f.close()