import os

from crossover_operator import SinglePointCrossover
from fitness_function import FitnessFunction
from genetic_algorithm import GeneticAlgorithm
from json_load_data import load_json_data
from mutation_operator import BitFlipMutation
from selection_strategy import TournamentSelection
from student_profile import get_student_profile
from topics import generate_topics


def adjust_weights(approval_rate: float):
    # Ajustar pesos dinámicamente
    if approval_rate > 0.8:  # Buen rendimiento
        alpha = 0.6
        beta = 0.4
    elif approval_rate > 0.6:  # Rendimiento medio
        alpha = 0.5
        beta = 0.5
    else:  # Bajo rendimiento
        alpha = 0.4
        beta = 0.6
    return alpha, beta

def filter_materials_by_styles(materials, preferred_styles):
    """Filtra materiales relevantes para los dos estilos predominantes."""
    filtered_materials = []
    for material in materials:
        is_relevant = any(
            style in material.estilos and material.estilos[style] > 0.5
            for style in preferred_styles
        )
        print(f"Material: {material} - Relevante: {is_relevant}")
        if is_relevant:
            filtered_materials.append(material)
    return filtered_materials


def select_materials_per_topic(topics, preferred_styles, student_performance, approval_rate):
    alpha, beta = adjust_weights(approval_rate)
    selected_materials = {}

    for topic, materials in topics.items():
        print(f"\nMateriales originales en {topic}:")
        for i, material in enumerate(materials):
            print(f"Material {i}: {material}")

        # Filtrar materiales según los estilos más predominantes
        filtered_materials = filter_materials_by_styles(materials, preferred_styles)
        if not filtered_materials:
            print(f"No se encontraron materiales relevantes para los estilos: {preferred_styles}")
            continue

        print(f"\nMateriales filtrados en {topic}:")
        for i, material in enumerate(filtered_materials):
            print(f"Material {i}: {material}")

        # Configurar dependencias para el tema
        fitness_function = FitnessFunction(
            alpha=alpha, beta=beta, preferred_styles=preferred_styles, preferred_difficulty=student_performance
        )
        selection_strategy = TournamentSelection(tournament_size=2)
        crossover_operator = SinglePointCrossover()
        mutation_operator = BitFlipMutation()

        # Ejecutar algoritmo genético para el tema
        ga = GeneticAlgorithm(
            materials=filtered_materials,  # Pasar solo los materiales filtrados
            population_size=10,
            generations=30,
            fitness_function=fitness_function,
            selection_strategy=selection_strategy,
            crossover_operator=crossover_operator,
            mutation_operator=mutation_operator,
        )
        best_individual, best_fitness = ga.run()

        selected_materials[topic] = [materials[i] for i in best_individual]
        print(f"\nMateriales seleccionados para {topic}:")
        for material in selected_materials[topic]:
            print(material)
        print(f"Fitness del mejor individuo: {best_fitness}")

    return selected_materials

if __name__ == "__main__":
    
    # Obtener el perfil del estudiante
    preferred_styles, approval_rate = get_student_profile()
    print(f"Estilos de aprendizaje predominantes: {preferred_styles}")
    print(f"Porcentaje de aprobación: {approval_rate}")

    # Ruta del archivo JSON
    json_path = "unidad_aprendizaje.json"
    
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"El archivo no fue encontrado: {json_path}")

    # Cargar datos desde el JSON
    unidad_aprendizaje, modulos = load_json_data(json_path)

    # Mostrar la información de la unidad de aprendizaje
    print(f"\nUnidad de Aprendizaje: {unidad_aprendizaje['nombre']}")
    print(f"Descripción: {unidad_aprendizaje['descripcion']}")

    for modulo in modulos:
        print(f"\nMódulo: {modulo['nombre']}")
        print(f"Descripción: {modulo['descripcion']}")

        for tema in modulo["temas"]:
            print(f"\nTema: {tema['nombre']}")
            print(f"Descripción: {tema['descripcion']}")

            print("Materiales:")
            for material in tema["materiales"]:
                print(material)

    # Seleccionar materiales relevantes
    for modulo in modulos:
        for tema in modulo["temas"]:
            print(f"\nSeleccionando materiales para el tema: {tema['nombre']}")
            selected_materials = select_materials_per_topic(
                {tema["nombre"]: tema["materiales"]},
                preferred_styles,
                "Medio",  # Dificultad preferida
                approval_rate
            )
            print("\nMateriales seleccionados:")
            for topic_name, materials in selected_materials.items():
                print(f"Tema: {topic_name}")
                for material in materials:
                    print(material)
