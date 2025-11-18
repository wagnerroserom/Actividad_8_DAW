# Python empleado para el desarrollo de soluciones

from datetime import datetime

# 1: Sistema de turnos médicos
def agregar_paciente(pacientes, nombre, edad, especialidad):
    # Agrega un paciente al final de la cola.
    pacientes.append((nombre, edad, especialidad))

def atender_paciente(pacientes):
    # Atiende al primer paciente en la cola.
    if pacientes:
        return pacientes.pop(0)
    else:
        return "No hay pacientes en espera."

def mostrar_pacientes(pacientes):
    # Devuelve una lista de pacientes en espera.
    return pacientes.copy()

# 2: Control de asistencia sin duplicados
def resgistrar_asistentes(asistentes, registros, nombre):
    # Registra a un asistente si no ha asistido antes.
    if nombre not in asistentes:
        asistentes.add(nombre)
        registros[nombre] = datetime.now().strftime("%d/%m/%y, %H:%M:%S") 
        return f"{nombre} ha sido registrado con éxito."
    else:
        return f"{nombre} ya está registrado"
    
def verificar_asistencia(asistentes, nombre):
    # Verifica si una persona ya asistió.
    return  nombre in asistentes

# 3: Inventario de tienda 
def vender_producto(inventario, agotados, producto, cantidad):
    # Resta la cantidad vendida, del inventario.
    if producto in inventario:
        if inventario[producto] >= cantidad:
            inventario[producto] -= cantidad
            if inventario[producto] == 0:
                agotados.add(producto)
            return f"Venta realizada. Quedan {inventario[producto]} unidades de {producto}."
        else: 
            return f"No hay sificiente stock de {producto}."
    else:
        return f"El producto {producto} no existe en el inventario"        
