import React, { useState, useEffect,useCallback } from 'react';
import axios from 'axios';
import './styles/Home.css'
import _ from 'lodash';

export default function Home() {
  const [language, setLanguage] = useState('English');
  const [category, setCategory] = useState('Animal');
  const [guess, setGuess] = useState('');
  const [feedback, setFeedback] = useState(null);
  const [previousGuesses, setPreviousGuesses] = useState([]);
  const [showHint, setShowHint] = useState(false);
  const [userName, setUserName] = useState('');
  const [showNamePrompt, setShowNamePrompt] = useState(true);

  const languages = ["English", "Hindi", "Kannada", "Tamil", "Malayalam", "Telugu"];
  const categories = ["Animal", "Bird", "Flower", "Vehicle", "Fruit", "Vegetable"];

  const resetGame = useCallback(async () => {
    try {
      await axios.post('http://localhost:8000/wordle/reset_game', {
        lang: language,
        category
      });
      setFeedback(null); 
      setPreviousGuesses([]); 
    } catch (error) {
      console.error("Error resetting the game:", error);
    }
  }, [language, category]);

  const debouncedResetGame = useCallback(_.debounce(resetGame, 500), [resetGame]);


  useEffect(() => {
    debouncedResetGame();
    return () => {
      debouncedResetGame.cancel();  
    };
  }, [language, category, debouncedResetGame]);

  useEffect(() => {
    const savedName = localStorage.getItem('userName');
    if (savedName) {
      setUserName(savedName);
      setShowNamePrompt(false);
    } else {
      const name = prompt('Please enter your name:');
      if (name) {
        setUserName(name);
        localStorage.setItem('userName', name); 
        setShowNamePrompt(false);
      }
    }
  }, []);
  
  

  const handleLanguageChange = (e) => {
    setLanguage(e.target.value);
    resetGame();  
  };
  
  const handleCategoryChange = (e) => {
    setCategory(e.target.value);
    resetGame();  
  };
  

  const handleSubmit = async () => {
    try {
      const response = await axios.post('http://localhost:8000/wordle/guess_word', {
        guess,
        lang: language,
        category
      });
      const responseData = response.data;
      setFeedback(responseData);

      const similarity = responseData.Similarity ? responseData.Similarity.toFixed(2) : null;
      const commonKeyword = responseData.Common_keywords || "No common keywords";
      
      setPreviousGuesses(prev => [...prev, { guess, similarity, commonKeyword }]);
      setGuess('');  // Clear the input after submission
    } catch (error) {
      console.error("Error submitting the guess:", error);
    }
  };

  return (
    <>
      <div className="container my-5">
      <h1 className="text-center my-4 title">Wordle Word Guessing Game</h1>

      {userName && <h2>Welcome, {userName}!</h2>}

        <div className="form-group">
        <label htmlFor="language-select">Select Language:</label>
        <select
          id="language-select"
          className="form-control"
          value={language}
          onChange={handleLanguageChange}
        >
          {languages.map(lang => (
            <option key={lang} value={lang}>{lang}</option>
          ))}
        </select>
      </div>


      <div className="form-group my-3">
        <label htmlFor="category-select">Select Category:</label>
        <select
          id="category-select"
          className="form-control"
          value={category} onChange={handleCategoryChange}
        >
          {categories.map(cat => (
            <option key={cat} value={cat}>{cat}</option>
          ))}
        </select>
      </div>

      <div className="form-group my-3">
        <label htmlFor="word-input">Enter Your Word:</label>
        <input
          type="text"
          id="word-input"
          className="form-control"
          value={guess}
          onChange={e => setGuess(e.target.value)}
          placeholder="Type your guess here..."
        />
      </div>

      <div className="d-flex justify-content-between">
        <button type="button" className="btn btn-primary w-50 mx-4" onClick={handleSubmit} disabled={!guess}>Submit</button>
        <button type="button" className="btn btn-secondary w-50 mx-4" onClick={resetGame}>Reset</button>
      </div>

      {/* Feedback and Previous Guesses */}
      {feedback && (
        <div className="feedback mt-4 p-3 border rounded">
          <h4>Feedback:</h4>
          {feedback.Similarity && <p>Similarity Score: {feedback.Similarity.toFixed(2)}</p>}
          {feedback.Common_keywords && (
            <p>Common Keywords: {feedback.Common_keywords || "No common keywords"}</p>
          )}
          {feedback.message && <p>{feedback.message}</p>}
          <>
            <button
              className="btn btn-info mt-2"
              onClick={() => setShowHint(!showHint)}
            >
              {showHint ? "Hide Hint" : "Show Hint"}
            </button>
            {showHint && <p>Similar Words: {feedback.Similar_words}
            
            </p> 
            }
          </>
        </div>
      )}

      {previousGuesses.length > 0 && (
        <div className="previous-guesses mt-4">
          <h4>Previous Guesses:</h4>
          <ul className="list-group">
            {previousGuesses.map((entry, index) => (
              <li key={index} className="list-group-item">
                <strong>Word:</strong> {entry.guess}, <strong>Similarity:</strong> {entry.similarity || "N/A"}, <strong>Common Keyword:</strong> {entry.commonKeyword}
              </li>
            ))}
          </ul>
        </div>
      )}
      </div>
    </>
  )
}
