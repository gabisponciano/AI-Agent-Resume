import streamlit as st
import requests

st.set_page_config(
    page_title="AICV — CV Intelligence",
    page_icon="✦",
    layout="centered",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,500;1,400&family=Inter:wght@300;400;500&display=swap');

/* ── Base ── */
html, body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background-color: #F4F6F7 !important;
    color: #1C3A3F !important;
    font-family: 'Inter', sans-serif !important;
}

[data-testid="stMain"] .block-container {
    max-width: 680px !important;
    padding: 3.5rem 2rem 5rem !important;
}

/* ── Header ── */
.main-header {
    text-align: center;
    padding-bottom: 2.75rem;
    margin-bottom: 2.5rem;
    border-bottom: 1.5px solid #D0DFE2;
}

.main-header .eyebrow {
    font-size: 0.6rem;
    letter-spacing: 0.28em;
    text-transform: uppercase;
    color: #2E7D8A;
    margin-bottom: 1.1rem;
    font-weight: 500;
}

.main-header h1 {
    font-family: 'Lora', serif;
    font-size: clamp(2.4rem, 5.5vw, 3.6rem);
    font-weight: 400;
    line-height: 1.12;
    color: #0F2A2F;
    margin: 0 0 0.9rem;
    letter-spacing: -0.01em;
}

.main-header h1 em {
    font-style: italic;
    color: #2E7D8A;
}

.main-header .subtitle {
    font-size: 0.87rem;
    color: #7A9EA5;
    font-weight: 300;
    line-height: 1.7;
    max-width: 380px;
    margin: 0 auto;
}

/* ── Section label ── */
.section-label {
    font-size: 0.58rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #2E7D8A;
    font-weight: 500;
    margin-bottom: 0.65rem;
}

/* ── Cards ── */
.card {
    background: #FFFFFF;
    border: 1px solid #D0DFE2;
    border-radius: 12px;
    padding: 1.75rem;
    margin-bottom: 1rem;
    box-shadow: 0 1px 4px rgba(14, 42, 47, 0.05);
}

/* ── File uploader ── */
[data-testid="stFileUploader"] {
    background: transparent !important;
    border: none !important;
}

[data-testid="stFileUploaderDropzone"] {
    background: #F9FBFC !important;
    border: 1.5px dashed #B2CDD3 !important;
    border-radius: 10px !important;
    transition: border-color 0.2s, background 0.2s !important;
}

[data-testid="stFileUploaderDropzone"]:hover {
    border-color: #2E7D8A !important;
    background: #EEF5F7 !important;
}

[data-testid="stFileUploaderDropzone"] * {
    color: #7A9EA5 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.82rem !important;
}

[data-testid="stFileUploader"] label {
    display: none !important;
}

[data-testid="stFileUploaderFile"] {
    background: #EEF5F7 !important;
    border: 1px solid #B2CDD3 !important;
    border-radius: 8px !important;
    color: #2E7D8A !important;
    font-size: 0.8rem !important;
}

/* ── Buttons ── */
[data-testid="stButton"] > button {
    background: #2E7D8A !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 7px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.72rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    padding: 0.6rem 1.6rem !important;
    cursor: pointer !important;
    transition: background 0.2s, transform 0.15s, box-shadow 0.2s !important;
    box-shadow: 0 2px 8px rgba(46, 125, 138, 0.25) !important;
    white-space: nowrap !important;
}

[data-testid="stButton"] > button:hover {
    background: #256b77 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 14px rgba(46, 125, 138, 0.3) !important;
}

[data-testid="stButton"] > button:active {
    transform: translateY(0) !important;
    box-shadow: 0 1px 4px rgba(46, 125, 138, 0.2) !important;
}

/* ── Text input ── */
[data-testid="stTextInput"] input {
    background: #FFFFFF !important;
    border: 1.5px solid #D0DFE2 !important;
    border-radius: 8px !important;
    color: #1C3A3F !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.88rem !important;
    padding: 0.75rem 1rem !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
    box-shadow: 0 1px 3px rgba(14, 42, 47, 0.04) !important;
}

[data-testid="stTextInput"] input:focus {
    border-color: #2E7D8A !important;
    box-shadow: 0 0 0 3px rgba(46, 125, 138, 0.1) !important;
}

[data-testid="stTextInput"] input::placeholder {
    color: #B2CDD3 !important;
}

[data-testid="stTextInput"] label {
    display: none !important;
}

