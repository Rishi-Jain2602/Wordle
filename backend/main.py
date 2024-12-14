from word_gen.eng_word import get_random_english_word
from word_gen.hindi_word import get_random_hindi_word
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from pydantic import BaseModel
from model import compare_words
import uvicorn
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

game_state_english = {
    "max_attempts": 5,
    "attempts": 0,
    "game_over": False,
}

get_random_hindi= get_random_hindi_word("जानवर")
game_state = game_state_hindi = {
    "max_attempts": 5,
    "attempts": 0,
    "game_over": False,
    "target_word": get_random_hindi[0],
    "target_hint":get_random_hindi[1] 
}

class UserWord(BaseModel):
    category:str
    guess:str
    lang:str

@app.post("/wordle/guess_word")
def guess_word(user_word: UserWord):
    global game_state_english, game_state_hindi
    global game_state
    
    guess = user_word.guess.lower()
    lang = user_word.lang
    category = user_word.category
    if lang == "eng" and "target_word" not in game_state_english:
        rand_english_word = get_random_english_word(category)  
        game_state_english = { 
            "max_attempts": 5,
            "attempts": 0,
            "game_over": False,
            "target_word": rand_english_word[0].lower(),
            "target_hint": rand_english_word[1].lower() + "\nSimilar words Like: " + rand_english_word[2][0] + " , " + rand_english_word[2][1]
        }   
        game_state = game_state_english
    elif lang == "hin" and "target_word" not in game_state_hindi:
        get_random_hindi= get_random_hindi_word("जानवर")
        game_state_hindi = {
            "max_attempts": 5,
            "attempts": 0,
            "game_over": False,
            "target_word": get_random_hindi[0],
            "target_hint":get_random_hindi[1] + "\n Similar words like: " + get_random_hindi[2][0] + "," + get_random_hindi[2][1]
        }
        game_state = game_state_hindi

    if game_state["game_over"]:
        return {"message": f"Game is over. Please start a new game. Word was {game_state['target_word']}"}

    guess = guess.lower()
    game_state["attempts"] += 1

    if guess == game_state["target_word"]:
        game_state["game_over"] = True
        return generate_feedback(guess, lang, win=True)

    if game_state["attempts"] >= game_state["max_attempts"]:
        game_state["game_over"] = True
        return generate_feedback(guess, lang, win=False)

    return generate_feedback(guess, lang)



def generate_feedback(guess: str,lang:str, win=False):
    global game_state
    
    similarity = compare_words(guess,game_state["target_word"],lang)
    
    if win:
        return {"Similarity":similarity, "message": "Congratulations! You've won!", "attempts": game_state["attempts"]}
    elif game_state["game_over"]:
        return {"Similarity":similarity, "message": f"Game over! The word was {game_state['target_word']}.", "attempts": game_state["attempts"]}
    else:
        return {"Hint" : game_state["target_hint"],"Similarity":similarity, "message": f"{game_state['max_attempts'] - game_state['attempts']} attempts remaining."}

class reset(BaseModel):
    category:str
    lang:str

@app.post("/wordle/reset_game")
def reset_game(user_reset:reset):
    global game_state_english,game_state_hindi
    global game_state
    lang = user_reset.lang
    if lang == "eng":
        get_random_english = get_random_english_word(user_reset.category)
        game_state_english = {
            "max_attempts": 5,
            "attempts": 0,
            "game_over": False,
            "target_word": get_random_english[0].lower(),
            "target_hint": get_random_english[1].lower() + "\nSimilar words Like: "+get_random_english[2][0]+" , "+get_random_english[2][1]
        }
        game_state = game_state_english
    else:
        get_random_hindi = get_random_hindi_word("जानवर")
        game_state_hindi = {
            "max_attempts": 5,
            "attempts": 0,
            "game_over": False,
            "target_word": get_random_hindi[0],
            "target_hint":get_random_hindi[1] + "\n Similar words like: " + get_random_hindi[2][0] + "," + get_random_hindi[2][1]
        }
        game_state = game_state_hindi
    return {"message": "Game reset successfully. A new word has been chosen."}


if __name__ == "__main__": 
    uvicorn.run(app, host="0.0.0.0", port=8000)