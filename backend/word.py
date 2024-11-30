from nltk.corpus import wordnet as wn
import random
import nltk
import requests
nltk.download('wordnet')

def get_random_english_word(length=5):
    all_synsets = list(wn.all_synsets())
    five_letter_words = [lemma.name() for synset in all_synsets for lemma in synset.lemmas() if len(lemma.name()) == length]
    return random.choice(five_letter_words) if five_letter_words else None

def get_random_hindi_word():
    response = requests.get("https://random-hindi-word.onrender.com/random_hindi_word/")
    if response.status_code == 200:
        return response.json().get("random_hindi_word", "").strip()  
    return None