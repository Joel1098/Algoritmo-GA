from typing import List

from material import Material


class FitnessFunction:
    def __init__(self, alpha: float, beta: float, preferred_styles: List[str], preferred_difficulty: str):
        self.alpha = alpha
        self.beta = beta
        self.preferred_styles = preferred_styles
        self.preferred_difficulty = preferred_difficulty

    def evaluate(self, individual: List[int], materials: List[Material]) -> float:
        # Suma ponderada de evaluación y estilos
        S_evaluacion = sum(materials[i].evaluacion for i in individual)
        S_estilos = sum(
            sum(materials[i].estilos[style] for style in self.preferred_styles)
            for i in individual
        )

        # Bonus por dificultad adecuada
        difficulty_bonus = sum(
            0.2 if materials[i].difficulty == self.preferred_difficulty else 0
            for i in individual
        )

        return self.alpha * S_evaluacion + self.beta * S_estilos + difficulty_bonus
