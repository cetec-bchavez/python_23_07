IVA,producto,cantidad,precio,subtotal,total = 0.14,'Mouse',10,4.5,0.0,0.0

# Procesar Valores
subtotal = cantidad * precio
total = subtotal + (subtotal * IVA)

# Imprimir Valores

print('Producto=', producto)
print('Total=', total)


print('Type Producto=', type(producto))
print('Type Cantidad=', type(cantidad))
print('Type Total=', type(total))

# ------------------- CAST ----------------

x = int('15')
y = int(9.7)

print('X=', x,type(x))
print('Y=', y,type(y))

x = float(x)
y = float(y)

print('X=', x,type(x))
print('Y=', y,type(y))


es_float = isinstance(y,int)
print("Y es float:", es_float)

edadesx = [5,7,9,'65asd']
i=0
for edad in edadesx:

    es_texto = isinstance(edad,str)
    
    if es_texto :
       
       for t in edad:
            if t.isdigit():
                print(t)

    i+=1

print(i)

"""
xf = float(x)
yf = float(y)

print('XF=', xf,type(xf))
print('YF=', yf,type(yf))
"""