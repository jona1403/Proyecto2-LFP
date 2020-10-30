from graphviz import Digraph
from Clases import NodoLista
def GraficarListas(ListaDeListas, NodoDefecto):
    NodoInicio = NodoLista("", "")
    NodoFin = NodoLista("", "")
    f = Digraph(format="svg", name="Lista")
    f.attr(rankdir="LR", size="12")
    f.attr("node")
    for i in ListaDeListas:
        print(i.nombre)
        print(i.forma)
        print(i.doble)
        for e in i.listanodos:
            f.node(e.nombre, shape=i.forma, label=e.nombre + "\n", fillcolor = e.color, style="filled")
            if NodoInicio.nombre == "":
                NodoInicio = e
            elif NodoFin.nombre == "":
                NodoFin = e
                f.edge(NodoInicio.nombre, NodoFin.nombre)
                NodoInicio = NodoFin
                NodoFin = NodoLista("", "")


        f.attr(label=i.nombre)
        f.view()
