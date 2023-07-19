class Factura:

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