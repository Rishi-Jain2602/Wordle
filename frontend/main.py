import streamlit as st
import requests

st.title("Wordle - English / Hindi")

if "previous_guesses" not in st.session_state:
    st.session_state.previous_guesses = []
if "previous_category" not in st.session_state:
    st.session_state.previous_category = None
if "feedback" not in st.session_state:  
    st.session_state.feedback = None

lang = st.selectbox("Choose your language", ["English", "Hindi"])

category = st.selectbox("Choose your category",["Animal","Bird","Flower","Vehicle"])

if lang == "English":
    language_code = "eng"
else:
    language_code = "hin"
 
st.write("### Guess a word.")
guess = st.text_input("Enter your word guess:", key="guess_eng" if language_code == "eng" else "guess_hin")

if st.button("Submit Guess"):
    guess = st.session_state.get("guess_eng") if language_code == "eng" else st.session_state.get("guess_hin")
    response = requests.post(
        "http://localhost:8000/wordle/guess_word",
        json={"guess": guess, "lang": language_code,"category":category}
    )
    st.session_state.feedback = response.json()

    feedback = st.session_state.feedback
    
    if "Similarity" in feedback:
        st.write(f"Similarity Score is {feedback['Similarity']}")
        st.session_state.previous_guesses.append((guess, feedback["Similarity"],None))
    else:
        st.session_state.previous_guesses.append((guess, None,category))
        st.write("No similarity score available.")


    if feedback.get("message"):
        st.write(feedback["message"])

if st.button("Hint"):
    feedback = st.session_state.get("feedback")  # Get feedback from session state
    if feedback:  # Ensure feedback is not None
        if "Hint" in feedback: 
            st.write("Hint: " + feedback["Hint"])
        else:
            st.write("No hints available.")
    else:
        st.write("Please submit a guess first to receive hints.")

if st.session_state.previous_guesses:
    st.write("## Previous Guesses:")
    for guess, similarity,cat in st.session_state.previous_guesses:
        st.write(f"Word: {guess} - Similarity: {similarity}")

if st.session_state.previous_category != category or st.session_state.selected_language != lang:
    requests.post("http://localhost:8000/wordle/reset_game", json={"lang": language_code,"category":category})
    st.session_state.previous_guesses = []
    st.session_state.selected_language = lang
    st.session_state.previous_category = category
    st.rerun() 

if st.button("Reset Game"):
    requests.post("http://localhost:8000/wordle/reset_game",json={"category":category,"lang":language_code})
    st.session_state.previous_guesses = []
    st.write("The game has been reset. A new word has been chosen.")
    st.rerun()