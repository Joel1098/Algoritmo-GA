# genetic_algorithm/core.py


from typing import Callable, List, Tuple

from .crossover import representacionBinaria_dosPuntos
from .fitness import funcion_aptitud
from .mutation import mutacion_binaria
from .population import generar_poblacion
from .selection import seleccion_torneo


class AlgoritmoGenetico:
    def __init__(self, funcion_mutacion: Callable[[List[int], float], List[int]],
                 funcion_cruza: Callable[[List[int], List[int], float], Tuple[List[int], List[int]]],
                 funcion_seleccion: Callable[[List[List[int]], Callable[[List[int]], float], int], List[int]],
                 funcion_aptitud: Callable[[List[int], dict, dict, float, float], float],
                 tasa_mutacion: float, tasa_de_cruza: float,
                 tamano_poblacion: int, longitud_individuo: int,
                 datos_estudiante: dict, datos_materiales: dict, alpha: float, beta: float, sigma: float,
                 tam_torneo: int = 5, generaciones_detencion_temprana: int = 10):
        self.funcion_mutacion = funcion_mutacion
        self.funcion_cruza = funcion_cruza
        self.funcion_seleccion = funcion_seleccion
        self.funcion_aptitud = funcion_aptitud
        self.tasa_mutacion = tasa_mutacion
        self.tasa_de_cruza = tasa_de_cruza
        self.tamano_poblacion = tamano_poblacion
        self.longitud_individuo = longitud_individuo
        self.datos_estudiante = datos_estudiante
        self.datos_materiales = datos_materiales
        self.alpha = alpha
        self.beta = beta
        self.sigma = sigma
        self.tam_torneo = tam_torneo
        self.generaciones_detencion_temprana = generaciones_detencion_temprana
        
    #Determinar el tamaño del cromosoma dinámicamente basado en los materiales
        self.longitud_individuo = sum(len(tema['recursos']) for modulo in datos_materiales['unidad_aprendizaje']['modulos'] for tema in modulo['temas'])
        print(f"Tamaño del cromosoma: {self.longitud_individuo}")  # ✅ Debug: Verifica la cantidad de genes

    def inicializar_poblacion(self) -> List[List[int]]:
        return generar_poblacion(self.tamano_poblacion, self.datos_materiales)

    def evolucionar(self, poblacion: List[List[int]]) -> List[List[int]]:
        
        nueva_poblacion = []
        while len(nueva_poblacion) < self.tamano_poblacion:
            padre1 = self.funcion_seleccion(poblacion, lambda x: self.funcion_aptitud(x, self.datos_estudiante, self.datos_materiales, self.alpha, self.beta, self.sigma), self.tam_torneo)
            padre2 = self.funcion_seleccion(poblacion, lambda x: self.funcion_aptitud(x, self.datos_estudiante, self.datos_materiales, self.alpha, self.beta, self.sigma), self.tam_torneo)


            hijo1, hijo2 = self.funcion_cruza(padre1, padre2, self.tasa_de_cruza)

            hijo1 = self.funcion_mutacion(hijo1, self.tasa_mutacion)
            hijo2 = self.funcion_mutacion(hijo2, self.tasa_mutacion)

            hijo1 = hijo1[:self.longitud_individuo]
            hijo2 = hijo2[:self.longitud_individuo]

            nueva_poblacion.extend([hijo1, hijo2])

        return nueva_poblacion[:self.tamano_poblacion]

    def ejecutar(self, generaciones: int) -> Tuple[List[int], float, int]:
        poblacion = self.inicializar_poblacion()
        mejor_individuo = None
        mejor_aptitud = -float('inf')
        contador_sin_mejora = 0
        
        for generacion in range(generaciones):
            poblacion = self.evolucionar(poblacion)
            individuo_actual_mejor = max(poblacion, key=lambda x: self.funcion_aptitud(x, self.datos_estudiante, self.datos_materiales, self.alpha, self.beta, self.sigma))
            aptitud_actual_mejor = self.funcion_aptitud(individuo_actual_mejor, self.datos_estudiante, self.datos_materiales, self.alpha, self.beta, self.sigma)
            
            if aptitud_actual_mejor > mejor_aptitud:
                mejor_individuo = individuo_actual_mejor
                mejor_aptitud = aptitud_actual_mejor
                contador_sin_mejora = 0
            else:
                contador_sin_mejora += 1
            print(f"Generación {generacion + 1} : Mejor aptitud {mejor_aptitud:.2f}")
            if contador_sin_mejora >= self.generaciones_detencion_temprana:
                print(f"Deteniendo temprano en la generación {generacion + 1} (sin mejora en {self.generaciones_detencion_temprana} generaciones).")
                break
        return mejor_individuo, mejor_aptitud, generacion + 1
