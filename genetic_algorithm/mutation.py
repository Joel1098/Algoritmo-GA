import random
from typing import List


def mutacion_binaria(individual: List[int], tasa_mutacion: float) -> List[int]:
    return [1 - gen if random.random() < tasa_mutacion else gen for gen in individual] # Cambia 0 a 1 y viceversa
