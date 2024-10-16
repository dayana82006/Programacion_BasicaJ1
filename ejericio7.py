#Este programa nos dice si el numero es negativo, positivo o igual a cero

#pedimos los datos al usuario
numero= int(input('ingrese un número y determina si es positivo, negativo o cero: '))

if numero == 0:
    print('el numero es cero')
elif numero>0:
    print('el numero es positivo')
else:
    print('el numero es negativo')
