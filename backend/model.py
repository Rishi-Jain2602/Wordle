from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained("ai4bharat/indic-bert", use_fast=False)
model = AutoModel.from_pretrained("ai4bharat/indic-bert")

def get_word_embedding(word):
    inputs = tokenizer(word, return_tensors="pt")
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1)  

def cosine_similarity(embedding1, embedding2):
    return torch.nn.functional.cosine_similarity(embedding1, embedding2)

def compare_words(word1,word2):
    word1_embedding = get_word_embedding(word1)
    word2_embedding = get_word_embedding(word2)
    similarity_score = cosine_similarity(word1_embedding, word2_embedding)
    return similarity_score.item()
