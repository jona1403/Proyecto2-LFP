from graphviz import Digraph
from Clases import NodoMatriz
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
            for nodo in filas:
                if nodo.color == "#":
                    g.node(str(nodo.x)+str(nodo.y), shape=i.forma, label=nodo.nombre + "\n", fillcolor=nodoDefecto.color, style="filled")
                else:
                    g.node(str(nodo.x)+str(nodo.y), shape=i.forma, label=nodo.nombre + "\n", fillcolor=nodo.color, style="filled")
            NodoInicio = NodoMatriz(0,0,"","")
            NodoFin = NodoMatriz(0,0,"","")
            for nodo in filas:
                if NodoInicio.x == 0 and NodoInicio.y == 0:
                    NodoInicio = nodo
                elif NodoFin.x == 0 and NodoFin.y == 0:
                    NodoFin = nodo
                    if i.matrizdoble:
                        g.edge(str(NodoInicio.x) + str(NodoInicio.y), str(NodoFin.x) + str(NodoFin.y), dir="both")
                    else:
                        g.edge(str(NodoInicio.x)+str(NodoInicio.y), str(NodoFin.x)+str(NodoFin.y))
                    NodoInicio = NodoFin
                    NodoFin = NodoMatriz(0,0,"","")
        for la in range(0, i.columnas):
            NodoInicioV = NodoMatriz(0, 0, "", "")
            NodoFinV = NodoMatriz(0, 0, "", "")
            for lo in range(0, i.filas):
                if NodoInicioV.x == 0 and NodoInicioV.y == 0:
                    NodoInicioV = Listafinal[lo][la]
                elif NodoFinV.x == 0 and NodoFinV.y == 0:
                    NodoFinV = Listafinal[lo][la]
                    if i.matrizdoble:
                        g.edge(str(NodoInicioV.x) + str(NodoInicioV.y), str(NodoFinV.x) + str(NodoFinV.y), dir="both")
                    else:
                        g.edge(str(NodoInicioV.x)+str(NodoInicioV.y), str(NodoFinV.x)+str(NodoFinV.y))
                    NodoInicioV = NodoFinV
                    NodoFinV = NodoMatriz(0,0,"","")

        g.attr(label=i.nombre)
        g.view()