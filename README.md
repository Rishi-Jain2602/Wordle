# Sentiment-Analysis-on-Call-Transcripts
This project evaluate each transcript of phone call, providing sentiment scores to gauge emotions and attitudes in customer interactions.

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

## Note
1. Make sure you have Python 3.x installed
2. It is recommended to use a virtual environment to avoid conflict with other projects.
3. If you encounter any issue during installation or usage please contact rishijainai262003@gmail.com or rj1016743@gmail.com