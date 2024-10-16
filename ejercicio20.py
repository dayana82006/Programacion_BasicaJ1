#Este programa que convierte una calificación numérica en una letra de acuerdo a un sistema de calificación específico

#pedimos los datos al usuario
calificacion=int(input('Ingrese la calificacion de 0 a 100 para convertir en letra: '))

#usamos match para exponer los casos
match calificacion:
 
  case calificacion if calificacion>=0 and calificacion<60:
    print('La letra que corresponde es F')
  case calificacion if calificacion>=60 and calificacion<70:
    print('La letra que corresponde es D')
  case calificacion if calificacion>=70 and calificacion<80:
    print('La letra que corresponde es C')
  case calificacion if calificacion>=80 and calificacion<90:
    print('La letra que corresponde es B')
  case calificacion if calificacion>=90 and calificacion<100:
    print('La letra que corresponde es A')
  case _:
    print('error indefinido')


    