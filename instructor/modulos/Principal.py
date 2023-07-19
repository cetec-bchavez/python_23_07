from base.Factura import Factura

print('------------------------- 1 OBJETO ------------------------------')
# OBJETOS
# nombre = Clase(valor1,valor2,valor3)

factura1 = Factura('',0,0.0,0.0,0.0)

# Valores a Parametros
factura1.producto = 'Mouse'
factura1.cantidad = 5
factura1.precio = 7

# Procesar Calculo
factura1.calcularTotal()

print(factura1.producto,factura1.cantidad,factura1.total)


from base.Factura import Factura

print('------------------------- LISTA OBJETOS ------------------------------')
factura2 = Factura('Teclado',7,8.0,0.0,0.0)
factura2.calcularTotal()

factura3 = Factura('Monitor',9,3.0,0.0,0.0)
factura3.calcularTotal()


facturas = list()
#facturas = []

facturas.append(factura1)
facturas.append(factura2)
facturas.append(factura3)

# print(facturas)

facturax:Factura = None

for facturax in facturas:
    print(facturax.producto,facturax.cantidad,facturax.total)