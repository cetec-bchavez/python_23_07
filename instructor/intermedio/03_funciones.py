def calcularTotal(cantidad,precio): # Ingredientes / Parametros / Argumentos

    subtotal = cantidad * precio    # Procesos
    total = subtotal + subtotal * 0.12 # Procesos

    return total # Resultado / Retorno


cantidad1 = 5
precio1 = 8.5
resultado1 = 0.0

resultado1 = calcularTotal(cantidad1,precio1)

print(resultado1)


