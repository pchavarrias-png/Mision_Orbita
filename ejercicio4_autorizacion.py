
# ============================================================
# Archivo: ejercicio4_autorizacion.py
# Curso: SOFT-01 Principios de Programacion 1 - Seccion SCP0
# Integrantes: sury Arias, pablo Chavarria 
# Fecha: 16/10/2026 Version: 1.0
# Descripcion:  Autorización inicial de lanzamiento
# =============================================================

# Constantes
RESERVA_COMBUSTIBLE = 10

# Entrada de datos
combustible_disponible = int(input("Ingrese el combustible disponible: "))
combustible_ida = int(input("Ingrese el combustible requerido para la ida: "))
combustible_regreso = int(input("Ingrese el combustible requerido para el regreso: "))

oxigeno_disponible = int(input("Ingrese el oxigeno disponible: "))
oxigeno_requerido = int(input("Ingrese el oxigeno requerido: "))

energia_disponible = int(input("Ingrese la energia disponible: "))
energia_requerida = int(input("Ingrese la energia requerida: "))

provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese las provisiones requeridas: "))

# Procesamiento de datos
combustible_total = (
    combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
)

# Verificacion de recursos
combustible_suficiente = combustible_disponible >= combustible_total
oxigeno_suficiente = oxigeno_disponible >= oxigeno_requerido
energia_suficiente = energia_disponible >= energia_requerida
provisiones_suficientes = provisiones_disponibles >= provisiones_requeridas

# Autorizacion del lanzamiento
lanzamiento_autorizado = (
    combustible_suficiente
    and oxigeno_suficiente
    and energia_suficiente
    and provisiones_suficientes
)

# Salida de resultados
print("\n--- REPORTE DE LA MISION ---")
print("Combustible disponible:", combustible_disponible)
print("Combustible total requerido:", combustible_total)
print("Oxigeno disponible:", oxigeno_disponible)
print("Oxigeno requerido:", oxigeno_requerido)
print("Energia disponible:", energia_disponible)
print("Energia requerida:", energia_requerida)
print("Provisiones disponibles:", provisiones_disponibles)
print("Provisiones requeridas:", provisiones_requeridas)

if lanzamiento_autorizado:
    print("\nLANZAMIENTO AUTORIZADO: todos los recursos son suficientes.")
else:
    print("\nLANZAMIENTO DENEGADO: uno o mas recursos son insuficientes.")
