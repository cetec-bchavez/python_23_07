class Factura:
  def __init__(self, id, producto, cantidad,precio,total):
    self.id = id
    self.producto = producto
    self.cantidad = cantidad
    self.precio = precio
    self.total = total

  def cambiarValores(self):
    self.cantidad *= 10
    self.total *= 100

  def calcularTotal(self):
    self.total = self.cantidad * self.precio + self.cantidad * self.precio * 0.12

    #if self.cantidad == None:
    #  print("Nulos")

    #if,else,calculos