import controlador as con
from rich import print
from rich.console import Console




console= Console()

console.print("\n+-------------------------------------------+", style="bold blue")
console.print("|                INMOBILIARIA               |", style="bold blue")
console.print("+-------------------------------------------+\n", style="bold blue")
print("")

while True:

    print("")
    console.print("MENÚ PRINCIPAL\n", style=("bold green"))
    print("1 - NUEVO PROPIETARIO")
    print("2 - NUEVA PROPIEDAD")
    print("3 - MODIFICAR PROPIEDAD")
    print("4 - ELIMINAR PROPIEDAD")
    print("5 - PROPIEDADES")
    print("6 - PROPIEDADES A LA VENTA")
    print("7 - PROPIEDADES PARA ALQUILER")
    print("8 - PROPIEDADES VENDIDAS")
    print("9 - PROPIEDADES ALQUILADAS")
    print("10 - SALIR")
    print("\n")
    console.print("Ingrese su opcion", style="bold blue")
    opcion = int(console.input("->"))


    if opcion == 1:
        con.cargar_propietario()
    elif opcion == 2:
        con.cargar_propiedad()
    elif opcion == 3:
        con.modif_propiedad()
    elif opcion == 4:
        con.eliminar_propiedad()
    elif opcion == 5:
        con.listar_propiedades()
    elif opcion == 6:
        con.listar_propiedades_venta()
    elif opcion == 7:
        con.listar_propiedades_alquiler()
    elif opcion == 8:
        con.listar_propiedades_vendidas()
    elif opcion == 9:
        con.listar_propiedades_alquiladas()
    elif opcion == 10:
        break
    else:
        print("¡Opción incorrecta!")
        print("Preciones ENTER para volver al menu")

