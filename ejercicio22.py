#este programa clasisifica los triangulos en agudo, obtuso o rectángulo según sus ángulos internos

#pedimos los datos al usuario
a1=float(input(' Ingrese el primer angulo: '))
a2=float(input('Ingrese angulo dos: '))
a3=float(input(' Ingrese angulo tres: '))
suma=a1+a2+a3 

#usamos condicional if para clasificar que triangulo es 

if suma!=180:
    print('ingrese los angulos correctos')

elif a1==90 or a2==90 or a3 == 90:
    print('Es un triangulo rectangulo')

elif a1> 90 or a2> 90 or a3> 90 :
    print('El triangulo es Obstuso')
else:
    print('El triangulo es Agudo')   

