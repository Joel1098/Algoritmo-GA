import random


def simulate_vark_test():
    """Simular un test VARK y devolver los puntajes."""
    vark_scores = {
        "Visual": random.randint(5, 15),
        "Auditivo": random.randint(5, 15),
        "Lectura/Escritura": random.randint(5, 15),
        "Kinestésico": random.randint(5, 15),
    }
    return vark_scores

def get_preferred_styles(vark_scores):
    # Selecciona los 2 estilos más altos
    return sorted(vark_scores, key=vark_scores.get, reverse=True)[:2]

def calculate_approval_rate():
    """Simular porcentaje de aprobación en un test."""
    total_questions = 10
    correct_answers = random.randint(2, 10)  # Aciertos aleatorios entre 50% y 100%
    return correct_answers / total_questions

def get_student_profile():
    vark_scores = simulate_vark_test()
    preferred_styles = get_preferred_styles(vark_scores)
    approval_rate = calculate_approval_rate()
    return preferred_styles, approval_rate
