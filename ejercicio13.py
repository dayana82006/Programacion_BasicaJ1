#este ejercicio compara 3 numeros 

#pedimos los datos al usuario
num1= int(input('digite el primer digito a comparar: '))
num2=int(input('digite el segundo numero a comparar diferente: '))
num3=int(input('ditige el tercer numero a comparar diferente: '))

if num1>num2 and num2>num3:
    print (f'El numero mayor {num1}')
elif num2>num1 and num1>num3:
    print(f'El numero mayor es {num2}')
elif num3>num2 and num2>num1:
    print(f'EL numero mayor es {num3}')
else:
        print('Es un error')