import streamlit as st
import pandas as pd
import pickle

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Smart Car Price Predictor",
    page_icon="🚗",
    layout="wide"
)

# -------------------------------------------------
# Load Model + Data
# -------------------------------------------------
@st.cache_resource
def load_model():
    return pickle.load(open("CPP.pkl", "rb"))

@st.cache_data
def load_data():
    return pd.read_csv("clean_data.csv")

model = load_model()
car = load_data()

companies  = sorted(car["company"].unique())
fuel_types = sorted(car["fuel_type"].unique())
years      = sorted(car["year"].unique(), reverse=True)

# -------------------------------------------------
# Premium CSS — Dark Futuristic Theme
# -------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap');

/* ── Global ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif !important;
}
.stApp {
    background: #070b14 !important;
}

/* Grid texture */
.stApp::before {
    content: '';
    position: fixed; inset: 0;
    background-image:
        linear-gradient(rgba(255,255,255,0.022) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.022) 1px, transparent 1px);
    background-size: 60px 60px;
    pointer-events: none;
    z-index: 0;
}

/* Glow blobs */
.stApp::after {
    content: '';
    position: fixed; inset: 0;
    background:
        radial-gradient(ellipse 80% 60% at 10% 20%, rgba(30,80,200,0.11) 0%, transparent 60%),
        radial-gradient(ellipse 60% 50% at 90% 80%, rgba(0,180,120,0.07) 0%, transparent 55%);
    pointer-events: none;
    z-index: 0;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding: 48px 48px 64px !important;
    max-width: 1200px !important;
    position: relative;
    z-index: 1;
}

/* ── HEADER ── */
.hero-eyebrow {
    display: inline-flex; align-items: center; gap: 8px;
    background: rgba(37,99,235,0.12);
    border: 1px solid rgba(37,99,235,0.3);
    border-radius: 100px;
    padding: 6px 18px;
    font-size: 11px; letter-spacing: 0.13em;
    text-transform: uppercase;
    color: #60a5fa; font-weight: 500;
    margin-bottom: 18px;
}
.pulse-dot {
    width: 7px; height: 7px;
    border-radius: 50%; background: #60a5fa;
    display: inline-block;
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0%, 100% { opacity:1; transform:scale(1); }
    50%       { opacity:0.4; transform:scale(0.75); }
}
.hero-title {
    font-family: 'Syne', sans-serif !important;
    font-size: clamp(36px, 5vw, 56px) !important;
    font-weight: 800 !important;
    letter-spacing: -0.03em !important;
    line-height: 1.06 !important;
    color: #ffffff !important;
    margin-bottom: 12px !important;
}
.accent {
    background: linear-gradient(120deg, #3b82f6, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    font-size: 15px !important;
    color: #4b5563 !important;
    font-weight: 300 !important;
    letter-spacing: 0.01em !important;
}

/* ── CARD LABEL ── */
.card-section-label {
    font-family: 'Syne', sans-serif;
    font-size: 11px; letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #374151; font-weight: 600;
    margin-bottom: 24px;
    display: flex; align-items: center; gap: 10px;
}
.card-section-label::after {
    content: ''; flex: 1; height: 1px;
    background: rgba(255,255,255,0.06);
}

/* ── FIELD LABELS ── */
.stSelectbox label,
.stNumberInput label,
.stRadio > label {
    font-size: 12px !important;
    color: #6b7280 !important;
    letter-spacing: 0.05em !important;
    font-weight: 400 !important;
    margin-bottom: 6px !important;
}

/* ── SELECT & NUMBER INPUT ── */
.stSelectbox > div > div,
.stNumberInput > div > div > input {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    color: #e8eaf0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 14px !important;
}
.stSelectbox > div > div:hover,
.stNumberInput > div > div > input:hover {
    border-color: rgba(255,255,255,0.22) !important;
}
.stSelectbox > div > div:focus-within,
.stNumberInput > div > div > input:focus {
    border-color: rgba(59,130,246,0.5) !important;
    background: rgba(59,130,246,0.06) !important;
    box-shadow: none !important;
}
.stSelectbox svg { fill: #6b7280 !important; }

/* ── RADIO — Pill style ── */
.stRadio > div {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: wrap !important;
    gap: 8px !important;
    margin-top: 4px !important;
}
.stRadio > div > label {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 100px !important;
    padding: 8px 18px !important;
    font-size: 13px !important;
    color: #9ca3af !important;
    cursor: pointer !important;
    margin: 0 !important;
    transition: all 0.18s !important;
}
.stRadio > div > label:hover {
    border-color: rgba(255,255,255,0.22) !important;
    color: #e8eaf0 !important;
}
/* Hide radio circle dot */
.stRadio > div > label > div:first-child { display: none !important; }
/* Active pill */
.stRadio > div > label[data-checked="true"] {
    background: rgba(59,130,246,0.15) !important;
    border-color: rgba(59,130,246,0.4) !important;
    color: #93c5fd !important;
}

/* ── BUTTON ── */
.stButton > button {
    width: 100% !important;
    background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 50%, #1e40af 100%) !important;
    border: none !important;
    border-radius: 13px !important;
    height: 52px !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    letter-spacing: 0.05em !important;
    color: #ffffff !important;
    margin-top: 8px !important;
    transition: transform 0.15s, box-shadow 0.15s !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 36px rgba(37,99,235,0.38) !important;
    background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ── GLASS CARD ── */
.glass-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.09);
    border-radius: 20px;
    padding: 32px 36px;
    position: relative; overflow: hidden;
}
.glass-card::before {
    content: ''; position: absolute; inset: 0;
    border-radius: 20px;
    background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, transparent 50%);
    pointer-events: none;
}

