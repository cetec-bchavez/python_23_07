def dividir(x,y):
    r = x/ y

    return r


try:
    resultado = dividir(10,5)

    print(resultado)

except Exception as e:
    # Solo cuando ocurre error
    print('Ocurrio un Error consulte con el Admin')
else:
    print('Ejecuto try normalmente')
finally:
    # Cerrar conexiones Base de Datos
    # Cerrar Archivo
    print('Siempre se Ejecuta')