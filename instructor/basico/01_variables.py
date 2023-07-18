# nombre = valor

"""
aaaaaaa
bbbbbbbbbb
ccccccccc
"""

# Inicializar Variables
IVA = 0.0

producto = ''
cantidad = 0
precio = 0.0
subtotal=0.0
total = 0.0


# Asignar Valores a Variables
IVA = 0.12

producto = 'Mouse'
cantidad = 5
precio = 8.8

# Procesar Valores
subtotal = cantidad * precio
total = subtotal + (subtotal * IVA)

# Imprimir Valores

print('Producto=', producto)
print('Total=', total)

# Buenas Practias
# 1) Nombres Descriptivos
# p = 'Mouse' (MAL)
# product = 'Mouse' (BIEN)

# 2) Variables (Minusculas), Constantes (Mayusculas)