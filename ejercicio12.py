#este programa calcula su IMC

#pedimos los datos al usuario
peso=int(input('Ingrese su peso en kilogramos: '))
altura=float(input('Ingrese su altura en en metros: '))

IMC=float(peso/altura**2)
print(f'Su IMC es {IMC:.2f}')

if IMC < 18.5:
    print('Usted esta bajo peso')
elif IMC >=18.5 and IMC <24.9:
    print('Usted tiene un peso normal')
elif IMC>=24 and IMC <30:
    print('Usted esta en sobre peso')
else:
     print('Usted tiene obesidad')