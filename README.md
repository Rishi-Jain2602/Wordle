# Wordle - Word Guessing Game
A bilingual word guessing game built using FastAPI and Streamlit, supporting both English and Hindi. The game provides feedback based on correct letter positions and similarity scores for Hindi words, utilizing WordNet, IndoWordNet, and IndicBERT for contextual search.



****
## How to Play the Game
- Choose your preferred language (English or Hindi).
- Enter a word in the selected language and category.
- Click the Submit button, and the game will provide feedback:
   - Similarity score (ranges from 0 to 1).
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

Open a new terminal and run the backend:

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


