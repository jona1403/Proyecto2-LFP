from graphviz import Digraph
def juntar(lista):
    dato = ""
    dato +="<TR><TD>No.</TD>"
    for i in lista:
        dato+="<TD>"+i+"</TD>"
    dato += "</TR>"
    return dato

def JuntarCuerpo(lista, nododefecto):
    incremento = 0
    dato = ""
    for filas in lista:
        incremento += 1
        dato+= "<TR><TD>"+str(incremento)+"</TD>"
        for i in filas.listanombres:
            if i == "#":
                dato += "<TD>" + nododefecto.nombre + "</TD>"
            else:
                dato += "<TD>" + i + "</TD>"
        dato += "</TR>"
    return dato

def GraficarTablas(ListaDeTablas, nododefecto, Encabezado):
    encabezado = ""
    cuerpo = ""
    for i in ListaDeTablas:
        s = Digraph('structs', node_attr={'shape': 'plaintext'}, format="svg")
        for k in i.listafilas:
            if len(k.listanombres) < i.columnas:
                while len(k.listanombres) < i.columnas:
                    k.listanombres.append(nododefecto.nombre)
        encabezado = juntar(Encabezado[0].listanombres)
        cuerpo = JuntarCuerpo(i.listafilas, nododefecto)
        s.node('struct2', f'''<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
            {encabezado}
            {cuerpo}
        </TABLE>>''')

        s.view()
