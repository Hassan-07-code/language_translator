# translator/translator.py

from googletrans import Translator

def translate_text(text, src_lang, target_lang):
    try:
        translator = Translator()
        translated = translator.translate(text, src=src_lang, dest=target_lang)
        return translated.text
    except Exception as e:
        return f"❌ Translation failed: {str(e)}"
