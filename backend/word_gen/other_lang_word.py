from translator.trans import translate_lang
from word_gen.eng_word import get_random_english_word

def get_random_other_lang_word(lang,category, retry_count=3):
    response = get_random_english_word(category)
    
    if response is None :
        if retry_count > 0:
            return get_random_other_lang_word(lang, category, retry_count - 1)
        else:
            return {"message": "Error: Failed to generate a word after multiple attempts."}
    
    word = translate_lang(response[0],lang)
    description = translate_lang(response[1],lang)
    similar_word = response[2]
    similar_word_other_lang = []
    i = 0
    for words in similar_word:
        if i < 2:
            i += 1
            similar_word_other_lang.append(translate_lang(words, lang))
        else:
            break
    return [word,description,similar_word_other_lang]