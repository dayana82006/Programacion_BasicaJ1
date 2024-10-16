#este programa calcula el tiempo que tarda en llegar un automóvil a su destino.

#pedimos los datos al usuario
distancia= int(input('Escriba la distancia que desea recorrer en Km: '))
velocidad=int(input('Escriba la velocidad promedio en Km/h: '))

tiempoH= distancia/velocidad
tiempoM= (distancia/velocidad)*60

if velocidad>120:
    print('Alerta, disminuya la velocidad!!!')
else:
    print(tiempoH)
    print(tiempoM)
