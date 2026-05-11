import streamlit as st
import pandas as pd
import joblib

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================
st.set_page_config(
    page_title="Sistema Inteligente de Riesgo Vial",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CSS / ESTILO VISUAL
# =========================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* FONDO GENERAL */
.stApp {
    background:
        radial-gradient(circle at top left, rgba(0,255,213,0.08), transparent 30%),
        radial-gradient(circle at top right, rgba(124,58,237,0.10), transparent 30%),
        linear-gradient(135deg, #030712 0%, #020617 45%, #050816 100%);
    color: #F8FAFC;
}

/* HEADER */
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #050816 0%, #081021 100%);
    border-right: 1px solid rgba(0,255,213,0.10);
}

[data-testid="stSidebar"] * {
    color: #E2E8F0;
}

/* CONTENIDO */
.block-container {
    padding-top: 2rem;
    max-width: 1250px;
}

/* HERO */
.hero-card {
    padding: 36px;
    border-radius: 28px;
    background: rgba(15,23,42,0.75);
    border: 1px solid rgba(0,255,213,0.15);
    box-shadow: 0 0 35px rgba(0,255,213,0.06);
    margin-bottom: 28px;
}

.hero-title {
    font-size: 3rem;
    font-weight: 800;
    color: white;
    margin-bottom: 12px;
}

.neon {
    color: #00FFD5;
}

.hero-subtitle {
    color: #D6E2FF;
    font-size: 1.05rem;
    line-height: 1.6;
}

/* CARDS */
.glass-card {
    background: rgba(15,23,42,0.80);
    padding: 24px;
    border-radius: 24px;
    border: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 20px;
}

.section-title {
    color: white;
    font-size: 1.1rem;
    font-weight: 700;
    margin-bottom: 8px;
}

.section-caption {
    color: #D6E2FF;
    line-height: 1.5;
}

/* MÉTRICAS */
div[data-testid="metric-container"] {
    background: rgba(15,23,42,0.65);
    padding: 12px;
    border-radius: 18px;
    border: 1px solid rgba(0,255,213,0.08);
}

div[data-testid="stMetricLabel"] {
    color: #CBD5E1 !important;
    font-size: 0.9rem;
    font-weight: 600;
}

/* AQUÍ ESTÁ EL FIX IMPORTANTE */
div[data-testid="stMetricValue"] {
    color: #00FFD5;
    font-size: 1.3rem;
    font-weight: 700;
    line-height: 1.2;

    white-space: normal;
    overflow: visible;
    text-overflow: unset;
    word-break: break-word;
}

/* BOTÓN */
.stButton > button {
    width: 100%;
    border-radius: 16px;
    border: none;
    background: linear-gradient(90deg, #00FFD5 0%, #7C3AED 100%);
    color: #04111D;
    font-weight: 800;
    padding: 0.9rem;
    transition: 0.2s;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 20px rgba(0,255,213,0.25);
}

/* SELECTBOX */
.stSelectbox label {
    color: white !important;
    font-weight: 600;
}

.stSelectbox div[data-baseweb="select"] > div {
    background-color: rgba(255,255,255,0.95) !important;
    color: #0F172A !important;
    border-radius: 14px !important;
}

/* SLIDER */
.stSlider label {
    color: white !important;
    font-weight: 600;
}

/* ALERT */
[data-testid="stAlert"] {
    border-radius: 16px;
    background: rgba(0,255,213,0.08);
    border: 1px solid rgba(0,255,213,0.10);
}

/* RESULTADOS */
.result-high {
    padding: 24px;
    border-radius: 24px;
    background: rgba(255,0,80,0.12);
    border: 1px solid rgba(255,0,80,0.25);
}

.result-low {
    padding: 24px;
    border-radius: 24px;
    background: rgba(0,255,140,0.10);
    border: 1px solid rgba(0,255,140,0.20);
}

/* FOOTER */
.footer {
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid rgba(255,255,255,0.08);
    color: #94A3B8;
    font-size: 0.9rem;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# CARGA DEL MODELO
# =========================================================
data = joblib.load("pipeline.pkl")

modelo = data["modelo"]
scaler = data["scaler"]
columnas = data["columnas"]
localidades = data["localidades"]

# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:

    st.markdown("## 🚦 RiskAI Bogotá")

    st.markdown("""
    Modelo predictivo para estimar riesgo de
    siniestros viales con víctimas.
    """)

    st.divider()

    st.markdown("### Parámetros del escenario")

    hora = st.slider("Hora del día", 0, 23, 12)

    mes = st.selectbox(
        "Mes",
        list(range(1, 13))
    )

    localidad = st.selectbox(
        "Localidad",
        localidades
    )

    st.divider()

    st.markdown("### Lectura del modelo")

    st.caption("""
    La salida representa la probabilidad estimada
    de riesgo alto según las variables disponibles
    en el modelo.
    """)

# =========================================================
# HERO PRINCIPAL
# =========================================================
st.markdown("""
<div class="hero-card">

<div class="hero-title">
🚦 Sistema Inteligente de
<span class="neon">Riesgo Vial</span>
</div>

<div class="hero-subtitle">
Herramienta analítica para predecir escenarios
de mayor riesgo en siniestros viales de Bogotá.
Diseñada para transformar datos históricos en
decisiones preventivas.
</div>

</div>
""", unsafe_allow_html=True)

# =========================================================
# LAYOUT PRINCIPAL
# =========================================================
col1, col2 = st.columns([1.1, 0.9])

with col1:

    st.markdown("""
    <div class="glass-card">
        <div class="section-title">
        Configuración del escenario
        </div>

        <div class="section-caption">
        Ajuste las variables para simular
        un escenario vial.
        </div>
    </div>
    """, unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric("Hora", f"{hora}:00")

    with m2:
        st.metric("Mes", mes)

    with m3:
        st.metric("Localidad", localidad)

    st.markdown("")

    predecir = st.button("🔍 Ejecutar predicción inteligente")

with col2:

    st.markdown("""
    <div class="glass-card">
        <div class="section-title">
        ¿Qué predice el sistema?
        </div>

        <div class="section-caption">
        El modelo estima la probabilidad de que
        un siniestro vial involucre víctimas
        frente a eventos únicamente con daños.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.info("""
    El objetivo no es reemplazar decisiones humanas,
    sino apoyar estrategias preventivas y análisis
    de movilidad urbana.
    """)

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

    st.markdown("---")

    st.subheader("Resultado de la predicción")

    if pred == 1:

        st.markdown(f"""
        <div class="result-high">

        <h2>🔴 Riesgo Alto</h2>

        <p>
        El modelo estima una alta probabilidad
        de que el siniestro involucre
        heridos o fallecidos.
        </p>

        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div class="result-low">

        <h2>🟢 Riesgo Bajo</h2>

        <p>
        El modelo estima mayor probabilidad
        de eventos únicamente con daños.
        </p>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("")

    st.metric(
        "Probabilidad estimada de riesgo alto",
        f"{prob*100:.2f}%"
    )

    st.progress(int(prob * 100))

# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div class="footer">

<b>Proyecto de Analítica Aplicada</b><br>
Universidad de La Sabana<br><br>

Integrantes:<br>
• Tomás González<br>
• Nicolás Castillo<br>
• Ana Rodríguez

</div>
""", unsafe_allow_html=True)

