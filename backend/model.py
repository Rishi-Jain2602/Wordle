from transformers import AutoTokenizer, AutoModel
import torch
from word_gen.eng_word import description_word_eng
from word_gen.hindi_word import description_word_hin
from gensim.test.utils import common_texts
from gensim.models import Word2Vec
import gensim.downloader as api
import os
model_path = "word2vec.model"

if os.path.exists(model_path):
    print("Loading saved Word2Vec model...")
    model_word = Word2Vec.load(model_path)
    print("inside model_word")
else:
    print("Training a new Word2vec model....")
    model_word = Word2Vec(sentences=common_texts, vector_size=100, window=5, min_count=0, workers=4)
    model_word.save("word2vec.model")
    model_word = api.load('fasttext-wiki-news-subwords-300') 

if os.path.exists("./local_model") and os.path.exists("./local_tokenizer"):
    tokenizer = AutoTokenizer.from_pretrained("./local_tokenizer")
    model = AutoModel.from_pretrained("./local_model")
    print("Inside local bert model")
else:
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-multilingual-cased")
    tokenizer.save_pretrained("./local_tokenizer")
    model = AutoModel.from_pretrained("distilbert-base-multilingual-cased")
    model.save_pretrained("./local_model")

def get_word_embedding(word):
    inputs = tokenizer(word, return_tensors="pt")
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)  

def cosine_similarity(embedding1, embedding2):
    return torch.nn.functional.cosine_similarity(embedding1, embedding2)

def get_word_similarity(word1, word2):
  try:
    word1_emb = model_word.wv.get_vector(word1)
    word2_emb = model_word.wv.get_vector(word2)
    similarity = model_word.wv.cosine_similarities(word1_emb, word2_emb)
    return similarity
  except KeyError as e:
    print(f"Error: {e}. One or both words not found in the model's vocabulary.")
    return None

def compare_words(word1,word2,lang):
    if(lang == "eng"):
        des_word1 = description_word_eng(word1)
        des_word2 = description_word_eng(word2)
    elif (lang == "hin"):
        des_word1 = description_word_hin(word1)
        des_word2 = description_word_hin(word2)
    
    if des_word1 and des_word2:
        word1_embedding = get_word_embedding(des_word1)
        word2_embedding = get_word_embedding(des_word2)
        similarity_score = cosine_similarity(word1_embedding, word2_embedding)
    else:
        similarity_score = get_word_similarity(word1,word2)    
    return similarity_score.item() if similarity_score else 0.0
