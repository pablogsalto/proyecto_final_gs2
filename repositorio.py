import sqlite3
from paciente import Paciente

class Repositorio:
    ###Consulta y guarda notas en la BD###

    def __init__(self):
        self.bd = sqlite3.connect("turnos.db")
        self.cursor = self.bd.cursor()

    def get_all(self):
        ### Retorna una lista de objetos Paciente con todas los pacientes que haya guardadas en la BD###
        lista_pacientes = []
        consulta = "SELECT id, apellido, nombre, dni, telefono, mail FROM pacientes;"
        self.cursor.execute(consulta)
        todos_los_pacientes = self.cursor.fetchall()
        for id, apellido, nombre, dni, telefono, mail in todos_los_pacientes:
            if mail:
                #Crear paciente sin mail
                lista_pacientes.append(Paciente(apellido, nombre, dni, telefono, mail,id)) #probar y revisar cuando este el objeto paciente
            else:
                lista_pacientes.append(Paciente(apellido, nombre, dni, telefono, mail,id))
        return lista_pacientes

    def guardar(self, pacientes):
        ###Guarda el paciente en la BD### #probar y revisar!!!
        consulta = "INSERT INTO pacientes (apellido, nombre, dni, telefono, mail) VALUES (?, ?, ?, ?, ?);"
        resultado = self.cursor.execute(consulta, [pacientes.apellido, pacientes.nombre, pacientes.dni, pacientes.telefono, pacientes.mail])
        id_pacientes = resultado.lastrowid
        self.bd.commit()
        return id_pacientes

    def actualizar(self, pacientes):
        ###Actualiza el paciente en la BD###
        consulta = "UPDATE pacientes SET apellido = ?, nombre = ?, dni = ?, telefono = ?, mail = ? WHERE id = ?;"
        self.cursor.execute(consulta, [pacientes.apellido, pacientes.nombre, pacientes.dni, pacientes.telefono, pacientes.mail, pacientes.id])
        self.bd.commit()

    def eliminar(self, pacientes):
        ###Elimina la nota de la BD###
        consulta = "DELETE FROM pacientes WHERE id = ?;"
        self.cursor.execute(consulta, [pacientes.id])
        self.bd.commit()

    def get_one(self, id_paciente):
        consulta = "SELECT id, apellido, nombre, dni, telefono, mail FROM pacientes WHERE id=?;"
        self.cursor.execute(consulta,[id_paciente])
        datos_paciente = self.cursor.fetchone()
        id = datos_paciente[0]
        apellido = datos_paciente[1]
        nombre = datos_paciente[2]
        dni = datos_paciente[3]
        telefono =  datos_paciente[4]
        mail = datos_paciente[5]
        p = Paciente(apellido, nombre, dni, telefono, mail,id)
        return p