/* ── Divider ── */
.divider {
    height: 1.5px;
    background: #D0DFE2;
    margin: 2.25rem 0;
    border-radius: 2px;
}

/* ── Result card ── */
.result-card {
    background: #FFFFFF;
    border: 1px solid #D0DFE2;
    border-left: 3px solid #2E7D8A;
    border-radius: 12px;
    padding: 2rem 2.25rem;
    margin-top: 1.25rem;
    box-shadow: 0 2px 10px rgba(14, 42, 47, 0.06);
    animation: fadeUp 0.3s ease;
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
}

.result-tag {
    display: inline-block;
    font-size: 0.57rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    background: #EEF5F7;
    color: #2E7D8A;
    padding: 0.25rem 0.75rem;
    border-radius: 100px;
    font-weight: 500;
    margin-bottom: 1.1rem;
    border: 1px solid #B2CDD3;
}

.result-body {
    font-size: 0.9rem;
    line-height: 1.85;
    color: #3A5F65;
    font-weight: 300;
}

/* ── Success / warning / error ── */
[data-testid="stAlert"] {
    border-radius: 8px !important;
    font-size: 0.84rem !important;
    font-family: 'Inter', sans-serif !important;
}

/* ── Spinner ── */
[data-testid="stSpinner"] p {
    font-size: 0.8rem !important;
    color: #7A9EA5 !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #F4F6F7; }
::-webkit-scrollbar-thumb { background: #B2CDD3; border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: #2E7D8A; }

/* ── Hide chrome + sidebar ── */
#MainMenu, footer, [data-testid="stToolbar"],
[data-testid="stSidebar"], [data-testid="collapsedControl"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# ── API ───────────────────────────────────────────────────────────────────────
API_UPLOAD   = "http://localhost:8000/ai_agent/file_upload"
API_QUESTION = "http://localhost:8000/ai_agent/ai_expert"

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <div class="eyebrow">✦ Career Intelligence</div>
    <h1>Elevate your<br><em>résumé</em></h1>
    <p class="subtitle">Upload your CV and ask anything — structure, tone,
    keywords, role-specific improvements.</p>
</div>
""", unsafe_allow_html=True)

# ── Step 1 — Upload ───────────────────────────────────────────────────────────
st.markdown('<div class="section-label">① Upload your résumé</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("résumé", type=["pdf"])

if uploaded_file is not None:
    col_name, col_btn = st.columns([3, 1])
    with col_name:
        st.markdown(f"""
        <div style="
            background:#EEF5F7;border:1px solid #B2CDD3;border-radius:8px;
            padding:0.6rem 1rem;font-size:0.8rem;color:#2E7D8A;
            display:flex;align-items:center;gap:0.5rem;
        ">
            <span style="background:#2E7D8A;color:#fff;font-size:0.55rem;
                font-weight:600;padding:0.15rem 0.4rem;border-radius:4px;
                letter-spacing:0.05em;">PDF</span>
            <span style="color:#3A5F65;">{uploaded_file.name}</span>
        </div>
        """, unsafe_allow_html=True)
    with col_btn:
        if st.button("Upload →"):
            files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
            with st.spinner("Uploading…"):
                try:
                    resp = requests.post(API_UPLOAD, files=files)
                    if resp.status_code == 200:
                        st.success("Uploaded successfully!")
                    else:
                        st.error(f"Failed: {resp.text}")
                except Exception as e:
                    st.error(f"Connection error: {e}")

# ── Divider ───────────────────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ── Step 2 — Question ─────────────────────────────────────────────────────────
st.markdown('<div class="section-label">② Ask for a recommendation</div>', unsafe_allow_html=True)

question = st.text_input(
    "question",
    placeholder="e.g. How can I improve my experience section for a senior engineering role?",
)

if st.button("Get recommendation →"):
    if not question:
        st.warning("Please type a question first.")
    else:
        with st.spinner("Analyzing your résumé…"):
            try:
                resp = requests.post(API_QUESTION, params={"question": question})
                if resp.status_code == 200:
                    result = resp.json()
                    answer = result.get("response", resp.text)
                    st.markdown(f"""
                    <div class="result-card">
                        <div class="result-tag">AI Recommendation</div>
                        <div class="result-body">{answer}</div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error(f"Error {resp.status_code}: {resp.text}")
            except Exception as e:
                st.error(f"Connection error: {e}")