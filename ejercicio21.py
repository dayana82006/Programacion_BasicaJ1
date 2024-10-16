#este programa calcula el costo de estacionamiento basado en el número de horas, con tarifas progresivas.

#se piden los datos al usuario
cantidadH=int(input(' Ingrese la cantidad de horas que deja el\n vehiculo estacionado: '))
precioh=5

if cantidadH==1:
  print(f'El precio es ${precioh}')
elif cantidadH>1 and cantidadH<5:
  precio= 4* cantidadH
  print(f'el precio es ${precio}')
else:
  precio=3* cantidadH 
  print(f'el precio es ${precio}') 