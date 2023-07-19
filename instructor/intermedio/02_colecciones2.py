print('----------------------- ARREGLOS ---------------------')
# Listas o Arreglos []
pers1 = ['111','Luis','Sanchez']
pers2 = ['222','Pedro','Perez']
pers3 = ['333','Veronica','Hidaldo']

pers6 = ['666','Maria','Gutierez']

cars = [pers1,pers2,pers3]


cars.append(pers6)

print(type(cars))
print(cars[0]) # Auto
print(cars)


print('----------------------- TUPLAS ---------------------')
# Tuplas()
fruits =(pers1,pers2,pers3)

print(fruits[1]) # Auto
print(type(fruits))
print(fruits)

"""
print('----------------------- SETs ---------------------')
# Sets {}
persons ={'Luis','Pedro','Maria','Luis','Luis'}

persons.add('Veronica')

print(type(persons))
print(persons)
"""

print('----------------------- DICCIONARIO ---------------------')
# Diccionario { clave: valor}
personas = {'111':pers1,
           '222':pers2,
           '333':pers3
        }

personas['666'] = pers6

print(personas.get('222'))
print(type(personas))
print(personas)


print('----------------------- RECORRER ARREGLOS ---------------------')

# for(int i=0;i<10;i++) {
# }

print('----- Todos -----')
for car1 in cars:
    print(car1)

print('----- Cada Elemento -----')
for car1 in cars:
    
    for elem1 in car1:
        print(elem1)
    
    print('')