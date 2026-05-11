if pred == 1:

    titulo = "⚠️ RIESGO ALTO"

    texto = """
    El modelo estima una mayor probabilidad de que el siniestro
    involucre heridos o fallecidos.
    """

    color = "#FF4B5C"

else:

    titulo = "✅ RIESGO BAJO"

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
    <div class="gauge" style="--percent: {prob_pct}%;">
        <div class="gauge-inner">
            <div class="gauge-number">{prob_pct}%</div>
            <div class="gauge-label">
            Probabilidad<br>de riesgo alto
            </div>
        </div>
    </div>
</div>

<div>

    <div class="risk-title" style="color:{color};">
    {titulo}
    </div>

    <div class="risk-copy">{texto}</div>

</div>

</div>

<div class="progress-label">
    <div>Probabilidad estimada</div>
    <div>{prob_pct}%</div>
</div>

<div class="custom-progress">
    <div class="custom-progress-fill"
    style="width:{prob_pct}%; background:{color};">
    </div>
</div>

</div>
""", unsafe_allow_html=True)
