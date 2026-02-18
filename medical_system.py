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

    def verificar_disponibilidad(self, fecha, hora):
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
    
class Consultorio:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.pacientes = []
        self.doctores = []
        self.citas = []

    def registrar_paciente(self, nombre, edad, telefono, email):
        paciente = Paciente(nombre, edad, telefono, email)
        self.pacientes.append(paciente)
        print(f"\n✓ Paciente registrado exitosamente con ID: {paciente.id}")
        return paciente
    
    def registrar_doctor(self, tipo, nombre, telefono):
        if tipo == "1":
            doctor = Cardiologo(nombre, telefono)
        elif tipo == "2":
            doctor = Pediatra(nombre, telefono)
        elif tipo == "3":
            doctor = Dermatologo(nombre, telefono)
        else:
            print("✗ Tipo de especialidad no válido")
            return None
        self.doctores.append(doctor)
        print(f"\n✓ Doctor registrado exitosamente con ID: {doctor.id}")
        return doctor
    
    def agendar_cita(self, id_paciente, id_doctor, fecha, hora, motivo):
        paciente = self.buscar_paciente(id_paciente)
        doctor = self.buscar_doctor(id_doctor)

        if not paciente or not doctor:
            print("✗ Paciente o Doctor no encontrado")
            return None
        
        if not doctor.verificar_disponibilidad(fecha, hora):
            print("✗ El doctor no está disponible en ese horario")
            return None
        
        cita = Cita(paciente, doctor, fecha, hora, motivo)
        self.citas.append(cita)
        paciente.agregar_cita(cita)
        doctor.agregar_cita(cita)
        print(f"\n✓ Cita agendada exitosamente con ID: {cita.id}")
        return cita
    
    def buscar_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return paciente
        return None
    
    def buscar_doctor(self, id_doctor):
        for doctor in self.doctores:
            if doctor.id == id_doctor:
                return doctor
        return None
    
    def buscar_cita(self, id_cita):
        for cita in self.citas:
            if cita.id == id_cita:
                return cita
        return None
    
    def mostrar_pacientes(self):
        if not self.pacientes:
            print("\n✗ No hay pacientes registrados")
            return
        print(f"\n{'='*60}\nLISTADO DE PACIENTES ({len(self.pacientes)} total)\n{'='*60}")
        for paciente in self.pacientes:
            print(paciente)
    
    def mostrar_doctores(self):
        if not self.doctores:
            print("\n✗ No hay doctores registrados")
            return
        print(f"\n{'='*60}\nLISTADO DE DOCTORES ({len(self.doctores)} total)\n{'='*60}")
        for doctor in self.doctores:
            print(doctor)

    def mostrar_citas(self, filtro="todas"):
        if not self.citas:
            print("\n✗ No hay citas registradas")
            return

        if filtro == "programadas":
            citas_filtradas = [c for c in self.citas if c.estado == "Programada"]
        if filtro == "completadas":
            citas_filtradas = [c for c in self.citas if c.estado == "Completada"]
        if filtro == "canceladas":
            citas_filtradas = [c for c in self.citas if c.estado == "Cancelada"]
        else:
            citas_filtradas = self.citas

        print(f"\n{'='*60}\nCITAS - {filtro.upper()} ({len(citas_filtradas)} total)\n{'='*60}")
        for cita in citas_filtradas:
            print(cita)
    
