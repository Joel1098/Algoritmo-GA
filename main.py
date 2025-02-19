# main.py
from genetic_algorithm import (AlgoritmoGenetico, funcion_aptitud, load_data,
                               mutacion_binaria,
                               representacionBinaria_dosPuntos,
                               seleccion_torneo)

# Cargar datos del estudiante y materiales de aprendizaje
datos_estudiante = load_data('./data/alumno.json')
datos_materiales = load_data('./data/unidad_aprendizaje.json')

# Calcular la longitud del cromosoma (número total de recursos)
longitud_individuo = sum(len(tema['recursos']) for modulo in datos_materiales['unidad_aprendizaje']['modulos'] for tema in modulo['temas'])

# Configuraciones ya estandarizadas del algoritmo genético
tasa_mutacion = 0.01  # Tasa de mutación de 0.01
tasa_de_cruza = 0.8  # Tasa de cruza de 0.8
tamano_poblacion = 200
longitud_individuo = 15  # Longitud del cromosoma (asignación de materiales)
generaciones = 100  # Número máximo de generaciones
tam_torneo= 0.5

# Pesos de la función objetivo
alpha = 0.6  # Peso para la evaluación
beta = 0.4  # Peso para los estilos de aprendizaje
sigma = 2

# Inyectamos las dependencias y ejecutamos el algoritmo
algoritmo_genetico = AlgoritmoGenetico(funcion_mutacion=mutacion_binaria, funcion_cruza=representacionBinaria_dosPuntos,
                                       funcion_seleccion=seleccion_torneo, funcion_aptitud=funcion_aptitud,
                                       tasa_mutacion=tasa_mutacion, tasa_de_cruza=tasa_de_cruza,
                                       tamano_poblacion=tamano_poblacion, longitud_individuo=longitud_individuo,
                                       datos_estudiante=datos_estudiante, datos_materiales=datos_materiales, alpha=alpha, beta=beta, sigma=sigma, generaciones_detencion_temprana=10)

mejor_solucion, mejor_aptitud, generacion_detencion = algoritmo_genetico.ejecutar(generaciones)
print(f"Mejor solución encontrada en la generación {generacion_detencion}: {mejor_solucion} con aptitud {mejor_aptitud:.2f}")

# Asignación de materiales
materiales = []
for modulo in datos_materiales['unidad_aprendizaje']['modulos']:
    for tema in modulo['temas']:
        for recurso in tema['recursos']:
            materiales.append({
                "titulo": recurso['nombre'],
                "tipo": recurso['tipo'],
                
            })
            

asignacion = {material["titulo"]: valor for material, valor in zip(materiales, mejor_solucion)}
print("Asignación de materiales:")
for material, valor in asignacion.items():
    if valor == 1:
        tipo_material = next(item["tipo"] for item in materiales if item["titulo"] == material)
        print(f"Material asignado: {material} (Tipo: {tipo_material})")
   