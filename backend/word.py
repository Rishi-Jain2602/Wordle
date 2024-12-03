from nltk.corpus import wordnet as wn
import random
import nltk
import requests
nltk.download('wordnet')
import pyiwn
def description_word(word):
    synsets = wn.synsets(word)
    if synsets:
        return synsets[0].definition()
    else:
        return None

def get_random_english_word(category):
    try:
        synsets = wn.synsets(category)
        if synsets:
            hyponyms = []
            for synset in synsets:
                for hyponym in synset.hyponyms():
                  for lemma in hyponym.lemmas():
                    hyponyms.append(lemma.name())
            sampled_hyponym = random.sample(hyponyms,1)[0]
            other_hypo = random.sample([h for h in hyponyms if h != sampled_hyponym], 4)
            description = description_word(sampled_hyponym)
            result = [sampled_hyponym, description, other_hypo]
            return result
        else:
            return None
    except Exception as e:
      print(f"An error occurred: {e}")
      return None

def get_random_hindi_word():
    response = requests.get("https://random-hindi-word.onrender.com/random_hindi_word/")
    if response.status_code == 200:
        return [response.json().get("random_hindi_word", "").strip(),response.json().get("description","").strip()]  
    return None

# iwn = pyiwn.IndoWordNet(lang=pyiwn.Language.HINDI)

# def get_random_hindi_word_new(length=5):
#     all_synsets = list(iwn.all_synsets())
#     five_letter_words = [(synset._head_word, synset._gloss) for synset in all_synsets]
#     return random.choice(five_letter_words) if five_letter_words else None
# print(get_random_english_word('eagle'))