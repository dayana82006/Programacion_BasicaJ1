#este programa te da un numero al azar y debes tartar de adivinar cual es

#pedimos los datos al usuario
numeroU=int(input('Escriba un numero del 1 al 10 e intenta adivinar el que eligio la maquina'))


import random
numeroM = random.randint(1, 10)
if numeroU > numeroM:
    print('el numero secreto es menor')
elif numeroU< numeroM:
    print('el numero secreto es mayor')
else:
     print('El numero es correcto')