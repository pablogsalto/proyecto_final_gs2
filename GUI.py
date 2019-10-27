from gestion import Gestion 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Gui():    

    def __init__(self):
        #-----------------Pantalla inicial
        
        self.ventana = Tk()
        self.ventana.title("Consultorio")
        self.ventana.geometry("800x640")
        self.ventana.resizable(0, 0)
        self.ventana.iconbitmap("dentist.ico")
        self.gestion = Gestion()

        notebook = ttk.Notebook(self.ventana)
        notebook.pack(fill="both", expand="yes")
        
        #-----------------Pestaña agregar paciente----------
        
        agregar_p = ttk.Frame(notebook)
        notebook.add(agregar_p, text="Agregar paciente")
        
        #Nombre
        self.ep_nombre = Entry(agregar_p, width=75)
        self.ep_nombre.place(x=190, y=125)        
        label_nombre = Label(agregar_p, text="Nombre:").place(x=120, y=125)
        
        #Apellido
        self.ep_apellido = Entry(agregar_p, width=75)
        self.ep_apellido.place(x=190, y=155)        
        label_apellido = Label(agregar_p, text="Apellido:").place(x=120, y=155)
        
        #DNI
        self.ep_dni = Entry(agregar_p, width=75)
        self.ep_dni.place(x=190, y=185)        
        label_dni = Label(agregar_p, text="DNI:").place(x=120, y=185)
        
        #Telefono
        self.ep_tel = Entry(agregar_p, width=75)
        self.ep_tel.place(x=190, y=215)        
        label_tel = Label(agregar_p, text="Telefono:").place(x=120, y=215)
        
        #E-mail
        self.ep_mail = Entry(agregar_p, width=75)
        self.ep_mail.place(x=190, y=245)        
        label_mail = Label(agregar_p, text="E-mail:").place(x=120, y=245)
        label_opcional = Label(agregar_p, text="(opcional)", fg="gray").place(x=650, y=245)
        
        #Boton
        self.image11 = PhotoImage(file="checked.png")              
        confirmar_paciente = Button(agregar_p, text="  Confirmar  ", image=self.image11, compound="left",
                                 command=self.confirmar_paciente, cursor="hand2")
        confirmar_paciente.place(x=350, y=510)

        #-----------------Pestaña pacientes-----------------

        p_pacientes = ttk.Frame(notebook)
        notebook.add(p_pacientes, text="Pacientes")
        
        #Modificar
        self.image21 = PhotoImage(file="edit.png")
        boton_modificar = Button(p_pacientes, text="  Modificar  ", command=self.modificar_paciente,
                                 image=self.image21, compound="left", cursor="hand2")
        boton_modificar.place(x=230, y=530)
        
        #Eliminar
        self.image22 = PhotoImage(file="clear.png")
        boton_eliminar = Button(p_pacientes, text="  Eliminar  ", command=self.eliminar_paciente,
                                image=self.image22, compound="left", cursor="hand2")
        boton_eliminar.place(x=355, y=530)

        #Asignar turno
        self.image23 = PhotoImage (file="calendar.png")
        boton_asignar = Button(p_pacientes, text="   Asignar turno   ", command=self.asignar_turno,
                               image=self.image23, compound="left", cursor="hand2")
        boton_asignar.place(x=480, y=530)

                   #---------treeview---------

        self.tv_pacientes = ttk.Treeview(p_pacientes)
        self.tv_pacientes = ttk.Treeview(p_pacientes, height=20, columns=("Apellido", "Nombre", "DNI", "Teléfono", "Mail"))
        self.tv_pacientes.heading("#0", text="ID")
        self.tv_pacientes.column("#0", minwidth=0, width="40")
        self.tv_pacientes.heading("#1", text="Apellido")
        self.tv_pacientes.column("#1", minwidth=0, width="130")
        self.tv_pacientes.heading("#2", text="Nombre")
        self.tv_pacientes.column("#2", minwidth=0, width="130")
        self.tv_pacientes.heading("#3", text="DNI")
        self.tv_pacientes.column("#3", minwidth=0, width="100")
        self.tv_pacientes.heading("#4", text="Teléfono")
        self.tv_pacientes.column("#4", minwidth=0, width="100")
        self.tv_pacientes.heading("#5", text="Mail")
        self.tv_pacientes.column("#5", minwidth=0, width="100")
        for paciente in self.gestion.pacientes:
            self.tv_pacientes.insert("", END, text=paciente.id, values=(paciente.apellido, paciente.nombre, paciente.dni, paciente.telefono, paciente.mail))
        
        self.tv_pacientes.place(x=45, y=60)
       
        #-----------------Pestaña turnos-----------------

        p_turnos = ttk.Frame(notebook)
        notebook.add(p_turnos, text="Turnos")
        
        #Modificar turno
        self.image1 = PhotoImage(file="edit.png")
        boton_modificar = Button(p_turnos, text="  Modificar  ", command=self.modificar_turno,
                                 image=self.image1, compound="left", cursor="hand2")
        boton_modificar.place(x=270, y=530)
        
        #Eliminar turno
        self.image2 = PhotoImage(file="clear.png")
        boton_eliminar = Button(p_turnos, text="  Eliminar  ", command=self.eliminar_turno,
                                image=self.image2, compound="left", cursor="hand2")
        boton_eliminar.place(x=420, y=530)

                   #---------treeview---------
        

        self.tv_turnos = ttk.Treeview(p_turnos)
        self.tv_turnos = ttk.Treeview(p_turnos, height=20, columns=("Paciente", "Descripción", "Fecha", "Hora", "Estado"))
        self.tv_turnos.heading("#0", text="ID")
        self.tv_turnos.column("#0", minwidth=0, width="40")
        self.tv_turnos.heading("#1", text="Paciente")        
        self.tv_turnos.heading("#2", text="Descripción")
        self.tv_turnos.heading("#3", text="Fecha")
        self.tv_turnos.column("#3", minwidth=0, width="100")
        self.tv_turnos.heading("#4", text="Hora")
        self.tv_turnos.column("#4", minwidth=0, width="100")
        self.tv_turnos.heading("#5", text="Estado")
        self.tv_turnos.column("#5", minwidth=0, width="80")
        
        for turno in self.gestion.turnos:
            self.tv_turnos.insert("", END, text=turno.id, values=(turno.paciente.apellido, turno.descripcion, turno.fecha_turno, turno.hora))
        
        self.tv_turnos.place(x=35, y=60)

        #-----------------Pestaña informes---------------
        
        p_informes = ttk.Frame(notebook)
        notebook.add(p_informes, text="Informes")

        label_help3=Label(p_informes, text="Seleccione el tipo de informe").place(x=55, y=20)
        self.sel=IntVar() 
        
        #Turnos pendientes
        info_D=Radiobutton(p_informes, text="Turnos pendientes del dia", value=1,
                           variable=self.sel, command=self.tipo_informe, cursor="hand2")
        info_D.place(x=55, y=40)
        
        #Consultas del mes
        info_M=Radiobutton(p_informes, text="Consultas finalizadas del mes", value=2,
                           variable=self.sel, command=self.tipo_informe, cursor="hand2")
        info_M.place(x=55, y=60)

        #Pacientes pendientes
        info_P=Radiobutton(p_informes, text="Pacientes pendientes", value=3,
                           variable=self.sel, command=self.tipo_informe, cursor="hand2")
        info_P.place(x=55, y=80)

                   #---------treeview------------

        self.tv_informes = ttk.Treeview(p_informes)
        self.tv_informes = ttk.Treeview(p_informes, height=15, columns=("Descripción", "Fecha", "hora", "Estado"))
        self.tv_informes.heading("#0", text="Paciente")
        self.tv_informes.heading("#1", text="Descripción")        
        self.tv_informes.heading("#2", text="Fecha")
        self.tv_informes.column("#2", minwidth=0, width="100")
        self.tv_informes.heading("#3", text="Hora")
        self.tv_informes.column("#3", minwidth=0, width="100")
        self.tv_informes.heading("#4", text="Estado")
        self.tv_informes.column("#4", minwidth=0, width="80")
        self.tv_informes.place(x=55, y=125)

        #-----------------Ventana------------------------

        self.image4 = PhotoImage(file="logout.png")
        boton_salir = Button(self.ventana, text="  Salir  ", cursor="hand2",
                           image=self.image4, compound="left", command=self.salir)
        boton_salir.place(x=370, y=595)        

        #-----------------Funciones------------------------
        
    def tipo_informe(self):
        s = self.sel.get()
        if s == 1:
            print ("seleccionaste el primero") #El print es para indicar si funciona 
        elif s == 2:
            print ("seleccionaste el segundo")
        elif s == 3:
            print ("seleccionaste el tercero")
        #tv_informes
        
    def confirmar_paciente(self):
        if self.ep_nombre.get() == "" or self.ep_apellido.get() == "" or self.ep_dni.get() == "" or self.ep_tel.get() == "":
            messagebox.showwarning("", "No puede dejar campos sin completar")
        else:
            paciente = self.gestion.nuevo_paciente(self.ep_apellido.get(), self.ep_nombre.get(), self.ep_dni.get(), self.ep_tel.get(), self.ep_mail.get())
                        
            self.tv_pacientes.insert("", END, text=paciente.id, values=(paciente.apellido, paciente.nombre, paciente.dni, paciente.telefono, paciente.mail)) ## Da error
            messagebox.showinfo(message="Su paciente ha sido guardado")
            self.ep_apellido.delete(0, END)
            self.ep_nombre.delete(0, END)
            self.ep_dni.delete(0, END)
            self.ep_tel.delete(0, END)
            self.ep_mail.delete(0, END)

    def eliminar_paciente(self):
        if not self.tv_pacientes.selection():
            messagebox.showwarning("", "Debe seleccionar un paciente de la lista para eliminar")
            return False
        else:
            resp = messagebox.askyesno(message="¿Desea eliminar el paciente?", title="Atención")
            if resp == True:
                elemento = self.tv_pacientes.selection()
                i = int(self.tv_pacientes.item(elemento)['text'])
                self.tv_pacientes.delete(elemento)
                self.gestion.eliminar_paciente(i)
                
    def modificar_paciente(self):               
        if not self.tv_pacientes.selection():
            messagebox.showwarning("", "Debe seleccionar un paciente de la lista para modificar")
            return False
        else:
            resp = messagebox.askyesno(message="¿Desea modificar los datos del paciente?", title="Atención")
            if resp == True:
                elemento = self.tv_pacientes.selection()
                it = int(self.tv_pacientes.item(elemento)['text'])
                paciente = self.gestion._buscar_por_id(it)
                
                self.modificar = Toplevel(self.ventana)
                self.modificar.title("Modificar paciente")
                self.modificar.iconbitmap("dentist.ico")
                self.modificar.geometry("640x480")
                self.modificar.resizable(0, 0)
                self.modificar.grab_set()
                #Nombre
                self.mp_nombre = Entry(self.modificar, width=75)
                self.mp_nombre.place(x=130, y=125)        
                label_nombre = Label(self.modificar, text="Nombre:").place(x=60, y=125)       
                #Apellido
                self.mp_apellido = Entry(self.modificar, width=75)
                self.mp_apellido.place(x=130, y=155)        
                label_apellido = Label(self.modificar, text="Apellido:").place(x=60, y=155)        
                #DNI
                self.mp_dni = Entry(self.modificar, width=75)
                self.mp_dni.place(x=130, y=185)        
                label_dni = Label(self.modificar, text="DNI:").place(x=60, y=185)        
                #Telefono
                self.mp_tel = Entry(self.modificar, width=75)
                self.mp_tel.place(x=130, y=215)        
                label_tel = Label(self.modificar, text="Telefono:").place(x=60, y=215)        
                #E-mail
                self.mp_mail = Entry(self.modificar, width=75)
                self.mp_mail.place(x=130, y=245)        
                label_mail = Label(self.modificar, text="E-mail:").place(x=60, y=245)
                #Carga datos a modificar
                self.mp_nombre.insert(0, paciente.nombre)
                self.mp_apellido.insert(0, paciente.apellido)
                self.mp_dni.insert(0, paciente.dni)
                self.mp_tel.insert(0, paciente.telefono)
                self.mp_mail.insert(0, paciente.mail)
                #botones  no olvidar agregar y definir el comando para el boton_ok
                b_ok = Button(self.modificar, text="Guardar", compound="left", cursor="hand2", command = self.boton_ok)
                self.modificar.bind("<Return>", self.boton_ok)
                b_ok.place(x=390, y=300)
                b_cancelar = Button(self.modificar, text = "Cancelar", compound="left", cursor="hand2", command = self.modificar.destroy)
                b_cancelar.place(x=190, y=300)
                
    def boton_ok(self, event=None, pacientes=None):
        elem = self.tv_pacientes.selection()
        id = int(self.tv_pacientes.item(elem)['text'])
        self.gestion.modificar_paciente(id, self.mp_apellido.get(), self.mp_nombre.get(), self.mp_dni.get(), self.mp_tel.get(), self.mp_mail.get())

        for i in self.tv_pacientes.get_children():
            self.tv_pacientes.delete(i)
        if not pacientes:
            pacientes = self.gestion.pacientes
        for paciente in pacientes:
            self.tv_pacientes.insert("", END, text=paciente.id, values=(paciente.apellido, paciente.nombre, paciente.dni, paciente.telefono, paciente.mail), iid=paciente.id)
        self.modificar.destroy()
    
    def asignar_turno(self):
        if not self.tv_pacientes.selection():
            messagebox.showwarning("", "Debe seleccionar un paciente de la lista para asignarle un turno")
            return False
        else:
            selec = self.tv_pacientes.selection()
            id = int(self.tv_pacientes.item(selec)['text'])
            #p = self.gestion.turno_a_paciente(id)
            
            self.asign = Toplevel(self.ventana)
            self.asign.title("Asignar turno")
            self.asign.iconbitmap("dentist.ico")
            self.asign.geometry("640x480")
            self.asign.resizable(0, 0)
            self.asign.grab_set()
            #Fecha
            self.a_fecha = Entry(self.asign, width=75)
            self.a_fecha.place(x=130, y=125)
            label_fecha = Label(self.asign, text="Fecha:").place(x=60, y=125)
            label_help = Label(self.asign, text="Ingrese la fecha del turno en el siguiente formato: AAAA/MM/DD", fg="gray")
            label_help.place(x=130, y=145)
            #Hora
            self.a_hora = Entry(self.asign, width=75)
            self.a_hora.place(x=130, y=175)
            label_hora = Label(self.asign, text="Hora:").place(x=60, y=175)
            label_help = Label(self.asign, text="Ingrese la hora del turno en el siguiente formato: HH:MM:SS", fg="gray")
            label_help.place(x=130, y=195)
            #Descripcion
            self.a_desc = Entry(self.asign, width=75)
            self.a_desc.place(x=130, y=225)
            label_desc = Label(self.asign, text="Descripción:").place(x=60, y=225)
            b_ok2 = Button(self.asign, text="Guardar", compound="left", cursor="hand2", command = self.boton_ok2)
            self.asign.bind("<Return>", self.boton_ok2)
            b_ok2.place(x=390, y=300)
            b_cancelar2 = Button(self.asign, text = "Cancelar", compound="left", cursor="hand2", command = self.asign.destroy)    
            b_cancelar2.place(x=190, y=300)
            
            #   !!! Borrar estas lineas una vez que funcione todo bien, es para agilizar las purebas
            self.a_hora.insert(0, "17:00:00")
            self.a_fecha.insert(0, "2019/10/30")
            self.a_desc.insert(0, "hola")
            # --------------------------------
            
    def boton_ok2(self):
        elem = self.tv_pacientes.selection()
        id = int(self.tv_pacientes.item(elem)['text'])
        #print(int(self.tv_pacientes.item(elem)['text']))
        turno = self.gestion.asignar_turno(id, self.a_fecha.get(), self.a_hora.get(), self.a_desc.get())
        self.tv_turnos.insert("", END, text=turno.id, values=(turno.paciente.apellido, turno.descripcion, turno.fecha_turno, turno.hora))
                        
    def eliminar_turno(self):
        if not self.tv_turnos.selection():
            messagebox.showwarning("", "Debe seleccionar un turno para eliminarlo")
            return False
        else:
            resp = messagebox.askyesno(message="¿Desea eliminar el turno?", title="Atención")
            if resp == True:
                elemento = self.tv_turnos.selection()
                i = int(self.tv_turnos.item(elemento)['text'])
                self.tv_turnos.delete(elemento)
                self.gestion.eliminar_turno(i)

    def modificar_turno(self):
        if not self.tv_turnos.selection():
            messagebox.showwarning("", "Debe seleccionar un turno para modificarlo")
            return False
        else:
            resp = messagebox.askyesno(message="¿Desea modificar los datos del turno?", title="Atención")
            if resp == True:
                elemento = self.tv_turnos.selection()
                it = int(self.tv_turnos.item(elemento)['text'])
                turno = self.gestion._buscar_turno_id(it)
            
                self.modTurno = Toplevel(self.ventana)
                self.modTurno.title("Modificar turno")
                self.modTurno.iconbitmap("dentist.ico")
                self.modTurno.geometry("640x480")
                self.modTurno.resizable(0, 0)
                self.modTurno.grab_set()
                #Fecha
                self.n_fecha = Entry(self.modTurno, width=75)
                self.n_fecha.place(x=130, y=125)
                label_fecha = Label(self.modTurno, text="Fecha:").place(x=60, y=125)
                label_help = Label(self.modTurno, text="Ingrese la fecha del turno en el siguiente formato: AAAA/MM/DD", fg="gray")
                label_help.place(x=130, y=145)
                #Hora
                self.n_hora = Entry(self.asign, width=75)
                self.n_hora.place(x=130, y=175)
                label_hora = Label(self.modTurno, text="Hora:").place(x=60, y=175)
                label_help = Label(self.modTurno, text="Ingrese la hora del turno en el siguiente formato: HH:MM:SS", fg="gray")
                label_help.place(x=130, y=195)
                #Descripcion
                self.n_desc = Entry(self.modTurno, width=75)
                self.n_desc.place(x=130, y=225)
                label_desc = Label(self.modTurno, text="Descripción:").place(x=60, y=225)
                #botones  no olvidar agregar y definir el comando para el boton_ok3              !!!!!
                b_ok3 = Button(self.modTurno, text="Guardar", compound="left", cursor="hand2")
                self.modTurno.bind("<Return>", self.boton_ok3)
                b_ok3.place(x=390, y=300)
                b_cancelar3 = Button(self.modTurno, text = "Cancelar", compound="left", cursor="hand2", command = self.modTurno.destroy)
                b_cancelar3.place(x=190, y=300)

                #   !!! Borrar estas lineas una vez que funcione todo bien, es para agilizar las purebas
                self.n_hora.insert(0, "20:00:00")
                self.n_fecha.insert(0, "2019/11/20")
                self.n_desc.insert(0, "qwert")
                # --------------------------------
            
    def boton_ok3(self, event=None, turnos=None):
        elem = self.tv_turnos.selection()
        id = int(self.tv_turnos.item(elem)['text'])
        self.gestion.modificar_turno(id, self.n_fecha.get(), self.n_hora.get(), self.n_desc.get())

        for i in self.tv_turnos.get_children():
            self.tv_turnos.delete(i)
        if not turnos:
            turnos = self.gestion.turnos
        for turno in turnos:
            self.tv_turnos.insert("", END, text=turno.id, values=(turno.paciente.apellido, turno.descripcion, turno.fecha_turno, turno.hora), iid=turno.id)
        self.modTurno.destroy()
    
    def salir(self):        
        rta = messagebox.askyesno(message="¿Desea salir? Se perderán los cambios no guardados",
                                  title="Atención")
        if rta == True:            
            self.ventana.destroy()
            exit()

if __name__ == "__main__":
    g = Gui()
    g.ventana.mainloop()
