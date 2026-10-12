# Ejercicio 1 - Calculo de recursos de la mision

# Constantes
COMBUSTIBLE_POR_DIA = 8
RESERVA_COMBUSTIBLE = 10
OXIGENO_POR_TRIPULANTE = 2
RESERVA_OXIGENO = 5
ENERGIA_POR_DIA = 5
RESERVA_ENERGIA = 10
RESERVA_PROVISIONES = 3

# Entradas
nombre_mision = input("Ingrese el nombre de la mision: ")
tripulacion = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese los dias de viaje: "))

# Calculo del combustible
combustible_ida = dias_viaje * COMBUSTIBLE_POR_DIA
combustible_regreso = dias_viaje * COMBUSTIBLE_POR_DIA

combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# Calculo del oxigeno
oxigeno_requerido = dias_viaje * tripulacion * OXIGENO_POR_TRIPULANTE + RESERVA_OXIGENO

# Calculo de la energia
energia_requerida = dias_viaje * ENERGIA_POR_DIA + RESERVA_ENERGIA

# Calculo de las provisiones
provisiones_requeridas = dias_viaje * tripulacion + RESERVA_PROVISIONES

# Mostrar resultados
print("Mision:", nombre_mision)
print("Combustible total:", combustible_total)
print("Oxigeno requerido:", oxigeno_requerido)
print("Energia requerida:", energia_requerida)
print("Provisiones requeridas:", provisiones_requeridas)



