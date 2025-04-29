# inquiry_engine.py

import openai
import os
from dotenv import load_dotenv
import streamlit as st

# Cargar la clave API desde entorno
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_subquestions(user_question, n_subquestions=3):
    """
    Genera subpreguntas jerárquicas a partir de una pregunta central.
    """
    prompt = (
        f"Dada la siguiente pregunta central:\n\n"
        f"\"{user_question}\"\n\n"
        f"Genera {n_subquestions} subpreguntas jerárquicamente relevantes "
        f"que permitan explorar el tema en profundidad.\n"
        f"Subpreguntas:"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Cambia a "gpt-4o" si tienes acceso
            messages=[
                {"role": "system", "content": "Eres un asistente experto en generar preguntas epistémicas jerárquicas."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )

        output_text = response.choices[0].message.content
        subquestions = [line.strip("- ").strip() for line in output_text.split("\n") if line.strip()]
        return subquestions[:n_subquestions]

    except Exception as e:
        st.error(f"Error generando subpreguntas: {e}")
        return ["¿Subpregunta 1?", "¿Subpregunta 2?", "¿Subpregunta 3?"]
