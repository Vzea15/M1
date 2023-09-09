
#el diccionario para evaluar unas notas de los estudiantes ue son 3 personas
notas_estudiantes = {
    'valentina': [3.0, 4.2, 1.9],
    'juan': [3.5, 1.5, 4.5],
    'manuela': [5.0, 4.6, 2.6]
}



#se crea la funcion de calcular para que notas_total tenga funcionalidad,
# para que ese metodo sum mume todo o tambien se puede hacer con el for
def calcular(notas_total):
    total_notas = sum(notas_total)
    promedio = total_notas / len(notas_total)
    return promedio
     

#se toma un retur para que devuelva la funcion y vuelva a empezar 

for estudiante, notas in notas_estudiantes.items():
    promedio = calcular(notas) 
    # ya se imprime para que muestre y ya 
    print ("las notas de los estudiantes",estudiante, promedio)
    