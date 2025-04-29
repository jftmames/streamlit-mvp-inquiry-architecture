# Arquitectura Cognitiva para Modelos de Lenguaje Generativo

Este proyecto implementa un MVP funcional de una arquitectura cognitiva basada en **complejos de indagación jerárquicos**, diseñada para enriquecer el funcionamiento de modelos de lenguaje generativo (LLMs) con capacidades deliberativas, explicativas y trazables.

## 🔍 Funcionalidad

- Entrada de una pregunta central
- Generación jerárquica de subpreguntas
- Visualización del complejo epistémico
- Diálogo adaptativo para refinar subpreguntas
- Generación de respuesta reflexiva adaptada
- Registro y exportación del razonamiento completo

## ▶️ Cómo ejecutar

```bash
git clone https://github.com/tu_usuario/streamlit-mvp-inquiry-architecture.git
cd streamlit-mvp-inquiry-architecture

# Crear entorno virtual
python -m venv venv
.\venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
streamlit run app.py
