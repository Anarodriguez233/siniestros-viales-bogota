import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================
st.set_page_config(
    page_title="Riesgo Vial Bogotá | IA",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# ESTILOS CSS: OSCURO + TECNOLÓGICO + CORPORATIVO + NEÓN
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(0, 255, 213, 0.12), transparent 35%),
        radial-gradient(circle at top right, rgba(120, 80, 255, 0.14), transparent 35%),
        linear-gradient(135deg, #050816 0%, #080c18 45%, #0b1020 100%);
    color: #EAF2FF;
}

[data-testid="stHeader"] {
    background: rgba(5, 8, 22, 0);
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #070B18 0%, #0B1020 100%);
    border-right: 1px solid rgba(0, 255, 213, 0.16);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1250px;
}

.hero-card {
    padding: 34px 36px;
    border-radius: 28px;
    background: linear-gradient(135deg, rgba(11, 18, 38, 0.96), rgba(15, 23, 42, 0.78));
    border: 1px solid rgba(0, 255, 213, 0.18);
    box-shadow: 0 0 35px rgba(0, 255, 213, 0.08), 0 18px 60px rgba(0,0,0,0.40);
    margin-bottom: 28px;
}

.hero-title {
    font-size: 3rem;
    font-weight: 800;
    letter-spacing: -1.5px;
    line-height: 1.05;
    margin-bottom: 12px;
}

.neon-text {
    color: #00FFD5;
    text-shadow: 0 0 18px rgba(0,255,213,0.38);
}

.hero-subtitle {
    font-size: 1.1rem;
    color: #DCE7FF;
    max-width: 830px;
    line-height: 1.6;
}

.badge {
    display: inline-block;
    padding: 8px 13px;
    border-radius: 999px;
    background: rgba(0,255,213,0.10);
    color: #00FFD5;
    border: 1px solid rgba(0,255,213,0.30);
    font-size: 0.82rem;
    font-weight: 700;
    margin-bottom: 18px;
}

.glass-card {
    padding: 24px;
    border-radius: 24px;
    background: rgba(18, 28, 52, 0.88);
    border: 1px solid rgba(148, 163, 184, 0.16);
    box-shadow: 0 14px 40px rgba(0,0,0,0.28);
    min-height: 100%;
}

.section-title {
    font-size: 1.1rem;
    font-weight: 750;
    color: #FFFFFF;
    margin-bottom: 8px;
}

.section-caption {
    font-size: 0.92rem;
    color: #D6E2FF;
    margin-bottom: 22px;
}

.metric-card {
    padding: 20px;
    overflow-wrap: break-word;
    border-radius: 22px;
    background: linear-gradient(135deg, rgba(0,255,213,0.10), rgba(124,58,237,0.10));
    border: 1px solid rgba(0,255,213,0.20);
}

.risk-high {
    padding: 24px;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(255, 55, 95, 0.20), rgba(127, 29, 29, 0.28));
    border: 1px solid rgba(255, 55, 95, 0.45);
    box-shadow: 0 0 32px rgba(255, 55, 95, 0.14);
}

.risk-low {
    padding: 24px;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(0, 255, 149, 0.16), rgba(20, 83, 45, 0.26));
    border: 1px solid rgba(0, 255, 149, 0.42);
    box-shadow: 0 0 32px rgba(0, 255, 149, 0.12);
}

.risk-title {
    font-size: 2rem;
    font-weight: 850;
    margin-bottom: 6px;
}

.risk-copy {
    color: #C9D4EA;
    font-size: 1rem;
    line-height: 1.5;
}

.footer {
    margin-top: 35px;
    padding-top: 18px;
    border-top: 1px solid rgba(148, 163, 184, 0.18);
    color: #7C8AA5;
    font-size: 0.88rem;
}

