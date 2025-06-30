# translator/text_to_speech.py

from gtts import gTTS
from playsound import playsound
import os
import uuid

def speak_text(text, lang_code='en'):
    try:
        tts = gTTS(text=text, lang=lang_code)
        filename = f"temp_audio_{uuid.uuid4()}.mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print(f"[TTS ERROR]: {e}")
