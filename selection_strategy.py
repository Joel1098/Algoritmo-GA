import random
from typing import List, Tuple


class SelectionStrategy:
    def select(self, population: List[List[int]], fitnesses: List[float]) -> Tuple[List[int], List[int]]:
        raise NotImplementedError

class TournamentSelection(SelectionStrategy):
    def __init__(self, tournament_size: int = 3):
        self.tournament_size = tournament_size

    def select(self, population: List[List[int]], fitnesses: List[float]) -> Tuple[List[int], List[int]]:
        def tournament():
            participants = random.sample(list(zip(population, fitnesses)), self.tournament_size)
            winner = max(participants, key=lambda x: x[1])
            return winner[0]

        return tournament(), tournament()
