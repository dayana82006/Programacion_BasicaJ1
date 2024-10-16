#este programa clasifica a las personas segun su edad

#pedimos los datos al usuario
edad=int(input('Ingrese la edad: '))

if edad <= 12:
    print('La clasificacion de edad es un niño')
elif edad >=12 and edad <18:
    print('La clasificacion de edad es un adolescente')
elif edad >=18 and edad<65:
    print('La clasificacion de edad es un adulto')
else:
    print('La clasificacion de edad es un anciano')