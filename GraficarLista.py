def GraficarListas(ListaDeListas):
    for i in ListaDeListas:
        print(i.nombre)
        print(i.forma)
        print(i.doble)
        for e in i.listanodos:
            print("Nombre: "+e.nombre+" Color: "+e.color)