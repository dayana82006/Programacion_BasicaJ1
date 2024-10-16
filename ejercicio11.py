#programa que convierte grados Celsius a Fahrenheit o Fahrenheit a Celsius 

#pedimos los datos al usuario
temperatura= float(input('Ingrese la temperatura: '))
escala= str(input('Ingrese la escala, F para fahrenheit o C para celsius: '))

match escala:
   case'C': 
    tem_con= (temperatura * 9/5) + 32
    print(f'{temperatura} C° son {tem_con:.2f}F° ')
   case 'F':
    tem_con= (temperatura - 32) * 5/9
    print(f'{temperatura} F° son {tem_con:.2f} C° ')


#:.2f sirve para elegir la cantidad de decimales que se quiere mostrar en el resultado