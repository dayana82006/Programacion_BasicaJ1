#este programa te dice si el año es bisiesto

#pedimos los datos al usuario
año=int(input('Ingrese el año para saber si es bisiesto: '))

if año % 4 == 0 or año %400==0:
    print('el año es bisiesto')
else :
   print('el año no es bisiesto')