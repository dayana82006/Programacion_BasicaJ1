#este programa es un Sistema de calificaciones con bonificaciones
#pedimos los datos al usuario
calificacion=float(input('Ingrese la calificacion del estudiante: '))
extra=str(input('EL estudiante realizo trabajos extra?: '))

#usamos if para condicionar que si la calimificacion es mayor se deje en 100, 
#si es menor e hizo actividades extra te da 5% y si no, te deja la nota igual
if calificacion>100:
    print('Su nota es 100')
elif extra == 'si':
    total= round(calificacion*5)/100 + calificacion
    if total>100:
        print('Su nota es 100')
    else:
        print(f'el total es {total}')

elif extra == 'no':
    print(f'su calificacion es {calificacion}')
