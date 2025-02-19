import random
from typing import List


def generar_poblacion(size: int, tam_cromosoma: int)-> List[List[int]]:
    poblacion = []
    
    for i in range(size):
        individuo = [0] * tam_cromosoma
        
        select_indices = random.sample(range(tam_cromosoma), 5)
        for idx in select_indices:
            individuo[idx] = 1
        poblacion.append(individuo)
    return poblacion