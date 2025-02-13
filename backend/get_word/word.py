from word_gen.eng_word import get_random_english_word 
from word_gen.other_lang_word import get_random_other_lang_word


def generate_word(lang,category,cnt = 3):
    if lang.lower() == "English":
        response = get_random_english_word(category)
    else:
        response = get_random_other_lang_word(lang,category)
    
    if response is None and cnt > 0:
        return generate_word(lang, category, cnt - 1)
    
    return response if response is not None else None