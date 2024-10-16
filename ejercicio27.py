#Adivina el numero con while
 
import random
import os
Active=True
numR=(random.randint(1, 100))


while (Active):
     numU=int(input('Ingresa Un numero e intenta adivinar cual es el que escogio la maquina: '))

     if numR<numU:
        print('El numero que escogio es mayor, intenta de nuevo')
       

     elif numU<numR:
        print('EL numero que escogio es menor, intenta de nuevo ')

     else:
        print(f'Felicidades {numR} es el numero secreto')
        Active=False
        
     


