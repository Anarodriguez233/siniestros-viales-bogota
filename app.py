import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title=" Siniestros viales en Bogotá",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="expanded"
)

data = joblib.load("pipeline.pkl")

modelo = data["modelo"]
scaler = data["scaler"]
columnas = data["columnas"]
localidades = data["localidades"]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #020713 0%, #050B18 50%, #020713 100%);
    color: #F8FAFC;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #081120 0%, #07101E 100%);
    border-right: 2px solid rgba(0,255,240,0.25);
}

[data-testid="stSidebar"] > div:first-child {
    padding: 2rem 1.6rem;
}

.sidebar-title {
    font-size: 1.85rem;
    font-weight: 900;
    color: white;
    margin-bottom: 2rem;
}

.sidebar-title span {
    color: #00FFF0;
}

.sidebar-copy {
    color: #F1F5F9;
    line-height: 1.7;
    margin-bottom: 2rem;
}

.neon-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #00FFF0, transparent);
    margin: 2rem 0;
}

.sidebar-section {
    color: #00FFF0;
    letter-spacing: 3px;
    font-weight: 800;
    font-size: 0.9rem;
    margin-bottom: 1.5rem;
}

.help-card {
    margin-top: 4rem;
    padding: 1.3rem;
    border-radius: 18px;
    background: rgba(0,255,240,0.10);
    border: 1px solid rgba(0,255,240,0.35);
    color: #CFFAFE;
    line-height: 1.6;
}

.stSlider label,
.stSelectbox label {
    color: white !important;
    font-weight: 700;
}

.stSelectbox div[data-baseweb="select"] > div {
    background: #07101E !important;
    border: 1px solid rgba(0,255,240,0.75) !important;
    border-radius: 12px !important;
    color: white !important;
    min-height: 58px;
    font-weight: 700;
}

.stSelectbox div[data-baseweb="select"] span {
    color: white !important;
}

.top-label {
    color: #00FFF0;
    font-weight: 800;
    letter-spacing: 6px;
    font-size: 0.9rem;
    margin-bottom: 2.2rem;
}

.main-title {
    font-size: 2.8rem;
    line-height: 1.25;
    font-weight: 900;
    color: white;
    margin-bottom: 2rem;
}

.main-title span {
    color: #00FFF0;
}

.title-line {
    width: 130px;
    height: 2px;
    background: linear-gradient(90deg, #00FFF0, transparent);
    margin-bottom: 2.2rem;
}

.cyber-card {
    background: linear-gradient(135deg, rgba(8,17,32,0.96), rgba(7,15,29,0.90));
    border: 1px solid rgba(0,255,240,0.35);
    border-radius: 18px;
    padding: 2rem;
    margin-bottom: 1.8rem;
}

.card-title {
    color: #00FFF0;
    letter-spacing: 3px;
    font-weight: 900;
    font-size: 0.95rem;
    margin-bottom: 1.6rem;
}

.scenario-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1.4fr;
    gap: 1.5rem;
}

.scenario-item {
    border-right: 1px solid rgba(148,163,184,0.18);
    padding-right: 1rem;
}

.scenario-item:last-child {
    border-right: none;
}

.scenario-label {
    color: #CBD5E1;
    font-weight: 600;
    margin-bottom: 0.8rem;
}

.scenario-value {
    color: white;
    font-weight: 800;
    font-size: 1.35rem;
    line-height: 1.25;
}

.model-card {
    border-left: 3px solid #00FFF0;
}

.model-text,
.model-list {
    color: #F8FAFC;
    line-height: 1.8;
    font-size: 1.05rem;
}

.stButton > button {
    width: 100%;
    height: 64px;
    border-radius: 14px;
    border: 1px solid #00FFF0;
    background: rgba(0,255,240,0.04);
    color: #00FFF0;
    font-size: 1.2rem;
    font-weight: 900;
    letter-spacing: 1px;
}

.stButton > button:hover {
    background: rgba(0,255,240,0.12);
    color: white;
}

.result-card {
    background: linear-gradient(135deg, rgba(20,10,25,0.95), rgba(8,14,28,0.92));
    border: 1px solid rgba(255,75,92,0.45);
    border-radius: 18px;
    padding: 2rem;
    margin-top: 1.8rem;
}

.result-grid {
    display: grid;
    grid-template-columns: 0.9fr 1.2fr;
    gap: 2rem;
    align-items: center;
}

