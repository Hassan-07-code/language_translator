# translator/clipboard.py

import pyperclip

def copy_to_clipboard(text):
    try:
        pyperclip.copy(text)
    except Exception as e:
        print(f"[CLIPBOARD ERROR]: {e}")
