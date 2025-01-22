import random
from typing import List, Tuple


class CrossoverOperator:
    def crossover(self, parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
        raise NotImplementedError

class SinglePointCrossover(CrossoverOperator):
    def crossover(self, parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
        point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        

        # Asegúrate de devolver listas planas
        return list(child1), list(child2)


