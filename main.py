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
print(f'Longitud de individuo calculada: {longitud_individuo:.2f}')
# Configuraciones ya estandarizadas del algoritmo genético
tasa_mutacion = 0.01  # Tasa de mutación de 0.01
tasa_de_cruza = 0.8  # Tasa de cruza de 0.8
tamano_poblacion = 50

generaciones = 100  # Número máximo de generaciones
tam_torneo= 5

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
asignacion = []

tema_index = 0
for modulo in datos_materiales['unidad_aprendizaje']['modulos']:
    for tema in modulo['temas']:
        print(f"\nTema: {tema['nombre']}")  # para ver qué tema se está procesando
        
        materiales_tema = []
        for recurso in tema['recursos']:
            if tema_index < len(mejor_solucion) and mejor_solucion[tema_index] == 1:
                materiales_tema.append({
                    "titulo": recurso['nombre'],
                    "tipo": recurso['tipo']
                })
            tema_index += 1

        if materiales_tema:
            print(f"Materiales asignados:")
            for mat in materiales_tema:
                print(f"    - {mat['titulo']} ({mat['tipo']})")
            asignacion.append({tema["nombre"]: materiales_tema})
        else:
            print(f"Sin materiales asignados para este tema.")
   