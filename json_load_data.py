import json

from material import Material


def assign_styles(material_type):
    """Asigna relevancia VARK según el tipo de material."""
    style_mapping = {
        "PDF": {"Visual": 0.6, "Auditivo": 0.1, "Lectura/Escritura": 0.8, "Kinestésico": 0.2},
        "Video": {"Visual": 0.9, "Auditivo": 0.7, "Lectura/Escritura": 0.3, "Kinestésico": 0.4},
        "Texto": {"Visual": 0.5, "Auditivo": 0.1, "Lectura/Escritura": 1.0, "Kinestésico": 0.2},
        "Audio": {"Visual": 0.2, "Auditivo": 1.0, "Lectura/Escritura": 0.1, "Kinestésico": 0.3},
        "Práctico": {"Visual": 0.4, "Auditivo": 0.2, "Lectura/Escritura": 0.3, "Kinestésico": 1.0},
    }
    return style_mapping.get(material_type, {})  # Devuelve un dict vacío si el tipo no coincide


def load_json_data(file_path):
    """Carga los datos desde un archivo JSON y los convierte en materiales, temas y módulos."""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Extraer la información de la unidad de aprendizaje
    unidad_aprendizaje = {
        "id": data["unidad"]["id"],
        "nombre": data["unidad"]["nombre"],
        "descripcion": data["unidad"]["descripcion"],
    }

    modulos = []
    for modulo in data["modulos"]:
        temas = []
        for tema in modulo["temas"]:
            materials = [
                Material(
                    id=material["id"],
                    nombre=material["nombre"],
                    descripcion=material["descripcion"],
                    material_type=material["tipo"],
                    difficulty=material["dificultad"],
                    evaluacion=material["evaluacion"],
                    estilos=assign_styles(material["tipo"])  # Asigna estilos según el tipo de material
                )
                for material in tema["materiales"]
            ]
            temas.append({
                "id": tema["id"],
                "nombre": tema["nombre"],
                "descripcion": tema["descripcion"],
                "materiales": materials
            })
        modulos.append({
            "id": modulo["id"],
            "nombre": modulo["nombre"],
            "descripcion": modulo["descripcion"],
            "temas": temas
        })

    return unidad_aprendizaje, modulos
