from graphviz import Digraph
from Clases import NodoLista
import re
def GraficarListas(ListaDeListas, NodoDefecto):
    numero = 0
    PatternDef = r"#"
    NodoInicio = NodoLista("", "")
    NodoFin = NodoLista("", "")
    f = Digraph(format="svg", name="Lista")
    f.attr(rankdir="LR", size="12")
    f.attr("node")
    for i in ListaDeListas:
        for e in i.listanodos:
            if re.match(PatternDef, e.nombre) and e.color == "#":
                if e.nombre == "#":
                    f.node(NodoDefecto.nombre, shape=i.forma,
                           label=NodoDefecto.nombre+ "\n", fillcolor=NodoDefecto.color, style="filled")
                else:
                    numero += 1
                    f.node(NodoDefecto.nombre+str(numero), shape=i.forma, label=NodoDefecto.nombre+str(numero) + "\n", fillcolor=NodoDefecto.color, style="filled")
            elif re.match(PatternDef, e.nombre) and e.color != "#":
                if e.nombre == "#":
                    f.node(NodoDefecto.nombre, shape=i.forma,
                           label=NodoDefecto.nombre+ "\n", fillcolor=e.color, style="filled")
                else:
                    numero += 1
                    f.node(NodoDefecto.nombre+str(numero), shape=i.forma, label=NodoDefecto.nombre+str(numero) + "\n", fillcolor=e.color, style="filled")
            elif e.color == "#":
                f.node(e.nombre, shape=i.forma, label=e.nombre + "\n", fillcolor=NodoDefecto.color, style="filled")
            else:
                f.node(e.nombre, shape=i.forma, label=e.nombre + "\n", fillcolor = e.color, style="filled")
            if NodoInicio.nombre == "":
                if numero != 0:
                    NodoInicio = NodoLista(NodoDefecto.nombre+str(numero), e.color)
                else:
                    if e.nombre == "#":
                        NodoInicio = NodoLista(NodoDefecto.nombre, e.color)
                    else:
                        NodoInicio = e
            elif NodoFin.nombre == "":
                if numero != 0:
                    NodoFin = NodoLista(NodoDefecto.nombre + str(numero), e.color)
                else:
                    if e.nombre == "#":
                        NodoFin = NodoLista(NodoDefecto.nombre, e.color)
                    else:
                        NodoFin = e
                if re.match(PatternDef, NodoInicio.nombre) and re.match(PatternDef, NodoFin.nombre):
                    f.edge(NodoInicio.nombre, NodoFin.nombre)
                elif re.match(PatternDef, NodoInicio.nombre):
                    f.edge(NodoDefecto.nombre, NodoFin.nombre)
                elif re.match(PatternDef, NodoFin.nombre):
                    f.edge(NodoInicio.nombre, NodoDefecto.nombre)
                else:
                    f.edge(NodoInicio.nombre, NodoFin.nombre)
                NodoInicio = NodoFin
                NodoFin = NodoLista("", "")
        NodoInicio = NodoLista("", "")
        NodoFin = NodoLista("", "")
        if i.doble:
            for k in reversed(i.listanodos):
                if NodoInicio.nombre == "":
                    if numero != 0:
                        NodoInicio = NodoLista(NodoDefecto.nombre + str(numero), k.color)
                        numero -= 1
                    else:
                        if k.nombre == "#":
                            NodoInicio = NodoLista(NodoDefecto.nombre, k.color)
                        else:
                            NodoInicio = k
                elif NodoFin.nombre == "":
                    if numero != 0:
                        NodoFin = NodoLista(NodoDefecto.nombre + str(numero), k.color)
                    else:
                        if k.nombre == "#":
                            NodoFin = NodoLista(NodoDefecto.nombre, k.color)
                        else:
                            NodoFin = k
                    if re.match(PatternDef, NodoInicio.nombre) and re.match(PatternDef, NodoFin.nombre):
                        f.edge(NodoDefecto.nombre, NodoDefecto.nombre)
                    elif re.match(PatternDef, NodoInicio.nombre):
                        f.edge(NodoDefecto.nombre, NodoFin.nombre)
                    elif re.match(PatternDef, NodoFin.nombre):
                        f.edge(NodoInicio.nombre, NodoDefecto.nombre)
                    else:
                        f.edge(NodoInicio.nombre, NodoFin.nombre)
                    NodoInicio = NodoFin
                    NodoFin = NodoLista("", "")
        f.attr(label=i.nombre)
        f.view()
