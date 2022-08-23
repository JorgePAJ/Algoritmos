def validActivities(activities):
    # Declaras un indice para recorrer el arreglo
    idx = 0

    # Declaras un set para guardar las actividades que ya se han agregado
    res = set()
    # Agregamos 0 por la primera actividad
    if len(activities):
        res.add(0)

    # Ordenamos el arreglo dependiendo su hora de finalizacion
    activities.sort(key=lambda x: x[1])

    # Recorremos el arreglo desde la segunda actividad
    # Si la hora de inicio de i es mayor o igual a la hora
    # de finalizacion de la actividad anterior, entonces
    # agregamos la actividad i al set y movemos el indice a i

    for i in range(1, len(activities)):
        if activities[i][0] >= activities[idx][1]:
            res.add(i)
            idx = i

    return res


activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9),
              (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]

# Llamamos la funcion que nos devolvera un set con los indices de
# las actividades que se pueden realizar en el tiempo
result = validActivities(activities)

# Imprimimos los valores del array base a los valores guardados en el set
print([activities[i] for i in result])
