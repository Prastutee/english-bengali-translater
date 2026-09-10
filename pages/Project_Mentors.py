import streamlit as st

st.set_page_config(page_title="Project Documentation", page_icon="🔬", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e0e0e; color: #ffffff; }
    h1, h2, h3 { color: #ffcc00 !important; }
    .profile-card {
        background-color: #1a1a1a; border-left: 5px solid #ffcc00; padding: 20px; border-radius: 5px; margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔬 Project Documentation & Academic Overview")
st.markdown("### Comprehensive Report for Faculty Review")

st.markdown("""
<div class="profile-card">
    <h3>📋 Abstract & System Architecture</h3>
    <p>This project implements an advanced Low-Rank Adaptation (LoRA) fine-tuned Neural Machine Translation (NMT) framework tailored for English-to-Bengali translation. Built upon the <code>Helsinki-NLP/opus-mt-en-inc</code> base architecture and utilizing fine-tuned weights from <code>checkpoint-625</code>, the model achieves superior contextual fluency and linguistic precision.</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown("""
    <div class="profile-card">
        <h3>👨‍🏫 Faculty Advisor</h3>
        <p><b>Prof. Guha</b></p>
        <p>Providing expert academic direction, supervising model evaluation protocols, and reviewing natural language processing benchmarks.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="profile-card">
        <h3>💻 Lead Developer & Researcher</h3>
        <p><b>Prastutee Borah</b></p>
        <p>Undergraduate Student, Department of Electronics and Communication Engineering (ECE)<br>National Institute of Technology (NIT) Silchar</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("### ⚡ Core Technical Features Included")
st.markdown("""
1. **Multi-Page Responsive Layout:** Separates heavy workflows cleanly across dedicated views, preventing screen crowding on mobile phones and laptops.
2. **Interactive Quick-Select Chips:** Enables instant touch/click sentence testing during live evaluations.
3. **Side-by-Side Comparative Engine:** Directly contrasts stock base performance against LoRA <code>checkpoint-625</code>.
4. **Persistent History Audit Log:** Tracks all trial inputs and session outputs safely in state tables.
""")