.gauge {
    width: 165px;
    height: 165px;
    border-radius: 50%;
    background:
        radial-gradient(circle at center, #081120 58%, transparent 59%),
        conic-gradient(var(--color) var(--percent), rgba(71,85,105,0.45) 0);
    display: flex;
    align-items: center;
    justify-content: center;
}

.gauge-inner {
    text-align: center;
}

.gauge-number {
    color: #FFB4BD;
    font-size: 2.7rem;
    font-weight: 900;
}

.gauge-label {
    color: white;
    font-size: 0.9rem;
}

.risk-title {
    font-size: 1.6rem;
    font-weight: 900;
    letter-spacing: 1px;
    margin-bottom: 1rem;
}

.risk-copy {
    color: #F8FAFC;
    line-height: 1.65;
    font-size: 1.05rem;
}

.progress-label {
    display: flex;
    justify-content: space-between;
    margin-top: 1.7rem;
    color: white;
    font-weight: 600;
}

.custom-progress {
    height: 12px;
    background: rgba(71,85,105,0.5);
    border-radius: 999px;
    margin-top: 0.6rem;
    overflow: hidden;
}

.custom-progress-fill {
    height: 100%;
    border-radius: 999px;
}

.footer-card {
    margin-top: 1.8rem;
    padding: 1.4rem 2rem;
    border-radius: 16px;
    border: 1px solid rgba(148,163,184,0.20);
    background: rgba(8,17,32,0.75);
    color: #E2E8F0;
    text-align: center;
}

.footer-card span {
    color: #00FFF0;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
<div class="sidebar-title">🚦 <span>Siniestros viales </span> Bogotá</div>

<div class="sidebar-copy">
Modelo predictivo para estimar el riesgo de siniestros viales con víctimas.
</div>

<div class="neon-divider"></div>

<div class="sidebar-section">PARÁMETROS DEL ESCENARIO</div>
""", unsafe_allow_html=True)

    hora = st.slider(" Hora del día", 0, 23, 12)
    meses = {
    "Enero": 1,
    "Febrero": 2,
    "Marzo": 3,
    "Abril": 4,
    "Mayo": 5,
    "Junio": 6,
    "Julio": 7,
    "Agosto": 8,
    "Septiembre": 9,
    "Octubre": 10,
    "Noviembre": 11,
    "Diciembre": 12
}

mes_nombre = st.selectbox(
    " Mes",
    list(meses.keys())
)

mes = meses[mes_nombre]
    localidad = st.selectbox(" Localidad", localidades)

    st.markdown("""
<div class="help-card">
 Ajusta las condiciones del escenario que perfieras y ejecuta la predicción para conocer el nivel de riesgo estimado.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="top-label"> SISTEMA INTELIGENTE DE RIESGO VIAL</div>

<div class="main-title">
Predicción de riesgo de<br>
siniestros viales en <span>Bogotá</span>
</div>

<div class="title-line"></div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="cyber-card">
<div class="card-title">ESCENARIO SELECCIONADO</div>

<div class="scenario-grid">
<div class="scenario-item">
<div class="scenario-label"> Hora</div>
<div class="scenario-value">{hora}:00</div>
</div>

<div class="scenario-item">
<div class="scenario-label"> Mes</div>
<div class="scenario-value">{mes}</div>
</div>

<div class="scenario-item">
<div class="scenario-label"> Localidad</div>
<div class="scenario-value">{localidad}</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="cyber-card model-card">
<div class="card-title">⚙️ LECTURA DEL MODELO</div>

<div class="model-text">
La salida representa la probabilidad estimada de riesgo alto según las variables disponibles en el modelo.
</div>

<div class="model-list">
☑ El modelo analiza patrones históricos de siniestros.<br>
☑ Considera la hora, el mes y la localidad seleccionada.<br>
☑ Útil para priorizar intervenciones y vigilancia vial.
</div>
</div>
""", unsafe_allow_html=True)

predecir = st.button("  PREDECIR EL RIESGO")

if predecir:

    input_data = pd.DataFrame(0, index=[0], columns=columnas)

    input_data["HORA"] = hora
    input_data["MES"] = mes

    col_localidad = "LOCALIDAD_" + localidad

    if col_localidad in input_data.columns:
        input_data[col_localidad] = 1

    input_data[["HORA", "MES"]] = scaler.transform(input_data[["HORA", "MES"]])

    pred = modelo.predict(input_data)[0]
    prob = modelo.predict_proba(input_data)[0][1]

    prob_pct = int(prob * 100)

    if pred == 1:
        titulo = "⚠️ RIESGO ALTO"
        texto = "El modelo estima una mayor probabilidad de que el siniestro involucre heridos o fallecidos."
        color = "#FF4B5C"
    else:
        titulo = "✅ RIESGO BAJO"
        texto = "El modelo estima una mayor probabilidad de que el siniestro sea únicamente con daños."
        color = "#00FFF0"

    st.markdown(f"""
<div class="result-card">
<div class="card-title">RESULTADO DE LA PREDICCIÓN</div>

<div class="result-grid">
<div>
<div class="gauge" style="--percent: {prob_pct}%; --color: {color};">
<div class="gauge-inner">
<div class="gauge-number">{prob_pct}%</div>
<div class="gauge-label">Probabilidad<br>de riesgo alto</div>
</div>
</div>
</div>

<div>
<div class="risk-title" style="color:{color};">{titulo}</div>
<div class="risk-copy">{texto}</div>
</div>
</div>

<div class="progress-label">
<div>Probabilidad estimada</div>
<div>{prob_pct}%</div>
</div>

<div class="custom-progress">
<div class="custom-progress-fill" style="width:{prob_pct}%; background:{color};"></div>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer-card">
| Andres Felipe Cardona Ortegon |  Proyecto de Analítica Aplicada | Universidad de La Sabana<br><br>
Integrantes:
<span>Tomás González</span> •
<span>Nicolás Castillo</span> •
<span>Ana Rodríguez</span>
</div>
""", unsafe_allow_html=True)
