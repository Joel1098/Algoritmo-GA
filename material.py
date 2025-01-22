class Material:
    def __init__(self, id, nombre, descripcion, material_type, difficulty, evaluacion, estilos):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.material_type = material_type
        self.difficulty = difficulty
        self.evaluacion = evaluacion
        self.estilos = estilos

    def classify_for_vark(self):
        """Clasificar material según el estilo de aprendizaje más relevante."""
        dominant_style = max(self.estilos, key=self.estilos.get)
        return f"Material clasificado como relevante para {dominant_style}"

    def __repr__(self):
        classification = self.classify_for_vark()
        return f"ID: {self.id}, Nombre: {self.nombre}, Tipo: {self.material_type}, Dificultad: {self.difficulty}, Eval: {self.evaluacion}, {classification}, Descripción: {self.descripcion}"
