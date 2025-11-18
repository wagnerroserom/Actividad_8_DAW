# Python empleado para el desarrollo de soluciones

from datetime import datetime

# 1: Sistema de turnos médicos
def agregar_paciente(pacientes, nombre, edad, especialidad):
    # Agrega un paciente al final de la cola
    pacientes.append((nombre, edad, especialidad))

def atender_paciente(pacientes):
    # Atiende al primer paciente en la cola
    if pacientes:
        return pacientes.pop(0)
    else:
        return "Noo hay pacientes en espera."
    