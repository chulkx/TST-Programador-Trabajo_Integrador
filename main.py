import controlador as con
from rich import print
from rich.console import Console




console= Console()
while True:
    console.print("\n+-------------------------------------------+", style="bold blue")
    console.print("|                INMOBILIARIA               |", style="bold blue")
    console.print("+-------------------------------------------+\n", style="bold blue")
    print("")
    console.print("MENÚ PRINCIPAL\n", style=("bold underline green"))
    print("1 - NUEVA PROPIEDAD")
    print("2 - MODIFICAR PROPIEDAD")
    print("3 - ELIMINAR PROPIEDAD")
    print("4 - PROPIEDADES")
    print("5 - PROPIEDADES A LA VENTA")
    print("6 - PROPIEDADES PARA ALQUILER")
    print("7 - PROPIEDADES VENDIDAS")
    print("8 - PROPIEDADES ALQUILADAS")
    print("9 - SALIR")
    print("\n")
    console.print("Ingrese su opcion", style="bold blue")
    opcion = int(console.input("->"))

    if opcion == 1:
        con.cargar_propiedad()
    elif opcion == 2:
        con.modif_propiedad()
    elif opcion == 3:
        con.eliminar_propiedad()
    elif opcion == 4:
        con.listar_propiedades()
    elif opcion == 5:
        con.listar_propiedades_venta()
    elif opcion == 6:
        con.listar_propiedades_alquiler()
    elif opcion == 7:
        con.listar_propiedades_vendidas()
    elif opcion == 8:
        con.listar_propiedades_alquiladas()
    elif opcion == 9:
        break
    else:
        print("¡Opción incorrecta!")
        print("Preciones ENTER para volver al menu")

