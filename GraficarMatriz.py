from graphviz import Digraph
from Clases import Matriz, NodoMatriz, NodoLista
def GraficaMatriz(ListaDeMatrices, nodoDefecto):
    ListaAuxiliar = []
    ListaFilas = []
    Listafinal = []
    SeAgrego = False
    g = Digraph(format="svg", name="Matriz")
    g.attr(rankdir="LR", size="8")
    g.attr("node")
    for i in ListaDeMatrices:
        for j in i.listanodos:
            if j.nombre == "#":
                ListaAuxiliar.append(NodoMatriz(j.x, j.y, nodoDefecto.nombre, j.color))
            else:
                ListaAuxiliar.append(j)
        for Filas in range(1, i.filas+1):
            for Columnas in range(1, i.columnas+1):
                SeAgrego = False
                for q in ListaAuxiliar:
                    if q.x == Columnas and q.y == Filas and SeAgrego == False:
                        ListaFilas.append(q)
                        SeAgrego = True
                if SeAgrego == False:
                    ListaFilas.append(NodoMatriz(Columnas, Filas, nodoDefecto.nombre, nodoDefecto.color))
                    SeAgrego = True
            Listafinal.append(ListaFilas)
            ListaFilas = []
        for filas in Listafinal:
            print("fila:")
            for nodo in filas:
                print(nodo.nombre+nodo.color)
                if nodo.color == "#":
                    g.node(str(nodo.x)+str(nodo.y), shape=i.forma, label=nodo.nombre + "\n", fillcolor=nodoDefecto.color, style="filled")
                else:
                    g.node(str(nodo.x)+str(nodo.y), shape=i.forma, label=nodo.nombre + "\n", fillcolor=nodo.color, style="filled")
        g.attr(label=i.nombre)
        g.view()