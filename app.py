import streamlit as st

st.set_page_config(
    page_title="English-Bengali NMT Portal",
    page_icon="⚡",
    layout="wide"
)

# Poppy Studio Theme: Yellow (#FFCC00), Deep Black (#0a0a0a), Pure White (#ffffff)
st.markdown("""
    <style>
    @keyframes floatCard {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
        100% { transform: translateY(0px); }
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(15px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .stApp {
        background-color: #ffffff;
        color: #0a0a0a;
        animation: fadeIn 0.7s ease-out;
    }
    h1, h2, h3 {
        color: #0a0a0a !important;
        font-weight: 800 !important;
    }
    .hero-banner {
        background: #FFCC00;
        border: 3px solid #0a0a0a;
        padding: 45px;
        border-radius: 20px;
        text-align: left;
        box-shadow: 6px 6px 0px #0a0a0a;
        margin-bottom: 30px;
        animation: fadeIn 0.8s ease-out;
    }
    .feature-card {
        background-color: #f9f9f9;
        border: 2px solid #0a0a0a;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 4px 4px 0px #0a0a0a;
        transition: all 0.3s ease;
        animation: fadeIn 0.9s ease-out;
        height: 100%;
    }
    .feature-card:hover {
        transform: translateY(-6px);
        box-shadow: 8px 8px 0px #0a0a0a;
        background-color: #FFCC0022;
    }
    .stButton>button {
        background-color: #0a0a0a !important;
        color: #FFCC00 !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        border: 2px solid #0a0a0a !important;
        padding: 0.6rem 1.2rem !important;
        box-shadow: 3px 3px 0px #FFCC00;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #FFCC00 !important;
        color: #0a0a0a !important;
        box-shadow: 3px 3px 0px #0a0a0a;
        transform: translate(-2px, -2px);
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-banner">
    <span style="background-color: #0a0a0a; color: #FFCC00; padding: 6px 14px; border-radius: 20px; font-weight: 700; font-size: 0.85rem;">⚡ NMT STUDIO PROJECT</span>
    <h1 style="font-size: 2.8rem; margin-top: 15px;">Collaborate Smarter. Translate Faster.</h1>
    <p style="font-size: 1.2rem; font-weight: 500; color: #222222;">Advanced LoRA Fine-Tuned English-to-Bengali Transformer Architecture for Faculty Evaluation.</p>
    <hr style="border: 1px solid #0a0a0a; margin: 20px 0;">
    <p style="margin: 0; font-weight: 600;"><b>Lead Researcher:</b> Prastutee Borah &nbsp;|&nbsp; <b>Faculty Mentor:</b> Prof. Guha</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### 🚀 Explore Studio Portals")
st.write("Select a module below or use the sidebar to navigate seamlessly across mobile and desktop screens:")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🌐 Translator Engine</h3>
        <p>Experience the interactive playground equipped with quick-select chips, session translation history logs, and direct side-by-side model evaluation.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Launch Translator Playground ➔", use_container_width=True):
        st.switch_page("pages/1_Translator.py")

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🔬 Project & Mentors</h3>
        <p>Review comprehensive technical documentation, architecture abstracts, performance benchmarks, and dedicated mentor credits.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open Documentation Hub ➔", use_container_width=True):
        st.switch_page("pages/2_Project_Mentors.py")
