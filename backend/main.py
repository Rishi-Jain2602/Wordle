from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from pydantic import BaseModel
from models.model import compare_words
from get_word.word import generate_word
import uvicorn
from dotenv import load_dotenv
load_dotenv()
import os
PORT = int(os.getenv('PORT', 8000))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

game_state = {
    "max_attempts": 5,
    "attempts": 0,
    "game_over": False,
}

class UserWord(BaseModel):
    category:str
    guess:str
    lang:str

@app.post("/wordle/guess_word")
def guess_word(user_word: UserWord):
    global game_state
    
    guess = user_word.guess.lower()
    lang = user_word.lang
    category = user_word.category.lower()


    if "target_word" not in game_state:
        game_state_word = generate_word(lang,category)
        if len(game_state_word[2]) >= 1:  
            similar_word = game_state_word[2][0]  
        else:
            similar_word = "No similar word"

        if len(game_state_word[2]) >= 2:  
            similar_word += "," + game_state_word[2][1]
        
        if len(game_state_word) >= 4:  
            target_hint = game_state_word[3]
        else:
            target_hint = "No hint available"
        game_state = {
            "max_attempts": 5,
            "attempts": 0,
            "game_over": False,
            "target_word": game_state_word[0],
            "target_desc":game_state_word[1],
            "target_hint": target_hint,
            "Similar_words":similar_word  
        }

    if game_state["game_over"]:
        re_word = game_state['target_word'].replace("_", " ")
        return {"message": f"Game is over. Please start a new game. Word was {re_word}"}


    guess = guess.lower()
    game_state["attempts"] += 1

    if guess == game_state["target_word"].lower():
        game_state["game_over"] = True
        return generate_feedback(guess, lang, win=True)

    if game_state["attempts"] >= game_state["max_attempts"]:
        game_state["game_over"] = True
        return generate_feedback(guess, lang, win=False)

    return generate_feedback(guess, lang)

def generate_feedback(guess: str,lang:str, win=False):
    global game_state
    similarity_and_common_words = compare_words(guess,game_state["target_word"],game_state["target_desc"],lang)
    similarity = similarity_and_common_words[0]
    common_keywords = similarity_and_common_words[1]
    
    if win:
        return {"Similarity":1,"Common_keywords":common_keywords, "message": "Congratulations! You've won!", "attempts": game_state["attempts"]}
    elif game_state["game_over"]:
        return {"Similarity":similarity,"Common_keywords":common_keywords, "message": f"Game over! The word was {game_state['target_word']}.", "attempts": game_state["attempts"]}
    else:
        return {"Hint" : game_state["target_hint"],"Common_keywords":common_keywords,"Similar_words":game_state["Similar_words"],"Similarity":similarity, "message": f"{game_state['max_attempts'] - game_state['attempts']} attempts remaining."}

class reset(BaseModel):
    category:str
    lang:str

@app.post("/wordle/reset_game")
def reset_game(user_reset:reset):
    global game_state
    lang = user_reset.lang
    category = user_reset.category
    game_state_word = generate_word(lang,category)
    if game_state_word is None or not isinstance(game_state_word, list):
        return {"message": "Error: Could not generate a new word. Please refresh."}
    
    if len(game_state_word[2]) >= 1:  
        similar_word = game_state_word[2][0] 
    else:
        similar_word = "No similar word"

    if len(game_state_word[2]) >= 2: 
        similar_word += "," + game_state_word[2][1]
    
    if len(game_state_word) >= 4:  # Ensure the list has at least 4 elements
        target_hint = game_state_word[3]
    else:
        target_hint = "No hint available"

    game_state = {
        "max_attempts": 5,
        "attempts": 0,
        "game_over": False,
        "target_word": game_state_word[0],
        "target_desc":game_state_word[1],
        "target_hint": target_hint,
        "Similar_words":similar_word
    }
    return {"message": "Game reset successfully. A new word has been chosen."}

if __name__ == "__main__": 
    uvicorn.run(app, host="0.0.0.0", port=PORT)