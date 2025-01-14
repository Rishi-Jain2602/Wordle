from transformers import AutoTokenizer, AutoModel
import torch
# from word_gen.hindi_word import description_word_hin
from word_gen.mistral_desc import description
from translator.trans import translate_lang
import os
from models.keywords import common_keywords

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

def compare_words(word1,word2,desc,lang):
    if(lang == "English"):
        des_word1 = description(word1)
        common_words = common_keywords(des_word1,desc)   
    # elif(lang == "Hindi"):
    #     des_word1 = description_word_hin(word1)
    #     if des_word1:
    #         des_word1 = translate_lang(des_word1, "english")
    #     else:
    #         word1 = translate_lang(word1, "english")
    #         des_word1 = description(word1)

    #     desc = translate_lang(desc, "english")
    #     common_words = common_keywords(des_word1, desc)     
    else:
        trans_eng = translate_lang(word1,"english")
        des_word1 = description(trans_eng)
        desc = translate_lang(desc,"english")
        common_words = common_keywords(des_word1,desc)   

    if des_word1 and desc:
        word1_embedding = get_word_embedding(des_word1)
        word2_embedding = get_word_embedding(desc)
        similarity_score = cosine_similarity(word1_embedding, word2_embedding)
    
    return [similarity_score.item() if similarity_score else 0.0,common_words]
