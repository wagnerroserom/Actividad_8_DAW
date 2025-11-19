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
