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
        fgfg
