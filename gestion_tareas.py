import heapq   # importamos heapq para poder manegar colas con priodidad
import json  # importamos json para guardar aquí los datos y que persistan
from datetime import datetime # para manejar fechas 

# Clase para gestionar tareas con prioridad
class GestorDeTareas:
    def __init__(self):
        # Lista de tareas pendientes como una cola de prioridad, osea heap
        self.tareas = []
        # tareas completadas
        self.tareas_completadas = []

    def agregar_tarea(self, nombre, prioridad, dependencias=None, fecha_limite=None):
       
        if not isinstance(prioridad, int) or not nombre:  # comprobamos que el tipo de dato introducido es el correcto, en la prioridad debe de ser un numero entero
            raise ValueError("La prioridad debe ser un número entero y el nombre no puede estar vacío.")
        if dependencias is None:
            dependencias = []

        tarea = {
            "nombre": nombre,
            "prioridad": prioridad,
            "dependencias": dependencias,
            "fecha_limite": fecha_limite,
            "fecha_creacion": datetime.now().isoformat()  # Fecha en que se añadio lla tarea
        }
        # Añadimos la tarea al heap (cola de prioridad)
        heapq.heappush(self.tareas, (prioridad, tarea))
        print(f"Tarea '{nombre}' añadida con prioridad {prioridad}.")

    def mostrar_tareas(self):
        # Muestra todas las tareas pendientes ordenadas por prioridad.
        print("Tareas pendientes ordenadas por prioridad:")
        for _, tarea in sorted(self.tareas, key=lambda x: x[0]):  # Ordenar por prioridad, usamos la funcion lambda
            print(f"{tarea['nombre']} (Prioridad: {tarea['prioridad']})")

    def completar_tarea(self):
        # Marca la tarea con mayor prioridad como completada y elimina del sistema.
        if not self.tareas: 
            print("No hay tareas pendientes.")
            return
        _, tarea = heapq.heappop(self.tareas)  # Elimina la tarea de mayor prioridad
        self.tareas_completadas.append(tarea)  # Mueve la tarea a la lista de completadas
        print(f"Tarea completada: {tarea['nombre']}")

    def obtener_tarea_mayor_prioridad(self):
        #Devuelve la tarea pendiente con mayor prioridad sin eliminarla.
        if not self.tareas:
            print("No hay tareas pendientes.")
            return None
        _, tarea = self.tareas[0]
        print(f"Tarea de mayor prioridad: {tarea['nombre']} (Prioridad: {tarea['prioridad']})")
        return tarea

    def guardar_tareas(self, archivo="tareas.json"):
        #Guarda las tareas pendientes y completadas en un archivo json.
        with open(archivo, "w") as file:   # Guardamos las tareas en un archivo json
            json.dump({"pendientes": self.tareas, "completadas": self.tareas_completadas}, file)
        print("Tareas guardadas en el archivo.")

    def cargar_tareas(self, archivo="tareas.json"):
        #Carga las tareas desde un archivo JSON, si existe.
        try:  # Try and except por si acaso no encontramos o no podemos abrir el archivo
            with open(archivo, "r") as file:
                datos = json.load(file)
                self.tareas = datos["pendientes"]
                self.tareas_completadas = datos["completadas"]
                heapq.heapify(self.tareas)  # Convierte la lista cargada en un heap
            print("Tareas cargadas desde el archivo.")
        except FileNotFoundError:
            print("No se encontró el archivo. No se cargaron tareas.")



# no me da tiempo a hacer el bonus, pero sería así:

'''
Antes de completar una tarea, verifica que todas sus dependencias estén en la lista de tareas completadas
Si no es así, impide su finalización y muestra un mensaje indicando que las dependencias no están satisfechas.
Esto asegura que las tareas se completen en el orden correcto y necesario
'''