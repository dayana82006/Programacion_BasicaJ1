#este programa nos permite saber si un triangulo es isosceles, equilatero o escaleno

#pedimos los datos al usuario
lado1 = float(input('Ingrese la longitud del lado 1 '))
lado2 = float(input('Ingrese la longitud del lado 2 '))
lado3 = float(input('Ingrese la longitud del lado 3 '))


if lado1 == lado2 == lado3:
   print('El triangulo es equilatero')
elif lado1 != lado2 != lado3:
   print('EL triangulo es escaleno')
else:
   print('el triangulo es isosceles')