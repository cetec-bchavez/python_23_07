import numpy as np
import matplotlib.pyplot as plt

def show_constante():
    xs = [x for x in range(0,20,2)]
    ys = [10 for x in range(0,20,2)]

    plt.plot(xs,ys)
    plt.show()

#range(0,20,2) = [0,2,4,6..20]
# [x for x in range(0,20,2)] = [0,2,4,6..20]
# [x*2 for x in range(0,20,2)] = [0,4,6,12..40]
# print([x for x in range(0,20,2)])
# y = 5x +7
def show_lineal():
    xs = [x for x in range(0,20,2)]
    ys = [(5*x + 7) for x in range(0,20,2)]

    plt.plot(xs,ys)    
    plt.show()

def show_cuadratica():
    xs = [x for x in range(0,20,2)]
    ys = [(5*x*x) for x in range(0,20,2)]
    
    plt.plot(xs,ys)
    plt.show()

show_cuadratica()
#show_lineal()
#show_constante()
