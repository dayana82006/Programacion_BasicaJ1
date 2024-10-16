#Suma de los primeros N números enteros

#Pedir un número positivo al usuario
num = int(input("Introduce un número entero positivo que desees sumar: "))
operacion = int(0) 

# Usar un ciclo for para sumar los primeros números
for i in range(1, num + 1):
    operacion += i


print(f'La operacion de los primeros {num} es: {operacion}')