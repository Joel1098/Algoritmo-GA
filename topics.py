import random

from material import Material


def generate_topics(preferred_styles=None):
    if preferred_styles is None:
        preferred_styles = []  # Valor predeterminado si no se pasa nada

    topics = {}
    material_types = ["PDF", "Video", "Texto", "Audio", "Práctico"]
    difficulties = ["Bajo", "Medio", "Alto"]

    # Lógica para asignar estilos según el tipo de material
    style_mapping = {
        "PDF": {"Visual": 0.6, "Auditivo": 0.1, "Lectura/Escritura": 0.8, "Kinestésico": 0.2},
        "Video": {"Visual": 0.9, "Auditivo": 0.7, "Lectura/Escritura": 0.3, "Kinestésico": 0.4},
        "Texto": {"Visual": 0.5, "Auditivo": 0.1, "Lectura/Escritura": 1.0, "Kinestésico": 0.2},
        "Audio": {"Visual": 0.2, "Auditivo": 1.0, "Lectura/Escritura": 0.1, "Kinestésico": 0.3},
        "Práctico": {"Visual": 0.4, "Auditivo": 0.2, "Lectura/Escritura": 0.3, "Kinestésico": 1.0},
    }

    for topic_id in range(1, 7):  # Generar 6 temas
        materials = []
        for _ in range(4):  # Cada tema tiene 4 materiales
            material_type = random.choice(material_types)
            materials.append(
                Material(
                    material_type=material_type,
                    difficulty=random.choice(difficulties),
                    evaluacion=random.uniform(0.5, 1.0),
                    estilos=style_mapping[material_type],  # Asigna estilos basados en el tipo
                )
            )
        topics[f"Tema {topic_id}"] = materials

    return topics
