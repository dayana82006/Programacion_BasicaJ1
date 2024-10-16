
#este programa nos da los dias de la semana segun numero del 1 al 7

#pedimos los datos al usuario
numero= int(input('Digite un numero del 1 al 7 para saber el dia de la semana; '))

if numero>7:
    print('Elija un numero correcto')
    
elif numero == 0:
    print('Elija un numero correcto')
else: 
 match numero:
    case 1:
      print('el dia es lunes')
    case 2:
        print('el dia es Martes')
    case 3:
        print('el dia es miercoles')
    case 4:
        print('el dia es jueves')
    case 5:
        print('el dia es viernes')
    case 6:
        print('el dia es sabado')
    case 7:
        print('el dia es domingo')
