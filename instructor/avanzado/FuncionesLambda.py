# Funcion Tipica
def suma100(valor):
    resultado = valor + 100

    return resultado

# Uso Tipico
#r = suma100(50)
#print(r)

func1 = lambda valor : valor + 100
func2 = lambda valor1,valor2,valor3 : valor1 + valor2 + valor3

r = func1(70)
print(r)

r2 = func2(10,20,30)
print(r2)