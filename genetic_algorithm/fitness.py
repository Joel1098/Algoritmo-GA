import math
from typing import List


def funcion_aptitud(individuo: List[int], datos_estudiante: dict, datos_materiales: dict, alpha: float, beta: float, sigma: float) -> float:
    
    estilos_aprendizaje = datos_estudiante['alumno']['tipos_aprendizaje']
    temas_estudiante = {tema['id_tema']: tema['nivel'] for tema in datos_estudiante['alumno']['test_inicial']['temas']}

    puntaje_evaluacion = 0
    puntaje_estilos = 0
    
    num_selected = sum(individuo)
    
    
    tema_index = 0
    for modulo in datos_materiales['unidad_aprendizaje']['modulos']:
        for tema in modulo['temas']:
            nivel_estudiante = temas_estudiante.get(tema['id'], 0)

            for recurso in tema['recursos']:
                if tema_index < len(individuo) and individuo[tema_index] == 1:
                    
                    # Cálculo de S_evaluación (basado en la función exponencial)
                    dificultad_material = recurso.get('dificultad', 0)
                    diff = (dificultad_material - nivel_estudiante) / sigma
                    puntaje_evaluacion += math.exp(-diff ** 2)

                    # Cálculo de S_estilos
                    estilos_recurso = recurso.get('tipos_aprendizaje', {})
                    estilos_ordenados = sorted(estilos_recurso.items(), key=lambda x: x[1], reverse=True)
                    estilos_mas_altos = [estilo for estilo, valor in estilos_ordenados[:2]]
                    estilos_coincidentes = sum(1 for estilo in estilos_mas_altos if estilo in estilos_aprendizaje)
                    estilos_preferidos = len(estilos_aprendizaje)
                    puntaje_estilos += estilos_coincidentes / estilos_preferidos if estilos_preferidos > 0 else 0

                tema_index += 1

    # Normalización de S_evaluación
    if num_selected > 0:
        puntaje_evaluacion /= num_selected  # Promedio de evaluación

    # Penalización para evitar selección excesiva de materiales
    penalty = 0.1 * num_selected
    max_resources = 10
    if num_selected > max_resources:
        penalty += 10  

    # Cálculo final de aptitud
    #Debug de funcion objetivo
    # print(f"Evaluacion: {puntaje_evaluacion:.2f} y Estilo: {puntaje_estilos}") 
    fitness_value = (alpha * puntaje_evaluacion + beta * puntaje_estilos - penalty)
    return max(0, fitness_value)
