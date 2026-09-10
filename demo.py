import streamlit as st

st.set_page_config(
    page_title="English-Bengali NMT Portal",
    page_icon="⚡",
    layout="wide"
)

st.markdown("""
    <style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .stApp {
        background-color: #0e0e0e;
        color: #ffffff;
        animation: fadeIn 0.8s ease-out;
    }
    h1, h2, h3 {
        color: #ffcc00 !important;
    }
    .hero {
        background: linear-gradient(135deg, #1a1a1a 0%, #000000 100%);
        border: 2px solid #ffcc00;
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 0 20px rgba(255, 204, 0, 0.2);
    }
    .nav-card {
        background-color: #1a1a1a;
        border: 1px solid #333333;
        padding: 25px;
        border-radius: 10px;
        text-align: center;
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .nav-card:hover {
        transform: translateY(-5px);
        border-color: #ffcc00;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>⚡ English to Bengali Neural Machine Translation</h1>
    <p style="font-size: 1.2rem; color: #cccccc;">Advanced LoRA Fine-Tuned Transformer System for Academic Evaluation</p>
    <hr style="border-color: #ffcc00;">
    <p><b>Lead Researcher:</b> Prastutee Borah | <b>Mentor:</b> Prof. Guha</p>
    <p><b>Institution:</b> National Institute of Technology (NIT) Silchar</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 🚀 Choose a Portal Section Below")
st.write("Use the interactive cards below or the left sidebar icons to navigate seamlessly across pages:")

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown("""
    <div class="nav-card">
        <h3>🌐 Translator Engine</h3>
        <p>Access the interactive playground with quick-select example chips, history audit logs, and side-by-side base vs. fine-tuned evaluation.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Translator Page", use_container_width=True):
        st.switch_page("pages/1_🌐_Translator.py")

with col2:
    st.markdown("""
    <div class="nav-card">
        <h3>🔬 Project & Mentors</h3>
        <p>Explore detailed technical documentation, architecture abstracts, system performance metrics, and advisory credits for Prof. Guha.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Documentation Page", use_container_width=True):
        st.switch_page("pages/2_🔬_Project_&_Mentors.py")


