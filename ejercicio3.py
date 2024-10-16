#este programa es una calculadora 

#pedimos los datos al usuario
num1=float(input("Digite un numero: ")) 
num2=float(input("Digite el segundo numero: ")) 
operacion=input("Elija la operación + Suma/n, - Resta/n  , * Multiplicacion/n, / Division ") 


match operacion:
    case "+":
        print(f'el resultado es: {num1+num2}')
    case "-":
        print(f'el resultado es: {num1-num2}')
    case"*":
        print(f'el resultado es: {num1*num2}')

    case "/":
        if num2 == 0:
         print('No se puede dividir por cero, elige otro número')
        else: print(f'el resultado es: {num1/num2}')
     

