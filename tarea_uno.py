#tarea 1 
#campos victor

conjuntoA = {1,2,3,4,5}
conjuntoB = {1,2,7,8,0,9}

union = conjuntoA | conjuntoB
print(union)

intereseccion = conjuntoA & conjuntoB
print(intereseccion)

diferencia_simetrerica= conjuntoA.symmetric_difference(conjuntoB) 
print(diferencia_simetrerica)

esSubConjunto= conjuntoA.issubset(conjuntoB)
print(esSubConjunto)

longitud= len(conjuntoA)
print(longitud)