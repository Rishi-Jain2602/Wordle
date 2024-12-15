import streamlit as st
import requests

st.title("Wordle - English / Hindi")

# Initialize session state variables
if "previous_guesses" not in st.session_state:
    st.session_state.previous_guesses = []
if "previous_category" not in st.session_state:
    st.session_state.previous_category = None
if "feedback" not in st.session_state:  
    st.session_state.feedback = None
if "selected_language" not in st.session_state:
    st.session_state.selected_language = None

# Language and category selection
language_code = st.selectbox("Choose your language", ["English", "Hindi", "Kannada", "Tamil", "Malayalam"])
category = st.selectbox("Choose your category", ["Animal", "Bird", "Flower", "Vehicle", "Fruit", "Vegetable"])

st.write("### Guess a word.")
guess = st.text_input("Enter your word guess:", key="guess_eng" if language_code == "eng" else "guess_hin")

# Submit Guess
if st.button("Submit Guess"):
    guess = st.session_state.get("guess_eng") if language_code == "eng" else st.session_state.get("guess_hin")
    response = requests.post(
        "http://localhost:8000/wordle/guess_word",
        json={"guess": guess, "lang": language_code, "category": category}
    )
    
    st.session_state.feedback = response.json()
    feedback = st.session_state.feedback
    
    if "Similarity" in feedback:
        similar_score = round(feedback['Similarity'],2)
        st.write(f"Similarity Score is {similar_score}")
        if "Common_keywords" in feedback and feedback['Common_keywords'] != "":
            st.write(f"Common between Guess and Target word is {feedback['Common_keywords']}")
        else:
            st.write(f"No Common keywords between the guess word and target word")
        st.session_state.previous_guesses.append((guess, similar_score, None,feedback["Common_keywords"]))
    else:
        st.session_state.previous_guesses.append((guess, None, category,feedback["Common_keywords"]))
        st.write("No similarity score available.")
    

    if feedback.get("message"):
        st.write(feedback["message"])

# Hint button
if st.button("Hint"):
    feedback = st.session_state.get("feedback")  # Get feedback from session state
    if feedback:  # Ensure feedback is not None
        if "Hint" in feedback: 
            st.write("Hint: " + feedback["Hint"])
            st.write("Similar Words: " + feedback["Similar_words"])
        else:
            st.write("No hints available.")
    else:
        st.write("Please submit a guess first to receive hints.")

# Show previous guesses
if st.session_state.previous_guesses:
    st.write("## Previous Guesses:")
    for guess, similarity, cat,common_keyword in st.session_state.previous_guesses:
        if common_keyword:
            st.write(f"Word: {guess} - Similarity: {similarity} and Common Keyword: {common_keyword}")
        else:
            st.write(f"Word: {guess} - Similarity: {similarity} and No common keyword ")


# Only reset the game if the category or language changes
if (st.session_state.previous_category != category) or (st.session_state.selected_language != language_code):
    if st.session_state.previous_category != category or st.session_state.selected_language != language_code:
        requests.post("http://localhost:8000/wordle/reset_game", json={"lang": language_code, "category": category})
        st.session_state.previous_guesses = []
        st.session_state.selected_language = language_code
        st.session_state.previous_category = category
        st.rerun()  # Re-run the app to reflect the changes

# Reset Game button
if st.button("Reset Game"):
    requests.post("http://localhost:8000/wordle/reset_game", json={"category": category, "lang": language_code})
    st.session_state.previous_guesses = []
    st.write("The game has been reset. A new word has been chosen.")
    st.rerun()  # Re-run the app to reset the game state
