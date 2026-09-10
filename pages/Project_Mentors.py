import streamlit as st

st.set_page_config(page_title="Project & Mentors", page_icon="🔬", layout="wide")

st.markdown("""
    <style>
    @keyframes popIn {
        0% { opacity: 0; transform: translateY(15px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    .stApp { background-color: #fcfcfc; color: #111111; animation: popIn 0.5s ease-out; }
    h1, h2, h3 { color: #111111 !important; font-weight: 900 !important; }
    .pop-panel {
        background-color: #ffffff; border: 4px solid #111111; border-radius: 20px; padding: 30px; box-shadow: 6px 6px 0px #111111; margin-bottom: 25px;
    }
    .pop-badge {
        background-color: #ffcc00; color: #111111; padding: 6px 14px; border-radius: 20px; font-weight: 800; border: 2px solid #111111; display: inline-block; margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="pop-panel">
    <span class="pop-badge">ACADEMIC OVERVIEW</span>
    <h1>🔬 Project Documentation & Mentors</h1>
    <p>Comprehensive report and system architecture for faculty evaluation at NIT Silchar.</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="pop-panel">
        <h3>👨‍🏫 Faculty Advisor</h3>
        <p><b>Prof. Guha</b></p>
        <p>Providing expert academic direction, model evaluation protocols, and NLP assessment guidelines.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="pop-panel">
        <h3>💻 Lead Researcher</h3>
        <p><b>Prastutee Borah</b></p>
        <p>Undergraduate Student, ECE Department<br><b>NIT Silchar</b></p>
    </div>
    """, unsafe_allow_html=True)
