import streamlit as st
import requests

st.title("Wordle - English / Hindi")

if "previous_guesses" not in st.session_state:
    st.session_state.previous_guesses = []

lang = st.selectbox("Choose your language", ["English", "Hindi"])
if lang == "English":
    language_code = "eng"
else:
    language_code = "hin"

st.write("### Instructions:")
st.write("1. Guess a word.")
st.write("2. You have 5 attempts.")
st.write("3. Green: Correct letter in the correct position.")
st.write("4. Yellow: Correct letter in the wrong position.")
st.write("5. Gray: Incorrect letter.")

guess = st.text_input("Enter your word guess:", key="guess_eng" if language_code == "eng" else "guess_hin")


if st.button("Submit Guess"):
    guess = st.session_state.get("guess_eng") if language_code == "eng" else st.session_state.get("guess_hin")
    response = requests.post(
        "http://localhost:8000/wordle/guess_word",
        json={"guess": guess, "lang": language_code}
    )
    feedback = response.json()
    if "feedback" in feedback and "Similarity" in feedback:
        st.write("## Feedback:")
        feedback_html = "<div style='display: flex; gap: 10px;'>"
        for letter, color in feedback["feedback"]:
            if color == "green":
                feedback_html += f"<span style='color: green; font-size: 24px;'>{letter}</span>"
            elif color == "yellow":
                feedback_html += f"<span style='color: yellow; font-size: 24px;'>{letter}</span>"
            else:
                feedback_html += f"<span style='color: gray; font-size: 24px;'>{letter}</span>"
        feedback_html += "</div>"

        st.markdown(feedback_html, unsafe_allow_html=True)
        st.session_state.previous_guesses.append((guess, feedback["feedback"], feedback.get("Similarity", None)))
    
    elif "Similarity" in feedback:
        st.session_state.previous_guesses.append((guess, None, feedback["Similarity"]))

    if "Similarity" in feedback:
        st.write(f"Similarity score: {feedback['Similarity']}")
    else:
        st.write("No similarity score available.")

    if "Hint" in feedback: 
        st.write("Hint: " + feedback["Hint"])

    if feedback.get("message"):
        st.write(feedback["message"])

if st.session_state.previous_guesses:
    st.write("## Previous Guesses:")
    for guess, feedback_english, similarity in st.session_state.previous_guesses:
        prev_feedback_html = "<div style='display: flex; gap: 10px; align-items: center;'>"
        prev_feedback_html += f"<span style='font-size: 24px; font-weight: bold;'>{guess}: </span>"

        if feedback_english:
            for letter, color in feedback_english:
                if color == "green":
                    prev_feedback_html += f"<span style='color: green; font-size: 24px;'>{letter}</span>"
                elif color == "yellow":
                    prev_feedback_html += f"<span style='color: yellow; font-size: 24px;'>{letter}</span>"
                else:
                    prev_feedback_html += f"<span style='color: gray; font-size: 24px;'>{letter}</span>"

        if isinstance(similarity, (int, float)):
            prev_feedback_html += f"<span style='font-size: 24px; margin-left: 20px;'>Similarity: {similarity:.2f}</span>"
        else:
            st.write(f"Expected numeric value for similarity, but got: {similarity}")

        prev_feedback_html += "</div>"
        st.markdown(prev_feedback_html, unsafe_allow_html=True)

if "selected_language" not in st.session_state or st.session_state.selected_language != lang:
    requests.post("http://localhost:8000/wordle/reset_game", json={"lang": language_code})
    st.session_state.previous_guesses = []
    st.session_state.selected_language = lang
    st.rerun() 

if st.button("Reset Game"):
    requests.get("http://localhost:8000/wordle/reset_game",json={"lang":language_code})
    st.session_state.previous_guesses = []
    st.write("The game has been reset. A new word has been chosen.")
    st.rerun()