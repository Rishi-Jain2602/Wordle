import random
import pyiwn
from pyiwn import Language
from categories.category import random_species
from translator.trans import translate_lang
iwn = pyiwn.IndoWordNet(lang=Language.HINDI)

def get_random_hindi_word(category):
    word = random_species(category)
    word = translate_lang(word,"hindi")
    all_synsets = iwn.all_synsets()
    words = []
    similar_words = []
    for synset in all_synsets:
        for lemma in synset.lemmas():
            if word.lower() in synset.gloss().lower(): #Check if category is present in gloss
              words.append(lemma.name())
              for similar_lemma in synset.lemmas():
                    similar_words.append(similar_lemma.name())
    
    hindi_word = random.choice(words)
    hindi_def = description_word_hin(hindi_word)
    if words:
        return [hindi_word,hindi_def,similar_words]
    else:
        return None
def description_word_hin(word):
    synsets = iwn.synsets(word)
    if synsets:
        description = synsets[0].gloss() or synsets[0].examples()
        if not description:
            hypernyms = synsets[0].hypernyms()
            if hypernyms:
                description = [h.lemmas()[0].name() for h in hypernyms] 

        if not description:
            description = word
        return description
    else:
        return None
    
def random_word(category):
    word_data = get_random_hindi_word(category)  
    if word_data:
        hindi_word = word_data[0]  
        definition = word_data[1]  
        return {"random_hindi_word": hindi_word, "description": definition}  
    else:
        return {"message": f"No Hindi words of length found."}
