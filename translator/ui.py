import streamlit as st
from translator.language_map import LANGUAGES
from translator.translator import translate_text
from translator.text_to_speech import generate_tts_file  # ✅ updated import
from translator.clipboard import copy_to_clipboard
import os

def render_ui():
    st.set_page_config(page_title="Language Translator", page_icon="🌐", layout="centered")
    st.title("🌐 Language Translation Tool")

    st.markdown("""
    <style>
        label, .stTextArea label, .stSelectbox label {
            font-weight: 700;
            color: #1e88e5;  /* Bright Blue */
            font-size: 16px;
        }
        .stButton>button {
            background-color: #1e88e5;
            color: white;
            font-weight: bold;
            padding: 0.5rem 1rem;
            border-radius: 5px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("Translate text between multiple languages.")

    if 'translated' not in st.session_state:
        st.session_state.translated = ""

    text_input = st.text_area("Enter Text", height=150)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        src_lang = st.selectbox("Source Language", list(LANGUAGES.keys()), index=0)
    with col2:
        tgt_lang = st.selectbox("Target Language", list(LANGUAGES.keys()), index=1)
    with col3:
        if st.button("🔉 Download Input Speech"):
            if text_input.strip():
                file = generate_tts_file(text_input, LANGUAGES[src_lang])
                if file:
                    with open(file, "rb") as audio:
                        st.download_button("⬇️ Download Input MP3", audio, file_name="input_audio.mp3")
                    os.remove(file)
                else:
                    st.error("Failed to generate speech.")
            else:
                st.warning("No input text to speak.")

    if st.button("🔄 Translate"):
        if not text_input.strip():
            st.warning("Please enter some text first.")
        else:
            translated = translate_text(text_input, LANGUAGES[src_lang], LANGUAGES[tgt_lang])
            st.session_state.translated = translated

    if st.session_state.translated:
        st.text_area("Translated Text", st.session_state.translated, height=150)

        col4, col5 = st.columns(2)
        with col4:
            if st.button("📋 Copy Text"):
                copy_to_clipboard(st.session_state.translated)
                st.success("Copied to clipboard!")
        with col5:
            if st.button("🔉 Download Translated Speech"):
                file = generate_tts_file(st.session_state.translated, LANGUAGES[tgt_lang])
                if file:
                    with open(file, "rb") as audio:
                        st.download_button("⬇️ Download Translated MP3", audio, file_name="translated_audio.mp3")
                    os.remove(file)
                else:
                    st.error("Failed to generate speech.")
