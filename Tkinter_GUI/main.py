from tkinter import *
from tkinter import ttk
from conexion import *

ventana = Tk()
ventana.title("Bienes Raices Future CRUD")
ventana.geometry("720x1080")


db=DataBase()
pro_nombre = StringVar()
pro_direccion = StringVar()
pro_contacto = StringVar()
nombre = StringVar()
direccion = StringVar()
contacto = StringVar()
nombre_tipo = StringVar()
nombre_estado = StringVar()
nombre_OpComercial = StringVar()


marco = LabelFrame(ventana, text="Gestion de propiedades")
marco.place(x=50, y=50, width=2000, height=2000)

# label y entry

lblproNombre = Label(marco, text="nombre de propiedad").grid(column=0,row=0, padx=5, pady=5)
txtproNombre = Entry(marco, textvariable=pro_nombre)
txtproNombre.grid(column=1, row=0)

lblproDireccion = Label(marco, text="Direccion de propiedad").grid(column=0,row=1, padx=5, pady=5)
txtproDireccion = Entry(marco, textvariable=pro_direccion)
txtproDireccion.grid(column=1, row=1)

lblproContacto = Label(marco, text="Contacto de propiedad").grid(column=2,row=0, padx=5, pady=5)
txtproContacto = Entry(marco, textvariable=pro_contacto)
txtproContacto.grid(column=3, row=0)

lblNombre = Label(marco, text="nombre de propietario").grid(column=2,row=1, padx=5, pady=5)
txtNombre = Entry(marco, textvariable=nombre)
txtNombre.grid(column=3, row=1)

lblDireccion = Label(marco, text="Direccion").grid(column=2,row=2, padx=5, pady=5)
txtDireccion = Entry(marco, textvariable=direccion)
txtDireccion.grid(column=3, row=2)

lblContacto = Label(marco, text="Contacto").grid(column=2,row=3, padx=5, pady=5)
txtContacto = Entry(marco, textvariable=contacto)
txtContacto.grid(column=3, row=3)

lblNombre_tipo = Label(marco, text="Tipo").grid(column=2,row=4, padx=5, pady=5)
txtNombre_tipo = Entry(marco, textvariable=nombre_tipo)
txtNombre_tipo.grid(column=3, row=4)

lblNombre_estado = Label(marco, text="Estado").grid(column=2,row=5, padx=5, pady=5)
txtNombre_estado = Entry(marco, textvariable=nombre_estado)
txtNombre_estado.grid(column=3, row=5)

lblNombre_OpComercial = Label(marco, text="Operatoria comercial").grid(column=2,row=6, padx=5, pady=5)
txtNombre_OpComercial = Entry(marco, textvariable=nombre_OpComercial)
txtNombre_OpComercial.grid(column=3, row=6, padx=5, pady=5)

txtMensaje=Label(marco, text="mensajes", fg="green").grid(column=0, row=7, columnspan=4)

## Tabla de la lista de propiedades

tvPropiedades = ttk.Treeview(marco)
tvPropiedades.grid(column=0, row=8, columnspan=4, padx=5)
tvPropiedades["columns"]=("ID_Propiedad",
                          "ID_tipo",
                          "ID_estado",
                          "ID_operatoria",
                          "ID_propietario",
                          "nombre",
                          "direccion",
                          "contacto",
                          "tipo",
                          "estado",
                          "op_comercial",
                          "nombre_propietario",
                          "direccion_propietario",
                          "contacto_propietario",
                        )


tvPropiedades.column("#0", width=0, stretch=NO)
tvPropiedades.column("ID_Propiedad", width=50, anchor=CENTER)
tvPropiedades.column("ID_tipo", width=50,anchor=CENTER)
tvPropiedades.column("ID_estado", width=50, anchor=CENTER)
tvPropiedades.column("ID_propietario", width=50, anchor=CENTER)
tvPropiedades.column("nombre", width=50, anchor=CENTER)
tvPropiedades.column("direccion", width=50, anchor=CENTER)
tvPropiedades.column("contacto", width=50, anchor=CENTER)
tvPropiedades.column("op_comercial", width=50, anchor=CENTER)
tvPropiedades.column("nombre_propietario", width=50, anchor=CENTER)
tvPropiedades.column("direccion_propietario", width=50, anchor=CENTER)
tvPropiedades.column("contacto_propietario", width=50, anchor=CENTER)

tvPropiedades.heading("#0", text="")
tvPropiedades.heading("ID_Propiedad", text="ID_Propiedad", anchor=CENTER)
tvPropiedades.heading("ID_tipo", text="ID_tipo", anchor=CENTER)
tvPropiedades.heading("ID_estado", text="ID_estado", anchor=CENTER)
tvPropiedades.heading("ID_propietario", text="ID_propietario", anchor=CENTER)
tvPropiedades.heading("nombre", text="nombre", anchor=CENTER)
tvPropiedades.heading("direccion", text="direccion", anchor=CENTER)
tvPropiedades.heading("contacto", text="contacto", anchor=CENTER)
tvPropiedades.heading("op_comercial", text="op_comercial", anchor=CENTER)
tvPropiedades.heading("nombre_propietario", text="nombre_propietario", anchor=CENTER)
tvPropiedades.heading("direccion_propietario", text="direccion_propietario", anchor=CENTER)
tvPropiedades.heading("contacto_propietario", text="contacto_propietario", anchor=CENTER)

#BOTONES DE ACCION

btnEliminar=Button(marco, text="Eliminar", command=lambda:eliminar())
btnEliminar.grid(column=1, row=10)

btnNuevo=Button(marco, text="Nuevo", command=lambda:Nuevo())
btnNuevo.grid(column=2, row=10)

btnModificar=Button(marco, text="Modificar", command=lambda:Modificar())
btnModificar.grid(column=3, row=10)


## Funciones

def eliminar():
  id= tvPropiedades.selection()[0]
  
  if int(id)>0:
    sql="delete from propiedad where id="+id
    db.cursor.execute(sql)
    db.connection.commit()
    tvPropiedades.delete(id)
    txtMensaje.config(text="se elimino el registro correctamente")
  else:
    txtMensaje.config(text="seleccione un registro para eliminar")


def Nuevo():
  val=(nombre.get(),direccion.get(),contacto.get())
  sql= "insert into propiedad (id_Propiedad,nombre, direccion,contacto) values (0,%s,%s,%s,)"
  db.cursor.execute(sql,val)
  db.connection.commit()
  txtMensaje.config(text="se guardo el nuevo registro en la base de datos")
  




def Modificar():
  pass




def actualizarTabla():
  vaciarTabla()
  
  sql="select * from propiedad"
  db.cursor.execute(sql)
  filas= db.cursor.fetchall()
  for fila in filas:
    id = fila[0]
    tvPropiedades.insert("",END, id, text=id, values=fila)





def vaciarTabla():
  filas= tvPropiedades.get_children()
  for fila in filas:
    tvPropiedades.delete(fila)



actualizarTabla()
ventana.mainloop()

