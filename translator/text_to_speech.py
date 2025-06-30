# translator/text_to_speech.py

from gtts import gTTS
import uuid
import os

def generate_tts_file(text, lang_code='en'):
    """
    Generate a downloadable MP3 file from input text using gTTS.
    Returns the filename if successful, None otherwise.
    """
    try:
        filename = f"tts_{uuid.uuid4()}.mp3"
        tts = gTTS(text=text, lang=lang_code)
        tts.save(filename)
        return filename
    except Exception as e:
        print(f"[TTS ERROR]: {e}")
        return None
