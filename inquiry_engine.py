# inquiry_engine.py

import openai
import os

# Asegúrate de tener tu clave de OpenAI en una variable de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_subquestions(user_question, n_subquestions=3):
    """
    Genera un conjunto de subpreguntas jerárquicas a partir de una pregunta central.

    Args:
        user_question (str): Pregunta principal del usuario.
        n_subquestions (int): Número de subpreguntas a generar.

    Returns:
        list: Lista de subpreguntas generadas.
    """
    prompt = (
        f"Dada la siguiente pregunta central:\n\n"
        f"\"{user_question}\"\n\n"
        f"Genera {n_subquestions} subpreguntas jerárquicamente relevantes "
        f"que permitan explorar el tema en profundidad.\n"
        f"Las subpreguntas deben ser diversas y tocar distintos aspectos del problema (conceptuales, metodológicos, éticos, etc.).\n\n"
        f"Subpreguntas:"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Puedes usar "gpt-3.5-turbo" si es necesario
            messages=[
                {"role": "system", "content": "Eres un asistente experto en generar redes de preguntas para investigación científica."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )

        # Extraer texto y dividir por saltos de línea
        output_text = response['choices'][0]['message']['content']
        subquestions = [line.strip("- ").strip() for line in output_text.split("\n") if line.strip()]
        return subquestions[:n_subquestions]

    except Exception as e:
        print(f"Error generando subpreguntas: {e}")
        return ["¿Subpregunta 1?", "¿Subpregunta 2?", "¿Subpregunta 3?"]

