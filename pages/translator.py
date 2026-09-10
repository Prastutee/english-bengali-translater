import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from peft import PeftModel
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="NMT Translator Engine", page_icon="🌐", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e0e0e; color: #ffffff; }
    h1, h2, h3 { color: #ffcc00 !important; }
    .stButton>button {
        background-color: #ffcc00; color: #000000; font-weight: bold; border-radius: 8px; border: none;
    }
    .stButton>button:hover { background-color: #ffffff; color: #000000; }
    .comparison-box { background-color: #161616; border: 1px solid #333333; padding: 20px; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state.history = []

st.title("🌐 Neural Machine Translation Engine")
st.markdown("### Comparative English to Bengali Evaluation Framework")

# Quick-Select Example Chips (Responsive Grid)
st.markdown("#### 💡 Quick-Select Example Sentences")
ex_col1, ex_col2, ex_col3, ex_col4 = st.columns(4, gap="small")

selected_example = ""
if ex_col1.button("How are you?"):
    selected_example = "How are you?"
if ex_col2.button("Where is the station?"):
    selected_example = "Where is the station?"
if ex_col3.button("Technology is changing fast."):
    selected_example = "Technology is changing fast."
if ex_col4.button("Research proposal"):
    selected_example = "The research proposal on neural machine translation shows exceptional promise."

english_text = st.text_area(
    "Enter English Source Text:", 
    value=selected_example if selected_example else "The research proposal on neural machine translation shows exceptional promise.", 
    height=110
)

col_set1, col_set2 = st.columns([2, 1])
with col_set1:
    beam_search = st.checkbox("Enable Beam Search Decoding", value=True)
with col_set2:
    max_len = st.slider("Max Output Length", 32, 256, 128)

@st.cache_resource
def load_models():
    base_model_name = "Helsinki-NLP/opus-mt-en-inc"
    adapter_path = "./checkpoint-625"
    tokenizer = AutoTokenizer.from_pretrained(base_model_name)
    base_model = AutoModelForSeq2SeqLM.from_pretrained(base_model_name)
    lora_model = PeftModel.from_pretrained(base_model, adapter_path)
    lora_model.eval()
    base_model.eval()
    return tokenizer, base_model, lora_model

with st.spinner("⚡ Loading model checkpoints..."):
    tokenizer, base_model, lora_model = load_models()

if st.button("🚀 Run Translation & Comparison", use_container_width=True):
    if english_text.strip():
        inputs = tokenizer(english_text, return_tensors="pt", padding=True)
        num_beams = 4 if beam_search else 1
        
        base_outputs = base_model.generate(**inputs, max_length=max_len, num_beams=num_beams)
        base_translation = tokenizer.decode(base_outputs[0], skip_special_tokens=True)
        
        lora_outputs = lora_model.generate(**inputs, max_length=max_len, num_beams=num_beams)
        lora_translation = tokenizer.decode(lora_outputs[0], skip_special_tokens=True)
        
        st.markdown("---")
        st.markdown("### ⚖️ Side-by-Side Model Evaluation")
        comp_col1, comp_col2 = st.columns(2, gap="medium")
        
        with comp_col1:
            st.markdown(f"""
            <div class="comparison-box">
                <h4 style="color: #ff9999;">📉 Base Model (Helsinki-NLP)</h4>
                <p style="font-size: 1.05rem;">{base_translation}</p>
            </div>
            """, unsafe_allow_html=True)
            
        with comp_col2:
            st.markdown(f"""
            <div class="comparison-box" style="border: 2px solid #ffcc00;">
                <h4 style="color: #ffcc00;">📈 Fine-Tuned LoRA (Checkpoint-625)</h4>
                <p style="font-size: 1.05rem; font-weight: bold;">{lora_translation}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.success("✨ Fine-tuned model output successfully generated!")

        timestamp = datetime.now().strftime("%H:%M:%S")
        st.session_state.history.insert(0, {
            "Time": timestamp,
            "Source (EN)": english_text,
            "Base Output": base_translation,
            "LoRA Output": lora_translation
        })
    else:
        st.warning("Please input text to translate.")

if st.session_state.history:
    st.markdown("---")
    st.markdown("### 📜 Session Translation History Log")
    st.dataframe(pd.DataFrame(st.session_state.history), use_container_width=True)
    if st.button("🗑️ Clear History Log"):
        st.session_state.history = []
        st.rerun()
