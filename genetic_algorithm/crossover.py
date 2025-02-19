import random
from typing import List, Tuple


def representacionBinaria_dosPuntos(padre1: List[int], padre2: List[int], tasadeCruza: float) -> Tuple[List[int]]:
    if random.random() < tasadeCruza:
        punto1 = random.randint(0, len(padre1) -2)
        punto2 = random.randint(punto1 + 1, len(padre1) -1)
        hijo1 = padre1[:punto1] + padre2[punto1:punto2] + padre1[punto2:]
        hijo2 = padre2[:punto1] + padre1[punto1:punto2] + padre1[punto2:]
        
        return hijo1, hijo2
    return padre1, padre2