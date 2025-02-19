# genetic_algorithm/__init__.py
#importacion de archivos 

from .core import AlgoritmoGenetico
from .crossover import representacionBinaria_dosPuntos
from .data import load_data
from .fitness import funcion_aptitud
from .mutation import mutacion_binaria
from .population import generar_poblacion
from .selection import seleccion_torneo
