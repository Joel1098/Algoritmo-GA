import random
from typing import List


def mutacion_binaria(individual: List[int], tasa_mutacion: float) -> List[int]:
    """
    Aplica mutación binaria asegurando que al menos 1 a 3 genes cambien.
    """

    #Depuración: Verificar si individual es una lista de enteros binarios
    """
    if not isinstance(individual, list):
        raise TypeError(f"Error en mutación: `individual` no es una lista. Recibido: {type(individual)}")

    if not all(isinstance(gen, int) for gen in individual):
        print(f"Tipo de datos dentro de `individual`: {[type(gen) for gen in individual]}")
        raise ValueError(f"Error en la mutación: El individuo no es una lista de enteros. Recibido: {individual}")
    """
    num_genes = len(individual)
    mutado = individual[:]  # Copia del individuo

    #Se asegura que al menos 1 mutación ocurra
    indices_a_mutar = [i for i in range(num_genes) if random.random() < tasa_mutacion]

    
    if len(indices_a_mutar) == 0:  # Si no hay mutaciones, forzar 1 cambio mínimo
        indices_a_mutar = [random.randint(0, num_genes - 1)]

    for idx in indices_a_mutar:
        mutado[idx] = 1 - mutado[idx]  # Invierte 0 ↔ 1

    return mutado
