from nltk.corpus import wordnet as wn
import random
import nltk
from categories.category import random_species
from word_gen.mistral_desc import description
nltk.download('wordnet')

def description_word_eng(word):
    synsets = wn.synsets(word)
    if synsets:
        return synsets[0].definition()
    else:
        return None

def get_random_english_word(category):
    word = random_species(category)
    try:
        synsets = wn.synsets(word)
        if synsets:
            hyponyms = []
            for synset in synsets:
                for hyponym in synset.hyponyms():
                  for lemma in hyponym.lemmas():
                    hyponyms.append(lemma.name())
            sampled_hyponym = random.sample(hyponyms,2)
            desc = description(word)
            hint = description_word_eng(category)
            result = [word, desc, sampled_hyponym,hint]
            return result
        else:
            return None
    except Exception as e:
      print(f"An error occurred: {e}")
      return None
    
