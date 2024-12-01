# Wordle - Word Guessing Game
A bilingual word guessing game built using FastAPI and Streamlit, supporting both English and Hindi. The game provides feedback based on correct letter positions and similarity scores for Hindi words, utilizing WordNet, IndoWordNet, and IndicBERT for contextual search.



https://github.com/user-attachments/assets/0195380e-743a-4de7-957c-bed5374afc6c



****
## How to Play the Game
- Choose your preferred language (English or Hindi).
- Enter a 5-letter word in the selected language.
- Click the Submit button, and the game will provide feedback:
   - Similarity score (ranges from 0 to 1).
   - Letters that are part of the target word will be highlighted in different colors:
     1. **Green:** Correct letter in the correct position.
     2. **Yellow:** Correct letter, but in the wrong position.
     3. **Gray:** Incorrect letter.
- You have a total of 5 attempts to guess the word correctly.

****
## Installation

1. Clone the Repository
   
``` bash
git clone https://github.com/Rishi-Jain2602/Wordle.git
```

2. Create Virtual Environment

```bash
virtualenv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
```

3. Install the Project dependencies

Install the required dependencies listed in the requirements.txt file:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit App

Start the Streamlit app with the following command:

```bash
cd frontend
streamlit run app.py
```

5. Run the Backend (Flask App)

Open a new terminal, navigate to the api directory, and run the backend:

```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
****

## Tools and Models Used
- **FastAPI:** Backend framework for managing game logic and API requests.
- **Streamlit:** Frontend framework for creating an interactive user interface.
- **WordNet / IndoWordNet:** Used for selecting words in English and Hindi.
- **IndicBERT:** Employed for calculating similarity scores for Hindi word guesses.

*****
## Note
1. Make sure you have Python 3.x installed
2. It is recommended to use a virtual environment to avoid conflict with other projects.
3. If you encounter any issue during installation or usage please contact rishijainai262003@gmail.com or rj1016743@gmail.com
