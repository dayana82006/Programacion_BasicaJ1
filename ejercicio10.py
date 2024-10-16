#Este programa asigna una clasificacion basada en una nota numerica

#pedimos los datos al usuario
nota= int(input('Escribe la nota para saber su clasificación en la escala del 1 a 100:  '))

if nota<60:
    print ('su estado es F')
elif nota >= 60 and nota < 70:
    print('Su estado es D')
elif nota >= 70 and nota <80:
    print('su estado es C')
elif nota >=80 and nota <90:
    print('Su estado es B')
elif nota>100:
    print('Elija una nota correcta')
else:
 print('su nota es A')
 