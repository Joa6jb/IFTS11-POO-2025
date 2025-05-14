#  1. Clase Perro ● Atributos: nombre, raza, edad, tamaño, peso, estado_salud, vacunado, estado ('disponible', 'reservado', 'adoptado'), temperamento, id.
# ● Métodos: cambiar estado, mostrar información, etc.

class Perro:
    def __init__(self, nombre, raza, edad, tamaño, peso, estado_salud, vacunado, estado, temperamento, id):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tamaño = tamaño
        self.peso = peso
        self.estado_salud = estado_salud
        self.vacunado = vacunado
        self.estado = estado
        self.temperamento = temperamento
        self.id = id

    def cambiar_estado(self, estado):
        self.estado = estado

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Peso: {self.peso}")
        print(f"Estado salud: {self.estado_salud}")
        print(f"Vacunado: {self.vacunado}")
        print(f"Estado: {self.estado}")
        print(f"Temperamento: {self.temperamento}")
        print(f"ID: {self.id}")

#2. Clase UsuarioAdoptante
#● Atributos: nombre, dni, email, preferencias (raza, edad, tamaño),historial_adopciones.
#● Métodos: registrarse, modificar datos, ver historial, etc.

class UsuarioAdoptante:
    def __init__(self, nombre, dni, email, preferencias, historial_adopciones):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.preferencias = preferencias
        self.historial_adopciones = historial_adopciones

    def registrarse(self, nombre, dni, email, preferencias):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.preferencias = preferencias

    def modificar_datos(self, nombre, dni, email, preferencias):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.preferencias = preferencias

    def ver_historial(self):
        print(f"Nombre: {self.nombre}")
        print(f"DNI: {self.dni}")
        print(f"Email: {self.email}")
        print(f"Preferencias: {self.preferencias}")
        print(f"Historial de adopciones: {self.historial_adopciones}")

#🔁 3. Clase SistemaAdopcion ● Métodos para: ○ Cargar y eliminar perros ○ Registrar usuarios ○ Postular a un perro ○ Confirmar adopción ○ Sugerir perros según preferencias
# ○ Mostrar listados (perros disponibles, por estado, por usuario)



 
    