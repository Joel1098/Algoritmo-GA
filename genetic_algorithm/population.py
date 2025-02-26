import random
from typing import List


def generar_poblacion(size: int, datos_materiales: dict) -> List[List[int]]:
    """
    Genera una población inicial con individuos representados por listas de `0s` y `1s`.
    """
    tam_cromosoma = sum(len(tema['recursos']) for modulo in datos_materiales['unidad_aprendizaje']['modulos'] for tema in modulo['temas'])
    poblacion = []
    
    for _ in range(size):
        individuo = [0] * tam_cromosoma  #Crea una lista plana
        select_indices = random.sample(range(tam_cromosoma), min(5, tam_cromosoma))  # Garantiza selección de al menos 5 materiales
        for idx in select_indices:
            individuo[idx] = 1
        poblacion.append(individuo)

        #Depuración: Asegurar que `individuo` es una lista plana de `0s` y `1s`
        if isinstance(individuo[0], list):
            print(f"Error en generación de población: Individuo inválido {individuo}")
            raise ValueError(f"Individuo inválido en generación: {individuo}")

    return poblacion
