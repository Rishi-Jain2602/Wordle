import React from 'react';
import './styles/Instructions.css';

export default function Instructions() {
  return (
    <div className="instructions-container my-5">
      <h1 className="heading">How to Play the Game</h1>

      <div className="instructions-content">
        <h2 className="instruction-item">
          1. Choose your preferred language (English, Hindi, or any).
        </h2>
        <h2 className="instruction-item">
          2. Enter a word in the selected language and category.
        </h2>
        <h2 className="instruction-item">
          3. Click the Submit button, and the game will provide feedback:
        </h2>
        <h2 className="instruction-item mx-5">
          - Similarity score (ranges from 0 to 1).
        </h2>
        <h2 className="instruction-item mx-5">
          - Common keywords between your guess and the target word.
        </h2>

        <h2 className="instruction-item">
          4. You have a total of 5 attempts to guess the word correctly.
        </h2>
      </div>
    </div>
  );
}
