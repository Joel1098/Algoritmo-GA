import random
from typing import List

from crossover_operator import CrossoverOperator
from fitness_function import FitnessFunction
from material import Material
from mutation_operator import MutationOperator
from selection_strategy import SelectionStrategy


class GeneticAlgorithm:
    def __init__(
        self,
        materials: List[Material],
        population_size: int,
        generations: int,
        fitness_function: FitnessFunction,
        selection_strategy: SelectionStrategy,
        crossover_operator: CrossoverOperator,
        mutation_operator: MutationOperator,
    ):
        self.materials = materials
        self.population_size = population_size
        self.generations = generations
        self.fitness_function = fitness_function
        self.selection_strategy = selection_strategy
        self.crossover_operator = crossover_operator
        self.mutation_operator = mutation_operator

    def initialize_population(self) -> List[List[int]]:
        population = [
            random.sample(range(len(self.materials)), 2)  # Selecciona 2 materiales
            for _ in range(self.population_size)
        ]
        print(f"Población inicial: {population}")
        return population 

    def validate_individual(self, individual):
        
        if any(isinstance(gene, list) for gene in individual):
            raise ValueError(f"Genoma contiene sublistas, debe ser una lista plana: {individual}")
        if not all(isinstance(gene, int) for gene in individual):
            raise ValueError(f"Genoma inválido (debe contener solo enteros): {individual}")



        

    def run(self):
        
        population = self.initialize_population()

        for generation in range(self.generations):
            # Validar cada individuo
            for ind in population:
                self.validate_individual(ind)

            fitnesses = [
                self.fitness_function.evaluate(ind, self.materials) for ind in population
            ]

            next_population = []
            for _ in range(self.population_size // 2):
                parent1 = self.selection_strategy.select(population, fitnesses)
                parent2 = self.selection_strategy.select(population, fitnesses)
                child1, child2 = self.crossover_operator.crossover(parent1, parent2)
                
                child1 = [item for sublist in child1 for item in sublist] if any(isinstance(g, list) for g in child1) else child1
                child2 = [item for sublist in child2 for item in sublist] if any(isinstance(g, list) for g in child2) else child2
                
                self.validate_individual(child1)
                self.validate_individual(child2)
                
                next_population.append(self.mutation_operator.mutate(child1, len(self.materials)))
                next_population.append(self.mutation_operator.mutate(child2, len(self.materials)))

            population = next_population

        best_individual = max(
            population,
            key=lambda ind: self.fitness_function.evaluate(ind, self.materials),
        )
        best_fitness = self.fitness_function.evaluate(best_individual, self.materials)
        return best_individual, best_fitness
