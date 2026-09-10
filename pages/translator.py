import streamlit as st

st.set_page_config(page_title="Translator Engine", page_icon="🌐", layout="wide")

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
    .stButton>button {
        background-color: #111111 !important; color: #ffcc00 !important; font-weight: 900 !important; border-radius: 30px !important; border: 3px solid #111111 !important; box-shadow: 4px 4px 0px #ffcc00 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="pop-panel">
    <span class="pop-badge">LIVE PLAYGROUND</span>
    <h1>🌐 Neural Translation Engine</h1>
    <p>Input English text below or click a quick-select chip to test your LoRA fine-tuned model performance.</p>
</div>
""", unsafe_allow_html=True)

# Interactive Playground UI Box
with st.container():
    st.markdown('<div class="pop-panel">', unsafe_allow_html=True)
    text_input = st.text_area("Enter English Text:", "Machine learning models transform how we communicate across languages.")
    if st.button("Translate Text 🚀"):
        st.markdown("### **Bengali Output:**")
        st.success("মেশিন লার্নিং মডেলগুলি আমরা কীভাবে ভাষা জুড়ে যোগাযোগ করি তা রূপান্তরিত করে। (Simulated LoRA Output)")
    st.markdown('</div>', unsafe_allow_html=True)
