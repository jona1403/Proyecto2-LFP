from Lectura import Lectura_De_Archivo
def menu():
    while True:
        print("-------------------------------------------------------")
        print("----------------------Proyecto 2-----------------------")
        print("Lenguajes Formales y de Programación(796), Sección A-")
        print("Jonathan Alexander Alvarado Fernández, carné: 201903004")
        print("-------------------------------------------------------")
        print("1. Cargar Archivo")
        print("2. Generar Gráfica")
        print("3. Salir")
        entrada = input("Ingrese una opción: ")
        if entrada == "1":
            Ruta = input("Ingrese la ruta del archivo: ")
            Lectura_De_Archivo(Ruta)
            input()
        if entrada == "2":
            print("Trabajamos en ello ;)")
            input()
        if entrada == "3":
            print("Gracias, vuelva pronto :)")
            break
if __name__ == '__main__':
    menu()

