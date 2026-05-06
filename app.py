import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Siniestros Viales Bogotá",
    page_icon="🚦",
    layout="centered"
)

data = joblib.load("pipeline.pkl")

modelo = data["modelo"]
scaler = data["scaler"]
columnas = data["columnas"]
localidades = data["localidades"]

st.title("🚦 Sistema Inteligente de Riesgo Vial")
st.markdown("### Predicción de riesgo de siniestros viales en Bogotá")

st.info("Seleccione las condiciones del siniestro para estimar el nivel de riesgo.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    hora = st.slider("🕒 Hora del día", 0, 23, 12)

with col2:
    mes = st.selectbox("📅 Mes", list(range(1, 13)))

localidad = st.selectbox("📍 Localidad", localidades)

st.divider()

if st.button("🔍 Predecir riesgo"):
    input_data = pd.DataFrame(0, index=[0], columns=columnas)

    input_data["HORA"] = hora
    input_data["MES"] = mes

    col_localidad = "LOCALIDAD_" + localidad

    if col_localidad in input_data.columns:
        input_data[col_localidad] = 1

    input_data[["HORA", "MES"]] = scaler.transform(input_data[["HORA", "MES"]])

    pred = modelo.predict(input_data)[0]
    prob = modelo.predict_proba(input_data)[0][1]

    st.subheader("Resultado de la predicción")

    if pred == 1:
        st.error("🔴 RIESGO ALTO")
        st.write("El modelo estima una mayor probabilidad de que el siniestro involucre heridos o fallecidos.")
    else:
        st.success("🟢 RIESGO BAJO")
        st.write("El modelo estima una mayor probabilidad de que el siniestro sea solo con daños.")

    st.metric("Probabilidad estimada de riesgo alto", f"{prob*100:.2f}%")
    st.progress(int(prob * 100))

st.divider()

st.markdown("""
**Proyecto de Analítica Aplicada**  
Universidad de La Sabana  

Integrantes:  
- Tomás González  
- Nicolás Castillo  
- Ana Rodríguez
""")
