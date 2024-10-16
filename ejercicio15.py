#este programa calcula el salario neto

#pedimos los datos al usuario
salario=int(input('Escriba su salario en Bruto: '))
pais=str(input('Escriba su pais A (Argentina ), B ( Brasil ), C ( Canada ), D (Dinamarca ):  '))


if pais == 'A':
     total= (salario * 20)/100
     print(f'su salario neto es: {total}')
elif pais== 'B':
     total= (salario * 15)/100
     print(f'Su salario neto es: {total}')
elif pais== 'C':
     total=(salario*10)/100
     print(f'su salario neto es: {total}')
else:
     total=(salario*25)/100
     print(f'Su salario neto es: {total}')
