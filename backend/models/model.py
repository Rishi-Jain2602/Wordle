from transformers import AutoTokenizer, AutoModel
import torch
from word_gen.eng_word import description_word_eng
from word_gen.hindi_word import description_word_hin
from gensim.test.utils import common_texts
from gensim.models import Word2Vec
import gensim.downloader as api
from translator.trans import translate_lang
import os
from models.keywords import common_keywords
model_path = "./models/word2vec.model"

if os.path.exists(model_path):
    model_word = Word2Vec.load(model_path)
    
else:
    model_word = Word2Vec(sentences=common_texts, vector_size=100, window=5, min_count=0, workers=4)
    model_word.save("word2vec.model")
    model_word = api.load('fasttext-wiki-news-subwords-300') 

if os.path.exists("./models/local_model") and os.path.exists("./models/local_tokenizer"):
    tokenizer = AutoTokenizer.from_pretrained("./models/local_tokenizer")
    model = AutoModel.from_pretrained("./models/local_model")

else:
    tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-multilingual-cased")
    tokenizer.save_pretrained("./models/local_tokenizer")
    model = AutoModel.from_pretrained("google-bert/bert-base-multilingual-cased")
    model.save_pretrained("./models/local_model")

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

# Word2 is target word and desc is description of the target word
# Word1 is the input/guess word by the user

def compare_words(word1,word2,desc,lang):
    if(lang == "English"):
        des_word1 = description_word_eng(word1)
        common_words = common_keywords(des_word1,desc)   
    elif(lang == "Hindi"):
        des_word1 = description_word_hin(word1)
        if des_word1:
            des_word1 = translate_lang(des_word1, "english")
        desc = translate_lang(desc, "english")
        common_words = common_keywords(des_word1, desc)     
    else:
        trans_eng = translate_lang(word1,"english")
        des_word1 = description_word_eng(trans_eng)
        desc = translate_lang(desc,"english")
        common_words = common_keywords(des_word1,desc)   

    if des_word1 and desc:
        word1_embedding = get_word_embedding(des_word1)
        word2_embedding = get_word_embedding(desc)
        similarity_score = cosine_similarity(word1_embedding, word2_embedding)
    else:
        similarity_score = get_word_similarity(word1,word2) 
    
    print(common_words)
    print(des_word1)
    print(desc)
    return [similarity_score.item() if similarity_score else 0.0,common_words]
