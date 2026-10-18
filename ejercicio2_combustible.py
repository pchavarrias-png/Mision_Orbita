
## Ejercicio 2 - Combustible 
# ============================================================
# Archivo: ejercicio2_combustible.py
# Curso: SOFT-01 Principios de Programacion 1 - Seccion SCP0
# Integrantes: sury Arias, pablo Chavarria 
# Fecha: 16/10/2026 Version: 1.0
# Descripcion: verificar si una nave posee suficiente combustible 
# ============================================================

# Constantes
RESERVA_EMERGENCIA = 10
LIMITE_MARGEN_BAJO = 10

# Entrada de datos
combustible_disponible = int(input("Ingrese el combustible disponible: "))
combustible_ida = int(input("Ingrese el combustible requerido para llegar al destino: "))
combustible_regreso = int(input("Ingrese el combustible requerido para regresar: "))

# calculo del combustible total requerido
combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_EMERGENCIA
combustible_adicional = combustible_disponible - combustible_total_requerido


# Verificación del margen de combustible
if combustible_adicional < LIMITE_MARGEN_BAJO:
    print("Advertencia: el margen adicional de combustible es bajo.")

# Salida de resultados
print("Combustible disponible:", combustible_disponible, "unidades")
print("Combustible requerido para llegar:", combustible_ida, "unidades")
print("Combustible requerido para regresar:", combustible_regreso, "unidades")
print("Reserva de emergencia:", RESERVA_EMERGENCIA, "unidades")
print("Combustible total requerido:", combustible_total_requerido, "unidades")
print("Combustible adicional disponible:", combustible_adicional, "unidades")
