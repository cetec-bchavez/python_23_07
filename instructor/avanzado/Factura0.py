class Factura0:
    
    def __init__(self,producto,cantidad,precio,subtotal,total) -> None:
        # Columnas Ingredientes
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio

        # Columnas Resultado
        self.subtotal = subtotal
        self.total = total

    def calcularTotal(self):
        self.subtotal = self.cantidad * self.precio
        self.total = self.subtotal + self.subtotal * 0.12



print('------------------------- 1 OBJETO ------------------------------')
# OBJETOS
# nombre = Clase(valor1,valor2,valor3)

factura1 = Factura0('',0,0.0,0.0,0.0)

# Valores a Parametros
factura1.producto = 'Mouse'
factura1.cantidad = 5
factura1.precio = 7

# Procesar Calculo
factura1.calcularTotal()

print(factura1.producto,factura1.cantidad,factura1.total)


print('------------------------- LISTA OBJETOS ------------------------------')
factura2 = Factura0('Teclado',7,8.0,0.0,0.0)
factura2.calcularTotal()

factura3 = Factura0('Monitor',9,3.0,0.0,0.0)
factura3.calcularTotal()


facturas = list()
#facturas = []

facturas.append(factura1)
facturas.append(factura2)
facturas.append(factura3)

# print(facturas)

facturax:Factura0 = None

for facturax in facturas:
    print(facturax.producto,facturax.cantidad,facturax.total)