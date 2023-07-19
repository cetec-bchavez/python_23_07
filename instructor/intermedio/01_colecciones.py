print('----------------------- ARREGLOS ---------------------')
# Listas o Arreglos []
cars = ['Ford','Volvo','BMW']


cars.append('Toyota')

print(type(cars))
print(cars)

print('----------------------- TUPLAS ---------------------')
# Tuplas()
fruits =('Manzana','Pera','Limon')

print(fruits[1])
print(type(fruits))
print(fruits)

print('----------------------- SETs ---------------------')
# Sets {}
persons ={'Luis','Pedro','Maria','Luis','Luis'}

persons.add('Veronica')

print(type(persons))
print(persons)

print('----------------------- DICCIONARIO ---------------------')
# Diccionario { clave: valor}
personas = {'11111':'Luis',
           '22222':'Pedro',
           '33333':'Maria',
           '44444':'Luis',
           '55555':'Luis'}

personas['99999'] = 'Veronica'
print(type(personas))
print(personas)
