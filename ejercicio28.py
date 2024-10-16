#Suma de números pares hasta que se introduceun impar

#pedimos los datos al usuario
Active=True
suma=0
#usamos while para pedir el numero repetidas veces verificanco que si es par,
#o sino dar resultado de suma y romper el while
while Active:

   n1=int(input('Digite el numero que desee sumar: '))
   
   if n1 %2==0:
    suma = suma + n1

       
   else :
    Active= False
    print(f'La suma total fue {suma}')
