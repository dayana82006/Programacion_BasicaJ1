#Números pares en un rango
numInicio=int(input('Digite numero minimo: '))
numFin=int(input('Digite numero maximo: '))
 
if numInicio>numFin:
    print('El numero de inicio no puede mayor que el fin')
else:
    print(f'Numero pares entre {numInicio} y {numFin}')

for i in range(numInicio,numFin+1):
    if i %2==0:
        print(i)