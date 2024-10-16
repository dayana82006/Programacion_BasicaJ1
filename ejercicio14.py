#este programa es una adivinanza de letras

letra='D'
#.upper( convierte todas las letras en mayuscula)
#pedimos los datos al usuario
letraU=input('Adivina que letra tengo, escribe la que creas correcta, solo juegan letras en mayuscula: ').upper()
 
if letraU==letra:
    print('la letra es correcta')
else:
    print('La letra es incorrecta')