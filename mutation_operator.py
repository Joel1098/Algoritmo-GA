import random


def remove_duplicates(individual):
    seen = set()
    unique = []
    for item in individual:
        item_tuple = tuple(item) if isinstance(item, list) else item
        if item_tuple not in seen:
            seen.add(item_tuple)
            unique.append(list(item_tuple) if isinstance(item_tuple, tuple) else item)
    return unique

class MutationOperator:
    def mutate(self, individual, genome_size: int):
        raise NotImplementedError

class BitFlipMutation(MutationOperator):
    def mutate(self, individual, genome_size: int):
        # Asegúrate de que individual sea una lista plana
        individual = [item for sublist in individual for item in sublist] if any(isinstance(g, list) for g in individual) else individual

        
        if random.random() < 0.2:  # Probabilidad de mutación
            idx = random.randint(0, len(individual) - 1)
            individual[idx] = random.randint(0, genome_size - 1)  # Cambiar índice
        return remove_duplicates(individual)