.stButton > button {
    width: 100%;
    border-radius: 16px;
    border: 1px solid rgba(0,255,213,0.45);
    background: linear-gradient(90deg, #00FFD5 0%, #7C3AED 100%);
    color: #06101F;
    font-weight: 800;
    padding: 0.85rem 1rem;
    box-shadow: 0 0 24px rgba(0,255,213,0.20);
}

.stButton > button:hover {
    border: 1px solid rgba(255,255,255,0.75);
    transform: translateY(-1px);
}

div[data-testid="stMetricValue"] {
    color: #00FFD5;
    font-size: 2rem;
    font-weight: 700;
    line-height: 1.1;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.stSlider [data-baseweb="slider"] > div {
    color: #00FFD5;
}

/* SELECTBOX */
.stSelectbox label {
    color: #F8FAFC !important;
    font-weight: 600;
}

.stSelectbox div[data-baseweb="select"] > div {
    background-color: rgba(255,255,255,0.92) !important;
    color: #0F172A !important;
    border-radius: 14px !important;
    border: 1px solid rgba(0,255,213,0.25) !important;
    font-weight: 600;
}

/* SLIDER LABELS */
.stSlider label {
    color: #F8FAFC !important;
    font-weight: 600;
}

/* SIDEBAR TEXT */
[data-testid="stSidebar"] * {
    color: #EAF2FF;
}

/* MÉTRICAS */
div[data-testid="metric-container"] {
    background: rgba(15, 23, 42, 0.65);
    padding: 12px;
    border-radius: 18px;
    border: 1px solid rgba(0,255,213,0.10);
}

div[data-testid="stMetricLabel"] {
    color: #D6E2FF !important;
    font-weight: 600;
    font-size: 0.9rem;
}
}

[data-testid="stAlert"] {
    border-radius: 18px;
    border: 1px solid rgba(0,255,213,0.18);
    background: rgba(0,255,213,0.08);
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# CARGA DEL MODELO
# ============================================================
@st.cache_resource
def cargar_pipeline():
    return joblib.load("pipeline.pkl")

try:
    data = cargar_pipeline()
    modelo = data["modelo"]
    scaler = data["scaler"]
    columnas = data["columnas"]
    localidades = data["localidades"]
except Exception as e:
    st.error("No fue posible cargar el archivo pipeline.pkl. Verifique que esté en la misma carpeta de la app.")
    st.exception(e)
    st.stop()

# ============================================================
# FUNCIONES AUXILIARES
# ============================================================
def clasificar_probabilidad(prob):
    if prob >= 0.70:
        return "Crítico", "🔴", "risk-high"
    elif prob >= 0.50:
        return "Alto", "🟠", "risk-high"
    elif prob >= 0.30:
        return "Moderado", "🟡", "risk-low"
    else:
        return "Bajo", "🟢", "risk-low"


def construir_input(hora, mes, localidad):
    input_data = pd.DataFrame(0, index=[0], columns=columnas)
    input_data["HORA"] = hora
    input_data["MES"] = mes

    col_localidad = "LOCALIDAD_" + localidad
    if col_localidad in input_data.columns:
        input_data[col_localidad] = 1

    input_data[["HORA", "MES"]] = scaler.transform(input_data[["HORA", "MES"]])
    return input_data


def recomendacion_operativa(prob, hora, localidad):
    if prob >= 0.70:
        return f"Priorizar monitoreo preventivo en {localidad}, reforzar presencia institucional y revisar puntos críticos durante la franja de las {hora}:00."
    elif prob >= 0.50:
        return f"Activar alerta temprana para {localidad}. Se recomienda revisar patrones históricos y condiciones operativas de movilidad."
    elif prob >= 0.30:
        return f"Mantener seguimiento. El riesgo no es extremo, pero puede aumentar si coinciden lluvia, congestión o eventos masivos."
    return f"Condición de menor riesgo relativo. Mantener monitoreo básico y usar como referencia comparativa."

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown("### 🚦 RiskAI Bogotá")
    st.caption("Modelo predictivo para estimar riesgo de siniestros viales con víctimas.")
    st.divider()

    st.markdown("#### Parámetros del escenario")
    hora = st.slider("Hora del día", 0, 23, 12)
    mes = st.selectbox("Mes", list(range(1, 13)), index=0)
    localidad = st.selectbox("Localidad", localidades)

    st.divider()
    st.markdown("#### Lectura del modelo")
    st.caption("La salida representa la probabilidad estimada de riesgo alto según las variables disponibles en el modelo.")

# ============================================================
# HERO
# ============================================================
st.markdown("""
<div class="hero-card">
    <div class="badge">IA APLICADA · MOVILIDAD · BOGOTÁ</div>
    <div class="hero-title">Sistema Inteligente de <span class="neon-text">Riesgo Vial</span></div>
    <div class="hero-subtitle">
        Herramienta analítica para anticipar escenarios de mayor riesgo en siniestros viales de Bogotá.
        Diseñada para convertir un modelo predictivo en una experiencia de decisión clara, visual y accionable.
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# LAYOUT PRINCIPAL
# ============================================================
left, right = st.columns([1.05, 0.95], gap="large")

with left:
    st.markdown("""
    <div class="glass-card">
        <div class="section-title">Configurar escenario</div>
        <div class="section-caption">Seleccione una combinación de tiempo y localidad para simular el nivel de riesgo.</div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Hora", f"{hora}:00")
    with c2:
        st.metric("Mes", mes)
    with c3:
        st.metric("Localidad", localidad.title())

    st.markdown(" ")
    predecir = st.button("Ejecutar predicción inteligente")

with right:
    st.markdown("""
    <div class="glass-card">
        <div class="section-title">Qué predice el sistema</div>
        <div class="section-caption">
            El modelo estima si un siniestro tendría mayor probabilidad de involucrar heridos o fallecidos, frente a un evento solo con daños.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.info("Una buena app analítica no solo muestra una predicción: explica el escenario, comunica incertidumbre y orienta una decisión.")

# ============================================================
# PREDICCIÓN
# ============================================================
if predecir:
    input_data = construir_input(hora, mes, localidad)
    pred = modelo.predict(input_data)[0]
    prob = modelo.predict_proba(input_data)[0][1]
    nivel, icono, clase_css = clasificar_probabilidad(prob)
    recomendacion = recomendacion_operativa(prob, hora, localidad)

    st.markdown("---")
    st.markdown("### Resultado del análisis")

    r1, r2 = st.columns([0.95, 1.05], gap="large")

    with r1:
        st.markdown(f"""
        <div class="{clase_css}">
            <div class="risk-title">{icono} Riesgo {nivel}</div>
            <div class="risk-copy">
                Probabilidad estimada de riesgo alto: <strong>{prob*100:.2f}%</strong><br><br>
                {recomendacion}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with r2:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.metric("Probabilidad estimada", f"{prob*100:.2f}%")
        st.progress(int(prob * 100))
        st.caption("Interpretación: valores más altos sugieren mayor probabilidad de que el siniestro involucre víctimas.")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### Lectura ejecutiva")
    st.write(
        f"Para la localidad **{localidad.title()}**, durante el mes **{mes}** y a las **{hora}:00**, "
        f"el sistema clasifica el escenario como **riesgo {nivel.lower()}**. "
        "Esta salida debe entenderse como apoyo a la decisión, no como una certeza absoluta."
    )

else:
    st.markdown("---")
    st.markdown("### Esperando simulación")
    st.caption("Ajuste los parámetros en la barra lateral y ejecute la predicción para visualizar el resultado.")

# ============================================================
# PIE DE PÁGINA
# ============================================================
st.markdown("""
<div class="footer">
    <strong>Proyecto de Analítica Aplicada · Universidad de La Sabana</strong><br>
    Integrantes: Tomás González · Nicolás Castillo · Ana Rodríguez<br>
    Versión conceptual V2 · Enfoque: predicción, comunicación del riesgo y apoyo a decisiones públicas.
</div>
""", unsafe_allow_html=True)

