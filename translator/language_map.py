# translator/language_map.py

from googletrans import LANGUAGES

# Capitalize first letter of each language name
LANGUAGES = {lang_name.capitalize(): lang_code for lang_code, lang_name in LANGUAGES.items()}
