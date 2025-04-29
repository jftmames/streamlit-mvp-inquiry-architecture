# contextual_generator.py

import openai
import os
from dotenv import load_dotenv
import streamlit as st

# Cargar clave API desde entorno
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_contextual_response(subquestion):
    """
    Genera una respuesta reflexiva adaptada a una subpregunta.
    """
    prompt = (
        f"Responde de manera reflexiva y estructurada a la siguiente subpregunta:\n\n"
        f"\"{subquestion}\"\n\n"
        f"La respuesta debe incluir:\n"
        f"- Una explicación conceptual breve.\n"
        f"- Un análisis crítico con opciones o enfoques posibles.\n"
        f"- Consideraciones éticas o metodológicas relevantes.\n"
        f"Usa un estilo claro, objetivo y profesional."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # o "gpt-4o" si tu clave lo permite
            messages=[
                {"role": "system", "content": "Eres un asistente experto en razonamiento crítico y reflexivo."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        return response.choices[0].message.content

    except Exception as e:
        st.error(f"Error generando respuesta contextual: {e}")
        return "No se pudo generar una respuesta en este momento."
