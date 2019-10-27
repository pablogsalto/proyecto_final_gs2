import datetime
from paciente import Paciente
class Turno:
    def __init__(self, paciente, fecha_turno, hora, descripcion, id_turno = None):
        self.paciente = paciente
        self.fecha_turno = fecha_turno
        self.descripcion = descripcion
        self.hora = hora
        self.id = id_turno
        self.fecha_creacion = datetime.datetime.today()
        #self.id_paciente = paciente.id

    def busqueda(self, filtro):
        return (filtro in self.fecha_turno)
