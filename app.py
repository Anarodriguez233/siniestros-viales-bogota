import streamlit as st
import pandas as pd
import joblib

data = joblib.load("pipeline.pkl")

modelo = data["modelo"]
scaler = data["scaler"]
columnas = data["columnas"]
localidades = data["localidades"]

st.title("🚗 Predicción de Riesgo de Siniestros Viales en Bogotá")

st.write("Seleccione las condiciones del siniestro para estimar el nivel de riesgo.")

hora = st.slider("Hora del día", 0, 23, 12)
mes = st.selectbox("Mes", list(range(1, 13)))
localidad = st.selectbox("Localidad", localidades)

if st.button("Predecir riesgo"):
    input_data = pd.DataFrame(0, index=[0], columns=columnas)

    input_data["HORA"] = hora
    input_data["MES"] = mes

    col_localidad = "LOCALIDAD_" + localidad

    if col_localidad in input_data.columns:
        input_data[col_localidad] = 1

    input_data[["HORA", "MES"]] = scaler.transform(input_data[["HORA", "MES"]])

    pred = modelo.predict(input_data)[0]
    prob = modelo.predict_proba(input_data)[0][1]

    if pred == 1:
        st.error("⚠️ Riesgo alto: posible siniestro con heridos o fallecidos")
    else:
        st.success("✅ Riesgo bajo: posible siniestro solo con daños")

    st.write(f"Probabilidad estimada de riesgo alto: **{prob*100:.2f}%**")
