# Wordle - Word Guessing Game
A bilingual word guessing game built using **FastAPI and React.js**, supporting English, Hindi, and various other languages. The game evaluates guesses by providing similarity scores and common keywords based on the descriptions of the guessed word and the target word. It also offers hints for the target word, utilizing **WordNet and MistralAPI** for contextual search to enhance the guessing experience.



****
## How to Play the Game
- Choose your preferred language (English, Hindi or others).
- Enter a word in the selected language and category.
- Click the Submit button, and the game will provide feedback:
   - Similarity score (ranges from 0 to 1).
   - Common keywords between your guess and the target word.
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

- 3.1 Navigate to the **Backend** Directory and install Python dependencies:

```bash
cd backend
pip install -r requirements.txt
```
- 3.2 Navigate to the **Frontend** Directory and install Node.js dependencies:
```bash
cd frontend
npm install
```

4. Run the React App

Start the React app with the following command:

```bash
cd frontend
npm start
```

5. Run the Backend (FastAPI App)

Open a new terminal and run the backend:

```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
****

## Tools and Models Used
- **FastAPI:** Backend framework for managing game logic and API requests.
- **React.js:** Frontend framework for creating an interactive user interface.
- **WordNet** Used for selecting words and providing lexical relationships.
- **Google-bert:** Employed for calculating similarity scores between words.
- **Mistral AI:** Used to retrieve descriptions of words

