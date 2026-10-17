
# Universidad CENFOTEC
# Curso: Principios de Programacion 1
# Proyecto: Mision Orbita
# Ejercicio 3: Verificacion del soporte para la tripulacion
# Integrantes: Pablo Gerardo Chavarria Segura
#              Sury Francinie Arias Delgado
# Fecha: Octubre de 2026
# Version: 1.0

# Entrada de datos
oxigeno_disponible = int(input("Ingrese el oxigeno disponible: "))
oxigeno_requerido = int(input("Ingrese el oxigeno requerido: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese las provisiones requeridas: "))

# Verificacion de recursos para la tripulacion
if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")
