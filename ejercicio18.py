


#Este programa calcula los creditos de un estudiante segun las materias aprobadas

#pedimos los datos al usuario
materias = int(input('Ingrese el numero de materia cursadas: '))
creditos = 0

#usamos un for para recorrer la cantidad de materias y verificar si estan aprobadas
for _ in range (materias):
    puntaje = float(input('Digite el puntaje obtenido en la materia: '))

    if puntaje >= 60:
        creditos += 3 

print(f'El total de creditos son: {creditos}')