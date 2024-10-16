#Factorial de un número
"""Enunciado:
Escribe un programa que solicite al usuario un número entero positivo n y calcule el factorial de
dicho número ( n! = 1 * 2 * 3 * ... * n ). Usa un ciclo for para realizar el cálculo."""


num=int(input('Escriba el nuemro que desee factoriar: '))
total= int(1)


# Usar un ciclo for inverso para calcular el factorial
for i in range(1,num +1):
  total*=i
  print(f'El factor de {num} es: {total}')