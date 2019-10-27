from paciente import Paciente
from turno import Turno
from repositorio import Repositorio
from repositorio_turno import Repositorio_Turno

class Gestion:
    
    def __init__(self):
        self.r = Repositorio()
        self.rt = Repositorio_Turno()
        self.pacientes = self.r.get_all()
        #self.pacientes = []
        self.turnos = self.rt.get_all()

    def nuevo_paciente(self, apellido, nombre, dni, telefono, mail):
        paciente = Paciente(apellido, nombre, dni, telefono, mail)
        paciente.id = self.r.guardar(paciente)
        #self.pacientes.append(paciente)
        return paciente
        
    def _buscar_por_id(self,id_paciente):
        for paciente in self.pacientes:
            if str(paciente.id) == str(id_paciente):
                return paciente
        return None
    
    def turno_a_paciente(self, id_paciente, id_turno):
        for paciente in self.pacientes:
            if str(paciente.id) == str(id_paciente):
                pass                           
                    
    def modificar_paciente(self, id_paciente, apellido, nombre, dni, telefono, mail):
        paciente = self._buscar_por_id(id_paciente)             
        if paciente:
            paciente.apellido = apellido
            paciente.nombre = nombre
            paciente.dni = dni
            paciente.telefono = telefono
            paciente.mail = mail
            self.r.actualizar(paciente) # !!
            return True
        return False            
               
    def eliminar_paciente(self, id_paciente):        
        paciente = self._buscar_por_id(id_paciente)
        if paciente:
            self.r.eliminar(paciente)
            #self.pacientes.remove(paciente)
            return True
        return False
    
    def _buscar_turno_id(self,id_turno):
        for turno in self.turnos:
            if str(turno.id_t) == str(id_turno):
                return turno
        return None

    def asignar_turno(self, id_paciente, fecha_turno, hora, descripcion):
        #print("HOLA")
        paciente = self._buscar_por_id(id_paciente)        
        turno = Turno(paciente, fecha_turno, hora, descripcion)
        turno.id = self.rt.guardar(turno)
        return turno
        
        
    def eliminar_turno(self, id_paciente):
        if turno:
            self.rt.eliminar(turno)
            return True
        return False

    def modificar_turno(self, id_paciente, fecha_turno,hora, descripcion):        
        turno = self._buscar_turno_id(id_turno)             
        if turno:
            turno.fecha_turno = fecha_turno
            turno.hora = hora
            turno.descripcion = descripcion
            self.rt.actualizar(turno)
            return True
        return False
        