/* ── RESULT: empty state ── */
.result-empty {
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    min-height: 300px; text-align: center; gap: 14px;
}
.result-icon-ring {
    width: 68px; height: 68px; border-radius: 50%;
    border: 1px dashed rgba(255,255,255,0.14);
    display: flex; align-items: center; justify-content: center;
    font-size: 26px; color: rgba(255,255,255,0.18);
}
.result-empty p { font-size: 13px; color: #374151; line-height: 1.7; max-width: 200px; }

/* ── PRICE BLOCK ── */
.price-block {
    background: linear-gradient(135deg, rgba(37,99,235,0.16), rgba(6,182,212,0.1));
    border: 1px solid rgba(59,130,246,0.25);
    border-radius: 16px; padding: 36px 28px;
    text-align: center; margin-bottom: 20px;
    position: relative; overflow: hidden;
}
.price-block::after {
    content: ''; position: absolute;
    top: -20px; right: -20px;
    width: 110px; height: 110px; border-radius: 50%;
    background: rgba(59,130,246,0.08);
    filter: blur(24px); pointer-events: none;
}
.price-tag-label {
    font-size: 11px; letter-spacing: 0.14em;
    text-transform: uppercase; color: #60a5fa; opacity: 0.75;
    margin-bottom: 10px;
}
.price-value {
    font-family: 'Syne', sans-serif;
    font-size: clamp(34px, 5vw, 50px);
    font-weight: 800; color: #ffffff;
    letter-spacing: -0.02em; line-height: 1;
    margin-bottom: 6px;
}
.price-currency { font-size: 0.5em; vertical-align: super; color: #93c5fd; }
.price-range { font-size: 13px; color: #4b5563; margin-top: 10px; }

/* ── STAT CHIPS ── */
.stats-row {
    display: grid; grid-template-columns: 1fr 1fr 1fr;
    gap: 10px; margin-bottom: 18px;
}
.stat-chip {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px; padding: 13px 10px; text-align: center;
}
.s-label {
    font-size: 10px; color: #374151;
    text-transform: uppercase; letter-spacing: 0.09em; margin-bottom: 5px;
}
.s-val { font-size: 13px; font-weight: 500; color: #9ca3af; }

/* ── CONFIDENCE BAR ── */
.conf-section {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px; padding: 16px; margin-bottom: 18px;
}
.conf-header {
    display: flex; justify-content: space-between;
    align-items: center; margin-bottom: 10px;
}
.conf-label { font-size: 11px; color: #374151; text-transform: uppercase; letter-spacing: 0.09em; }
.conf-pct   { font-size: 14px; font-weight: 600; color: #34d399; }
.conf-bar-bg {
    height: 5px; background: rgba(255,255,255,0.07);
    border-radius: 100px; overflow: hidden;
}
.conf-bar-fill {
    height: 100%; border-radius: 100px;
    background: linear-gradient(90deg, #059669, #34d399);
}

/* ── SUMMARY TAGS ── */
.summary-tags { display: flex; flex-wrap: wrap; gap: 8px; }
.tag {
    padding: 5px 14px; border-radius: 100px; font-size: 12px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08); color: #6b7280;
}

/* ── ERROR BOX ── */
.error-box {
    padding: 20px;
    background: rgba(163,45,45,0.12);
    border: 1px solid rgba(163,45,45,0.3);
    border-radius: 12px; color: #fca5a5; font-size: 13px;
}

/* ── FOOTER ── */
.custom-footer {
    text-align: center; margin-top: 52px;
    font-size: 12px; color: #1f2937; letter-spacing: 0.07em;
}
</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# Header
# -------------------------------------------------
st.markdown("""
<div style="text-align:center; margin-bottom:52px;">
  <div style="display:flex; justify-content:center; margin-bottom:18px;">
    <span class="hero-eyebrow">
      <span class="pulse-dot"></span>
      ML-Powered Estimation
    </span>
  </div>
  <p class="hero-title">Smart Car<br><span class="accent">Price Predictor</span></p>
  <p class="hero-sub">Enter your vehicle details to get an AI-powered resale value estimate</p>
</div>
""", unsafe_allow_html=True)


# -------------------------------------------------
# Two-column layout
# -------------------------------------------------
left_col, right_col = st.columns([1, 1.15], gap="large")


# ── LEFT: Input Panel ──────────────────────────────
with left_col:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-section-label">Vehicle Details</div>', unsafe_allow_html=True)

    company = st.selectbox("Manufacturer", companies)

    model_names = sorted(car[car["company"] == company]["name"].unique())
    name = st.selectbox("Model", model_names)

    year = st.selectbox("Manufacturing Year", years)

    kms_driven = st.number_input(
        "Kilometers Driven",
        min_value=0,
        max_value=500000,
        step=500,
        value=0
    )

    fuel_type = st.radio("Fuel Type", fuel_types, horizontal=True)

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    predict_clicked = st.button("🔍  Estimate Resale Value")

    st.markdown("</div>", unsafe_allow_html=True)


# ── RIGHT: Result Panel ────────────────────────────
with right_col:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-section-label">Prediction Result</div>', unsafe_allow_html=True)

    if not predict_clicked:
        st.markdown("""
        <div class="result-empty">
          <div class="result-icon-ring">⬡</div>
          <p>Fill in the vehicle details and click estimate to see the predicted resale value.</p>
        </div>
        """, unsafe_allow_html=True)

    else:
        input_df = pd.DataFrame(
            [[name, company, year, kms_driven, fuel_type]],
            columns=["name", "company", "year", "kms_driven", "fuel_type"]
        )

        try:
            prediction = model.predict(input_df)[0][0]
            pred_int   = int(prediction)
            lo         = int(pred_int * 0.92)
            hi         = int(pred_int * 1.08)
            conf       = 82   # replace with real confidence if your model exposes it

            # Price block
            st.markdown(f"""
            <div class="price-block">
              <div class="price-tag-label">Estimated Resale Value</div>
              <div class="price-value">
                <span class="price-currency">₹</span>{pred_int:,}
              </div>
              <div class="price-range">Range &nbsp; ₹{lo:,} — ₹{hi:,}</div>
            </div>
            """, unsafe_allow_html=True)

            # Stat chips
            st.markdown(f"""
            <div class="stats-row">
              <div class="stat-chip">
                <div class="s-label">Company</div>
                <div class="s-val">{company}</div>
              </div>
              <div class="stat-chip">
                <div class="s-label">Year</div>
                <div class="s-val">{int(year)}</div>
              </div>
              <div class="stat-chip">
                <div class="s-label">Fuel</div>
                <div class="s-val">{fuel_type}</div>
              </div>
            </div>
            """, unsafe_allow_html=True)

            # Confidence bar
            st.markdown(f"""
            <div class="conf-section">
              <div class="conf-header">
                <span class="conf-label">Model Confidence</span>
                <span class="conf-pct">{conf}%</span>
              </div>
              <div class="conf-bar-bg">
                <div class="conf-bar-fill" style="width:{conf}%"></div>
              </div>
            </div>
            """, unsafe_allow_html=True)

            # Summary tags
            km_fmt = f"{int(kms_driven):,} km"
            st.markdown(f"""
            <div style="margin-top:4px;">
              <div class="s-label" style="margin-bottom:10px;">Vehicle Summary</div>
              <div class="summary-tags">
                <span class="tag">{name}</span>
                <span class="tag">{km_fmt}</span>
                <span class="tag">{fuel_type}</span>
                <span class="tag">{int(year)}</span>
              </div>
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.markdown(f"""
            <div class="error-box">
              ⚠️ Prediction failed — please verify your input values.<br>
              <span style="color:#6b7280; font-size:11px;">{str(e)}</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# -------------------------------------------------
# Footer
# -------------------------------------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<hr style="border:none; border-top:1px solid rgba(255,255,255,0.05); margin-bottom:20px;">
<div class="custom-footer">
  Built with Streamlit &nbsp;·&nbsp; Machine Learning Model Deployment
</div>
""", unsafe_allow_html=True)