#  1. Clase Perro ● Atributos: nombre, raza, edad, tamaño, peso, estado_salud, vacunado, estado ('disponible', 'reservado', 'adoptado'), temperamento, id.
# ● Métodos: cambiar estado, mostrar información, etc.

class Perro(object):
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
        
    def cambiarEstado(self,nuevo_estado):
        if nuevo_estado in ['disponible', 'reservado', 'adoptado']:
            self.estado = nuevo_estado
            print("Estado actualizado")
        else:
            print("Estado inválido")
        
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

class UsuarioAdoptante(object):
    def __init__(self, nombre, dni, email, preferencias, historial_adopciones):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.preferencias = preferencias
        self.historial_adopciones = historial_adopciones
    
    def preferencias(self, raza=None, edad=None, tamaño=None):
        if raza:
            self.preferencias['raza'] = raza
        if edad:
            self.preferencias['edad'] = edad
        if tamaño:
            self.preferencias['tamaño'] = tamaño
        print("Preferencias actualizadas")

    def registrarse(self, nombre, dni, email):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        print("Usuario registrado")
        


#🔁 3. Clase SistemaAdopcion ● Métodos para: ○ Cargar y eliminar perros ○ Registrar usuarios ○ Postular a un perro ○ Confirmar adopción ○ Sugerir perros según preferencias
# ○ Mostrar listados (perros disponibles, por estado, por usuario)

class CargarEliminarPerros:
    def __init__(self):
        self.perros = []
    
    def cargarPerro(self, nuevo_perro):
        self.perros.append(nuevo_perro)
        print(f"Perro cargado: {nuevo_perro.nombre}")
    
    def eliminarPerro(self, id_perro):
        for perro in self.perros:
            if perro.id == id_perro:
                self.perros.remove(perro)
                print(f"Perro eliminado: {perro.nombre}")
                return
        print("Perro no encontrado")

# Supongamos que ya tienes una clase Perro definida con atributos como id y nombre.
class Perro:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

# Crear una instancia de la clase CargarEliminarPerros
sistema = CargarEliminarPerros()

# Crear algunos perros
perro1 = Perro(1, "Max")
perro2 = Perro(2, "Luna")
perro3 = Perro(3, "Rocky")

# Probar el método cargarPerro
sistema.cargarPerro(perro1)  # Debería imprimir: "Perro cargado: Max"
sistema.cargarPerro(perro2)  # Debería imprimir: "Perro cargado: Luna"
sistema.cargarPerro(perro3)  # Debería imprimir: "Perro cargado: Rocky"

# Probar el método eliminarPerro
sistema.eliminarPerro(2)  # Debería imprimir: "Perro eliminado: Luna"
sistema.eliminarPerro(4)  # Debería imprimir: "Perro no encontrado"

# Verificar que los perros restantes están en la lista
for perro in sistema.perros:
    print(f"Perro en el sistema: {perro.nombre}")



 
    