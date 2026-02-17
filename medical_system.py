# Clase paciente

class Paciente:
    contador_pacientes = 0

    def __init__(self, nombre, edad, telefono, email):
        Paciente.contador_pacientes += 1
        self.id = f"PAC{Paciente.contador_pacientes:04d}"
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.email = email
        self.historial_citas = []

    def agregar_cita(self, cita):
        self.historial_citas.append(cita)

    def mostrar_info(self):
        print(f"\n{'='*50}")
        print(f"ID: {self.id} | Nombre: {self.nombre} | Edad: {self.edad} años")
        print(f"Teléfono: {self.telefono} | Email: {self.email}")
        print(f"Total de citas: {len(self.historial_citas)}")
        print(f"{'='*50}")

    def __str__(self):
        return f"{self.id} - {self.nombre} ({self.edad} años)"

class Doctor:
    contador_doctores = 0

    def __init__(self, nombre, especialidad, telefono):
        Doctor.contador_doctores +=1
        self.id = f"DOC{Doctor.contador_doctores:04d}"
        self.nombre = nombre
        self.especialidad = especialidad
        self.telefono = telefono
        self.citas_programadas = []
    
    def agregar_cita(self, cita):
        self.citas_programadas.append(cita)

    def verificar_disponibilidad(self,fecha, hora):
        for cita in self.citas_programadas:
          if cita.fecha == fecha and cita.hora == hora and cita.estado != "cancelada":
              return False 
        return True
    
    def mostrar_info(self):
        citas_activas = len([c for c in self.citas_programadas if c.estado == 'Programada'])
        print(f"\n{'='*50}")
        print(f"ID: {self.id} | Dr(a). {self.nombre}")
        print(f"Especialidad: {self.especialidad} | Teléfono: {self.telefono}")
        print(f"Citas programadas: {citas_activas}")
        print(f"{'='*50}")
    
    def __str__(self):
        return f"{self.id} - Dr(a). {self.nombre} - {self.especialidad} "
        
# ==================== HERENCIA: ESPECIALIDADES ====================
class Cardiologo(Doctor):
    def __init__(self, nombre, telefono):
        super().__init__(nombre, "Cardiologia", telefono)
        self.costo_consulta = 800

class Pediatra(Doctor):
    def __init__(self, nombre, telefono):
        super().__init__(nombre, "Pediatria", telefono)
        self.coste_consulta = 600

class Dermatologo(Doctor):
    def __init__(self, nombre, telefono):
        super().__init__(nombre, "Dermatologia", telefono)
        self.costo_consulta = 700

# ==================== CLASE CITA ====================
class Cita:
    contador_citas = 0

    def __init__(self, paciente, doctor, fecha, hora, motivo):
        Cita.contador_citas += 1
        self.id = f"CIT{Cita.contador_citas:04d}"
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.estado = "Programada"
        self.diagnostico = ""

    def cancelar(self):
        self.estado = "Cancelada"

    def completar(self, diagnostico):
        self.estado = "Completada"
        self.diagnostico = diagnostico
    
    def mostrar_info(self):
        print(f"\n{'='*60}")
        print(f"ID Cita: {self.id} | Estado: {self.estado}")
        print(f"Paciente: {self.paciente.nombre} (ID: {self.paciente.id})")
        print(f"Doctor: {self.doctor.nombre} - {self.doctor.especialidad}")
        print(f"Fecha: {self.fecha} | Hora: {self.hora}")
        print(f"Motivo: {self.motivo}")
        if self.diagnostico:
            print(f"Diagnóstico: {self.diagnostico}")
        print(f"Costo: ${self.doctor.costo_consulta}")
        print(f"{'='*60}")

    def __str__(self):
        return f"{self.id} - {self.paciente.nombre} con {self.doctor.nombre} ({self.fecha} {self.hora}) [{self.estado}]"
        