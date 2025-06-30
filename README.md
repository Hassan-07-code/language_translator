# 🌐 Language Translation Tool

A modern, lightweight **language translator app** built using **Streamlit** and **Google Translate API**. It supports real-time translation between 100+ global languages, along with **text-to-speech** and **copy-to-clipboard** features — all in a clean, interactive UI.

---

## ✅ Features

- 🌍 Translate between 100+ world languages
- 🔠 Choose source & target languages
- 🎙️ Speak both input and translated text (TTS with correct accents)
- 📋 Copy translated text to clipboard
- 🎨 Clean Streamlit UI (modular & customizable)

---
## Project Structure
Language_Translation/
│
├── app.py                      # Entry point
├── requirements.txt            # Required packages
├── README.md                   # Project info
│
└── translator/
    ├── __init__.py
    ├── language_map.py         # Dynamic list of supported languages
    ├── translator.py           # Translation logic
    ├── text_to_speech.py       # Multilingual text-to-speech
    ├── clipboard.py            # Clipboard utility
    └── ui.py                   # Streamlit interface


---
## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/Hassan-07-code/Language_Translation.git
cd Language_Translation

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
"# language_translator" 
