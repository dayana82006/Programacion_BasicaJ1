#Contador de vocales en una cadena
vocales = 'aeiou'
cadena =str(input('Escriba un texto para contar sus vocales: '))
totalV=int(0)
for i in cadena:
    if i in vocales:
        totalV +=1
print(f'Se encontraron {totalV} vocales texto')