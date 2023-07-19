# nombre = valor

"""
aaaaaaa
bbbbbbbbbb
ccccccccc
"""

# Inicializar Variables
IVA:float = 0.0

producto:str = ''
cantidad:int = 0
precio:float = 0.0
subtotal:float = 0.0
total:float = 0.0

# Java
# String producto = "";

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

# Java
# System.out.println("Producto="+ producto);

# Buenas Practias
# 1) Nombres Descriptivos
# p = 'Mouse' (MAL)
# product = 'Mouse' (BIEN)

# 2) Variables (Minusculas), Constantes (Mayusculas)