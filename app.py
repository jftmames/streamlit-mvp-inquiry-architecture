# app.py

import streamlit as st
from inquiry_engine import generate_subquestions
from epistemic_navigator import display_navigation
from contextual_generator import generate_contextual_response
from adaptive_dialogue import adaptive_dialogue_flow
from reasoning_tracker import ReasoningTracker

# Inicializar Reasoning Tracker
tracker = ReasoningTracker()

st.set_page_config(page_title="Arquitectura Cognitiva - Complejos de Indagación", layout="wide")
st.title("Arquitectura Cognitiva para Modelos de Lenguaje Generativo")
st.subheader("Navegación basada en Complejos de Indagación Jerárquicos")

# Input principal del usuario
user_question = st.text_input("Introduce tu pregunta central:")

if user_question:
    # Generar subpreguntas
    subquestions = generate_subquestions(user_question)
    st.write("### Subpreguntas generadas:")
    for idx, subq in enumerate(subquestions):
        st.write(f"{idx+1}. {subq}")
    
    # Mostrar navegación
    st.write("### Mapa de Indagación:")
    display_navigation(user_question, subquestions)
    
    # Elegir una subpregunta para profundizar
    selected_idx = st.selectbox("Selecciona una subpregunta para explorar:", range(len(subquestions)))
    
    if st.button("Explorar"):
        selected_question = subquestions[selected_idx]
        contextual_response = generate_contextual_response(selected_question)
        
        st.write("### Respuesta reflexiva:")
        st.write(contextual_response)
        
        # Registrar el razonamiento
        tracker.add_entry(user_question, selected_question, contextual_response)
        
        # Permitir diálogo adaptativo
        adaptive_dialogue_flow(selected_question, tracker)

# Exportar razonamiento
if st.button("Exportar razonamiento"):
    tracker.export()
    st.success("¡Razonamiento exportado exitosamente!")

