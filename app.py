# app.py

import streamlit as st
from inquiry_engine import generate_subquestions
from epistemic_navigator import display_navigation
from contextual_generator import generate_contextual_response
from adaptive_dialogue import adaptive_dialogue_flow
from reasoning_tracker import ReasoningTracker

# Configurar página
st.set_page_config(page_title="Arquitectura Cognitiva - Complejos de Indagación", layout="wide")
st.title("Arquitectura Cognitiva para Modelos de Lenguaje Generativo")
st.subheader("Explora un dominio epistémico mediante complejos de indagación jerárquicos")

# Inicializar Reasoning Tracker en session_state
if "tracker" not in st.session_state:
    st.session_state.tracker = ReasoningTracker()

# Entrada del usuario
user_question = st.text_input("Introduce tu pregunta central:")

if user_question:
    # Generar subpreguntas
    subquestions = generate_subquestions(user_question)

    st.write("### Subpreguntas generadas:")
    for idx, subq in enumerate(subquestions):
        st.write(f"{idx+1}. {subq}")

    # Visualizar mapa de indagación
    st.write("### Mapa de Indagación:")
    display_navigation(user_question, subquestions)

    # Selección de subpregunta
    selected_idx = st.selectbox("Selecciona una subpregunta para explorar más a fondo:", range(len(subquestions)))

    # Ejecutar al pulsar el botón
    if st.button("Explorar Subpregunta"):
        selected_question = subquestions[selected_idx]
        st.write("### Subpregunta seleccionada:")
        st.info(selected_question)

        # Diálogo adaptativo (refinamientos)
        adaptive_dialogue_flow(selected_question)

        # Generar respuesta reflexiva
        st.write("### Respuesta reflexiva generada:")
        contextual_response = generate_contextual_response(selected_question)
        st.write(contextual_response)

        # Registrar razonamiento
        st.session_state.tracker.add_entry(
            user_question=user_question,
            subquestion=selected_question,
            response=contextual_response
        )
        st.success("Entrada registrada en el historial.")

    # Mostrar historial y exportar
    st.markdown("---")
    st.subheader("Opciones de Historial de Razonamiento")

    if st.button("Mostrar historial de razonamiento"):
        st.session_state.tracker.show_history()

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Exportar historial como JSON"):
            st.session_state.tracker.export_to_json()
    with col2:
        if st.button("Exportar historial como CSV"):
            st.session_state.tracker.export_to_csv()
