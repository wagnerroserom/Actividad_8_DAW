from src.soluciones import *

# 1: Turnos médicos
print("=== 1. Sistema de turnos médicos ===")
cola_pacientes = []
agregar_paciente(cola_pacientes, "Carlos Rubira", 34, "Cardiología")
agregar_paciente(cola_pacientes, "Maite Gully", 27, "Ginecología")
print("Pacientes en espera:", mostrar_pacientes(cola_pacientes))
atendido = atender_paciente(cola_pacientes)
print("Paciente atendido:", atendido)
print("Pacientes restantes:", mostrar_pacientes(cola_pacientes))

print("\n" + "="*50 + "\n")

# 2: Control de asistencia sin duplicados
print("=== 2. Control de asistencia sin duplicados ===")
asistentes = set()
registros = {}
print(registrar_asistente(asistentes, registros, "Lucía Fernandez"))
print(registrar_asistente(asistentes, registros, "Héctor Paladines"))
print(registrar_asistente(asistentes, registros, "Lucía Fernandez")) # Intento de ingresar un duplicado
print("¿Lucía asistió?", verificar_asistencia(asistentes, "Lucía Fernandez"))
print("Total de asistentes únicos:", total_asistentes(asistentes))

print("\n" + "="*50 + "\n")

# 3: Inventario de tienda
print("=== 3. Inventario de tienda ===")
inventario = {"manzanas": 10, "plátanos": 5, "leche": 0}
agotados = set(producto for producto, cantidad in inventario.items() if cantidad == 0)
print("Inventario inicial:", mostrar_inventario(inventario))
print(vender_producto(inventario, agotados, "manzanas", 3))
print(vender_producto(inventario, agotados, "leche", 1)) # Producto agotado
print("Productos agotados:", agotados)

print("\n" + "="*50 + "\n")

# 4: Encuesta de satisfacción
print("=== 4. Encuesta de satisfacción ===")
encuestas = []
agergar_respuesta(encuestas, "Cliente A", 7, "Muy buen servicio")
agergar_respuesta(encuestas, "Cliente B", 2, "Demasiado tiempo de espera")
agergar_respuesta(encuestas, "Cliente C", 3, "El personal se portó impaciente")
print("Media de satisfacción:", calcular_media_satisfacción(encuestas))
print("Comentarios negativos:", listar_comentarios_negativos(encuestas))

print("\n" + "="*50 + "\n")




