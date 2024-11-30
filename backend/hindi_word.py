# I faced some problems locally while working with IndoWordNet that I couldn't resolve. 
# As a result, this file was deployed differently on Render, in a separate directory.
# API Endpoint: https://random-hindi-word.onrender.com/random_hindi_word/

# from fastapi import FastAPI
# import uvicorn
# import random
# import pyiwn
# from pyiwn import Language
# app = FastAPI()

# iwn = pyiwn.IndoWordNet(lang=Language.HINDI)

# def get_random_hindi_word(length=5):
#     all_synsets = iwn.all_synsets()
#     words = []
#     for synset in all_synsets:
#         for lemma in synset.lemmas():
#             if len(lemma.name()) == length:
#                 words.append(lemma.name())
#     if words:
#         return random.choice(words)
#     else:
#         return None

# @app.get("/random_hindi_word/")
# async def random_word(length: int = 5):
#     word = get_random_hindi_word(length)
#     if word:
#         return {"random_hindi_word": word}
#     else:
#         return {"message": f"No Hindi words of length {length} found."}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)  