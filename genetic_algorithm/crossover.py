import random
from typing import List, Tuple


def representacionBinaria_dosPuntos(padre1: List[int], padre2: List[int], tasadeCruza: float) -> Tuple[List[int], List[int]]:
    """
    Realiza cruce en dos puntos asegurando que el resultado es una lista de enteros binarios.
    """

    #Realizar la cruza si se cumple la tasa de cruza
    if random.random() < tasadeCruza:
        tam_cromosoma = len(padre1)
        punto1 = random.randint(1, tam_cromosoma // 2)
        punto2 = random.randint(punto1 + 1, tam_cromosoma - 1)

        hijo1 = padre1[:punto1] + padre2[punto1:punto2] + padre1[punto2:]
        hijo2 = padre2[:punto1] + padre1[punto1:punto2] + padre2[punto2:]

        #Verificar que los hijos sean listas de enteros binarios
        if not all(isinstance(gen, int) and gen in [0, 1] for gen in hijo1 + hijo2):
            print(f"Error en cruce: Hijos generados no son enteros. Recibido: {hijo1}, {hijo2}")
            raise ValueError(f"Error en cruce: Hijos inválidos {hijo1} y {hijo2}")

        return hijo1, hijo2

    return padre1, padre2
