from graphviz import Digraph
from Clases import NodoMatriz
def juntar(lista):
    dato = ""
    for i in lista:
        dato+="<TD>"+i+"</TD>"
    return dato

def JuntarCuerpo(lista):
    dato = ""
    for filas in lista:
        dato+= "<TR>"
        for i in filas.listanombres:
            dato += "<TD>" + i + "</TD>"
        dato += "</TR>"
    return dato

def GraficarTablas(ListaDeTablas, nododefecto, Encabezado):
    encabezado = ""
    cuerpo = ""
    for i in ListaDeTablas:
        s = Digraph('structs', node_attr={'shape': 'plaintext'}, format="png")
        encabezado = juntar(Encabezado[0].listanombres)
        cuerpo = JuntarCuerpo(i.listafilas)
        s.node('struct2', f'''<
        <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
          <TR>
            {encabezado}
          </TR>
            {cuerpo}
        </TABLE>>''')

        s.view()
