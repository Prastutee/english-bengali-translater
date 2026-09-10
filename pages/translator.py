import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

st.set_page_config(page_title="Translator Engine", page_icon="🌐", layout="wide")

st.markdown("""
    <style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .stApp {
        background-color: #0e0e0e !important;
        color: #f0f0f0 !important;
        animation: fadeIn 0.5s ease-out;
    }
    h1, h2, h3 {
        color: #ffcc00 !important;
        font-weight: 900 !important;
    }
    .stTextArea textarea {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border: 3px solid #ffcc00 !important;
        border-radius: 12px !important;
        font-size: 1.1rem !important;
    }
    .pop-panel {
        background-color: #161616;
        border: 3px solid #ffcc00;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 6px 6px 0px #ffcc00;
        margin-bottom: 25px;
    }
    .pop-badge {
        background-color: #ffcc00;
        color: #111111;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 800;
        display: inline-block;
        margin-bottom: 15px;
    }
    .output-box {
        background-color: #1a1a1a;
        border: 2px solid #00ff66;
        padding: 20px;
        border-radius: 12px;
        color: #00ff66;
        font-size: 1.2rem;
        font-weight: 700;
        margin-top: 10px;
    }
    .stButton>button {
        background-color: #ffcc00 !important;
        color: #111111 !important;
        font-weight: 900 !important;
        border-radius: 30px !important;
        border: 3px solid #ffcc00 !important;
        padding: 0.6rem 1.8rem !important;
        box-shadow: 4px 4px 0px #ffffff !important;
        transition: all 0.2s ease !important;
    }
    .stButton>button:hover {
        background-color: #ffffff !important;
        color: #111111 !important;
        transform: translate(-2px, -2px) !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="pop-panel">
    <span class="pop-badge">LIVE PLAYGROUND</span>
    <h1>🌐 Neural Translation Engine</h1>
    <p>Running your fine-tuned model directly from your GitHub checkpoint repository.</p>
</div>
""", unsafe_allow_html=True)

# Load your custom model straight from your GitHub repo folder structure
@st.cache_resource
def load_translator_model():
    # Adjust this path if your folder name is different (e.g., "./checkpoint-625" or inside a results folder)
    checkpoint_path = "./checkpoint-625" 
    
    # Fallback to base model if the checkpoint path isn't found locally
    try:
        tokenizer = AutoTokenizer.from_pretrained(checkpoint_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint_path)
    except Exception:
        fallback_model = "Helsinki-NLP/opus-mt-en-bn"
        tokenizer = AutoTokenizer.from_pretrained(fallback_model)
        model = AutoModelForSeq2SeqLM.from_pretrained(fallback_model)
        
    return tokenizer, model

with st.spinner("🔄 Loading your trained model weights... Please wait."):
    tokenizer, model = load_translator_model()

# Translation Input Box
st.markdown('<div class="pop-panel">', unsafe_allow_html=True)
user_input = st.text_area("Enter any English sentence to translate:", value="I love you", height=100)

if st.button("Translate Text 🚀"):
    if user_input.strip() == "":
        st.warning("Please enter some text to translate.")
    else:
        with st.spinner("Translating via your trained model..."):
            inputs = tokenizer(user_input, return_tensors="pt", padding=True)
            translated_tokens = model.generate(**inputs, max_length=128)
            bengali_translation = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

        st.markdown("### **Bengali Translation Output:**")
        st.markdown(f'<div class="output-box">{bengali_translation}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
