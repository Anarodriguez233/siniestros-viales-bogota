import streamlit as st
import pandas as pd
import joblib

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================
st.set_page_config(
    page_title="RiskAI Bogotá",
    page_icon="■",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CARGA DEL MODELO
# =========================================================
data = joblib.load("pipeline.pkl")

modelo = data["modelo"]
scaler = data["scaler"]
columnas = data["columnas"]
localidades = data["localidades"]

# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Times New Roman', serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(0,255,240,0.08), transparent 32%),
        radial-gradient(circle at top right, rgba(0,120,255,0.08), transparent 35%),
        linear-gradient(135deg, #020713 0%, #050B18 45%, #020713 100%);
    color: #F8FAFC;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #081120 0%, #07101E 100%);
    border-right: 2px solid rgba(80, 140, 190, 0.35);
    box-shadow: 0 0 22px rgba(0, 255, 240, 0.08);
}

[data-testid="stSidebar"] > div:first-child {
    padding: 2rem 1.6rem;
}

.sidebar-title {
    font-size: 2rem;
    font-weight: 800;
    margin-bottom: 2rem;
    color: white;
}

.sidebar-title span {
    color: #00FFF0;
    text-shadow: 0 0 12px rgba(0,255,240,0.5);
}

.sidebar-copy {
    font-size: 1.15rem;
    line-height: 1.8;
    color: #F1F5F9;
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
    font-weight: 700;
    font-size: 1rem;
    margin-bottom: 1.5rem;
}

.help-card {
    margin-top: 4rem;
    padding: 1.5rem;
    border-radius: 18px;
    background: rgba(0,255,240,0.10);
    border: 1px solid rgba(0,255,240,0.35);
    color: #CFFAFE;
    line-height: 1.8;
    font-size: 1rem;
}

/* INPUTS */
.stSlider label,
.stSelectbox label {
    color: white !important;
    font-weight: 700;
    font-size: 1rem;
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

/* HEADER */
.top-label {
    color: #00FFF0;
    font-weight: 700;
    letter-spacing: 6px;
    font-size: 0.95rem;
    margin-bottom: 2rem;
}

.main-title {
    font-size: 3rem;
    line-height: 1.3;
    font-weight: 800;
    color: white;
    margin-bottom: 2rem;
}

.main-title span {
    color: #00FFF0;
}

.title-line {
    width: 140px;
    height: 2px;
    background: linear-gradient(90deg, #00FFF0, transparent);
    margin-bottom: 2.5rem;
}

/* CARDS */
.cyber-card {
    background: linear-gradient(
        135deg,
        rgba(8,17,32,0.96),
        rgba(7,15,29,0.90)
    );

    border: 1px solid rgba(0,255,240,0.35);
    border-radius: 18px;
    padding: 2rem;
    margin-bottom: 1.8rem;

    box-shadow:
        0 0 20px rgba(0,255,240,0.05),
        0 0 60px rgba(0,0,0,0.25);
}

.card-title {
    color: #00FFF0;
    letter-spacing: 3px;
    font-weight: 800;
    font-size: 1rem;
    margin-bottom: 1.8rem;
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
    font-size: 1rem;
}

.scenario-value {
    color: white;
    font-weight: 800;
    font-size: 1.4rem;
    line-height: 1.3;
}

.model-card {
    border-left: 3px solid #00FFF0;
}

.model-text {
    color: #F8FAFC;
    line-height: 1.9;
    font-size: 1.1rem;
}

.model-list {
    margin-top: 1rem;
    color: #F8FAFC;
    line-height: 2;
    font-size: 1.05rem;
}

/* BOTÓN */
.stButton > button {
    width: 100%;
    height: 68px;

    border-radius: 14px;
    border: 1px solid #00FFF0;

    background: rgba(0,255,240,0.04);

    color: #00FFF0;

    font-size: 1.25rem;
    font-weight: 800;
    letter-spacing: 1px;

    transition: 0.2s;
}

.stButton > button:hover {
    background: rgba(0,255,240,0.12);
    color: white;
    border: 1px solid #00FFF0;

    box-shadow: 0 0 18px rgba(0,255,240,0.18);
}

/* RESULTADO */
.result-card {
    background: linear-gradient(
        135deg,
        rgba(20,10,25,0.95),
        rgba(8,14,28,0.92)
    );

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
    width: 170px;
    height: 170px;
    border-radius: 50%;

    background:
        radial-gradient(circle at center, #081120 58%, transparent 59%),
        conic-gradient(var(--color) var(--percent), rgba(71,85,105,0.45) 0);

    display: flex;
    align-items: center;
    justify-content: center;

    margin: auto;
}

.gauge-inner {
    text-align: center;
}

.gauge-number {
    color: #FFB4BD;
    font-size: 2.8rem;
    font-weight: 800;
}

.gauge-label {
    color: white;
    font-size: 1rem;
    line-height: 1.6;
}

.risk-title {
    font-size: 2rem;
    font-weight: 800;
    margin-bottom: 1rem;
}

.risk-copy {
    color: #F8FAFC;
    line-height: 1.8;
    font-size: 1.15rem;
}

.progress-label {
    display: flex;
    justify-content: space-between;

    margin-top: 1.7rem;

    color: white;
    font-weight: 600;
    font-size: 1rem;
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

/* FOOTER */
.footer-card {
    margin-top: 2rem;

    padding: 1.6rem 2rem;

    border-radius: 16px;

    border: 1px solid rgba(148,163,184,0.20);

    background: rgba(8,17,32,0.75);

    color: #E2E8F0;

    text-align: center;

    line-height: 1.8;
    font-size: 1rem;
}

.footer-card span {
    color: #00FFF0;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:

    st.markdown("""
<div class="sidebar-title">
<span>RiskAI</span> Bogotá
</div>

<div class="sidebar-copy">
Modelo predictivo para estimar riesgo
de siniestros viales con víctimas.
</div>

<div class="neon-divider"></div>

<div class="sidebar-section">
PARÁMETROS DEL ESCENARIO
</div>
""", unsafe_allow_html=True)

    hora = st.slider(
        "Hora del día",
        0,
        23,
        12
    )

    mes = st.selectbox(
        "Mes",
        list(range(1, 13))
    )

    localidad = st.selectbox(
        "Localidad",
        localidades
    )

    st.markdown("""
<div class="help-card">
Ajuste las condiciones del escenario y ejecute la predicción
para conocer el nivel estimado de riesgo vial.
</div>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
st.markdown("""
<div class="top-label">
SISTEMA INTELIGENTE DE RIESGO VIAL
</div>

<div class="main-title">
Predicción de riesgo de<br>
siniestros viales en <span>Bogotá</span>
</div>

<div class="title-line"></div>
""", unsafe_allow_html=True)

# =========================================================
# CARD ESCENARIO
# =========================================================
st.markdown(f"""
<div class="cyber-card">

<div class="card-title">
ESCENARIO SELECCIONADO
</div>

<div class="scenario-grid">

<div class="scenario-item">
<div class="scenario-label">
Hora
</div>

<div class="scenario-value">
{hora}:00
</div>
</div>

<div class="scenario-item">
<div class="scenario-label">
Mes
</div>

<div class="scenario-value">
{mes}
</div>
</div>

<div class="scenario-item">
<div class="scenario-label">
Localidad
</div>

<div class="scenario-value">
{localidad}
</div>
</div>

</div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# LECTURA DEL MODELO
# =========================================================
st.markdown("""
<div class="cyber-card model-card">

<div class="card-title">
LECTURA DEL MODELO
</div>

<div class="model-text">
La salida representa la probabilidad estimada de riesgo alto
según las variables disponibles en el modelo.
</div>

<div class="model-list">
• El modelo analiza patrones históricos de siniestros.<br>
• Considera la hora, el mes y la localidad seleccionada.<br>
• Útil para priorizar intervenciones y vigilancia vial.
</div>

</div>
""", unsafe_allow_html=True)

# =========================================================
# BOTÓN
# =========================================================
predecir = st.button("PREDECIR RIESGO")

# =========================================================
# PREDICCIÓN
# =========================================================
if predecir:

    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=columnas
    )

    input_data["HORA"] = hora
    input_data["MES"] = mes

    col_localidad = "LOCALIDAD_" + localidad

    if col_localidad in input_data.columns:
        input_data[col_localidad] = 1

    input_data[["HORA", "MES"]] = scaler.transform(
        input_data[["HORA", "MES"]]
    )

    pred = modelo.predict(input_data)[0]
    prob = modelo.predict_proba(input_data)[0][1]

    prob_pct = int(prob * 100)

    if pred == 1:

        titulo = "RIESGO ALTO"

        texto = """
        El modelo estima una mayor probabilidad de que el siniestro
        involucre heridos o fallecidos.
        """

        color = "#FF4B5C"

    else:

        titulo = "RIESGO BAJO"

        texto = """
        El modelo estima una mayor probabilidad de que el siniestro
        sea únicamente con daños.
        """

        color = "#00FFF0"

    st.markdown(f"""
<div class="result-card">

<div class="card-title">
RESULTADO DE LA PREDICCIÓN
</div>

<div class="result-grid">

<div>

<div class="gauge"
style="--percent: {prob_pct}%; --color: {color};">

<div class="gauge-inner">

<div class="gauge-number">
{prob_pct}%
</div>

<div class="gauge-label">
Probabilidad<br>de riesgo alto
</div>

</div>
</div>

</div>

<div>

<div class="risk-title"
style="color:{color};">

{titulo}

</div>

<div class="risk-copy">
{texto}
</div>

</div>

</div>

<div class="progress-label">

<div>
Probabilidad estimada
</div>

<div>
{prob_pct}%
</div>

</div>

<div class="custom-progress">

<div class="custom-progress-fill"
style="width:{prob_pct}%; background:{color};">
</div>

</div>

</div>
""", unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div class="footer-card">

Proyecto de Analítica Aplicada |
Universidad de La Sabana<br><br>

Integrantes:<br>

<span>Tomás González</span> •
<span>Nicolás Castillo</span> •
<span>Ana Rodríguez</span>

</div>
""", unsafe_allow_html=True)
