import random
from typing import Callable, List


def seleccion_torneo(poblacion: List[List[int]], fitness: Callable[[List[int]], float], tam_torneo: int) -> List[int]:
    tam_torneo = min(tam_torneo, len(poblacion))
    seleccion = random.sample(poblacion, tam_torneo)
    seleccion.sort(key=lambda x: fitness(x), reverse=True)
    return seleccion[0]