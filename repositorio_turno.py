import sqlite3
from turno import Turno
from repositorio import Repositorio

class Repositorio_Turno:
    ###Consulta y guarda turnos en la BD###

    def __init__(self):
        self.bd = sqlite3.connect ("turnos.db")
        self.cursor = self.bd.cursor()
        self.rp = Repositorio()

    def get_all(self):
        ###Retorna una lista de objetos Turno con todos los turnos que haya guardados en la BD###
        lista_turnos = []
        consulta = "SELECT id, descripcion,  fecha_creacion, fecha_turno, hora, id_paciente FROM turnos;"
        self.cursor.execute(consulta)
        todos_los_turnos = self.cursor.fetchall()
        for id, descripcion,  fecha_creacion, fecha_turno, hora, id_paciente in todos_los_turnos:
            paciente = self.rp.get_one(id_paciente)
            lista_turnos.append(Turno(paciente, fecha_turno, hora, descripcion, id))
        return lista_turnos

    def guardar (self, turnos):
        ###Guarda el turno en la BD### #probar y revisar!!! #ver que onda id_paciente
        consulta = "INSERT INTO turnos (descripcion,  fecha_creacion, fecha_turno, hora, id_paciente) VALUES (?, ?, ?, ?, ?);"  # 29/10 agregado id_paciente
        resultado = self.cursor.execute(consulta, [turnos.descripcion, turnos.fecha_creacion, turnos.fecha_turno, turnos.hora, turnos.id_paciente])
        id_turnos = resultado.lastrowid
        self.bd.commit()
        return id_turnos

    def actualizar (self, turnos):
        ###Actualiza el turno en la BD### #ver que onda " paciente = ? "
        consulta = "UPDATE turnos SET fecha_turno = ?, hora = ?, descripcion = ? WHERE id = ?;"
        self.cursor.execute(consulta, [turnos.fecha_turno, turnos.hora, turnos.descripcion, turnos.id]) # 29/10 eliminado turnos.paciente
        self.bd.commit()

    def eliminar (self, turnos):
        ###Elimina el turno de la BD###
        print(turnos.id)
        consulta = "DELETE FROM turnos WHERE id = ?;"
        self.cursor.execute(consulta, [turnos.id])
        self.bd.commit()
        
