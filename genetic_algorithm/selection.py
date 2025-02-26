import random
from typing import Callable, List


def seleccion_torneo(poblacion: List[List[int]], fitness: Callable[[List[int]], float], tam_torneo: int, elitismo: int = 2) -> List[int]:
    """
    Selección de torneo con elitismo: Mantiene los mejores individuos y elige el resto con torneo.
    """
    tam_torneo = min(tam_torneo, len(poblacion))
    seleccionados = sorted(poblacion, key=fitness, reverse=True)[:elitismo]  # Mantiene los mejores individuos

    while len(seleccionados) < len(poblacion):
        torneo = random.sample(poblacion, tam_torneo)
        mejor = max(torneo, key=fitness)
        seleccionados.append(mejor)

    #Depuración: Asegurar que cada individuo es una lista de `0s` y `1s`, no una lista de listas
    """if any(isinstance(individuo[0], list) for individuo in seleccionados):
        print(f"Error en selección de torneo: Devolviendo una lista de listas {seleccionados}")
        raise ValueError(f"Selección de torneo inválida: {seleccionados}")
    """
    return random.choice(seleccionados)  #Retorna solo un individuo (lista de `0s` y `1s`)
