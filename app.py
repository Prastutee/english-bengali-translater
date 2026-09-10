import streamlit as st

st.set_page_config(
    page_title="LinguaPulse | EN-BN NMT Portal",
    page_icon="⚡",
    layout="wide"
)

st.markdown("""
    <style>
    @keyframes popIn {
        0% { opacity: 0; transform: scale(0.95) translateY(20px); }
        100% { opacity: 1; transform: scale(1) translateY(0); }
    }
    .stApp {
        background-color: #fcfcfc;
        color: #111111;
        animation: popIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    h1, h2, h3 {
        color: #111111 !important;
        font-weight: 900 !important;
        letter-spacing: -0.5px;
    }
    .pop-hero {
        background: #ffcc00;
        border: 4px solid #111111;
        border-radius: 28px;
        padding: 50px 40px;
        box-shadow: 10px 10px 0px #111111;
        margin-bottom: 40px;
    }
    .pop-card {
        background-color: #ffffff;
        border: 4px solid #111111;
        border-radius: 22px;
        padding: 35px 30px;
        box-shadow: 7px 7px 0px #111111;
        transition: all 0.3s ease;
        height: 100%;
    }
    .pop-card:hover {
        transform: translate(-4px, -4px);
        box-shadow: 11px 11px 0px #ffcc00, 11px 11px 0px 4px #111111;
    }
    .pop-badge {
        background-color: #111111;
        color: #ffcc00;
        padding: 8px 18px;
        border-radius: 30px;
        font-size: 0.85rem;
        font-weight: 800;
        display: inline-block;
        margin-bottom: 20px;
    }
    .meta-tag {
        background-color: #ffffff;
        border: 2px solid #111111;
        padding: 6px 14px;
        border-radius: 15px;
        font-weight: 700;
        display: inline-block;
        margin-right: 10px;
        color: #111111;
        box-shadow: 3px 3px 0px #111111;
    }
    .stButton>button {
        background-color: #111111 !important;
        color: #ffcc00 !important;
        font-weight: 900 !important;
        border-radius: 40px !important;
        border: 3px solid #111111 !important;
        padding: 0.7rem 1.8rem !important;
        box-shadow: 5px 5px 0px #ffcc00 !important;
        transition: all 0.2s ease !important;
    }
    .stButton>button:hover {
        background-color: #ffcc00 !important;
        color: #111111 !important;
        transform: translate(-3px, -3px) !important;
        box-shadow: 7px 7px 0px #111111 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="pop-hero">
    <div class="pop-badge">⚡ NIT Silchar Research Portal</div>
    <h1>English-to-Bengali Neural Machine Translation Engine</h1>
    <p style="font-size: 1.25rem; font-weight: 600;">Experience high-precision Low-Rank Adaptation (LoRA) fine-tuned transformer architectures built for superior linguistic preservation.</p>
    <div>
        <span class="meta-tag">👩‍💻 Lead: Prastutee Borah</span>
        <span class="meta-tag">👨‍🏫 Mentor: Prof. Guha</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("### 🎯 System Navigation Workspace")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="pop-card">
        <span class="pop-badge">Module 01</span>
        <h3>🌐 Translator Playground</h3>
        <p>Test real-time neural translations, pick from quick-select chips, examine audit history logs, and compare model outputs.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Launch Translator Engine ➔", use_container_width=True):
        st.switch_page("pages/translator.py")

with col2:
    st.markdown("""
    <div class="pop-card">
        <span class="pop-badge">Module 02</span>
        <h3>🔬 Project & Mentors</h3>
        <p>Review comprehensive architecture abstracts, evaluation metrics, system workflows, and formal faculty credits for Prof. Guha.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Open Documentation Hub ➔", use_container_width=True):
        st.switch_page("pages/documentation.py")
